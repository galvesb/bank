from people.models import Person
from people.repositories.repository import PersonRepository


class CreatePerson:

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def execute(self, data: dict) -> Person:
        return self.repository.create_person(data)