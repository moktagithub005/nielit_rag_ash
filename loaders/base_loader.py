from abc import ABC, abstractmethod


class BaseLoader(ABC):
    """
    Every loader must implement load().
    """

    @abstractmethod
    def load(self, source):
        """
        Returns a list of AppDocument objects.
        """
        pass