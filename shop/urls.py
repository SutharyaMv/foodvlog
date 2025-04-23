from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),  # Make sure 'about' is placed above 'prod_cat'
    path('', views.home, name='home'),
    path('MenuDetails/', views.menu_details, name='MenuDetails'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodDetails, name='details'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),  # Keep this for category filtering
    path('search', views.searching, name='search'),
    
]
