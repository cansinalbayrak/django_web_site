from django.urls import path
from . import views
#Burada pathlerimizi(yollarımız, uzantılarımız) tanımlıyor ve görünümlerimizle bağlıyoruz.
# Bizim 3 tane pathimiz var; anasayfa, hakkında ve formların bulunduğu iletişim sayfamız.
urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contact/', views.contact, name="contact"),
]