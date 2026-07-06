from config.prompts import SYSTEM_PROMPT


class PromptBuilder:

    def build(
        self,
        context,
        question
    ):

        return f"""
{SYSTEM_PROMPT}

Context
-------

{context}

Question
--------

{question}
"""