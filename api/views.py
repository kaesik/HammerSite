from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_data(request):
    data = request.data
    return Response(data)


@api_view(['POST'])
def post_data(request):
    data = request.data
    return Response(data)
