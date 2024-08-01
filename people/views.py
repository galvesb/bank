from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from people.repositories.repository import PersonRepository
from .serializers import PersonSerializer, PersonCreateUpdateSerializer
from .use_cases.list_people import ListPeople
from .use_cases.create_person import CreatePerson
from .use_cases.update_person import UpdatePerson
from .use_cases.delete_person import DeletePerson
from .use_cases.retrieve_person import RetrievePerson
from .use_cases.deposit_money import DepositMoney
from .use_cases.withdraw_money import WithdrawMoney
from .use_cases.transfer_money import TransferMoney

from rest_framework.permissions import IsAuthenticated

repository = PersonRepository()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_people(request):
    use_case = ListPeople(repository)
    filters = request.query_params.dict()
    page = int(filters.pop('page', 1))
    per_page = int(filters.pop('per_page', 10))
    people = use_case.execute(filters, page, per_page)
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_person(request):
    use_case = CreatePerson(repository)
    serializer = PersonCreateUpdateSerializer(data=request.data)
    if serializer.is_valid():
        person = use_case.execute(serializer.validated_data)
        return Response(PersonSerializer(person).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_person(request, person_id):
    use_case = UpdatePerson(repository)
    serializer = PersonCreateUpdateSerializer(data=request.data)
    if serializer.is_valid():
        person = use_case.execute(person_id, serializer.validated_data)
        return Response(PersonSerializer(person).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_person(request, person_id):
    use_case = DeletePerson(repository)
    use_case.execute(person_id)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_person(request, person_id):
    use_case = RetrievePerson(repository)
    person = use_case.execute(person_id)
    serializer = PersonSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_money(request, person_id):
    amount = request.data.get('amount')
    if amount is None:
        return Response({"error": "Amount is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    use_case = DepositMoney(repository)
    try:
        person = use_case.execute(person_id, float(amount))
        return Response(PersonSerializer(person).data)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def withdraw_money(request, person_id):
    amount = request.data.get('amount')
    if amount is None:
        return Response({"error": "Amount is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    use_case = WithdrawMoney(repository)
    try:
        person = use_case.execute(person_id, float(amount))
        return Response(PersonSerializer(person).data)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transfer_money(request):
    from_person_id = request.data.get('from_person_id')
    to_person_id = request.data.get('to_person_id')
    amount = request.data.get('amount')

    if from_person_id is None or to_person_id is None or amount is None:
        return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)
    
    use_case = TransferMoney(repository)
    try:
        use_case.execute(from_person_id, to_person_id, float(amount))
        return Response({"message": "Transfer successful"})
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
