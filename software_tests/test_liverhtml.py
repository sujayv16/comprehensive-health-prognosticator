import unittest
from app import app

class TestLiverPage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_liver_page(self):
        """
        Test if the liver disease prediction page loads successfully and contains the expected content
        """
        response = self.app.get('/liver')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Liver Disease Prediction', response.data)
        self.assertIn(b'Age (years) eg: 62', response.data)
        self.assertIn(b'Total Bilirubin (mg/dL) eg: 7.3', response.data)
        self.assertIn(b'Direct Bilirubin (mg/dL) eg: 4.1', response.data)
        self.assertIn(b'Alkaline Phosphotase (IU/L) eg: 490', response.data)
        self.assertIn(b'Alamine Aminotransferase (IU/L) eg: 60', response.data)
        self.assertIn(b'Aspartate Aminotransferase (IU/L) eg: 68', response.data)
        self.assertIn(b'Total Protiens (g/dL) eg: 7.0', response.data)
        self.assertIn(b'Albumin (g/dL) eg: 3.3', response.data)
        self.assertIn(b'Albumin and Globulin Ratio eg: 0.89', response.data)
        self.assertIn(b'Select Gender', response.data)
        self.assertIn(b'Male', response.data)
        self.assertIn(b'Female', response.data)
        self.assertIn(b'Predict', response.data)
        self.assertIn(b'Developed by Sujay, Manoj, Suresh', response.data)


if __name__ == '__main__':
    unittest.main()
