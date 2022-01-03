from django.urls import path
from home.views import index, get_single, get_category, get_search, test


urlpatterns = [
    path('', index, name='base'),
    path('product/<int:slug>/', get_single, name='single'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('get_search/', get_search, name='search'),
    path('test/', test)
]