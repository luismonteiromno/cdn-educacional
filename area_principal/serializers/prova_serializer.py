from rest_framework import serializers


from ..models import Prova


class ProvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prova
        fields = '__all__'
        