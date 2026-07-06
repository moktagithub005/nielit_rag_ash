from memory.session_memory import SessionMemory


class MemoryManager:

    @staticmethod
    def get_history():

        return SessionMemory.get_conversation_memory().get_messages()

    # ------------------------------------

    @staticmethod
    def get_chat_messages():

        return SessionMemory.get_chat_messages()

    # ------------------------------------

    @staticmethod
    def add_user_message(content):

        SessionMemory.add_user_message(content)

    # ------------------------------------

    @staticmethod
    def add_assistant_message(
        content,
        sources
    ):

        SessionMemory.add_assistant_message(
            content=content,
            sources=sources
        )
