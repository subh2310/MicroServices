from rest_framework import serializers
from apimanager.models import ConnectNE

class ConnectNESerializers(serializers.ModelSerializer):
    class Meta:
        model = ConnectNE
        fields = '__all__'