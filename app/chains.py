import enum
from typing import List, NamedTuple, Optional, Union
from .config import settings

class GeneralSignerChainType(enum.Enum):
    EVMBased = "EVMBased"
    SOLANA = "Solana"
    Other = "Other"


class Chain(NamedTuple):
    # name must be usable in functions and should be consistent throught the project
    name: str
    native_asset: str
    crypto_asset: str
    decimal: int
    chain_id: Optional[Union[str, int]]
    gql_graph_name: str
    chain_type: GeneralSignerChainType
    rpc_endpoint: str

class GeneralSignerChains(enum.Enum):
    # EVM chains
    Ethereum = Chain(name="ethereum", native_asset="ETH", crypto_asset="ethereum", decimal=18, chain_id=1,
                     gql_graph_name="Ethereum", chain_type=GeneralSignerChainType.EVMBased, rpc_endpoint=settings.ETH_MAINNET_RPC_ENDPOINT)
    Polygon = Chain(name="polygon", native_asset="MATIC", crypto_asset="polygon", decimal=18, chain_id=137,
                    gql_graph_name="Polygon", chain_type=GeneralSignerChainType.EVMBased, rpc_endpoint=settings.POLYGON_MAINNET_RPC_ENDPOINT)
    Avalanche = Chain(name="avalanche", native_asset="AVAX", crypto_asset="avalanche", decimal=18, chain_id=43114,
                      gql_graph_name="Avalanche", chain_type=GeneralSignerChainType.EVMBased, rpc_endpoint=settings.AVALANCHE_MAINNET_RPC_ENDPOINT)

    BinanceSmartChain = Chain(name="bsc", native_asset="BNB", crypto_asset="bsc", decimal=18, chain_id=56,
                              gql_graph_name="BinanceSmartChain", chain_type=GeneralSignerChainType.EVMBased, rpc_endpoint=settings.BSC_MAINNET_RPC_ENDPOINT)

    Fantom = Chain(name="fantom", native_asset="FTM", crypto_asset="fantom", decimal=18, chain_id=250,
                   gql_graph_name="Fantom", chain_type=GeneralSignerChainType.EVMBased, rpc_endpoint=settings.FANTOM_MAINNET_RPC_ENDPOINT)

    Arbitrum = Chain(name="arbitrum", native_asset="ETH", crypto_asset="arbitrum", decimal=18, chain_id=42161,
                     gql_graph_name="Arbitrum", chain_type=GeneralSignerChainType.EVMBased, rpc_endpoint=settings.ARBITRUM_MAINNET_RPC_ENDPOINT)

    Optimism = Chain(name="optimism", native_asset="ETH", crypto_asset="optimism", decimal=18, chain_id=10,
                     gql_graph_name="Optimism", chain_type=GeneralSignerChainType.EVMBased, rpc_endpoint=settings.OPTIMISM_RPC_ENDPOINT)

    Base = Chain(name="base", native_asset="ETH", crypto_asset="base", decimal=18,
                 chain_id=8453, gql_graph_name="Base", chain_type=GeneralSignerChainType.EVMBased, rpc_endpoint=settings.BASE_RPC_ENDPOINT)

    Gnosis = Chain(name="gnosis", native_asset="ETH", crypto_asset="gnosis", decimal=18,
                   chain_id=100, gql_graph_name="gnosis", chain_type=GeneralSignerChainType.EVMBased, rpc_endpoint=settings.GNOSIS_MAINNET_RPC_ENDPOINT)

    # Solana chain
    Solana = Chain(name="solana", native_asset="SOL", crypto_asset="solana", decimal=9,
                   chain_id=900, gql_graph_name="solana", chain_type=GeneralSignerChainType.SOLANA, rpc_endpoint=settings.SOLANA_MAINNET_ENDPOINT)

    @classmethod
    def chain_name_migration_middle_step(cls, name: str) -> Optional[str]:
        chain_name_mappings = {
            'BinanceSmartChain': 'bsc',
            'binancesmartchain': 'bsc',
            'smartchain': 'bsc'
        }
        mapped_name = chain_name_mappings.get(name)
        if mapped_name:
            return mapped_name
        else:
            return name

    @classmethod
    def get_chains_by_type(cls, type: GeneralSignerChainType) -> List["GeneralSignerChains"]:
        return [chain for chain in cls if chain.value.chain_type.value == type]

    @classmethod
    def get_chain_by_name(cls, name: str) -> "GeneralSignerChains":
        return next((chain for chain in cls if chain.value.name == name), None)

    @classmethod
    def get_chain_by_crypto_asset(cls, crypto_asset: str) -> "GeneralSignerChains":
        return next((chain for chain in cls if chain.value.crypto_asset == crypto_asset), None)

    @property
    def is_evm_chain(self) -> bool:
        return self.chain_type.value == GeneralSignerChainType.EVMBased.value

    @property
    def is_solana(self) -> bool:
        return self.chain_type.value == GeneralSignerChainType.SOLANA.value

    @property
    def name(self) -> str:
        return self.value.name

    @property
    def rpc_endpoint(self) -> str:
        return self.value.rpc_endpoint

    @property
    def native_asset(self) -> str:
        return self.value.native_asset

    @property
    def chain_id(self) -> Optional[Union[str, int]]:
        return self.value.chain_id

    @property
    def crypto_asset(self) -> Optional[str]:
        return self.value.crypto_asset

    @property
    def decimal(self) -> int:
        return self.value.decimal

    @property
    def gql_graph_name(self) -> str:
        return self.value.gql_graph_name

    @property
    def chain_type(self) -> GeneralSignerChainType:
        return self.value.chain_type
