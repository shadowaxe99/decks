```python
from web3 import Web3
from solcx import compile_source
from src.blockchain_integration import integrateBlockchain

class NFTMintingManagement:
    def __init__(self):
        self.web3 = integrateBlockchain()
        self.contract = None
        self.nftToken = None

    def compile_contract(self, contract_path):
        with open(contract_path, 'r') as file:
            contract_source_code = file.read()

        compiled_sol = compile_source(contract_source_code)
        contract_id, contract_interface = compiled_sol.popitem()
        return contract_interface

    def deploy_contract(self, contract_interface, account):
        Contract = self.web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
        tx_hash = Contract.constructor().transact({'from': account})
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return self.web3.eth.contract(address=tx_receipt['contractAddress'], abi=contract_interface['abi'])

    def mint_nft(self, account, ai_character):
        tx_hash = self.contract.functions.mint(account, ai_character).transact({'from': account})
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        self.nftToken = self.contract.functions.tokenOfOwnerByIndex(account, 0).call()
        return self.nftToken

    def list_nft(self, account, price):
        tx_hash = self.contract.functions.listToken(self.nftToken, price).transact({'from': account})
        self.web3.eth.waitForTransactionReceipt(tx_hash)

    def purchase_nft(self, buyer_account, seller_account, price):
        tx_hash = self.contract.functions.purchaseToken(self.nftToken).transact({'from': buyer_account, 'value': price})
        self.web3.eth.waitForTransactionReceipt(tx_hash)
        return self.contract.functions.ownerOf(self.nftToken).call() == buyer_account
```