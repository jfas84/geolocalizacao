from django.shortcuts import render
from django.views.generic import View


from .utils import yelp_search, get_client_data

class IndexView(View):
    def get(self, request, *args, **kwards):
        itens = []

        city = None
        
        while not city:
            ret = get_client_data()
            if ret:
                city = ret['city']
        
        q = request.GET.get('key', None)
        loc = request.GET.get('loc', None)
        location = city

        context = {
            'city': city,
            'busca': False
        }

        if loc:
            location = loc
        if q:
            itens = yelp_search(keyword=q, location=location)
            context = {
                'itens': itens,
                'city': location,
                'busca': True
            }
        return render(request, 'index.html', context)