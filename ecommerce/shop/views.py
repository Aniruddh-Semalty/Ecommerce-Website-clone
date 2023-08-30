from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"shop/ShopHome.html")
def about(request):
    return HttpResponse("Hi i am about page")
def contact(request):
    return HttpResponse("Hi i am contact page")
def tracker(request):
    return HttpResponse("Hi i am tracker page")
def search(request):
    return HttpResponse("Hi i am search page")
def viewProduct(request):
    return HttpResponse("Hi i am product page")
def checkout(request):
    return HttpResponse("Hi i am checkout page")



