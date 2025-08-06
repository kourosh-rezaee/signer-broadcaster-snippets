import base64
import os

import base58
import requests
import solana.transaction as txlib
from solana.rpc.api import Client
from solders.message import Message, MessageV0
from solders.signature import Signature
from solders.transaction import Transaction, VersionedTransaction

from app.config import settings



client = Client(endpoint=settings.SOLANA_MAINNET_ENDPOINT)


def get_b58_tx(tx_sig_str: str):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTransaction",
        "params": [
        tx_sig_str,
        {
            "maxSupportedTransactionVersion": 0,
            "encoding": "base58"
        }
        ]
    }
    
    res = requests.post(settings.SOLANA_MAINNET_ENDPOINT, json=payload)
    return res.json().get("result").get("transaction")[0]


# def get_b64_sol_tx_from_sig(tx_sig_str: str):
#     tx_sig = Signature.from_string(tx_sig_str)
#     tx_resp = client.get_transaction(tx_sig, max_supported_transaction_version=0)
#     transaction = tx_resp.value.transaction.transaction
#     sol_tx = txlib.Transaction.from_solders(transaction)
#     return base64.b64encode(sol_tx.serialize(verify_signatures=False))



sig = "YUXp3Xc5fMUDTgJcxqqhPFxKmXbqCSQh8gE59QmDvNC2UnDDerWRB7F4DqwLgAWqf1ShCvd4CrqnUwFpyRn3Jv9"

# get_b58_sol_tx_from_sig(sig)
