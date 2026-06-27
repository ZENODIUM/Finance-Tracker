from django.test import TestCase, Client
from django.urls import reverse
import json


class PingEndpointTestCase(TestCase):
    """Test case for the /ping health check endpoint."""

    def setUp(self):
        """Set up the test client."""
        self.client = Client()

    def test_ping_returns_200(self):
        """Test that GET /ping returns HTTP 200 status code."""
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)

    def test_ping_returns_json_content_type(self):
        """Test that GET /ping returns Content-Type: application/json."""
        response = self.client.get('/ping')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_ping_returns_correct_body(self):
        """Test that GET /ping returns exactly {"status": "ok"}."""
        response = self.client.get('/ping')
        data = json.loads(response.content)
        self.assertEqual(data, {"status": "ok"})

    def test_ping_no_extra_fields(self):
        """Test that the response contains no extra fields beyond status."""
        response = self.client.get('/ping')
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertIn("status", data)
