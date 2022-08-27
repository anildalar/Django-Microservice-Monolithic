from django.db import models

# Create your models here.

class Country(models.Model):
    #1. Properties
    country_name = models.CharField(max_length=20)
    local_currency = models.CharField(max_length=20)
    added_on = models.DateTimeField(auto_now_add=True)
    
    
    #3. method
    def __str__(self):
        return self.country_name+', '+self.local_currency
        pass
    
    #4. Nested class
    
    class Meta():
        verbose_name_plural = 'Countries';
    pass
