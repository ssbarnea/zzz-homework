from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from models import Topic, User, Message, Subscription
import logging
import json

def fallback(request):
    return Http404()

def page(request, topic, user):

    if request.method == 'GET':

        try:
            topic = Topic.objects.get(name=topic)
        except:
            return HttpResponse(reason="No topic found", status=204)

        try:
            user = User.objects.get(name=user)
        except:
            return HttpResponse(reason="No user found", status=204)


        subs = Subscription.objects.filter(topic=topic, user=user)
        if not subs:
            return HttpResponse(reason="No subscription found", status=204)

        msgs = []
        for m in Message.objects.filter(topic=topic, user=user):
            msgs.append(m.body)
            m.delete()
        if not msgs:
            return HttpResponse(reason="No messages found", status=204)

        return JsonResponse({'messages': msgs})

    elif request.method == 'POST':

        t, created = Topic.objects.get_or_create(name=topic)
        if created:
            t.save()
        u, created  = User.objects.get_or_create(name=user)
        if created:
            u.save()
        s, created = Subscription.objects.get_or_create(user=u, topic=t)
        if created:
            s.save()
        return HttpResponse(reason='POST: topic=%s user=%s subscription=%s' % (t.id, u.id, s.id), status=201)

    elif request.method == 'DELETE':

        try:
            topic = Topic.objects.get(name=topic)
        except:
            return HttpResponse(reason="No topic found", status=404)

        try:
            user = User.objects.get(name=user)
        except:
            return HttpResponse(reason="No user found", status=404)


        subs = Subscription.objects.filter(topic=topic, user=user)
        if not subs:
            return HttpResponse(reason="No subscription found", status=404)

        for sub in subs:
            sub.delete()
        return HttpResponse(status=200)


    else:
        raise Http404()

def post_message(request, topic):
    if request.method == 'POST':
        t, created = Topic.objects.get_or_create(name=topic)
        if created:
            t.save()
        subs = Subscription.objects.filter(topic=t)
        d = json.loads(request.body)
        msg = d['message']
        for sub in subs:
            Message(body=msg, user=sub.user, topic=t).save()
        return HttpResponse(reason='Posted to %s users' % len(subs), status=201)
    raise Http404()
