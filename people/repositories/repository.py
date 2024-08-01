from typing import List

from people.interfaces.person_repository_interface import PersonRepositoryInterface
from people.models import Person


class PersonRepository(PersonRepositoryInterface):

    def list_people(self, filters: dict = {}, page: int = 1, per_page: int = 10) -> List[Person]:
        queryset = Person.objects.filter(**filters)
        return queryset[(page - 1) * per_page : page * per_page]

    def create_person(self, data: dict) -> Person:
        return Person.objects.create(**data)

    def update_person(self, person_id: int, data: dict) -> Person:
        person = Person.objects.get(id=person_id)
        for field, value in data.items():
            setattr(person, field, value)
        person.save()
        return person

    def delete_person(self, person_id: int) -> None:
        person = Person.objects.get(id=person_id)
        person.delete()

    def retrieve_person(self, person_id: int) -> Person:
        return Person.objects.get(id=person_id)
