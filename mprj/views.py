from django.shortcuts import render
from .forms import ContactForm

#Burada sayfa görünümlerini tanımlayan ve gelen requestleri templatelerimizle bağlayıp yönledirecek fonksiyonları tanımlıyoruz.
# Fonskiyonları html sayfalarımızdaki templatelerimize render methodu ile yönlendirerek görünüm kazandırıyoruz.
#render methodu ilk parametre olan requestleri alıp 2. parametre olan html sayfalarına yönlendiriyoruz.
#Üçüncü paremetlerimizle formumuzun dahil olduğu sözlüğümüze yönlendiriyoruz.
# Ayrıca forma girilen bilgilerin POST methoduyla alınmasını sağlayacak işlevleri yazıyoruz.
# Böylece formlarımız kaydedilip veri tabanımıza da düşecektir.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)

def aboutus(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, "mycontact.html", context)



