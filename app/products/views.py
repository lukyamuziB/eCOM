from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product


#class based view
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView).get_context_data(*args, **kwargs)
    #     return context

#function based view
def productlistview(request):
    queryset = Product.objects.a()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)

#class based view
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView).get_context_data(*args, **kwargs)
        return context

#function based view
def productdetailview(request, id, *args, **kwargs):
    # queryset = Product.objects.get(pk=id)
    queryset = get_object_or_404(Product, pk=id)
    context = {
        'object': queryset
    }
    return render(request, 'products/detail.html', context)