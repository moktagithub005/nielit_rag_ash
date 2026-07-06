from datetime import datetime
from pathlib import Path
import shutil

from config.settings import settings


def ensure_upload_directories():

    settings.UPLOAD_INCOMING_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    settings.UPLOAD_PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


def save_uploaded_file(uploaded_file):

    ensure_upload_directories()

    timestamp = datetime.utcnow().strftime(
        "%Y%m%d%H%M%S"
    )

    safe_name = Path(uploaded_file.name).name

    target_path = (
        settings.UPLOAD_INCOMING_DIR /
        f"{timestamp}_{safe_name}"
    )

    target_path.write_bytes(
        uploaded_file.getvalue()
    )

    return target_path


def move_to_processed(file_path):

    ensure_upload_directories()

    source_path = Path(file_path)

    target_path = (
        settings.UPLOAD_PROCESSED_DIR /
        source_path.name
    )

    shutil.move(
        str(source_path),
        str(target_path)
    )

    return target_path
