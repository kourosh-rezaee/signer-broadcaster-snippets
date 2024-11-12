import web3
from web3 import Account
from web3.middleware import geth_poa_middleware

from app.chains import GeneralSignerChains
from app.config import settings

evm_chain = GeneralSignerChains.Ethereum
assert evm_chain.is_evm_chain

wallet_private_key = settings.EVM_PRIVATE_KEY_HEX
wallet_account: Account = web3.Account.from_key(wallet_private_key)
wallet_address = wallet_account.address


Web3Provider = web3.Web3.HTTPProvider(evm_chain.rpc_endpoint)
w3 = web3.Web3(Web3Provider)
if evm_chain.value != GeneralSignerChains.Ethereum.value:
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
nonce = w3.eth.getTransactionCount(wallet_address)

to = ""
amount_in_wei = web3.Web3.toWei("0x33", "ether")
gas = web3.Web3.toWei("2000000", "wei")
gasPrice = w3.toWei("40", "gwei")

txn_dict = {
    "to": to,
    "value": amount_in_wei,
    "gas": gas,
    "gasPrice": gasPrice,
    "nonce": nonce,
    "chainId": evm_chain.chain_id,
}

signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
