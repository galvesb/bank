from typing import List
from agencies.models import Agency
from agencies.repositories.repository import AgencyRepository


class ListAgencies:

    def __init__(self, repository: AgencyRepository):
        self.repository = repository

    def execute(self, filters: dict = {}, page: int = 1, per_page: int = 10) -> List[Agency]:
        return self.repository.list_agencies(filters, page, per_page)
