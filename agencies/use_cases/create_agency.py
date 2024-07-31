
from agencies.models import Agency
from agencies.repositories.repository import AgencyRepository


class CreateAgency:

    def __init__(self, repository: AgencyRepository):
        self.repository = repository

    def execute(self, data: dict) -> Agency:
        return self.repository.create_agency(data)
