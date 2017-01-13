from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Cashflows, Deal

class CashflowsForm(ModelForm):
    class Meta:
        model = Cashflows
        fields = ['id', 'did', 'valuedate', 'cftype', 'cashflows']
        

class DealForm(ModelForm):
    class Meta:
        model = Deal
        fields = ['id', 'name', 'currency', 'fund']


# cashflow  

def cashflow_list(request, template_name='cashflows/index.html'):
    cashflows = Cashflows.objects.all()
    data = {}
    data['object_list'] = cashflows 
    return render(request, template_name, data)
    
def cashflow_create(request, template_name='cashflows/insert.html'):
    form = CashflowsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cashflow_list')
    return render(request, template_name, {'form':form})
    
def cashflow_update(request, pk, template_name='cashflows/insert.html'):
    cashflows = get_object_or_404(Cashflows, pk=pk)
    form = CashflowsForm(request.POST or None, instance=cashflows)
    if form.is_valid():
        form.save()
        return redirect('cashflow_list')
    return render(request, template_name, {'form':form})
    
def cashflow_delete(request, pk, template_name='cashflows/delete.html'):
    cashflows = get_object_or_404(Cashflows, pk=pk)
    if request.method == 'POST':
        cashflows.delete()
        return redirect('cashflow_list')
    return render(request, template_name, {'object':cashflows})
            

  
# deal  

def deal_list(request, template_name='deal/index.html'):
    deals = Deal.objects.all()
    data = {}
    data['object_list'] = deals 
    return render(request, template_name, data)
    
def deal_create(request, template_name='deal/insert.html'):
    form = DealForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('deal_list')
    return render(request, template_name, {'form':form})
    
def deal_update(request, pk, template_name='deal/insert.html'):
    deal = get_object_or_404(Deal, pk=pk)
    form = DealForm(request.POST or None, instance=deal)
    if form.is_valid():
        form.save()
        return redirect('deal_list')
    return render(request, template_name, {'form':form})
    
def deal_delete(request, pk, template_name='deal/delete.html'):
    deal = get_object_or_404(Deal, pk=pk)
    if request.method == 'POST':
        deal.delete()
        return redirect('deal_list')
    return render(request, template_name, {'object':deal})