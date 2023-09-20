from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name = 'mainpage'),
    path('registration/', views.registr_page, name = 'registr_page'),
    path('list_of_products/<int:log_id>/', views.list_of_products, name = 'list_of_products'),
    path('list_of_lessons/<int:log_id>/<int:product_id>', views.list_of_lessons, name = 'list_of_lessons'),
    path('lesson_detail/<int:log_id>/<int:product_id>/<int:lesson_id>', views.lesson_detail, name = 'lesson_detail'),

]