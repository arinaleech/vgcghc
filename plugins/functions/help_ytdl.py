import os
import time
import logging
import random
import string
import yt_dlp as ytdl
from pyrogram import Client, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Setting up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Helper function to generate random strings
def random_char(y):
    """
    Generate a random string of length y.

    Parameters:
    - y (int): Length of the random string.

    Returns:
    - str: Random string of length y.
    """
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

# Helper function to download videos with yt-dlp
async def download_video(client, url, chat_id, message_id):
    """
    Downloads a video from a given URL using yt-dlp and sends progress updates to the user.

    Parameters:
    - client (Client): The Pyrogram client instance.
    - url (str): URL of the video to download.
    - chat_id (int): ID of the chat where the message is being sent.
    - message_id (int): ID of the message to update with download progress.

    Returns:
    - str: The file name of the downloaded video.
    """
    # Create a random file name for saving
    file_name = random_char(8) + '.mp4'
    
    # Define the download options for yt-dlp
    ydl_opts = {
        'outtmpl': file_name,  # Set output template (file name)
        'progress_hooks': [lambda d: progress_hook(d, client, chat_id, message_id)],  # Progress callback
        'format': 'bestvideo+bestaudio/best',  # Download the best quality available
    }

    # Start the download using yt-dlp
    with ytdl.YoutubeDL(ydl_opts) as ydl:
        try:
            await client.send_message(chat_id, "Starting download...")
            logger.info(f"Downloading video from: {url}")
            ydl.download([url])  # Start downloading the video
            logger.info(f"Download completed: {file_name}")
            await client.send_message(chat_id, f"Download completed! File saved as {file_name}")
            return file_name
        except Exception as e:
            logger.error(f"Error downloading video: {e}")
            await client.send_message(chat_id, "Failed to download the video. Please try again later.")
            return None

# Progress callback function for yt-dlp
def progress_hook(d, client, chat_id, message_id):
    """
    Tracks download progress and sends progress updates to the user.

    Parameters:
    - d (dict): Dictionary containing download progress information.
    - client (Client): The Pyrogram client instance.
    - chat_id (int): ID of the chat.
    - message_id (int): ID of the message to update with progress.
    """
    if d['status'] == 'downloading':
        current = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes', 1)  # Prevent division by zero
        percentage = current * 100 / total
        speed = d.get('speed', 0)
        eta = d.get('eta', 0)  # Estimated time of arrival (download time remaining)
        
        # Formatting the progress update message
        progress_message = f"Download Progress: {percentage:.2f}% | Speed: {humanbytes(speed)}/s | ETA: {eta}s"
        
        # Send the progress update message to the user
        try:
            client.edit_message_text(
                chat_id,
                message_id,
                text=progress_message,
                parse_mode=enums.ParseMode.MARKDOWN
            )
        except Exception as e:
            logger.error(f"Error updating progress: {e}")

# Helper function to convert bytes to a human-readable format
def humanbytes(size):
    """
    Convert bytes to a human-readable format.

    Parameters:
    - size (int): Size in bytes.

    Returns:
    - str: Human-readable size.
    """
    power = 2 ** 10
    n = 0
    dic_power = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + ' ' + dic_power[n]

# Main function to handle the bot client and video download requests
async def main(client: Client, url: str, chat_id: int, message_id: int):
    """
    Main handler for downloading the video and sending it to the user.

    Parameters:
    - client (Client): The Pyrogram client instance.
    - url (str): URL of the video to download.
    - chat_id (int): ID of the chat.
    - message_id (int): ID of the message.
    """
    file_name = await download_video(client, url, chat_id, message_id)
    
    if file_name:
        # Optionally, you can send the file to the user after downloading
        try:
            await client.send_document(
                chat_id,
                file_name,
                caption="Here is the video you requested!",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Download Again", callback_data='download_again')]
                ])
            )
            os.remove(file_name)  # Clean up the file after sending
        except Exception as e:
            logger.error(f"Error sending the file: {e}")
            await client.send_message(chat_id, "There was an issue sending the video file. Please try again.")
    else:
        await client.send_message(chat_id, "The download failed, please try again later.")

# Sample test URL (this should be replaced with actual user input in a real application)
sample_video_url = 'https://www.youtube.com/watch?v=example_video_id'

# Usage example
# Assuming `client` is a Pyrogram Client instance and `message_id` and `chat_id` are valid.
# Example usage in a function where `client` is the bot instance.
# await main(client, sample_video_url, chat_id, message_id) 
