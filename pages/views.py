from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *arg, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *arg, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "contact.html", {})


def about_view(request, *arg, **kwargs):
    my_context = {
        "my_text": "text",
        "my_number": 123,
        "my_list": [[123, 234, 345], [234, 345, 456], [345, 456, 567], ["ABC", "BCD", "CDE"]]
    }
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "about.html", my_context)
