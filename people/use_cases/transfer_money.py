

from people.repositories.repository import PersonRepository
from decimal import Decimal


class TransferMoney:

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def execute(self, from_person_id: int, to_person_id: int, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")

        from_person = self.repository.retrieve_person(from_person_id)
        to_person = self.repository.retrieve_person(to_person_id)

        if from_person.balance < amount:
            raise ValueError("Insufficient funds")

        from_person.balance -= Decimal(amount)
        to_person.balance += Decimal(amount)

        from_person.save()
        to_person.save()
