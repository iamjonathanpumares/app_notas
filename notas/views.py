from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from notas.models import Nota
from notas.serializers import NotaSerializer

def nota_index(request):
    return render(request, 'notas/index.html')

@api_view(['GET', 'POST'])
def nota_list(request):
    """
    List all code notas, or create a new nota.
    """
    if request.method == 'GET':
        notas = Nota.objects.all()
        serializer = NotaSerializer(notas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
