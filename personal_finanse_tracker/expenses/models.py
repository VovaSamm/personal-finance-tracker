from django.db import models



# Create your models here.
class Expenses(models.Model):
    title=models.CharField(max_length=30, unique=True)
    amout=models.DecimalField(max_digits=10, decimal_places=2)
    data=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Расходы'

