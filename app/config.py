from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    
    
    # EMV chains
    EVM_PRIVATE_KEY_HEX: str

    
    # SOLANA    
    SOL_PRIVATE_KEY_HEX: str
    SOLANA_MAINNET_ENDPOINT = "https://solanalb-rpc.xdefi.services/"
    SOLANA_TESTNET_ENDPOINT = "https://api.testnet.solana.com/"
    
    # RPC ENDPOINTS
    ETH_MAINNET_RPC_ENDPOINT = "https://rpc.flashbots.net"
    ETH_TESTNET_RPC_ENDPOINT = "https://rpc.ankr.com/eth_rinkeby"

    BSC_MAINNET_RPC_ENDPOINT = "https://bsc-dataseed1.binance.org/"
    BSC_TESTNET_RPC_ENDPOINT = "https://data-seed-prebsc-1-s3.binance.org:8545"

    POLYGON_MAINNET_RPC_ENDPOINT = "https://polygon-rpc.com"  # "https://polygon-rpc.com"
    POLYGON_TESTNET_RPC_ENDPOINT = "https://rpc.ankr.com/polygon_mumbai"

    FANTOM_MAINNET_RPC_ENDPOINT = "https://rpc.ftm.tools"
    FANTOM_TESTNET_RPC_ENDPOINT = "https://rpc.ankr.com/fantom_testnet"

    AVALANCHE_MAINNET_RPC_ENDPOINT = "https://api.avax.network/ext/bc/C/rpc"
    AVALANCHE_TESTNET_RPC_ENDPOINT = "https://api.avax-test.network/ext/bc/C/rpc"

    AURORA_MAINNET_RPC_ENDPOINT = "https://mainnet.aurora.dev"
    AURORA_TESTNET_RPC_ENDPOINT = "https://testnet.aurora.dev"

    ARBITRUM_MAINNET_RPC_ENDPOINT = "https://arb1.arbitrum.io/rpc"
    ARBITRUM_TESTNET_RPC_ENDPOINT = "https://rinkeby.arbitrum.io/rpc"

    THORCHAIN_MAINNET_ENDPOINT = "https://thornode-api.xdefi.services"
    THORCHAIN_MAINNET_BACKUP_ENDPOINT = "https://thornode.ninerealms.com"
    THORCHAIN_RPC_MAINNET_ENDPOINT = "https://rpc-proxy.xdefi.services/thornode/rpc"
    THORCHAIN_RPC_MAINNET_BACKUP_ENDPOINT = "https://rpc.thorchain.info"
    THORCHAIN_TESTNET_ENDPOINT = "https://testnet.thornode.ninerealms.com"

    # http://141.94.137.240:3030/
    # This is our node, need to be in VPN to access it!
    NEAR_MAINNET_ENDPOINT = "https://rpc.mainnet.near.org"
    NEAR_MAINNET_BACKUP_ENDPOINT = "https://archival-rpc.mainnet.near.org"
    NEAR_MAINNET_ARCHIVAL_ENDPOINT = "https://archival-rpc.mainnet.near.org"
    NEAR_TESTNET_ENDPOINT = "https://rpc.testnet.near.org"
    NEAR_TESTNET_ARCHIVAL_ENDPOINT = "https://archival-rpc.testnet.near.org"



    OSMOSIS_MAINNET_BACKUP_ENDPOINT = "https://osmosis-mainnet-rpc.allthatnode.com:1317"
    OSMOSIS_MAINNET_ENDPOINT = "https://rpc-proxy.xdefi.services/osmosis/lcd/mainnet"
    OSMOSIS_LCD_MAINNET_ENDPOINT = "https://lcd.osmosis.zone"
    OSMOSIS_LCD_MAINNET_ENDPOINT_BACKUP = "https://lcd-osmosis.blockapsis.com"

    AXELAR_MAINNET_ENDPOINT = "https://axelar-mainnet-rpc.allthatnode.com:26657"
    AXELAR_LCD_MAINNET_ENDPOINT = "https://axelar-lcd.quickapi.com"
    AXELAR_LCD_MAINNET_ENDPOINT_BACKUP = "https://axelar-lcd.quantnode.tech"

    JUNO_LCD_MAINNET_ENDPOINT = "https://rest-juno.ecostake.com"
    JUNO_LCD_MAINNET_ENDPOINT_BACKUP = "https://api-juno.cosmos-spaces.cloud"
    CRESCENT_LCD_MAINNET_ENDPOINT = "https://crescent-mainnet-lcd.autostake.com"
    CRESCENT_LCD_MAINNET_ENDPOINT_BACKUP = "https://mainnet.crescent.network:1317"
    KUJIRA_LCD_MAINNET_ENDPOINT = "https://kujira-rest.publicnode.com"
    KUJIRA_LCD_MAINNET_ENDPOINT_BACKUP = "https://rest-kujira.ecostake.com"
    STARGAZE_LCD_MAINNET_ENDPOINT = "https://api-stargaze.pupmos.network"
    STARGAZE_LCD_MAINNET_ENDPOINT_BACKUP = "https://rest.stargaze-apis.com"
    STRIDE_LCD_MAINNET_ENDPOINT = "https://lcd-stride.whispernode.com"
    STRIDE_LCD_MAINNET_ENDPOINT_BACKUP = "https://stride-api.w3coins.io"
    MARS_LCD_MAINNET_ENDPOINT = "https://mars-rest.publicnode.com"
    MARS_LCD_MAINNET_ENDPOINT_BACKUP = "https://rest.marsprotocol.io:443"
    AKASH_LCD_MAINNET_ENDPOINT = "https://akash-rest.publicnode.com"
    AKASH_LCD_MAINNET_ENDPOINT_BACKUP = "https://rest-akash.ecostake.com"

    COSMOSHUB_LCD_MAINNET_ENDPOINT = "https://cosmos-rest.publicnode.com/"
    COSMOSHUB_LCD_MAINNET_ENDPOINT_BACKUP = "https://cosmos-lcd.quickapi.com"

    # Change it for one with a proper provider, as they say on their docs
    # See https://community.optimism.io/docs/useful-tools/networks/#
    OPTIMISM_RPC_ENDPOINT = "https://mainnet.optimism.io"
    OPTIMISM_TESTNET_RPC_ENDPOINT = ""

    GNOSIS_MAINNET_RPC_ENDPOINT = "https://gnosis-mainnet.public.blastapi.io"
    GNOSIS_TESTNET_RPC_ENDPOINT = ""

    KLAYTN_MAINNET_RPC_ENDPOINT = "https://public-node-api.klaytnapi.com/v1/cypress"
    KLAYTN_TESTNET_RPC_ENDPOINT = ""

    CRONOS_EVM_MAINNET_RPC_ENDPOINT = "https://cronos-evm.publicnode.com"
    CRONOS_EVM_TESTNET_RPC_ENDPOINT = ""

    AVA_RPC_ENDPOINT = "https://api.avax.network/ext/bc/C/rpc"

    BASE_RPC_ENDPOINT = "https://mainnet.base.org"
    BASE_TESTNET_RPC_ENDPOINT = "https://goerli.base.org"

    # WS ENDPOINTS
    ETH_MAINNET_WS_ENDPOINT = "wss://main-light.eth.linkpool.io/ws"
    ETH_TESTNET_WS_ENDPOINT = "wss://rinkeby-light.eth.linkpool.io/ws"

    BSC_MAINNET_WS_ENDPOINT = "wss://bsc-ws-node.nariox.org:443"


    
    class Config:
        case_sensitive = True
        env_file_encoding = 'utf-8'
        env_file = ".env"


settings = Settings()  # type: ignore
