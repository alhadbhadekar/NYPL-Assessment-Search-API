import unittest 
from src.dataretriever.dataretriever import dataretriever
from unittest.mock import patch
import os
import json


class TestDataretriever(unittest.TestCase):
    def setUp(self):
        os.environ['NYPL_URL'] = 'https://api.repo.nypl.org/api/v2/items/search'

    def test_dataretriever_ShouldReturnValidDataWhenStatusCodeOk(self):

        # Arrange
        with patch('src.dataretriever.dataretriever.requests.get') as mocked_get:
            path = os.getcwd() + "/tests/mocks/hellosearchmock.json"
            with open(path, 'r', encoding='utf-8') as f:
                json_object = json.loads(f.read())
                mocked_get.return_value.text = json.dumps(json_object)
                mocked_get.return_value.status_code = 200

                # Act
                response, status_code = dataretriever("sampletext")

                # Assert
                self.assertEqual(status_code, 200)
                self.assertEqual(response, json_object['nyplAPI']['response']['result'])
    
    def test_dataretriever_ShouldReturnNoneWhenStatusCodeNotOk(self):

        # Arrange
        with patch('src.dataretriever.dataretriever.requests.get') as mocked_get:
            mocked_get.return_value.status_code = 403

            # Act
            response, status_code = dataretriever("sampletext")

            # Assert
            self.assertEqual(status_code, 403)
            self.assertEqual(response, None)

    def tearDown(self):
        os.environ.pop("NYPL_URL")

if __name__ == '__main__':
    unittest.main()