from django.shortcuts import render
from django.http import HttpResponse
from .models import Producct

def index(request):
    user = "rhythm"
    product_1 = 4
    products = Producct.objects.all()
    product1 = products[0]
    product2 = products[1]
    product3 = products[2]
    product4 = products[3]
    return render(request, "products/home.html",{
        "name":user,
        "product_num":product_1,
        "products":products,
        "product1":product1,
        "product2":product2,
        "product3":product3,
        "product4":product4,
    })

def signup(request):
    return render(request, "products/signup.html")
def suit(request,product,product_id):
    if product=="suits" or product=="dress" or product=="shirts":
        return HttpResponse(f"Here is the list of out {product}")
    else:
        return HttpResponse("The page does not exist")