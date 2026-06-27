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
        """Test that GET /ping returns Content-Type: application/json (with optional charset)."""
        response = self.client.get('/ping')
        content_type = response['Content-Type']
        self.assertTrue(
            content_type == 'application/json' or content_type.startswith('application/json;'),
            f"Expected 'application/json' or 'application/json; charset=...', got '{content_type}'"
        )

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

    def test_ping_rejects_post(self):
        """Test that POST /ping returns HTTP 405 Method Not Allowed."""
        response = self.client.post('/ping')
        self.assertEqual(response.status_code, 405)

    def test_ping_rejects_put(self):
        """Test that PUT /ping returns HTTP 405 Method Not Allowed."""
        response = self.client.put('/ping')
        self.assertEqual(response.status_code, 405)

    def test_ping_rejects_delete(self):
        """Test that DELETE /ping returns HTTP 405 Method Not Allowed."""
        response = self.client.delete('/ping')
        self.assertEqual(response.status_code, 405)
