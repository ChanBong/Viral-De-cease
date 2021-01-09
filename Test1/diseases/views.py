from django.shortcuts import render
from .models import Diseas
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


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
