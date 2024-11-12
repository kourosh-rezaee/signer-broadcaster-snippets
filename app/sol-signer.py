import requests
import base58
import base64
import json
import solders
from solders.keypair import Keypair
import solders.message
from solders.transaction import VersionedTransaction
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Processed

from .config import settings

# Constants
# WALLET_ADDRESS = "YOUR_WALLET_ADDRESS_PUBLIC_KEY"
# INPUT_MINT = "So11111111111111111111111111111111111111112"
# OUTPUT_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
# AMOUNT = 5000000
# QUOTE_URL = f"https://quote-api.jup.ag/v6/quote?inputMint={INPUT_MINT}&outputMint={OUTPUT_MINT}&amount={AMOUNT}"
# SWAP_URL = "https://quote-api.jup.ag/v6/swap"
PRIVATE_KEY = Keypair.from_bytes(bytes.fromhex(settings.SOL_PRIVATE_KEY_HEX))

# # Get quote response
# quote_response = requests.get(url=QUOTE_URL).json()

# # Prepare swap payload
# payload = {
#     "quoteResponse": quote_response,
#     "userPublicKey": WALLET_ADDRESS,
#     "wrapUnwrapSOL": True
# }

# Initialize Solana client
client = Client(endpoint=settings.SOLANA_MAINNET_ENDPOINT)
swapTransaction = "AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAQAHFcHtSXANz7ULVMlna9D0voiXTLPJB0cErSlRr4fez5ayAyNYOhJ7KcMJvfPYqK94oPRD/G9vbQ560ID421aBwKEhr9l1MuSE8vvOR5YBLDAq7oOKEupLzNSAV3BV2B0m+ylSSakjUloC7W44y9KrTJCBnHo3IpglsyswP8dK5SO1PbdaVhuqlrT5hZnIkdcW67eCFvm9ZzXM9jeWm2GwnLA97JMvKQLOwJjV2959+PWk8FY+3VnxZRBM/Pra+lqQ9krpWYIeEh0mTKpDP5CKqXW5Mhl+Ce8vWgor/IxBgBzXZ0EED+QHqrBQRqB+cbMfYZjXZcTe9r+CfdbguirL8P5363+hKuqM2gx6szKT2eIMv4wPKYf8MxSzDzwiV9Y3X4yvoZanUR/a9QD5ds7ksWU7bFocviCynC8nxWsdnf73ovpZxwGn6HH+hPhH/zcMiE3kBvntnv/GoZAjpz5t96y9yxwr9BS091kPctqXXILxhNdntcF02HM70TcUudY6VOhKS5Fzsx5EV5Rlh+Dc6vfxF3dFNKVlQED7JXKQA/zU/515xJpHmUizAarI2wAtNMaYCXD636xyznR18ndg82QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMGRm/lIRcy/+ytunLDm+e8jOW7xfcSayxDmzpAAAAABHnVW/IxwG7udMVuzmgVB/2xst6j9I5RArHNola8E48G3fbh12Whk9nL4UbO63msHLSF7V9bN5E6jPWFfv8AqVE+LF26QsO9gzDavYNO6ZflUDWJ+gBV9eCQ5OcuzAMSjJclj04kifG7PRApFI4NgwtaE5na/xCEBI572Nvp+Fm0P/on9df2SnTAmx8pWHneSwmrNt/J3VFLMhqns4zl6B0B1EYOsRhAg4kIPEb8X05v7Ab7GkxVhdl4Ee3Bgw09BQ8ABQJLUgUADwAJAxRgBAAAAAAAEwYAAQAiDhEBARBGERIABgQHASYiCxAUECEeISAdBAMkJh8hEhERJSECECEWIRcYAwgjJBUhEhERJSENBQwQIRkhGhwIByMiGyESERElIQkKECzBIJszQdacgQMDAAAAJmQAASZkAQImZAIDNAgAAAAAAADKJwAAAAAAAAoAPBEDAQAAAQkD7i6VrgJD9AwuuxENR2Qh6NPvr8Yw1bO0CLZDlNMTKUYE3N7i4AXfyuXd5hiZ8R6ukZyrlWINCo64a1IlbLKb/q7sKoEZg/iwb29nBAMNDAEBEcUSDv0nLn7lNPmvUU/7elwGAgUu2VVs5P7vvkzRymG5BA8ODVkA"
# Decode and sign the transaction
raw_transaction = VersionedTransaction.from_bytes(base64.b64decode(swapTransaction))
signature = PRIVATE_KEY.sign_message(solders.message.to_bytes_versioned(raw_transaction.message))
signed_txn = VersionedTransaction.populate(raw_transaction.message, [signature])

# Send the signed transaction
opts = TxOpts(skip_preflight=False, preflight_commitment=Processed)
result = client.send_raw_transaction(txn=bytes(signed_txn), opts=opts)

# Extract and print the transaction ID
transaction_id = json.loads(result.to_json())['result']
print(f"Transaction sent: https://explorer.solana.com/tx/{transaction_id}")