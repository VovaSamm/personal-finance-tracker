from django.db import models



# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES=[
        ('FOOD','Еда'),
        ('TRANSPORT','Транспорт'),
        ('HOUSING','Жилье'),
        ('ENTERTAINMENT','Развлечение'),
        ('OTHER','Другое')
    ]

    title=models.CharField(max_length=100, verbose_name='Название')
    amount=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Сумма')
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='OTHER',verbose_name='Категория')
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.amount}'

    class Meta:
        verbose_name='Расход'
        verbose_name_plural='Расходы'
        ordering=['-data']

