import unittest
from app import app

class TestDiabetesPage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_diabetes_page(self):
        """
        Test if the diabetes page loads successfully and contains the expected content
        """
        response = self.app.get('/diabetes')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Diabetes Prediction', response.data)
        self.assertIn(b'Select number of pregnancies', response.data)
        self.assertIn(b'Glucose (mg/dL) eg. 80', response.data)
        self.assertIn(b'Blood Pressure (mmHg) eg. 80', response.data)
        self.assertIn(b'Skin Thickness (mm) eg. 20', response.data)
        self.assertIn(b'Insulin Level (IU/mL) eg. 80', response.data)
        self.assertIn(b'Body Mass Index (kg/m\xc2\xb2) eg. 23.1', response.data)
        self.assertIn(b'Diabetes Pedigree Function eg. 0.52', response.data)
        self.assertIn(b'Age (years) eg. 34', response.data)
        self.assertIn(b'Developed by sujay,manoj,suresh', response.data)


if __name__ == '__main__':
    unittest.main()
