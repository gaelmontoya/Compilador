from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Definicion de las apis o rutas 
@api_view(['POST'])
def main(requets):
    return Response(
        {'message':'Hola'},
        status=status.HTTP_200_OK
    )
