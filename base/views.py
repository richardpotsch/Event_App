from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from .models import Event, EventResponse, Message, Type_event
from django.views.generic import ListView

from .models import *
#from .forms import SearchForm
from django.shortcuts import render, get_object_or_404
#from .recommender import Recommender
# Create your views here.

class ListOfEvents(ListView):
    template_name = 'base/events.html'
    model = Event

def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    messages = event.message_set.all()
    # POST
    if request.method == 'POST':
        Message.objects.create(
            user=request.user,
            event=event,
            message=request.POST.get('message')
        )
        return redirect('one_event', pk=event.id)
    # GET
    context = {'event': event, 'messages': messages}
    return render(request, 'base/one_event.html', context)


def event_search(request):
    q = request.GET.get('q', '')
    if q == "":
        return HttpResponse("empty q")
    events = Event.objects.filter(
        Q(description__contains=q) |
        Q(name__contains=q))
    context = {'q': q, 'events': events}
    return render(request, "base/search.html", context)
