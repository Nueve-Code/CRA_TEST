from abc import abstractmethod, ABC


class GradeInterface(ABC):
    def __init__(self, standard: int):
        self._standard = standard

    @property
    def standard(self):
        return self._standard

    @abstractmethod
    def get_str(self):
        pass