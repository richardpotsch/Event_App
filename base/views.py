from django.shortcuts import render
from .models import Event
from .forms import SearchForm
from django.shortcuts import render, get_object_or_404
from .recommender import Recommender
# Create your views here.
def event_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Event.published.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request,
                  'event/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})

def event_detail(request, id, slug):
    event = get_object_or_404(Event,
                                translations__slug=slug,
                                available=True)
    #cart_product_form = CartAddProductForm()
    r = Recommender(event)
    recommended_events = r.suggest_products_for([event], 4)

    return render(request,
                  'events/event.html',
                  {'event': event,
                   'cart_product_form': event_form,
                   'recommended_event': recommended_events})