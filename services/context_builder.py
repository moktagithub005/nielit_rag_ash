
class ContextBuilder:

    def build(self, search_result):

        context = []

        for chunk in search_result.chunks:

            context.append(chunk.text)

        return "\n\n".join(context)