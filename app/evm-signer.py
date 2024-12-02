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


# },
# "transaction": {
# "actions": null,
# "amount": "0",
# "chain": "ETH",
# "data": "0x095ea7b3000000000000000000000000d37bbe5744d730a1d98d8dc97c42f0ca46ad71460000000000000000000000000000000000000000000000000000000000e4e1c0",
# "feeRate": "16852000000",
# "gasLimit": "80000",
# "gasPrice": "16852000000",
# "memo": null,
# "receiverId": null,
# "recipient": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
# "routeId": null,
# "signerId": null,
# "tradeId": "24",
# "unsignedStdTx": null,
# "txType": "approval"
# }
# },
# hash: 0x2b7f7057d3cc9e6796bf9423aa6abab09f98b61d07755809eeda5a6cc1488865

route_id = "772f0203-7ac9-48ac-a713-b845c0eac1ee"

to = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
amount_in_wei = web3.Web3.toWei("0", "ether")
gas = web3.Web3.toWei("80000", "wei")
gasPrice = w3.toWei("16852000000", "wei")
data = "0x095ea7b3000000000000000000000000d37bbe5744d730a1d98d8dc97c42f0ca46ad71460000000000000000000000000000000000000000000000000000000000e4e1c0"
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