import logging
import asyncio
import os
import time
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

# Configure logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def run_ffmpeg_command(command):
    """ Helper function to run ffmpeg command and log output/errors """
    logger.debug(f"Running command: {' '.join(command)}")
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    # Log both stdout and stderr
    stdout = stdout.decode().strip()
    stderr = stderr.decode().strip()
    
    if stderr:
        logger.error(f"FFmpeg error: {stderr}")
    if stdout:
        logger.debug(f"FFmpeg output: {stdout}")

    return stdout, stderr


async def place_water_mark(input_file, output_file, water_mark_file):
    watermarked_file = output_file + ".watermark.png"
    metadata = extractMetadata(createParser(input_file))
    width = metadata.get("width")

    if not width:
        logger.error("Failed to retrieve video width.")
        return None

    # Shrink the watermark to fit the video width
    shrink_watermark_file_genertor_command = [
        "ffmpeg", "-i", water_mark_file, "-y", "-v", "quiet",
        "-vf", f"scale={width}*0.5:-1", watermarked_file
    ]
    
    _, stderr = await run_ffmpeg_command(shrink_watermark_file_genertor_command)
    if stderr:
        return None

    # Overlay watermark on the video
    commands_to_execute = [
        "ffmpeg", "-i", input_file, "-i", watermarked_file,
        "-filter_complex", "\"overlay=(main_w-overlay_w):(main_h-overlay_h)\"",
        output_file
    ]

    _, stderr = await run_ffmpeg_command(commands_to_execute)
    if stderr:
        return None

    return output_file


async def take_screen_shot(video_file, output_directory, ttl):
    out_put_file_name = os.path.join(output_directory, f"{time.time()}.jpg")
    file_genertor_command = [
        "ffmpeg", "-ss", str(ttl), "-i", video_file, "-vframes", "1", out_put_file_name
    ]

    _, stderr = await run_ffmpeg_command(file_genertor_command)
    if stderr:
        return None

    if os.path.exists(out_put_file_name):
        return out_put_file_name
    else:
        logger.error(f"Screenshot file not created: {out_put_file_name}")
        return None


async def cult_small_video(video_file, output_directory, start_time, end_time):
    out_put_file_name = os.path.join(output_directory, f"{round(time.time())}.mp4")
    file_genertor_command = [
        "ffmpeg", "-i", video_file, "-ss", start_time, "-to", end_time, 
        "-async", "1", "-strict", "-2", out_put_file_name
    ]

    _, stderr = await run_ffmpeg_command(file_genertor_command)
    if stderr:
        return None

    if os.path.exists(out_put_file_name):
        return out_put_file_name
    else:
        logger.error(f"Video clipping failed: {out_put_file_name}")
        return None


async def generate_screen_shots(
    video_file,
    output_directory,
    is_watermarkable,
    wf,
    min_duration,
    no_of_photos
):
    metadata = extractMetadata(createParser(video_file))
    duration = 0
    if metadata is not None and metadata.has("duration"):
        duration = metadata.get('duration').seconds

    if duration < min_duration:
        logger.warning(f"Video is too short. Duration: {duration} seconds, Minimum duration: {min_duration} seconds.")
        return None

    images = []
    ttl_step = duration // no_of_photos
    current_ttl = ttl_step

    for looper in range(no_of_photos):
        ss_img = await take_screen_shot(video_file, output_directory, current_ttl)
        current_ttl += ttl_step

        if ss_img and is_watermarkable:
            ss_img = await place_water_mark(ss_img, os.path.join(output_directory, f"{time.time()}.jpg"), wf)

        if ss_img:
            images.append(ss_img)

    return images if images else None
