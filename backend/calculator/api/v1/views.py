from calculator.tasks import add_numbers
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['POST'])
def add_numbers_view(request: Request):
    num1 = request.data.get('num1')
    num2 = request.data.get('num2')
    if (num1 is None) or (num2 is None):
        return Response({'error': 'Parameters not provided.'}, status=400)

    task = add_numbers.delay(num1, num2)
    return Response({'task_id': task.id}, status=202)
