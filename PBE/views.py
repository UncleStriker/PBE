from django.http import HttpResponse

def testing(request):
    return HttpResponse('Testeando app')

def algunaOtraCosa(request):
    return HttpResponse('Hola')

