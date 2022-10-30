from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Event, EventResponse, Message, Type_event
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from datetime import date
from base.forms import EventForm

from .models import *
#from .forms import SearchForm
from django.shortcuts import render, get_object_or_404
#from .recommender import Recommender
# Create your views here.

class ListOfEvents(ListView):
    template_name = 'base/events.html'
    model = Event

    #ToDo -potřebujeme vracet i response



def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    messages = event.message_set.all()

    # latest response in database
    latest_response = EventResponse.objects.filter(
        user_id=request.user,
        event_id=event
    ).order_by('-response_date').first()

    # POST
    if request.method == 'POST':
        Message.objects.create(
            user=request.user,
            event=event,
            message=request.POST.get('message')
        )
        return redirect('one event', pk=event.id)
    # GET
    context = {'event': event, 'messages': messages, 'latest_response': latest_response}
    return render(request, 'base/one_event.html', context)


def event_search(request):
    q = request.GET.get('q')
    c = request.GET.get('c')

    if not q and not c:
        return HttpResponse("empty q")
    query_text = None
    if q:
        events = Event.objects.filter(
            Q(description__contains=q) |
            Q(name__contains=q))


    elif c:
        events = Event.objects.filter(type_event_id = c)
        event_type = Type_event.objects.get(id = c)
        q = event_type.name

    context = {'q': q, 'events': events}
    return render(request, "base/search.html", context)

#@login_required
def make_event_response(request):
    event_id = request.GET.get('event_id')
    response = request.GET.get('response') # 'yes' / 'maybe' / 'not'

    if request.method == 'POST':
        # creates new record in db:
        EventResponse.objects.create(
            response_type = response,
            user_id = request.user,
            event_id= event_id
        )
        return redirect('one_event', pk=event_id)

class EventCreateView(CreateView): #LoginRequiredMixin, PermissionRequiredMixin,
    template_name = 'base/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('events')

    def form_invalid(self, form):
        return super().form_invalid(form)