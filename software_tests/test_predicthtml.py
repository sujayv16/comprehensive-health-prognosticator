import unittest
from flask import Flask, render_template_string
from unittest.mock import patch

class TestPredictHTML(unittest.TestCase):
    def test_predict_healthy(self):
        app = Flask(__name__)
        with app.test_request_context():
            prediction = 0  # Assuming prediction result for healthy
            with patch('flask.templating._render') as mock_render:
                with patch('flask.helpers.url_for') as mock_url_for:
                    mock_url_for.return_value = '/'
                    render_template_string(
                        """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Result</title>
                            <!-- Jquery CDN -->
                            <script src="https://code.jquery.com/jquery-2.2.4.js"
                            integrity="sha256-iT6Q9iMJYuQiMWNd9lDyBUStIq/8PuOW33aOqmvFpqI=" crossorigin="anonymous"></script>
                            
                            <!-- Font Awesome Link -->
                            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css">
                            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
                            <!-- CSS -->
                            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
                        </head>
                        <body class="result_main">
                            <h3 class="result_heading">Result</h3>
                            <div class="result_row">
                                {% if prediction==1 %}
                                <div class="suffer">Apologies, it appears you're unwell. Please see a doctor for proper care and assistance. Your health is important..</div>
                                {% elif prediction==0 %}
                                <div class="not_suffer">GREAT!! You are healthy.</div>
                                {% endif %}
                            </div>
                            <div class="result_home">
                                <div class="return"><a href="{{ url_for('index') }}">Home</a></div>
                            </div>
                        </body>
                        </html>
                        """,
                        prediction=prediction
                    )
                    mock_render.assert_called_once()

    def test_predict_unhealthy(self):
        app = Flask(__name__)
        with app.test_request_context():
            prediction = 1  # Assuming prediction result for unhealthy
            with patch('flask.templating._render') as mock_render:
                with patch('flask.helpers.url_for') as mock_url_for:
                    mock_url_for.return_value = '/'
                    render_template_string(
                        """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Result</title>
                            <!-- Jquery CDN -->
                            <script src="https://code.jquery.com/jquery-2.2.4.js"
                            integrity="sha256-iT6Q9iMJYuQiMWNd9lDyBUStIq/8PuOW33aOqmvFpqI=" crossorigin="anonymous"></script>
                            
                            <!-- Font Awesome Link -->
                            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css">
                            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
                            <!-- CSS -->
                            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
                        </head>
                        <body class="result_main">
                            <h3 class="result_heading">Result</h3>
                            <div class="result_row">
                                {% if prediction==1 %}
                                <div class="suffer">Apologies, it appears you're unwell. Please see a doctor for proper care and assistance. Your health is important..</div>
                                {% elif prediction==0 %}
                                <div class="not_suffer">GREAT!! You are healthy.</div>
                                {% endif %}
                            </div>
                            <div class="result_home">
                                <div class="return"><a href="{{ url_for('index') }}">Home</a></div>
                            </div>
                        </body>
                        </html>
                        """,
                        prediction=prediction
                    )
                    mock_render.assert_called_once()

    def test_predict_url_for_error(self):
        app = Flask(__name__)
        with app.test_request_context():
            prediction = 1  # Assuming prediction result for unhealthy
            with patch('flask.templating._render') as mock_render:
                with patch('flask.helpers.url_for') as mock_url_for:
                    mock_url_for.side_effect = Exception("Error occurred in url_for")
                    render_template_string(
                        """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Result</title>
                            <!-- Jquery CDN -->
                            <script src="https://code.jquery.com/jquery-2.2.4.js"
                            integrity="sha256-iT6Q9iMJYuQiMWNd9lDyBUStIq/8PuOW33aOqmvFpqI=" crossorigin="anonymous"></script>
                            
                            <!-- Font Awesome Link -->
                            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css">
                            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
                            <!-- CSS -->
                            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
                        </head>
                        <body class="result_main">
                            <h3 class="result_heading">Result</h3>
                            <div class="result_row">
                                {% if prediction==1 %}
                                <div class="suffer">Apologies, it appears you're unwell. Please see a doctor for proper care and assistance. Your health is important..</div>
                                {% elif prediction==0 %}
                                <div class="not_suffer">GREAT!! You are healthy.</div>
                                {% endif %}
                            </div>
                            <div class="result_home">
                                <div class="return"><a href="{{ url_for('index') }}">Home</a></div>
                            </div>
                        </body>
                        </html>
                        """,
                        prediction=prediction
                    )
                    mock_render.assert_called_once()

if __name__ == '__main__':
    unittest.main()
