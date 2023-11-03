from django.shortcuts import render
from .forms import SimpleForm, CaptchaForm
from .models import SimpleFormData, CaptchaFormData

def simple_form(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            # обработка данных формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # сохранение данных в базу данных
            simple_form_data = SimpleFormData(name=name, email=email, message=message)
            simple_form_data.save()

            # отправка данных на страницу подтверждения
            return render(request, 'form_submitted.html', {'name': name, 'email': email, 'message': message})
    else:
        form = SimpleForm()
    return render(request, 'simple_form.html', {'form': form})


def form_with_captcha(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            # обработка данных 
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # сохранение данных 
            captcha_form_data = CaptchaFormData(name=name, email=email, message=message)
            captcha_form_data.save()

            # отправка данных 
            return render(request, 'form_submitted.html', {'name': name, 'email': email, 'message': message})
    else:
        form = CaptchaForm()
    return render(request, 'form_with_captcha.html', {'form': form})
