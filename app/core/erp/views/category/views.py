
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from core.erp.models import Category


# from core.erp.models import Product



# Create your views here.



def category_list(request):
    # return HttpResponse('Hola esta es mi primera url')
    data = {
        'title':'listado de categorias',
        'categories': Category.objects.all()
    }

    return render(request, 'category/list.html', data)



class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias' 
        context['object_list'] =  Category.objects.all()
        return context


    def get_queryset(self):
        return Category.objects.filter(name__startswith='l')
    

    

