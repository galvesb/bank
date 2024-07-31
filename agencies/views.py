from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from agencies.repositories.repository import AgencyRepository
from .serializers import AgencySerializer
from .use_cases.list_agencies import ListAgencies
from .use_cases.create_agency import CreateAgency
from .use_cases.update_agency import UpdateAgency
from .use_cases.delete_agency import DeleteAgency
from .use_cases.retrieve_agency import RetrieveAgency

repository = AgencyRepository()

@api_view(['GET'])
def list_agencies(request):
    use_case = ListAgencies(repository)
    filters = request.query_params.dict()
    page = int(filters.pop('page', 1))
    per_page = int(filters.pop('per_page', 10))
    agencies = use_case.execute(filters, page, per_page)
    serializer = AgencySerializer(agencies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_agency(request):
    use_case = CreateAgency(repository)
    serializer = AgencySerializer(data=request.data)
    if serializer.is_valid():
        agency = use_case.execute(serializer.validated_data)
        return Response(AgencySerializer(agency).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_agency(request, agency_id):
    use_case = UpdateAgency(repository)
    serializer = AgencySerializer(data=request.data)
    if serializer.is_valid():
        agency = use_case.execute(agency_id, serializer.validated_data)
        return Response(AgencySerializer(agency).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_agency(request, agency_id):
    use_case = DeleteAgency(repository)
    use_case.execute(agency_id)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def retrieve_agency(request, agency_id):
    use_case = RetrieveAgency(repository)
    agency = use_case.execute(agency_id)
    serializer = AgencySerializer(agency)
    return Response(serializer.data)
