from rest_framework.test import APITestCase


class HealthCheckViewTests(APITestCase):
    def test_health_check_returns_ok(self):
        response = self.client.get("/api/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "status": "ok",
                "project": "stock_pilot_back",
            },
        )

# Create your tests here.
