from typing import List

from django.shortcuts import get_object_or_404
from agencies.models import Agency
from agencies.interfaces.agency_repository_interface import AgencyRepositoryInterface

class AgencyRepository(AgencyRepositoryInterface):

    def list_agencies(self, filters: dict = {}, page: int = 1, per_page: int = 10) -> List[Agency]:

        if "name-icontains" in filters:
            queryset = Agency.objects.filter(name__icontains=filters["name-icontains"])
        else:
            queryset = Agency.objects.filter(**filters)

        return queryset[(page - 1) * per_page : page * per_page]
    
    def create_agency(self, data: dict) -> Agency:
        return Agency.objects.create(**data)

    def update_agency(self, agency_id: int, data: dict) -> Agency:
        agency = get_object_or_404(Agency, id=agency_id)
        for field, value in data.items():
            setattr(agency, field, value)
        agency.save()
        return agency

    def delete_agency(self, agency_id: int) -> None:
        agency = get_object_or_404(Agency, id=agency_id)
        agency.delete()

    def retrieve_agency(self, agency_id: int) -> Agency:
        return get_object_or_404(Agency, id=agency_id)
