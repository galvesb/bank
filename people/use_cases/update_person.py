from people.models import Person
from people.repositories.repository import PersonRepository


class UpdatePerson:

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def execute(self, person_id: int, data: dict) -> Person:
        return self.repository.update_person(person_id, data)