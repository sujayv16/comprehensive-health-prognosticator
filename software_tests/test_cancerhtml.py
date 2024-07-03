import unittest
from app import app

class TestCancerPage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_cancer_page(self):
        """
        Test if the cancer page loads successfully and contains the expected content
        """
        response = self.app.get('/cancer')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cancer Prediction', response.data)
        self.assertIn(b'Radius Mean (5-30)', response.data)
        self.assertIn(b'Texture Mean (5-45)', response.data)
        self.assertIn(b'Perimeter Mean (40-200)', response.data)
        self.assertIn(b'Area Mean (100-2600)', response.data)
        self.assertIn(b'Smoothness Mean (0-0.2)', response.data)
        self.assertIn(b'Compactness Mean (0-0.5)', response.data)
        self.assertIn(b'Concavity Mean (0-1)', response.data)
        self.assertIn(b'Concave Points Mean (0-0.5)', response.data)
        self.assertIn(b'Symmetry Mean (0-0.5)', response.data)
        self.assertIn(b'Fractal Dimension Mean (0-0.1)', response.data)
        self.assertIn(b'Radius SE (0-5)', response.data)
        self.assertIn(b'Perimeter SE (0.5-30)', response.data)
        self.assertIn(b'Area SE (5-600)', response.data)
        self.assertIn(b'Smoothness SE (0-0.1)', response.data)
        self.assertIn(b'Compactness SE (0-0.5)', response.data)
        self.assertIn(b'Concavity SE (0-0.5)', response.data)
        self.assertIn(b'Concave Points SE (0-0.1)', response.data)
        self.assertIn(b'Symmetry SE (0-0.1)', response.data)
        self.assertIn(b'Fractal Dimension SE (0-0.1)', response.data)
        self.assertIn(b'Radius Worst (5-40)', response.data)
        self.assertIn(b'Texture Worst (10-60)', response.data)
        self.assertIn(b'Perimeter Worst (40-300)', response.data)
        self.assertIn(b'Area Worst (100-4500)', response.data)
        self.assertIn(b'Smoothness Worst (0-1)', response.data)
        self.assertIn(b'Compactness Worst (0-5)', response.data)
        self.assertIn(b'Concavity Worst (0-5)', response.data)
        self.assertIn(b'Concave Points Worst (0-0.5)', response.data)
        self.assertIn(b'Symmetry Worst (0-1)', response.data)
        self.assertIn(b'Fractal Dimension Worst (0-0.5)', response.data)
        self.assertIn(b'Developed by Sujay, Manoj, Suresh', response.data)


if __name__ == '__main__':
    unittest.main()
