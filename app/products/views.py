from django.views.generic import ListView
from django.shortcuts import render

from .models import Product


#class based view
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView).get_context_data(*args, **kwargs)
    #     return context

#function based view
def productlistview(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product.html', context)