from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import Expense
from .forms import ExpenseForms

def exprnse_list(request):
    expenses=Expense.objects.all()
    return render(request,'expenses/expense_list.html',{'expense':expenses})

def expense_create(request):
    if request.method == "POST":
        form = ExpenseForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForms()
    return render(request, "expenses/expense_form.html", {"form": form})

def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForms(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForms(instance=expense)
    return render(request, "expenses/expense_form.html", {"form": form})

def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        expense.delete()
        return redirect("expense_list")
    return render(request, "expenses/expense_confirm_delete.html", {"expense": expense})