from django.shortcuts import render,redirect
#from django.views.generic.base import TemplateView
from django.views.generic import TemplateView
from django.views.generic import CreateView,ListView,DetailView
from leadlogisticsApp import models
from leadlogisticsApp.forms import ContactUsForm
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
import smtplib

# Create your views here.

def nodata(request):
    return render(request,'leadlogisticsApp/Docket_nodata.html')

def DocketList(request):
    #obj = models.Docket.objects.all()
    return render(request,'leadlogisticsApp/Docket_form.html')

def DetailList(request):
    obj = models.Docket.objects.all()
    #data =
    #print(request.GET.get('Docket'))
    data = request.GET.get('Docket')
    #print("length is: ",len(obj))
    k = len(obj)

    for content in obj:

        #print(str(content))
        if data == str(content):
            #print("data Found")
            pass

        else:
            k -= 1
            if k == 0:
                #print(" No data Found")
                return HttpResponseRedirect(reverse('leadlogisticsApp:nodata'))


    return render(request,"leadlogisticsApp/Docket_detail.html",{'obj':obj,'data':data})


def ContactUs(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            Name = form['name'].value()
            Email = form['email'].value()
            Phone = form['phone'].value()
            Subject = form['subject'].value()
            Requirements = form['requirements'].value()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("raki.039@gmail.com", "Hamsa@123")
            msg = ("From: %s\r\nTo: %s\r\n\r\nPhone: %s\r\n Subject: %s\r\n Requirements: %s\r\n"
       % (Email,Email,Phone,Subject,Requirements))

            s.sendmail("raki.039@gmail.com", "raki.039@gmail.com", msg)
            s.quit()
            return HttpResponseRedirect(reverse('Thanks'))

    else:
        form = ContactUsForm()

    return render(request,'leadlogisticsApp/contact.html',{'form': form})
