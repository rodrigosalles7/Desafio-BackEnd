from rest_framework import serializers
from proj.models import Proj

class ProjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proj
        fields = "__all__"