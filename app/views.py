from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from app.forms import MomentForm
import os

def welcome(req):
    return HttpResponse("<h1>Welcome to my tiny twitter!</h1>")

@csrf_protect
def moments_input(request):
    # render(requtest, 'app/test.html')
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("app:welcome"))
    else:
        form = MomentForm()
    return render(request, 'app/moments_input.html', {'form': form})
