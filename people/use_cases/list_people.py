from typing import List
from people.models import Person
from people.repositories.repository import PersonRepository

class ListPeople:

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def execute(self, filters: dict = {}, page: int = 1, per_page: int = 10) -> List[Person]:
        return self.repository.list_people(filters, page, per_page)
