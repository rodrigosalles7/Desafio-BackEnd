from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from proj.serializers import ProjSerializer
from proj.models import Proj

# Create your views here.


class ListProjAPIView(ListAPIView):
    queryset = Proj.objects.all()
    serializer_class = ProjSerializer


class CreateProjAPIView(CreateAPIView):
    queryset = Proj.objects.all()
    serializer_class = ProjSerializer


class UpdateProjAPIView(UpdateAPIView):
    queryset = Proj.objects.all()
    serializer_class = ProjSerializer


class DeleteProjAPIView(DestroyAPIView):
    queryset = Proj.objects.all()
    serializer_class = ProjSerializer
