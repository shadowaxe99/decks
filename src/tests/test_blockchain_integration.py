```python
import unittest
from unittest.mock import patch
from src import blockchain_integration

class TestBlockchainIntegration(unittest.TestCase):

    @patch('src.blockchain_integration.web3')
    def test_integrateBlockchain(self, mock_web3):
        # Mocking the web3 connection
        mock_web3.HTTPProvider.return_value = True

        # Call the function
        result = blockchain_integration.integrateBlockchain()

        # Check if the function correctly called the web3 provider
        mock_web3.HTTPProvider.assert_called_once_with('http://localhost:8545')

        # Check if the function returned True
        self.assertEqual(result, True)

    @patch('src.blockchain_integration.web3')
    def test_mintNFT(self, mock_web3):
        # Mocking the web3 contract
        mock_web3.eth.contract.return_value = True

        # Call the function
        result = blockchain_integration.mintNFT('0x123', '0xabc', 'AI Character')

        # Check if the function correctly called the web3 contract
        mock_web3.eth.contract.assert_called_once()

        # Check if the function returned True
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
```