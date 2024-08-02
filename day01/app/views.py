from django.shortcuts import render
from .forms import CategoryForm, EmployeeForm, ItemForm, OrderForm, SupplierForm, TestForm, UnitForm 
from .models import *
from django.core.paginator import Paginator
from .filters import CategoryFilter
from .filters import *

# Create your views here.
def category_view(request):
    page_number = request.GET.get('page')
    
    filter = CategoryFilter(request.GET, queryset=Category.objects.all())
    categories = filter.qs
    paginator = Paginator(categories, 3)
    
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)  # Deliver first page if page_number is not an integer
    except EmptyPage:
        page = paginator.page(paginator.num_pages)  # Deliver last page if page_number is out of range

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()

    context = {'form': form, 'page': page}
    return render(request, 'Category.html', context)



def unitview(request):
    units = Unit.objects.all()
    context_Unt = {'uts':units}
    return render(request, 'Unit.html', context_Unt)

def test(request):
    if request.method =='POST':
        form = TestForm(request.POST)
    else:    
        form = TestForm()
    context = {'form':form}
    return render(request, 'test.html', context)


def unit_view(request):
    units = Unit.objects.all()
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = UnitForm()
    context = {'form':form, 'uts':units}
    return render(request, 'Unit.html', context)


def item_view(request):
    page_number = request.GET.get('page')
    filter = ItemFilter(request.GET, queryset=Item.objects.all())
    items = filter.qs
    paginator = Paginator(items, 3)
    page = paginator.page(page_number)
    
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)  # Deliver first page if page_number is not an integer
    except EmptyPage:
        page = paginator.page(paginator.num_pages)  # Deliver last page if page_number is out of range

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = ItemForm()
    context = {'form':form, 'page':page}
    return render(request, 'Item.html', context)


def supplier_view(request):
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = SupplierForm()
    context = {'form':form, 'supplrs':suppliers}
    return render(request, 'supplier.html', context)

def order_view(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = OrderForm()
    context = {'form':form, 'ordrs':orders}
    return render(request, 'order.html', context)

def employee_view(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = EmployeeForm()
    context = {'form':form, 'employs':employees}
    return render(request, 'employee.html', context)