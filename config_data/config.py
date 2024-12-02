# solana_wallet_telegram_bot/config_data/config.py

from typing import Union
from httpx import Timeout
from pydantic.v1 import BaseSettings, SecretStr

# CURRENT_BLOCKCHAIN ​​= 'solana'
CURRENT_BLOCKCHAIN ​​= 'bsc'

# Constant to define the URL of the Solana node on the Devnet testnet
SOLANA_NODE_URL = "https://api.testnet.solana.com"
# SOLANA_NODE_URL = "https://api.devnet.solana.com"

#Testnet
# https://data-seed-prebsc-1-s1.bnbchain.org:8545
# https://data-seed-prebsc-2-s1.bnbchain.org:8545
# https://data-seed-prebsc-1-s2.bnbchain.org:8545
# https://data-seed-prebsc-2-s2.bnbchain.org:8545
# https://data-seed-prebsc-1-s3.bnbchain.org:8545
# https://data-seed-prebsc-2-s3.bnbchain.org:8545
BINANCE_NODE_URL = 'https://data-seed-prebsc-2-s2.bnbchain.org:8545'

# For example, set the timeout for reading the response to 120 seconds, the timeout for the connection to 20 seconds
timeout_settings = Timeout(read=120.0, connect=20.0, write=None, pool=None)
# Constant to determine the relationship between lamps and SOL. 1 SOL = 10^9 lamports.
LAMPORT_TO_SOL_RATIO = 10 **9

# Constant to determine the relationship between WEI and BNB. 1 BNB = 10^18 lamports.
WEI_TO_BNB_RATIO = 10 **18

# Constant to determine the length of the hexadecimal representation of the private key in characters.
PRIVATE_KEY_HEX_LENGTH = 64

# Constant to determine the length of the binary representation of the private key in bytes.
PRIVATE_KEY_BINARY_LENGTH = 32
# A constant that determines the lifetime of the cache for transaction history (in seconds).
# This is set to 3600 seconds (1 hour).
TRANSACTION_HISTORY_CACHE_DURATION = 3600

# Constant to determine the maximum number of transactions in history
TRANSACTION_LIMIT = 5


class Settings(BaseSettings):
    """
        Settings class for configuring the application.

        Attributes:
            db_engine (str): Database engine.
            db_name (str): Name of the database.
db_host (str): URL address of the database.
            db_user (str): Username for the database.
            db_password (SecretStr): Password for the database.
            bot_token (SecretStr): Token for the bot.
            admin_ids (Union[list[int], int]): List of bot administrators' IDs.
    """
    db_engine: str # database engine
    db_name: str # Database name
    db_host: str # Database URL
db_user: str # Database username
    db_password: SecretStr # Database password
    bot_token: SecretStr # Bot token
    admin_ids: Union[list[int], int] # List of bot administrator ids

    class Config:
        """
            Settings for working with Pydantic.

            This nested class defines parameters for loading environment variables from the `.env` file.

            Attributes:
env_file (str): The name of the file containing environment variables.
                env_file_encoding (str): The encoding of the file containing environment variables.
        """
        # Specify the .env file to load environment variables
        env_file = ".env"
        # Specify the encoding of the .env file
        env_file_encoding = "utf-8"


# Create an instance of the Settings class to store configuration data
config: Settings = Settings()