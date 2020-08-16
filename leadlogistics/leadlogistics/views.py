from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class MainView(TemplateView):
    template_name = 'index.html'

class FleetView(TemplateView):
    template_name = 'fleet.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class SampleView(TemplateView):
    template_name = 'sample.html'

class ServiceView(TemplateView):
    template_name = 'services.html'

class Thanks(TemplateView):
    template_name = 'Thanks.html'

def nodata(request):
    return render(request,'nodata.html')
