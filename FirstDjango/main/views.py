from django.http import HttpResponse

def data(request):
    return HttpResponse("<h1>Ув. Куратор! Давно хотел сказать:</h1>")

def test(request):
    return HttpResponse("<h1> Благодарю за обратную связь и потраченное время🤝!</h1>")