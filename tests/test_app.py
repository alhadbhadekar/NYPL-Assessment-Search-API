import unittest 
from unittest.mock import patch
import os
import json
from src import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        os.environ['NYPL_URL'] = 'https://api.repo.nypl.org/api/v2/items/search'

    def test_pathexists_checkcontenttype_responsedata(self):
        
        # Arrange
        with patch('src.dataretriever.dataretriever.requests.get') as mocked_get:
            path = os.getcwd() + "/tests/mocks/hellosearchmock.json"
            with open(path, 'r', encoding='utf-8') as f:
                json_object = json.loads(f.read())
                mocked_get.return_value.text = json.dumps(json_object)
                mocked_get.return_value.status_code = 200
                app = create_app()

                tester_app = app.test_client(self)

                # Act
                response = tester_app.get("/api/v1/search/hello")

                status = response.status_code

                # Assert
                self.assertEqual(status, 200)
                self.assertEqual(response.content_type, "application/json")
                self.assertTrue(b'result' in response.data)
    
    def test_app_shouldReturnErrorWhenStatusCodeNotOk(self):

        # Arrange
        with patch('src.dataretriever.dataretriever.requests.get') as mocked_get:
            path = os.getcwd() + "/tests/mocks/hellosearchmock.json"
            with open(path, 'r', encoding='utf-8') as f:
                json_object = json.loads(f.read())
                mocked_get.return_value.text = json.dumps(json_object)
                mocked_get.return_value.status_code = 500
                app = create_app()

                tester_app = app.test_client(self)

                # Act
                response = tester_app.get("/api/v1/search/hello")

                status = response.status_code

                # Arrange
                self.assertEqual(status, 500)
                self.assertEqual(response.content_type, "application/json")
                self.assertTrue(b'error' in response.data)
    
    def test_app_shouldReturnErrorForBadUserInput(self):

        # Arrange
        
        app = create_app()

        tester_app = app.test_client(self)

        # Act
        response = tester_app.get("/api/v1/search/hello$")

        status = response.status_code

        # Arrange
        self.assertEqual(status, 400)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'error' in response.data)
    
    def tearDown(self):
        os.environ.pop("NYPL_URL")


if __name__ == '__main__':
    unittest.main()