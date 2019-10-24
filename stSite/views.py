from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
#from .forms import EmailForm


def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})


def portfolio(request):
    return render(request, "portfolio.html", {})


def games(request):
    return render(request, "games.html", {})


def ksjof(request):
    return render(request, "ksjof.html", {})


def sftc(request):
    return render(request, "sftc.html", {})

def contact(request):
    return  render(request, "contact.html")


def messagecomplete(request):
    return render(request, "messagecomplete.html", {})

# django email code
#def email(request):
 #   if request.method == 'GET':
  #3 else:
    #    form = EmailForm(request.POST)
     #   if form.is_valid():
      #      name = form.cleaned_data['name']
       #     from_email = form.cleaned_data['from_email']
        #    subject = form.cleaned_data['subject']
         #   message = form.cleaned_data['message']
          #  try:
           #     send_mail(name, from_email, subject, message, ['admin@example.com'])
            #except BadHeaderError:
             #   return HttpResponse('Invalid header found.')
            #return redirect('messagecomplete.html')
    #return render(request, "contact.html", {'form': form})
