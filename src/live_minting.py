```python
from web3 import Web3
from solcx import compile_source
from src.blockchain_integration import integrateBlockchain
from src.ai_model_integration import integrateAIModel

def mintNFT(investor, aiCharacter):
    """
    Function to mint a new NFT for the given AI character.
    """
    # Connect to the Ethereum blockchain
    web3 = integrateBlockchain()

    # Compile the smart contract
    with open('NFTContract.sol', 'r') as file:
        contract_source_code = file.read()
    compiled_sol = compile_source(contract_source_code)
    contract_interface = compiled_sol['<stdin>:NFTContract']

    # Deploy the contract
    NFTContract = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    tx_hash = NFTContract.constructor().transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    nft_contract = web3.eth.contract(address=tx_receipt['contractAddress'], abi=contract_interface['abi'])

    # Mint the NFT
    tx_hash = nft_contract.functions.mint(investor, aiCharacter).transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    return tx_receipt['contractAddress']

def liveMinting(investorPreferences):
    """
    Function to perform live minting of an AI character NFT.
    """
    # Generate a new AI character based on the investor's preferences
    aiCharacter = integrateAIModel(investorPreferences)

    # Mint the NFT
    nftToken = mintNFT(investorPreferences['name'], aiCharacter)

    return nftToken
```