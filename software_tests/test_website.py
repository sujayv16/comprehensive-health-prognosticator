import unittest
from flask import Flask
from app import app

class TestWebsite(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        

    def test_heart_page(self):
        """
        Test the heart disease prediction page
        """
        response = self.app.get('/heart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Chest pain type', response.data)
        self.assertIn(b'Maximum heart rate achieved', response.data)
        self.assertIn(b'Predict', response.data)

    def test_kidney_page(self):
        """
        Test the kidney disease prediction page
        """
        response = self.app.get('/kidney')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Blood Pressure', response.data)
        self.assertIn(b'White Blood Cell Count', response.data)
        self.assertIn(b'Predict', response.data)

    def test_liver_page(self):
        """
        Test the liver disease prediction page
        """
        response = self.app.get('/liver')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Albumin', response.data)
        self.assertIn(b'Albumin and Globulin Ratio', response.data)
        self.assertIn(b'Predict', response.data)

   
if __name__ == "__main__":
    unittest.main()
