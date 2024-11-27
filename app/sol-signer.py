import base64
import json

import base58
import requests
import solders
import solders.message
from solana.rpc.api import Client
from solana.rpc.commitment import Processed
from solana.rpc.types import TxOpts
from solders.keypair import Keypair
from solders.transaction import VersionedTransaction

from app.config import settings

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
swapTransaction = "AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAQAIDCwtrbkIwjPjBjh+CHzfmYint+YqkpV7Ton3rAVRJ+V4AS7Zk9NBlq+3xS0bd3vGU9v9pVVenqCz3s7wLO4rynxMJr3bWPKiTcq1Klua/ujWAO1+iSP5aEUMsfk4vV8PZnoe2jfjuDG7A9fUe36Or7ry0mkrhvCbNUYVbBNOrQpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADBkZv5SEXMv/srbpyw5vnvIzlu8X3EmssQ5s6QAAAAAR51VvyMcBu7nTFbs5oFQf9sbLeo/SOUQKxzaJWvBOPBpuIV/6rgYT7aH9jRhjANdrEOdwa6ztVmKDwAAAAAAEG3fbh12Whk9nL4UbO63msHLSF7V9bN5E6jPWFfv8AqU1km+5O34BvXzJYlV/JngU0ivPjN2KZsAJW1qDQihV/jJclj04kifG7PRApFI4NgwtaE5na/xCEBI572Nvp+Fm0P/on9df2SnTAmx8pWHneSwmrNt/J3VFLMhqns4zl6PEAS89QVeBak+6abW1SCvpvmy8AjBYs+z7TYV4SXkYABwUABQIlAQIACgYAAQAHBAgBAQQCAAEMAgAAAIDw+gIAAAAACAEBAREKBgADAAkECAEBBhsIAAEDBgkCCwYQCA0PDQ4MDQ0NDQ0NDQ0BAwAj5RfLl3rjrSoBAAAAB2QAAYDw+gIAAAAAxQ3mNgAAAAAsATwIAwEAAAEJAU6KB+v4M63FolqO4vFNuqKHqp123nx0KHw/qIalYDzaA7CDgAIFCA=="
# Decode and sign the transaction
raw_transaction = VersionedTransaction.from_bytes(base64.b64decode(swapTransaction))
signature = PRIVATE_KEY.sign_message(
    solders.message.to_bytes_versioned(raw_transaction.message)
)
signed_txn = VersionedTransaction.populate(raw_transaction.message, [signature])

# Send the signed transaction
opts = TxOpts(skip_preflight=False, preflight_commitment=Processed)
result = client.send_raw_transaction(txn=bytes(signed_txn), opts=opts)

# Extract and print the transaction ID
transaction_id = json.loads(result.to_json())["result"]
print(f"Transaction sent: https://explorer.solana.com/tx/{transaction_id}")
