from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Home, HomeProduct, HomeProduct1, HomeProduct2, Eror404, Checkout, Footer
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homes = Home.objects.all()
        product = HomeProduct.objects.all()
        product1 = HomeProduct1.objects.all()
        product2 = HomeProduct2.objects.all()
        return render(request, self.template_name, {'homes':homes, 
                                                    'product':product, 
                                                    'product1':product1,
                                                    'product2':product2
                                                    })



class ErorListView(ListView):
    template_name = '404.html'
    
    def get(self, request):
        eror = Eror404.objects.all()
        return render(request, self.template_name,{'eror':eror})




class CheckoutListView(ListView):
    template_name = 'checkout.html'
    
    def get(self, request):
        checkouts = Checkout.objects.all()
        return render(request, self.template_name,{'checkouts':checkouts})



class FooterListView(ListView):
    template_name = 'base.html'
    
    def get(self, request):
        footers = Footer.objects.all()
        return render(request, self.template_name,{'footers':footers})



def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')