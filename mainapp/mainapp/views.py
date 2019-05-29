from django.http import HttpResponse


def home(request):
    user = request.user
    return HttpResponse("<h1>Royal Hotels</h1>".format(user))