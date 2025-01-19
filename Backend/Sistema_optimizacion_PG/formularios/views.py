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

    def get(self, request, *args, **kwargs):
            # Si se pasa un 'id' en la URL, se busca esa solicitud específica
            id = kwargs.get('id')
            if id:
                try:
                    solicitud = SolicitudVisa.objects.get(id=id)
                    serializer = SolicitudVisaSerializer(solicitud)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except SolicitudVisa.DoesNotExist:
                    return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                # Si no se pasa 'id', se devuelven todas las solicitudes
                solicitudes = SolicitudVisa.objects.all()
                serializer = SolicitudVisaSerializer(solicitudes, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        try:
            solicitud = SolicitudVisa.objects.get(id=id)
        except SolicitudVisa.DoesNotExist:
            return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SolicitudVisaSerializer(solicitud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
            id = kwargs.get('id')
            try:
                solicitud = SolicitudVisa.objects.get(id=id)
            except SolicitudVisa.DoesNotExist:
                return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
            
            solicitud.delete()
            return Response({'detail': 'Solicitud eliminada exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
class SolicitudPasaporteAPIView(APIView):
    def post(self, request):
        serializer = SolicitudPasaporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
            # Si se pasa un 'id' en la URL, se busca esa solicitud específica
            id = kwargs.get('id')
            if id:
                try:
                    solicitud = SolicitudPasaporte.objects.get(id=id)
                    serializer = SolicitudPasaporteSerializer(solicitud)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except SolicitudPasaporte.DoesNotExist:
                    return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                # Si no se pasa 'id', se devuelven todas las solicitudes
                solicitudes = SolicitudPasaporte.objects.all()
                serializer = SolicitudPasaporteSerializer(solicitudes, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        try:
            solicitud = SolicitudPasaporte.objects.get(id=id)
        except SolicitudPasaporte.DoesNotExist:
            return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SolicitudPasaporteSerializer(solicitud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        try:
            solicitud = SolicitudPasaporte.objects.get(id=id)
        except SolicitudPasaporte.DoesNotExist:
            return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        solicitud.delete()
        return Response({'detail': 'Solicitud eliminada exitosamente.'}, status=status.HTTP_204_NO_CONTENT)


class SolicitudCedulaAPIView(APIView):
    def post(self, request):
        serializer = SolicitudCedulaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
            # Si se pasa un 'id' en la URL, se busca esa solicitud específica
            id = kwargs.get('id')
            if id:
                try:
                    solicitud = SolicitudCedula.objects.get(id=id)
                    serializer = SolicitudCedulaSerializer(solicitud)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except SolicitudCedula.DoesNotExist:
                    return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                # Si no se pasa 'id', se devuelven todas las solicitudes
                solicitudes = SolicitudCedula.objects.all()
                serializer = SolicitudCedulaSerializer(solicitudes, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        try:
            solicitud = SolicitudCedula.objects.get(id=id)
        except SolicitudCedula.DoesNotExist:
            return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SolicitudCedulaSerializer(solicitud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        try:
            solicitud = SolicitudCedula.objects.get(id=id)
        except SolicitudCedula.DoesNotExist:
            return Response({'detail': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        solicitud.delete()
        return Response({'detail': 'Solicitud eliminada exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
