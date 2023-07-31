```python
import unittest
from unittest.mock import patch
from src import backend_management

class TestBackendManagement(unittest.TestCase):

    @patch('src.backend_management.manageBackend')
    def test_manage_backend(self, mock_manage_backend):
        # Mocking the manageBackend function
        mock_manage_backend.return_value = True

        # Test data
        test_investor = {
            'name': 'John Doe',
            'preferences': {
                'ai_character': 'Einstein',
                'nft_preference': 'Rare'
            },
            'owned_nfts': []
        }

        test_ai_character = {
            'name': 'Einstein',
            'traits': ['Intelligent', 'Witty', 'Knowledgeable'],
            'conversation_history': []
        }

        test_nft = {
            'owner': 'John Doe',
            'minting_date': '2022-01-01',
            'ai_character': 'Einstein'
        }

        # Call the function with test data
        result = backend_management.manageBackend(test_investor, test_ai_character, test_nft)

        # Assert the function was called with the correct arguments
        mock_manage_backend.assert_called_with(test_investor, test_ai_character, test_nft)

        # Assert the function returned the expected result
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
```