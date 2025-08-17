from django.contrib import admin
from .models import Expense,Income

# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title','amount','category','data')
    list_filter = ('category','data')
    search_fields = ('title',)

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('title','amount','source','data')
    list_filter = ('source','data')
    search_fields = ('title',)