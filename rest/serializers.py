from rest_framework import serializers
from rest.models import KindChoices, CurrencyChoices, History
 
class KindChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindChoices

class CurrencyChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyChoices
 
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'