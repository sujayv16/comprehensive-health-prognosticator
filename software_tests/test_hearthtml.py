import unittest
from app import app

class TestHeartPage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_heart_page(self):
        """
        Test if the heart disease prediction page loads successfully and contains the expected content
        """
        response = self.app.get('/heart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Heart Disease Prediction', response.data)
        self.assertIn(b'Age eg: 37', response.data)
        self.assertIn(b'Sex', response.data)
        self.assertIn(b'Chest pain type', response.data)
        self.assertIn(b'Resting blood pressure in mm Hg eg: 130', response.data)
        self.assertIn(b'Serum cholestoral in mg/dl eg: 250', response.data)
        self.assertIn(b'Fasting blood sugar 120 mg/dl', response.data)
        self.assertIn(b'Resting electrocardiographic results', response.data)
        self.assertIn(b'Maximum heart rate achieved eg: 187', response.data)
        self.assertIn(b'Exercise induced angina', response.data)
        self.assertIn(b'ST depression induced by exercise relative to rest eg: 3.5', response.data)
        self.assertIn(b'The slope of the peak exercise ST segment', response.data)
        self.assertIn(b'Number of major vessels colored by flourosopy', response.data)
        self.assertIn(b'Thal', response.data)
        self.assertIn(b'Developed by Sujay, Manoj, Suresh', response.data)


if __name__ == '__main__':
    unittest.main()
