from django.test import SimpleTestCase
from django.urls import reverse


class StatusEndpointTests(SimpleTestCase):
    def test_status_returns_online(self):
        response = self.client.get(reverse("app:status"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "online")
        self.assertEqual(data["message"], "I am online")
        self.assertIn("timestamp", data)

    def test_status_rejects_post(self):
        response = self.client.post(reverse("app:status"))
        self.assertEqual(response.status_code, 405)
