from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.

class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('date')
    template_name = "event_list.html"
    paginate_by = 6