from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


class HttpResponseNoContent(HttpResponse):
    status_code = 204


@ensure_csrf_cookie
def csrf(request):
    return HttpResponseNoContent()

