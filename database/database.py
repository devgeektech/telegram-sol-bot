#solana_wallet_telegram_bot/database/database.py

import aiosqlite
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from config_data.config import config

# Getting database connection parameters from the configuration file
DB_ENGINE = config.db_engine # Type of database engine to use (SQLite or PostgreSQL)
DB_NAME = config.db_name # Database name
DB_HOST = config.db_host # Database URL
DB_USER = config.db_user # Database username
DB_PASSWORD = config.db_password.get_secret_value() # Password for the database (we get it in encrypted form)


# If SQLite is used, create the appropriate objects to work with the SQLite database
if DB_ENGINE == 'sqlite':

    # Creating a database engine
engine = create_async_engine(f"sqlite+aiosqlite:///{DB_NAME}.db", echo=True)

    # Create a database session
    AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_db() -> AsyncSession:
        """
            Get a database session.

            Returns:
                AsyncSession: The database session.
        """
        # Open a new asynchronous database session
        async with AsyncSessionLocal() as session:
# Return the session after the block is completed (the session will close automatically)
            return session

    # Function to create a database
    async def create_database() -> None:
        """
            Create the database.

            Returns:
                None
        """
        # Establish a connection to the SQLite database and open an asynchronous session context
        async with aiosqlite.connect(f"{DB_NAME}.db") as db:
# Enable support for foreign keys for the database
            await db.execute("PRAGMA foreign_keys = ON")

            # Create a user table (if it does not exist)
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    telegram_id INTEGER,
                    username TEXT
                )
            """)

            # Create a table of Solana wallets (if it does not exist)
await db.execute("""
                CREATE TABLE IF NOT EXISTS solana_wallets (
                    id INTEGER PRIMARY KEY,
                    wallet_address TEXT,
                    balance REAL,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    name TEXT,
                    description TEXT,
                    user_id INTEGER,
FOREIGN KEY(user_id) REFERENCES users(id)
                )
            """)

            # Apply all changes to the database
            await db.commit()


    async def init_database() -> None:
        """
            Initialize the database.

            Returns:
                None
        """
        # Open an asynchronous database session
        async with AsyncSessionLocal() as session:
            # Start a transaction in the database
async with session.begin():
                # Call the function to create the database
                await create_database()

# If PostgreSQL is used, create the appropriate objects for working with the PostgreSQL database
elif DB_ENGINE == 'postgresql':

    # Creating a database engine
    engine = create_async_engine("postgresql+asyncpg://solanabot:solanabot@localhost:5432/solanabot")

    # Create a database session
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_db() -> AsyncSession:
        """
           Get a database session.

           Returns:
               AsyncSession: The database session.
        """
        # Open a new asynchronous database session
        async with AsyncSessionLocal() as session:
            # Return the session after the block is completed (the session will close automatically)
            return session
from models.models import Base

    # Function to initialize the database
    async def init_database() -> None:
        """
            Initialize the database.

            Returns:
                None
        """
        async with AsyncSessionLocal() as session:
            async with session.begin():
                # code for creating tables and other necessary steps to initialize the database
                # Create all tables in the database
async with engine.begin() as conn:
                    # remove all tables from the database
                    # await conn.run_sync(Base.metadata.drop_all)
                    # create all tables in the database
                    await conn.run_sync(Base.metadata.create_all)