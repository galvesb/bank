
from agencies.models import Agency
from agencies.repositories.repository import AgencyRepository


class UpdateAgency:

    def __init__(self, repository: AgencyRepository):
        self.repository = repository

    def execute(self, agency_id: int, data: dict) -> Agency:
        return self.repository.update_agency(agency_id, data)
