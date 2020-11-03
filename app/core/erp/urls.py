
from django.urls import path 
# from core.erp.views import myfirstview, mysecondview, mainview
# from core.erp.views.category.views import category_list
from core.erp.views.category.views import *


urlpatterns = [
    path('category/list/',  CategoryListView.as_view() ,    name = 'category_list'),
    # path('category/list/',  category_list,    name = 'category_list'),
    
    # path('uno/' , myfirstview, name = 'vista1'),
    # path('dos/' , mysecondview, name = 'vista2'),
    # path('main/' , mainview,    name = 'vistamain')
    
]
