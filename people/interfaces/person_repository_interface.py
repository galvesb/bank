from abc import ABC, abstractmethod
from typing import List
from ..models import Person

class PersonRepositoryInterface(ABC):

    @abstractmethod
    def list_people(self, filters: dict = {}, page: int = 1, per_page: int = 10) -> List[Person]:
        pass

    @abstractmethod
    def create_person(self, data: dict) -> Person:
        pass

    @abstractmethod
    def update_person(self, person_id: int, data: dict) -> Person:
        pass

    @abstractmethod
    def delete_person(self, person_id: int) -> None:
        pass

    @abstractmethod
    def retrieve_person(self, person_id: int) -> Person:
        pass
