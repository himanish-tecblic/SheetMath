from django.shortcuts import render
from app.serializer import PBPMSerializer
from rest_framework.viewsets import ModelViewSet
from app.models import PBPM
from rest_framework import status
from rest_framework.response import Response
from app.utils import calc_pbm
# Create your views here.

class PBPMApi(ModelViewSet):
    serializer_class = PBPMSerializer
    queryset = PBPM.objects.all()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        id = request.data.get("id")
        ft = request.data.get("id")
        pbpm = calc_pbm(ft,id)
        serializer = PBPMSerializer(pbpm)
        return Response(serializer.data,status = status.HTTP_200_OK)