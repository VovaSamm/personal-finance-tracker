from django.conf import settings
from django.db import models
from django.conf import settings
class Income(models.Model):
    SOURSE_CHOISE=[
        ('SALARY','Зарплата'),
        ('BUSINESS','Бизнес'),
        ('GIFT','Подарок'),
        ('OTHER','Другое')
    ]
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='incomes')
    title = models.CharField(max_length=100, verbose_name='Название')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    source = models.CharField(max_length=20, choices=SOURSE_CHOISE, default='OTHER', verbose_name='Источник')
    data = models.DateTimeField(auto_now_add=True,verbose_name='Дата получения')

    def __str__(self):
        return f'{self.title} - {self.amount}'

    verbose_name = 'Доход'
    verbose_name_plural = 'Доходы'
    ordering = ['-data']
