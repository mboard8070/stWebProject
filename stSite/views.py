from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})


def portfolio(request):
    return render(request, "portfolio.html", {})


def games(request):
    return render(request, "games.html", {})


def contact(request):
    return render(request, "contact.html", {})


def ksjof(request):
    return render(request, "ksjof.html", {})


def sftc(request):
    return render(request, "sftc.html", {})
