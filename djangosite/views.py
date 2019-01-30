from django.http import HttpResponse, HttpResponseRedirect

def index(req):
    return HttpResponse("<h1>Welcome to MyDjangoStie</h1>")