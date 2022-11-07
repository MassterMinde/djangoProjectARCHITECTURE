from django.http import HttpResponse
import URL


# Create your views here.

def index(request, input):
    return HttpResponse(f"Текст без ссылки: {URL.URL(input)}")
