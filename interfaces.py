from abc import ABC, abstractmethod
from student import Student


class IInputReader(ABC):
    @abstractmethod
    def read(self) -> Student:
        pass


class IOutputWriter(ABC):
    @abstractmethod
    def write(self, student: Student) -> None:
        pass