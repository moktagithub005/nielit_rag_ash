from config.settings import settings

groq_key_preview = (
    settings.GROQ_API_KEY[:10] + "..."
    if settings.GROQ_API_KEY
    else "Not set"
)

print("Groq Key:", groq_key_preview)
print("Model:", settings.MODEL_NAME)
print("Embedding:", settings.EMBEDDING_MODEL)
print("Vector Path:", settings.CHROMA_DB_PATH)
