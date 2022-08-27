
from rest_framework import serializers

from currency_country.models import Country

class CountrySerializer(serializers.ModelSerializer):
    
    #4. Nested Class
    class Meta():
        model = Country
        fields = '__all__'
    pass