from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Hello World</body></html>', content_type='text/html')
