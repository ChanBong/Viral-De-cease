from django.shortcuts import render
from .models import Diseas
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def searchproduct(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Diseas.objects.filter(name__contains=query_name)
            return render(request, 'diseases/productsearch.html', {"results": results})

    return render(request, 'diseases/productsearch.html')


def home(request):
    context = {
        'diseas': Diseas.objects.all()
    }
    return render(request,)


class DiseasListView(ListView):
    model = Diseas
    template_name = 'diseases/home.html'
# <app>/<model>_<viewtype>.html
    context_object_name = 'diseases'
# can't use decoraters on classes
# log_in mixing
