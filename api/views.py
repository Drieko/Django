from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Raiz")

def sobre(request):
    return HttpResponse("Sobre nos")

def contatos(request):
    return HttpResponse("Meus contatos")
