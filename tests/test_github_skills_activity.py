import unittest

from fastapi.testclient import TestClient

from src.app import app


class GitHubSkillsActivityTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_github_skills_activity_is_available(self):
        response = self.client.get("/activities")

        self.assertEqual(response.status_code, 200)

        activities = response.json()
        self.assertIn("GitHub Skills", activities)

        activity = activities["GitHub Skills"]
        self.assertIn("GitHub", activity["description"])
        self.assertEqual(activity["max_participants"], 15)


if __name__ == "__main__":
    unittest.main()
