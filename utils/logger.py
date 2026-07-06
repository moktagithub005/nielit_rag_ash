"""
Centralized Logger
"""

import sys
from loguru import logger

from config.settings import settings


# -----------------------------
# Create logs folder
# -----------------------------

LOG_DIR = settings.BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


# -----------------------------
# Remove default logger
# -----------------------------

logger.remove()


# -----------------------------
# Console Logger
# -----------------------------

logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level:<8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
           "<level>{message}</level>"
)


# -----------------------------
# File Logger
# -----------------------------

logger.add(
    LOG_DIR / "application.log",
    level=settings.LOG_LEVEL,
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | "
           "{level:<8} | "
           "{name}:{function}:{line} | "
           "{message}"
)
