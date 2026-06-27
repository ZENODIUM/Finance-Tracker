from django.test import TestCase, Client
from django.urls import reverse
import json


class PingEndpointTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ping_returns_200(self):
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)

    def test_ping_returns_json_content_type(self):
        response = self.client.get('/ping')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_ping_returns_correct_body(self):
        response = self.client.get('/ping')
        data = json.loads(response.content)
        self.assertEqual(data, {"status": "ok"})

    def test_ping_has_no_extra_fields(self):
        response = self.client.get('/ping')
        data = json.loads(response.content)
        self.assertEqual(set(data.keys()), {"status"})
