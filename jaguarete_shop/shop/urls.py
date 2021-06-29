# shop/url.py

from django.urls import path

from .import views

app_name = 'shop'

 
urlpatterns = [
            path ('', views.index, name='index'),
            path ('login/', views.login_page, name='login'),
            path ('logout/', views.logout_page, name='logout'),
            path('register/', views.register_page, name='register'),
            path('index/', views.index, name='index'),
            path ('product_list/', views.product_list, name='product_list'),
            path ('<slug:category_slug>', views.product_list, name='product_list_by_category'),
            path ('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'), 
                
        ]
 
