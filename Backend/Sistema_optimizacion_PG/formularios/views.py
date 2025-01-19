from django.shortcuts import render
from rest_framework.exceptions import NotFound
# Create your views here.
# forms.py



from rest_framework import serializers
from .models import SolicitudVisa, SolicitudPasaporte, SolicitudCedula

class SolicitudVisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudVisa
        fields = '__all__'

class SolicitudPasaporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudPasaporte
        fields = '__all__'

class SolicitudCedulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudCedula
        fields = '__all__'

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SolicitudVisa, SolicitudPasaporte, SolicitudCedula

class SolicitudVisaAPIView(APIView):
    def post(self, request):
        serializer = SolicitudVisaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Método GET para obtener todas las solicitudes de visa
    def get(self, request):
        solicitudes = SolicitudVisa.objects.all()
        serializer = SolicitudVisaSerializer(solicitudes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        # Buscar la solicitud por el id que viene en el JSON
        id = request.data.get('id')
        try:
            solicitud = SolicitudVisa.objects.get(id=id)
        except SolicitudVisa.DoesNotExist:
            return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        # Actualizar los campos de la solicitud con los datos del JSON
        serializer = SolicitudVisaSerializer(solicitud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class SolicitudPasaporteAPIView(APIView):
    def post(self, request):
        serializer = SolicitudPasaporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Método GET para obtener todas las solicitudes de pasaporte
    def get(self, request):
        solicitudes = SolicitudPasaporte.objects.all()
        serializer = SolicitudPasaporteSerializer(solicitudes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SolicitudCedulaAPIView(APIView):
    def post(self, request):
        serializer = SolicitudCedulaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Método GET para obtener todas las solicitudes de cédula
    def get(self, request):
        solicitudes = SolicitudCedula.objects.all()
        serializer = SolicitudCedulaSerializer(solicitudes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
