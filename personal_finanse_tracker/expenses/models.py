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

class Income(models.Model):
    SOURSE_CHOISE=[
        ('SALARY','Зарплата'),
        ('BUSINESS','Бизнес'),
        ('GIFT','Подарок'),
        ('OTHER','Другое')
    ]
    title = models.CharField(max_length=100, verbose_name='Название')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    source = models.CharField(max_length=20, choices=SOURSE_CHOISE, default='OTHER', verbose_name='Источник')
    data = models.DateTimeField(auto_now_add=True,verbose_name='Дата получения')

    def __str__(self):
        return f'{self.title} - {self.amount}'

    verbose_name = 'Доход'
    verbose_name_plural = 'Доходы'
    ordering = ['-data']
