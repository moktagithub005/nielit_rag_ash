class SourceBuilder:

    def build(self, search_result):

        sources = []

        for chunk in search_result.chunks:

            metadata = chunk.metadata

            sources.append(

                {

                    "document": metadata.get(

                        "document_name",

                        "Unknown"

                    ),

                    "page": metadata.get(

                        "page",

                        "-"

                    ),

                    "score": round(

                        chunk.score,

                        2

                    )

                }

            )

        return sources