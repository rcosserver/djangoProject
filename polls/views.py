from django.http import HttpResponse
from django.shortcuts import render


def my_image(request):
    image_data = open("/djangoProject/public_html/media/img/favicon.ico", "rb").read()
    return HttpResponse(image_data, mimetype="image/png")

#def index(request):
#    return HttpResponse("Как то так")



def index(request):
    result = "пример"
    return render(request, 'index.html', {"result": result})


