from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import Product, LessonTopic
from .forms import LoginForm

def main(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('list_of_products', args = [user.id]))
            else:
                err_mess = 'Неправильный логин или пароль'
                return render(request, 'Lessons/mainpage.html', {'form': form, 'err_mess': err_mess})
    else:
        form = LoginForm()
    return render(request, 'Lessons/mainpage.html', {'form': form})

def registr_page(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect(reverse('mainpage'))
    else:
        form1 = UserCreationForm()
    return render(request, 'Lessons/registr_page.html', {'form1': form1})

def list_of_products(request, log_id):
    content = Product.objects.all()
    return render(request, 'Lessons/list_of_products.html', {'content': content, 'log_id': log_id})

def list_of_lessons(request, log_id, product_id):
    content = Product.objects.get(id = product_id).lesson_to_product.all()
    return render(request, 'Lessons/list_of_lessons.html', {'content': content, 'log_id': log_id, 'product_id': product_id})

def lesson_detail(request, log_id, product_id, lesson_id):
    content = LessonTopic.objects.get(id = lesson_id)
    return render(request, 'Lessons/lesson_detail.html', {'content': content, 'log_id': log_id}) 
  