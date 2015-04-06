#!/usr/bin/env python
from django.test import TestCase
from homework.models import User, Topic
from django.test.client import Client
from django.http import HttpResponseNotFound
import logging
import json
import random
import string


class WebClientTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_one(self, user='john', topic='economy'):

        url_topic_user = "/%s/%s/" % (topic, user)
        url_topic = '/' + topic + '/'

        r = self.c.get('/zzz')
        self.assertEqual(r.status_code, 404, msg=r.reason_phrase) # unspecied behavior, 404 would be ok

        r = self.c.get(url_topic_user)
        self.assertEqual(r.status_code, 204, msg=r.reason_phrase)

        r = self.c.post(url_topic_user)
        self.assertEqual(r.status_code, 201, msg=r.reason_phrase)

        r = self.c.post(url_topic_user)
        self.assertEqual(r.status_code, 201, msg=r.reason_phrase)

        r = self.c.get(url_topic_user)
        self.assertEqual(r.status_code, 204, msg=r.reason_phrase) # no subscription

        # publish a message
        json_str = json.dumps({"message": "MSFT goes up!"})
        r = self.c.post(url_topic, data=json_str, content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )
        self.assertEqual(r.status_code, 201, msg=r.reason_phrase)

        # first time we need to get one message for john
        r = self.c.get(url_topic_user)
        self.assertEqual(r.status_code, 200, msg=r.reason_phrase)

        # 2nd time we need to get no messages for john (204 code)
        r = self.c.get(url_topic_user)
        self.assertEqual(r.status_code, 204, msg=r.reason_phrase)

        # unsubcribe user from topic
        r = self.c.delete(url_topic_user)
        self.assertEqual(r.status_code, 200, msg=r.reason_phrase)

        # re-unsubcribe user from topic (should get 404)
        r = self.c.delete(url_topic_user)
        self.assertEqual(r.status_code, 404, msg=r.reason_phrase)

        # publish a new message
        json_str = json.dumps({"message": "APPL goes down!"})
        r = self.c.post(url_topic, data=json_str, content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )
        self.assertEqual(r.status_code, 201, msg=r.reason_phrase)

        # now we should NOT get this message for john because he unsubscribed
        r = self.c.get(url_topic_user)
        self.assertEqual(r.status_code, 204, msg=r.reason_phrase)

# def test_generator():
#
#     cnt_users = 100
#     cnt_topics = 100
#     cnt_maxsubs = 20
#     cnt_subs = 2000
#     cnt_msgs = 10000
#     users = []
#     topics = []
#     for i in range(cnt_users):
#         users.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))
#     for i in range(cnt_topics):
#         topics.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))
#     for s in range(cnt_subs):
#         topic = topic=topics[random.randint(0,cnt_topics-1)]
#         user = users[random.randint(0,cnt_users-1)]
#         def ch(topic, user):
#             return lambda self: self.test_one(topic=topic, user=user)
#         setattr(WebClientTestCase, "test_gen_%s_%s" % (topic, user), ch(user=user, topic=topic))
#
# test_generator()

if __name__ == '__main__':
    
    unittest.main()