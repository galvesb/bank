from people.repositories.repository import PersonRepository


class DeletePerson:

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def execute(self, person_id: int) -> None:
        self.repository.delete_person(person_id)