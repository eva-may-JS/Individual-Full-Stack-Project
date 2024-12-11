from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event

# Create your views here.

class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('date')
    template_name = "event_list.html"
    paginate_by = 6


def event_detail(request, slug):
    """
    Display an individual :model:`events.Event`.

    **Context**

    ``event``
        An instance of :model:`events.Event`.

    **Template:**

    :template:`events/event_detail.html`
    """

    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "events/event_detail.html",
        {"event": event},
    )