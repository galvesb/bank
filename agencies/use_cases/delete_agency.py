from agencies.repositories.repository import AgencyRepository


class DeleteAgency:

    def __init__(self, repository: AgencyRepository):
        self.repository = repository

    def execute(self, agency_id: int) -> None:
        self.repository.delete_agency(agency_id)
