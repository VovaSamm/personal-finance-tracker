from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Income
from .forms import IncomeForm

@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, "incomes/income_list.html", {"incomes": incomes})

@login_required
def income_create(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=True)
            income.user=request.user
            income.save()
            return redirect("income_list")
    else:
        form = IncomeForm()
    return render(request, "incomes/income_form.html", {"form": form})

@login_required
def income_update(request, pk):
    income = get_object_or_404(Income, pk=pk,user=request.user)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect("income_list")
    else:
        form = IncomeForm(instance=income)
    return render(request, "incomes/income_form.html", {"form": form})



@login_required
def income_delete(request, pk):
    income = get_object_or_404(Income, pk=pk,user=request.user)
    if request.method == "POST":
        income.delete()
        return redirect("income_list")
    return render(request, "incomes/income_confirm_delete.html", {"income": income})