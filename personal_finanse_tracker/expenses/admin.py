from django.contrib import admin
from .models import Expense

# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title','amount','category','data')
    list_filter = ('category','data')
    search_fields = ('title',)

