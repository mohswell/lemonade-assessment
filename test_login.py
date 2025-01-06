import requests
import unittest
from unittest.mock import patch

class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json_data = json_data
        
    def json(self):
        return self._json_data

class TestLoginAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/auth/v1/login"
    
    def setUp(self):
        self.valid_credentials = {
            "username": "testuser",
            "password": "password123"
        }
        self.invalid_credentials = {
            "username": "wronguser",
            "password": "wrongpassword"
        }
        
    @patch('requests.post')
    def test_successful_login(self, mock_post):
        # Mock successful response
        mock_post.return_value = MockResponse(200, {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MzYyNTU3NDJ9.9HwW3pR5gW23w71fdQh7m5PWMgsR-kw_jjRwkyBXoTI",
            "status": "success"
        })
        
        # Make the request
        response = requests.post(
            self.BASE_URL,
            json=self.valid_credentials
        )
        
        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())
        self.assertEqual(response.json()["status"], "success")
        
    @patch('requests.post')
    def test_invalid_credentials(self, mock_post):
        # Mock failed response
        mock_post.return_value = MockResponse(401, {
            "error": "Invalid credentials",
            "status": "failure"
        })
        
        # Make the request
        response = requests.post(
            self.BASE_URL,
            json=self.invalid_credentials
        )
        
        # Assertions
        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()["status"], "failure")
        
    @patch('requests.post')
    def test_missing_credentials(self, mock_post):
        # Test with missing password
        incomplete_credentials = {"username": "testuser"}
        
        # Mock bad request response
        mock_post.return_value = MockResponse(400, {
            "error": "Missing required fields",
            "status": "failure"
        })
        
        # Make the request
        response = requests.post(
            self.BASE_URL,
            json=incomplete_credentials
        )
        
        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

if __name__ == '__main__':
    unittest.main()