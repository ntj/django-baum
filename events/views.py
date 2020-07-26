from django.http import HttpResponse


def index(request):
    return HttpResponse("Roter Baum Event Management")
