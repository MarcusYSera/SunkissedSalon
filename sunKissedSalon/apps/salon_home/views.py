from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'salon_home/home.html');

def about(request):
    return render(request, 'salon_home/about.html');

def stylists(request):
    return render(request, 'salon_home/stylists.html');

def stylistKacie(request):
    return render(request, 'salon_home/kacie.html');

def stylistCooki(request):
    return render(request, 'salon_home/cooki.html');

def stylistKimberly(request):
    return render(request, 'salon_home/kimberly.html');

def stylistHeather(request):
    return render(request, 'salon_home/heather.html');

def stylistMaxine(request):
    return render(request, 'salon_home/maxine.html');

def stylistMyHuynh(request):
    return render(request, 'salon_home/myHuynh.html');

def stylistPhuong(request):
    return render(request, 'salon_home/phuong.html');

def stylistMyPhan(request):
    return render(request, 'salon_home/myPhan.html');

def stylistHan(request):
    return render(request, 'salon_home/han.html');
