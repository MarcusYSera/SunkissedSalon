from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'salon_home/Home.html');

def stylists(request):
    return render(request, 'salon_home/Stylists.html');

def stylistKacie(request):
    return render(request, 'salon_home/Kacie.html');

def stylistCooki(request):
    return render(request, 'salon_home/Cooki.html');

def stylistKimberly(request):
    return render(request, 'salon_home/Kimberly.html');

def stylistHeather(request):
    return render(request, 'salon_home/Heather.html');

def stylistMaxine(request):
    return render(request, 'salon_home/Maxine.html');

def stylistMyHuynh(request):
    return render(request, 'salon_home/MyHuynh.html');

def stylistPhuong(request):
    return render(request, 'salon_home/Phuong.html');

def stylistMyPhan(request):
    return render(request, 'salon_home/MyPhan.html');

def stylistHan(request):
    return render(request, 'salon_home/Han.html');
