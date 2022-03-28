from django.db import models

# Create your models here.
class Proj(models.Model):
    id = models.CharField(primary_key=True, max_length=16,  
                          help_text='Adicione um ID com 16 caracteres')
    name = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    amount_products = models.IntegerField()

    def __str___(self):
        return self.name