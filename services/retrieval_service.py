from factories.repository_factory import RepositoryFactory
from memory.search_result import SearchResult
from config.constants import TOP_K_RESULTS


class RetrievalService:

    def __init__(self):

        self.repositories = [
            RepositoryFactory.get_repository("static"),
            RepositoryFactory.get_repository("upload")
        ]

    # ------------------------------------

    def retrieve(
        self,
        question,
        top_k=TOP_K_RESULTS
    ):

        merged_result = SearchResult()

        for repository in self.repositories:

            result = repository.search(

                query=question,

                top_k=top_k

            )

            merged_result.chunks.extend(
                result.chunks
            )

        merged_result.chunks.sort(
            key=lambda chunk: chunk.score,
            reverse=True
        )

        merged_result.chunks = merged_result.chunks[:top_k]

        return merged_result
