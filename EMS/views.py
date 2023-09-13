from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import RegistrationForm

# Create your views here.
def index(request):
    events = Event.objects.all()
    context = {
        'events' : events
    }
    return render(request,'index.html',context)
def eventdetails(request,pk):
    events=Event.objects.get(pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            applicant=form.save(commit=False)
            applicant.event=events
            applicant.save()
    form=RegistrationForm()
    context = {
        'event' : events,
        'form' : form
    }
    return render(request,'details.html',context)