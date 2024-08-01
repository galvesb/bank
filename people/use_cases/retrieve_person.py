from people.models import Person
from people.repositories.repository import PersonRepository


class RetrievePerson:

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def execute(self, person_id: int) -> Person:
        return self.repository.retrieve_person(person_id)