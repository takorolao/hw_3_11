from django.urls import path
from .views import simple_form, form_with_captcha

urlpatterns = [
    path('simple_form/', simple_form, name='simple_form'),
    path('form_with_captcha/', form_with_captcha, name='form_with_captcha'),
]
