from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..base.models import PyPartner, PyProduct
from django.contrib.auth.models import User


@login_required(login_url="/erp/login")
def erp_home(request):
    partners = PyPartner.objects.all()
    return render(request, "home.html", {
        'customers': partners.filter(customer=True),
        'providers': partners.filter(provider=True),
        'users': User.objects.all(),
        'products': PyProduct.objects.all()
    })
