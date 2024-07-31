from abc import ABC, abstractmethod
from typing import List

from agencies.models import Agency

class AgencyRepositoryInterface(ABC):

    @abstractmethod
    def list_agencies(self, filters: dict = {}, page: int = 1, per_page: int = 10) -> List[Agency]:
        pass

    @abstractmethod
    def create_agency(self, data: dict) -> Agency:
        pass

    @abstractmethod
    def update_agency(self, agency_id: int, data: dict) -> Agency:
        pass

    @abstractmethod
    def delete_agency(self, agency_id: int) -> None:
        pass

    @abstractmethod
    def retrieve_agency(self, agency_id: int) -> Agency:
        pass
