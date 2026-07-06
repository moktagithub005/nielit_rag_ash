class ConversationMemory:

    def __init__(self, max_turns=6):

        self.max_turns = max_turns

        self.messages = []

    # ------------------------------------

    def add_message(
        self,
        role,
        content
    ):

        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )

        max_messages = self.max_turns * 2

        if len(self.messages) > max_messages:
            self.messages = self.messages[-max_messages:]

    # ------------------------------------

    def get_messages(self):

        return list(self.messages)
