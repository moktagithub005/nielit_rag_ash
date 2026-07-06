import streamlit as st

from memory.conversation_memory import ConversationMemory


class SessionMemory:

    MEMORY_KEY = "conversation_memory"

    CHAT_KEY = "chat_messages"

    # ------------------------------------

    @classmethod
    def get_conversation_memory(cls):

        if cls.MEMORY_KEY not in st.session_state:
            st.session_state[cls.MEMORY_KEY] = ConversationMemory()

        return st.session_state[cls.MEMORY_KEY]

    # ------------------------------------

    @classmethod
    def get_chat_messages(cls):

        if cls.CHAT_KEY not in st.session_state:
            st.session_state[cls.CHAT_KEY] = []

        return st.session_state[cls.CHAT_KEY]

    # ------------------------------------

    @classmethod
    def add_user_message(cls, content):

        cls.get_chat_messages().append(
            {
                "role": "user",
                "content": content
            }
        )

        cls.get_conversation_memory().add_message(
            role="user",
            content=content
        )

    # ------------------------------------

    @classmethod
    def add_assistant_message(
        cls,
        content,
        sources
    ):

        cls.get_chat_messages().append(
            {
                "role": "assistant",
                "content": content,
                "sources": sources
            }
        )

        cls.get_conversation_memory().add_message(
            role="assistant",
            content=content
        )
