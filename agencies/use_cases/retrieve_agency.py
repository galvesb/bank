from agencies.models import Agency
from agencies.repositories.repository import AgencyRepository


class RetrieveAgency:

    def __init__(self, repository: AgencyRepository):
        self.repository = repository

    def execute(self, agency_id: int) -> Agency:
        return self.repository.retrieve_agency(agency_id)
