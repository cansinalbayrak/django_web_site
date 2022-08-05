from django.contrib import admin
from .models import Contact

#Burada admin sayfamızla iletişime geçeceğimiz methodları tanımlıyoruz.
# Admin panel sayesinde modelimizi import ederek üzerinde düzenlemeler yapabiliyoruz.
#Sayfamızda Contact modelimizi görünür kılmak için register methodu ile ekliyoruz.

admin.site.register(Contact)



