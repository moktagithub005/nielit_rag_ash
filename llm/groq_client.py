from groq import Groq

from config.settings import settings


class GroqClient:

    def __init__(self):

        if not settings.GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY is not set. Add it to nielit_rag/.env."
            )

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    # ------------------------------------

    def generate(
        self,
        context,
        question,
        history=None
    ):

        history = history or []

        history_text = self._format_history(
            history
        )

        prompt = f"""
You are an AI Assistant for NIELIT.

Answer ONLY from the context.

Use conversation history only to understand
follow-up questions and references such as
"this", "that", "it", or "above".

If the context does not contain the answer,
say you do not know.

Conversation History:

{history_text}

Context:

{context}

Question:

{question}
"""

        response = self.client.chat.completions.create(

            model=settings.MODEL_NAME,

            messages=[

                {
                    "role":"system",
                    "content":"You answer only from context."
                },

                {
                    "role":"user",
                    "content":prompt
                }

            ]

        )

        return response.choices[0].message.content

    # ------------------------------------

    def stream_generate(
        self,
        context,
        question,
        history=None
    ):

        history = history or []

        history_text = self._format_history(
            history
        )

        prompt = f"""
You are an AI Assistant for NIELIT.

Answer ONLY from the context.

Use conversation history only to understand
follow-up questions and references such as
"this", "that", "it", or "above".

If the context does not contain the answer,
say you do not know.

Conversation History:

{history_text}

Context:

{context}

Question:

{question}
"""

        stream = self.client.chat.completions.create(

            model=settings.MODEL_NAME,

            messages=[

                {
                    "role": "system",
                    "content": "You answer only from context."
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            stream=True

        )

        for chunk in stream:

            delta = chunk.choices[0].delta.content or ""

            if delta:
                yield delta

    # ------------------------------------

    @staticmethod
    def _format_history(history):

        if not history:
            return "No previous conversation."

        lines = []

        for message in history:
            role = message["role"].capitalize()
            content = message["content"]
            lines.append(f"{role}: {content}")

        return "\n".join(lines)
