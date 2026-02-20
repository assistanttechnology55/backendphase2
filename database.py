from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from models.user import User, Task  # Import all models here to register them with SQLModel
from core.config import settings

# Create the async engine
# Using async SQLite driver for development - for production, you might want to use PostgreSQL
engine = create_async_engine(
    settings.DATABASE_URL.replace("sqlite:///", "sqlite+aiosqlite:///"),
    echo=True,  # Set to False in production
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    # Add SQLite-specific connect args
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

# Create async session maker
AsyncSessionLocal = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

async def get_async_session():
    """Get async database session."""
    async with AsyncSessionLocal() as session:
        yield session

# Function to create database tables
async def create_db_and_tables():
    """Create database tables."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)