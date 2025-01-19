from django.shortcuts import render

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

class SolicitudPasaporteAPIView(APIView):
    def post(self, request):
        serializer = SolicitudPasaporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SolicitudCedulaAPIView(APIView):
    def post(self, request):
        serializer = SolicitudCedulaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
