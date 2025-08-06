import web3
from web3 import Account
from web3.middleware import geth_poa_middleware

from app.chains import GeneralSignerChains
from app.config import settings

evm_chain = GeneralSignerChains.BeraChain
assert evm_chain.is_evm_chain

wallet_private_key = settings.EVM_PRIVATE_KEY_HEX
wallet_account: Account = web3.Account.from_key(wallet_private_key)
wallet_address = wallet_account.address


Web3Provider = web3.Web3.HTTPProvider(evm_chain.rpc_endpoint)
w3 = web3.Web3(Web3Provider)
if evm_chain.value != GeneralSignerChains.Ethereum.value:
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
nonce = w3.eth.getTransactionCount(wallet_address)

route_id = "fc766e46-ceed-4a62-9b25-449b5dfc67c0"

to = "0x549943e04f40284185054145c6E4e9568C1D3241"
amount_in_wei = web3.Web3.toWei("0", "wei")
gas = web3.Web3.toWei("80000", "wei")
gasPrice = w3.toWei("6288", "wei")
data = "0x095ea7b30000000000000000000000000000000000001ff3684f28c67538d4d072c227340000000000000000000000000000000000000000000000000000000000023280"
# gasLimit = "80000"

txn_dict = {
    "from": wallet_address,
    "to": to,
    "value": amount_in_wei,
    "gas": gas,
    "gasPrice": gasPrice,
    "nonce": nonce,
    "chainId": evm_chain.chain_id,
    "data": data
}

signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
txn_hash