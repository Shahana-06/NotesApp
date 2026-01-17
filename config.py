from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import os

# Database configuration
<<<<<<< HEAD
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "Shan1234$$")
=======
# You can either set environment variables or change these defaults directly
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "....")
>>>>>>> a9401e4bc3eb184398ea3d6385a732374cfef622
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "shahanas")

# Create database URL with proper encoding for special characters
db_url = f"postgresql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create engine with connection pooling
engine = create_engine(
    db_url,
<<<<<<< HEAD
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)

# Create session factory
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
=======
    pool_pre_ping=True,  # Verify connections before using
    pool_size=5,  # Number of connections to maintain
    max_overflow=10  # Max additional connections when pool is full
)

# Create session factory
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
>>>>>>> a9401e4bc3eb184398ea3d6385a732374cfef622
