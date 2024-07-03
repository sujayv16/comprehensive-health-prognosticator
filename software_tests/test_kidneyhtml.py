import unittest
from app import app

class TestKidneyPage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_kidney_page(self):
        """
        Test if the kidney disease prediction page loads successfully and contains the expected content
        """
        response = self.app.get('/kidney')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kidney Disease Prediction', response.data)
        self.assertIn(b'Age (years) [2, 90]', response.data)
        self.assertIn(b'Blood Pressure (mm/Hg) [50, 200]', response.data)
        self.assertIn(b'Albumin (g/dL) [0, 10]', response.data)
        self.assertIn(b'Sugar (g/dL) [0, 10]', response.data)
        self.assertIn(b'Red Blood Cells (million cells/mcL) [4, 7]', response.data)
        self.assertIn(b'Pus Cell (cells/cubic millimeter) [0, 5]', response.data)
        self.assertIn(b'Pus Cell Clumps (0: Not present, 1: Present)', response.data)
        self.assertIn(b'Bacteria in Urine (0: Not present, 1: Present)', response.data)
        self.assertIn(b'Blood Glucose Random (mg/dL) [20, 500]', response.data)
        self.assertIn(b'Blood Urea (mg/dL) [1, 400]', response.data)
        self.assertIn(b'Serum Creatinine (mg/dL) [0, 100]', response.data)
        self.assertIn(b'Potassium (mEq/L) [1, 100]', response.data)
        self.assertIn(b'White Blood Cell Count (cells/cu mm) [1000, 30000]', response.data)
        self.assertIn(b'Hypertension: No', response.data)
        self.assertIn(b'Diabetes Mellitus: No', response.data)
        self.assertIn(b'Coronary Artery Disease: No', response.data)
        self.assertIn(b'Pedal Edema: No', response.data)
        self.assertIn(b'Anemia: No', response.data)
        self.assertIn(b'Predict', response.data)
        self.assertIn(b'Developed by Sujay, Manoj, Suresh', response.data)


if __name__ == '__main__':
    unittest.main()
