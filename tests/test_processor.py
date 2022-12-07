import unittest 
from src.processor.processor import processor
from unittest.mock import patch
import os
import json
from src import create_app

class TestFormatter(unittest.TestCase):

    def setUp(self):
        os.environ['NYPL_URL'] = 'https://api.repo.nypl.org/api/v2/items/search'

    def test_processor_ShouldReturnValidData(self):

        # Arrange
        with patch('src.dataretriever.dataretriever.requests.get') as mocked_get:
            path = os.getcwd() + "/tests/mocks/hellosearchmock.json"
            with open(path, 'r', encoding='utf-8') as f:
                json_object = json.loads(f.read())
                mocked_get.return_value.text = json.dumps(json_object)
                mocked_get.return_value.status_code = 200

                path = os.getcwd() + "/tests/mocks/formattermock.json"
                with open(path, 'r', encoding='utf-8') as f:
                    json_object_formattermock = json.loads(f.read())

                    # Act
                    response, status_code = processor("sampletext")

                    # Assert
                    self.assertEqual(response, json_object_formattermock)
                    self.assertEqual(status_code, 200)
    
    def test_processor_ShouldReturnEmptyDataWhenStatusCodeNotOk(self):
        
        # Arrange
        with patch('src.dataretriever.dataretriever.requests.get') as mocked_get:
            app = create_app()
            with app.app_context():
                mocked_get.return_value.status_code = 500

                # Act
                response, status_code = processor("sampletext")

                # Assert
                self.assertEqual(response['result'], [])
                self.assertEqual(status_code, 500)
    
    def test_processor_ShouldReturnEmptyDataWhenNumberOfResultsEmpty(self):

        # Arrange
        with patch('src.dataretriever.dataretriever.requests.get') as mocked_get:
            app = create_app()
            with app.app_context():
                path = os.getcwd() + "/tests/mocks/noresults.json"
                with open(path, 'r', encoding='utf-8') as f:
                    json_object = json.loads(f.read())
                    mocked_get.return_value.text = json.dumps(json_object)
                    mocked_get.return_value.status_code = 200

                    # Act
                    response, status_code = processor("sampletext")

                    # Assert
                    self.assertEqual(response['result'], [])
                    self.assertEqual(status_code, 200)

    def tearDown(self):
        os.environ.pop("NYPL_URL")

if __name__ == '__main__':
    unittest.main()