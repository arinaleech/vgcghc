# motor/frameworks/asyncio/__init__.py

import asyncio
from pymongo import monitoring

# Fallback for coroutine if the attribute exists
coroutine = None
if hasattr(asyncio, "coroutine"):
    coroutine = asyncio.coroutine

# Rest of the motor asyncio implementation
