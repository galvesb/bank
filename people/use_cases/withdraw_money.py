

from people.models import Person
from people.repositories.repository import PersonRepository
from decimal import Decimal


class WithdrawMoney:

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def execute(self, person_id: int, amount: float) -> Person:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        person = self.repository.retrieve_person(person_id)
        if person.balance < amount:
            raise ValueError("Insufficient funds")
        
        person.balance -= Decimal(amount)
        person.save()
        return person
