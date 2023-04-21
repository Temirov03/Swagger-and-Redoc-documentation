from rest_framework import serializers
from .models import Metto,iPhone



class MettoSerializers(serializers.ModelSerializer):



    class Meta:
        model = Metto
        fields = '__all__'


class iPhoneSerializers(serializers.ModelSerializer):



    class Meta:
        model = iPhone
        fields = '__all__'