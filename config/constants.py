"""
Project Constants
"""

# --------------------------
# Chunking
# --------------------------

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# --------------------------
# Retrieval
# --------------------------

TOP_K_RESULTS = 5

# --------------------------
# Supported Files
# --------------------------

SUPPORTED_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".txt",
    ".xlsx",
]

# --------------------------
# Collection Names
# --------------------------

STATIC_COLLECTION = "static_documents"

WEBSITE_COLLECTION = "website_documents"

UPLOAD_COLLECTION = "uploaded_documents"
