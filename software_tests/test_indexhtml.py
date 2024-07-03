import unittest
from app import app

class TestHTMLContent(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        """
        Test if the index page loads successfully and contains the expected content
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comprehensive Health Prognosticator', response.data)
        self.assertIn(b'Machine learning based Health Prognosticator', response.data)
        self.assertIn(b'This website is built with the motive to predict various disease based on symptoms and other factors.', response.data)
        self.assertIn(b'Model Accuracy', response.data)
        self.assertIn(b'Diabetes : 97%', response.data)
        self.assertIn(b'Heart : 83.61%', response.data)
        self.assertIn(b'Kidney : 100%', response.data)
        self.assertIn(b'Liver: 78%', response.data)
        self.assertIn(b'Cancer : 94.74%', response.data)
        self.assertIn(b'Disease our webApp can predict', response.data)
        self.assertIn(b'Diabetes', response.data)
        self.assertIn(b'Heart Disease', response.data)
        self.assertIn(b'Liver Disease', response.data)
        self.assertIn(b'Kidney Disease', response.data)
        self.assertIn(b'Cancer', response.data)
        self.assertIn(b'Developed by Sujay, Manoj, Suresh', response.data)

    

if __name__ == '__main__':
    unittest.main()
