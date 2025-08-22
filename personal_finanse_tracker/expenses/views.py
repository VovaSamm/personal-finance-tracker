from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import Expense
from .forms import ExpenseForms
from django.contrib.auth.decorators import login_required

@login_required
def exprnse_list(request):
    expenses=Expense.objects.filter(user=request.user)
    return render(request,'expenses/expense_list.html',{'expense':expenses})


@login_required
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForms(request.POST)
        if form.is_valid():
            expense= form.save(commit=True)
            expense.user = request.user
            expense.save()
            return redirect("expense_list")
    else:
        form = ExpenseForms()
    return render(request, "expenses/expense_form.html", {"form": form})


@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk,user=request.user)
    if request.method == "POST":
        form = ExpenseForms(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForms(instance=expense)
    return render(request, "expenses/expense_form.html", {"form": form})


@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk,user=request.user)
    if request.method == "POST":
        expense.delete()
        return redirect("expense_list")
    return render(request, "expenses/expense_confirm_delete.html", {"expense": expense})