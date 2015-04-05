from django.http import HttpResponse

def fallback(request):
    return HttpResponse('not implemented')

def page(request, topic, user):
    return HttpResponse('TBD: topic=%s user=%s' % (topic, user))
