from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    if request.method == 'POST':
        receiver = request.POST.get('receiver-email')
        subject = request.POST.get('subject')
        mess = request.POST.get('msg')


        if receiver:
            if mess:
                from_mail = settings.EMAIL_HOST_USER
                send_mail(subject, mess, from_mail, [receiver,])
                messages.success(request, 'Email Sent Successfully.')

                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Email should have message.')
       
                return HttpResponseRedirect('/')
        else:
            messages.error(request, "Please enter receiver's email id")

            return HttpResponseRedirect('/')


    return render(request, 'home.html')