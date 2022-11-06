from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import logging
from .models import Event, EventResponse, Message, Type_event
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from datetime import date
from base.forms import EventForm

from .models import *
#from .forms import SearchForm
from django.shortcuts import render, get_object_or_404
logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s')
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
        return redirect('one_event', pk=event.id)
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
def make_event_response(request, pk):
    response = request.GET.get('response') # 'yes' / 'maybe' / 'not'
    EventResponse.objects.create(
        response_type = response,
        user_id = request.user.id,
        event_id= pk
    )
    logging.info(f"User id {request.user.id} responded {response} to event id {pk}.")
    return redirect('one_event', pk=pk)

class EventCreateView(CreateView): #LoginRequiredMixin, PermissionRequiredMixin,
    template_name = 'base/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('events')

    def form_invalid(self, form):
        return super().form_invalid(form)

class EventUpdateView(UpdateView):
    template_name = 'base/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('events')


    def form_invalid(self, form):
        return super().form_invalid(form)

class EventDeleteView(DeleteView):
    template_name = 'base/event_delete.html'
    form_class = EventForm
    success_url = reverse_lazy('events')
    def form_invalid(self, form):
        return super().form_invalid(form)

class MessageUpdateView(UpdateView):
    template_name = 'base/message_update.html'
    form_class = EventForm
    success_url = reverse_lazy('events')
    def form_invalid(self, form):
        return super().form_invalid(form)

class MessageDeleteView(DeleteView):
    template_name = 'base/message_delete.html'
    form_class = EventForm
    success_url = reverse_lazy('events')
    def form_invalid(self, form):
        return super().form_invalid(form)