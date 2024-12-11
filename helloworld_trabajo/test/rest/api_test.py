import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "3", "ERROR ADD"
        )

    def test_api_sqrt(self):
        url = f"{BASE_URL_MOCK}/calc/sqrt/64"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "8", "ERROR SQRT"
        )

   def test_api_multiply(self):
    # Define the URL for the multiplication API
    url = f"{BASE_URL_MOCK}/calc/multiply/8/8"
    
    # Send the request and get the response
    response = urlopen(url, timeout=DEFAULT_TIMEOUT)
    
    # Assert that the response status is OK (200)
    self.assertEqual(
        response.status, http.client.OK, f"Error en la petición API a {url}"
    )
    
    # Assert that the response content is the correct multiplication result (64)
    self.assertEqual(
        response.read().decode(), "64", "ERROR en la multiplicación"
    )

def test_api_divide_by_zero(self):
    # Define the URL for the division API where the divisor is zero
    url = f"{BASE_URL_MOCK}/calc/divide/64/0"
    
    # Send the request and get the response
    response = urlopen(url, timeout=DEFAULT_TIMEOUT)
    
    # Assert that the response status is 406 (Not Acceptable) due to division by zero
    self.assertEqual(
        response.status, 406, f"Error en la petición API a {url}"
    )
    
    # Optionally, check if the response body contains a relevant error message
    self.assertIn(
        "Cannot divide by zero", response.read().decode(), "ERROR: No se manejó la división por cero correctamente"
    )

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
