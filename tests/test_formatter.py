import unittest 
from src.formatter.formatter import formatter
from unittest.mock import patch
import os
import json


class TestFormatter(unittest.TestCase):

    def test_formatter_ShouldReturnValidData(self):

        # Arrange
        with patch('src.formatter.formatter') as mocked_get:
            path = os.getcwd() + "/tests/mocks/formattermock.json"
            with open(path, 'r', encoding='utf-8') as f:
                json_object_formattermock = json.loads(f.read())
                mocked_get.return_value = json_object_formattermock

                path = os.getcwd() + "/tests/mocks/hellosearchmock.json"
                with open(path, 'r', encoding='utf-8') as dataretrieverresponse:
                    json_object_dataretrieverresponse = json.loads(dataretrieverresponse.read())
                    response = {
                        'result': []
                    }

                    # Act
                    response = formatter(response, json_object_dataretrieverresponse['nyplAPI']['response']['result'])

                    # Assert
                    self.assertEqual(response, json_object_formattermock)
    
    def test_formatter_ShouldReturnValidDataWhenFewEntriesMissing(self):

        # Arrange
        with patch('src.formatter.formatter') as mocked_get:
            path = os.getcwd() + "/tests/mocks/formatterfewdetailsmissingmock.json"
            with open(path, 'r', encoding='utf-8') as f:
                json_object_formattermock = json.loads(f.read())
                mocked_get.return_value = json_object_formattermock

                path = os.getcwd() + "/tests/mocks/hellosearchmissingfewdetailsmock.json"
                with open(path, 'r', encoding='utf-8') as dataretrieverresponse:
                    json_object_dataretrieverresponse = json.loads(dataretrieverresponse.read())
                    response = {
                        'result': []
                    }

                    # Act
                    response = formatter(response, json_object_dataretrieverresponse['nyplAPI']['response']['result'])

                    # Assert
                    self.assertEqual(response, json_object_formattermock)


if __name__ == '__main__':
    unittest.main()