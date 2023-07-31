```python
from web3 import Web3
from solcx import compile_standard

class BlockchainIntegration:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider('http://localhost:8545')) # Connect to Ethereum node
        self.contract_address = None
        self.contract = None

    def compile_contract(self, contract_path):
        with open(contract_path, 'r') as file:
            contract_source_code = file.read()

        compiled_sol = compile_standard({
            "language": "Solidity",
            "sources": {
                "Contract.sol": {
                    "content": contract_source_code
                }
            },
            "settings":
                {
                    "outputSelection": {
                        "*": {
                            "*": [
                                "metadata", "evm.bytecode"
                                , "evm.bytecode.sourceMap"
                            ]
                        }
                    }
                }
        })

        bytecode = compiled_sol['contracts']['Contract.sol']['Contract']['evm']['bytecode']['object']
        abi = json.loads(compiled_sol['contracts']['Contract.sol']['Contract']['metadata'])['output']['abi']

        return bytecode, abi

    def deploy_contract(self, bytecode, abi):
        contract = self.web3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = contract.constructor().transact()
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        self.contract_address = tx_receipt['contractAddress']
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=abi)

    def mint_nft(self, ai_character):
        tx_hash = self.contract.functions.mint(ai_character).transact()
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def get_nft(self, token_id):
        nft = self.contract.functions.get(token_id).call()
        return nft

blockchain_integration = BlockchainIntegration()
bytecode, abi = blockchain_integration.compile_contract('path_to_your_contract')
blockchain_integration.deploy_contract(bytecode, abi)
```