```python
import unittest
from unittest.mock import patch
from src.live_minting import mintNFT

class TestLiveMinting(unittest.TestCase):

    @patch('src.live_minting.mintNFT')
    def test_mintNFT(self, mock_mintNFT):
        # Mocking the mintNFT function
        mock_mintNFT.return_value = True

        # Test data
        aiCharacter = {
            "name": "AI Character",
            "traits": ["intelligent", "witty"],
            "conversation_history": []
        }
        investor = {
            "name": "Investor",
            "preferences": ["intelligent", "witty"],
            "owned_NFTs": []
        }

        # Call the function with test data
        result = mintNFT(aiCharacter, investor)

        # Assert the function was called with correct arguments
        mock_mintNFT.assert_called_with(aiCharacter, investor)

        # Assert the function returned the expected result
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
```