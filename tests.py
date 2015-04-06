#!/usr/bin/env python
from django.test import TestCase
from homework.models import User, Topic
from django.test.client import Client
from django.http import HttpResponseNotFound
import logging
import json

class WebClientTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_one(self):
        r = self.c.get('/zzz')
        self.assertEqual(r.status_code, 404, msg=r.reason_phrase) # unspecied behavior, 404 would be ok

        r = self.c.get(r'/economy/john/')
        self.assertEqual(r.status_code, 204, msg=r.reason_phrase)

        r = self.c.post(r'/economy/john/')
        self.assertEqual(r.status_code, 201, msg=r.reason_phrase)

        r = self.c.post(r'/nothing/john/')
        self.assertEqual(r.status_code, 201, msg=r.reason_phrase)

        r = self.c.get(r'/economy/john/')
        self.assertEqual(r.status_code, 204, msg=r.reason_phrase) # no subscription

        # publish a message
        json_str = json.dumps({"message": "MSFT goes up!"})
        r = self.c.post('/economy', data=json_str, content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )
        self.assertEqual(r.status_code, 201, msg=r.reason_phrase)

        # first time we need to get one message for john
        r = self.c.get(r'/economy/john/')
        self.assertEqual(r.status_code, 200, msg=r.reason_phrase)

        # 2nd time we need to get no messages for john (204 code)
        r = self.c.get(r'/economy/john/')
        self.assertEqual(r.status_code, 204, msg=r.reason_phrase)
