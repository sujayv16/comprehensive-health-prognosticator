import unittest
from app import app

class FlaskTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_diabetes(self):
        response = self.app.get('/diabetes')
        self.assertEqual(response.status_code, 200)

    def test_cancer(self):
        response = self.app.get('/cancer')
        self.assertEqual(response.status_code, 200)

    def test_heart(self):
        response = self.app.get('/heart')
        self.assertEqual(response.status_code, 200)

    def test_kidney(self):
        response = self.app.get('/kidney')
        self.assertEqual(response.status_code, 200)

    def test_liver(self):
        response = self.app.get('/liver')
        self.assertEqual(response.status_code, 200)

    def test_predict_diabetes(self):
        data = {
            'pregnancies': 6,
            'glucose': 148,
            'bloodpressure': 72,
            'skinthickness': 35,
            'insulin': 0,
            'bmi': 33.6,
            'dpf': 0.627,
            'age': 50
        }
        response = self.app.post('/predict', data=data)
        self.assertEqual(response.status_code, 200)

    def test_predict_cancer(self):
        data = {
            'radius_mean': 17.99,
            'texture_mean': 10.38,
            'perimeter_mean': 122.8,
            'area_mean': 1001,
            'smoothness_mean': 0.1184,
            'compactness_mean': 0.2776,
            'concavity_mean': 0.3001,
            'concave points_mean': 0.1471,
            'symmetry_mean': 0.2419,
            'radius_se': 1.095,
            'perimeter_se': 8.589,
            'area_se': 153.4,
            'compactness_se': 0.006399,
            'concavity_se': 0.04904,
            'concave points_se': 0.05373,
            'fractal_dimension_se': 0.006193,
            'radius_worst': 25.38,
            'texture_worst': 17.33,
            'perimeter_worst': 184.6,
            'area_worst': 2019,
            'smoothness_worst': 0.1622,
            'compactness_worst': 0.6656,
            'concavity_worst': 0.7119,
            'concave points_worst': 0.2654,
            'symmetry_worst': 0.4601,
            'fractal_dimension_worst': 0.1189
        }
        response = self.app.post('/predict', data=data)
        self.assertEqual(response.status_code, 200)

    def test_predict_heart(self):
        data = {
            'age': 63,
            'sex': 1,
            'cp': 3,
            'trestbps': 145,
            'chol': 233,
            'fbs': 1,
            'restecg': 0,
            'thalach': 150,
            'exang': 0,
            'oldpeak': 2.3,
            'slope': 0,
            'ca': 0,
            'thal': 1
        }
        response = self.app.post('/predict', data=data)
        self.assertEqual(response.status_code, 200)

    def test_predict_liver(self):
        data = {
            'Age': 65,
            'Total_Bilirubin': 0.7,
            'Direct_Bilirubin': 0.1,
            'Alkaline_Phosphotase': 187,
            'Alamine_Aminotransferase': 16,
            'Aspartate_Aminotransferase': 18,
            'Total_Protiens': 6.8,
            'Albumin': 3.3,
            'Albumin_and_Globulin_Ratio': 0.9,
            'Gender_Male': 0
        }
        response = self.app.post('/predict', data=data)
        self.assertEqual(response.status_code, 200)

    def test_predict_kidney(self):
        data = {
            'age': 150,
            'bp': 80,
            'al': 1.02,
            'su': 1,
            'rbc': 1,
            'pc': 1,
            'pcc': 0,
            'ba': 0,
            'bgr': 121,
            'bu': 36,
            'sc': 1.2,
            'pot': 15.2,
            'wc': 7800,
            'htn': 1,
            'dm': 1,
            'cad': 1,
            'pe': 1,
            'ane': 1
        }
        response = self.app.post('/predict', data=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
