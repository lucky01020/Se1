from rest_framework import serializers

from .models import Beverages

class BeveragesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Beverages
        fields = ['id','name','flavour']