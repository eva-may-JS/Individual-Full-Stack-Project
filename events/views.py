from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Comment
from .forms import CommentForm


class EventList(generic.ListView):
    """
    Returns all published events in :model:`events.Event`
    and displays them in a page of six events. 
    **Context**

    ``queryset``
        All published instances of :model:`events.Event` in order from
        soonest to latest date.
    ``paginate_by``
        Number of events per page.
        
    **Template:**

    :template:`events/event_list.html`
    """
    queryset = Event.objects.filter(status=1).order_by('date')
    template_name = "event_list.html"
    paginate_by = 6


def event_detail(request, slug):
    """
    Display an individual instance of :model:`events.Event`.

    **Context**

    ``event``
        An instance of :model:`events.Event`.
    ``comments``
        All approved comments related to the event.
    ``comment_count``
        A count of approved comments related to the event.
    ``comment_form``
        An instance of :form:`events.CommentForm`.

    **Template:**

    :template:`events/event_detail.html`
    """

    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    comments = event.comments.all().order_by("-created_on")
    comment_count = event.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for editing.

    **Context**

    ``event``
        An instance of :model:`events.Event`.
    ``comment``
        A single comment related to the event.
    ``comment_form``
        An instance of :form:`events.CommentForm`
    """
    if request.method == "POST":

        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``event``
        An instance of :model:`events.Event`.
    ``comment``
        A single comment related to the event.
    """
    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))
    