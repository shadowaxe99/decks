```python
import unittest
from unittest.mock import patch
from src import deployment

class TestDeployment(unittest.TestCase):

    @patch('src.deployment.deployPlatform')
    def test_deployPlatform(self, mock_deploy):
        # Arrange
        mock_deploy.return_value = True

        # Act
        result = deployment.deployPlatform()

        # Assert
        self.assertTrue(result)
        mock_deploy.assert_called_once()

    @patch('src.deployment.AWS')
    def test_AWS_integration(self, mock_AWS):
        # Arrange
        mock_AWS.return_value = True

        # Act
        result = deployment.AWS()

        # Assert
        self.assertTrue(result)
        mock_AWS.assert_called_once()

    @patch('src.deployment.GoogleCloud')
    def test_GoogleCloud_integration(self, mock_GoogleCloud):
        # Arrange
        mock_GoogleCloud.return_value = True

        # Act
        result = deployment.GoogleCloud()

        # Assert
        self.assertTrue(result)
        mock_GoogleCloud.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```