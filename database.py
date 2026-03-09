from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# PostgreSQL connection string for Docker container
SQLALCHEMY_DATABASE_URL = "postgresql://admin:adminpassword@localhost:5432/irrigation_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency for database session management"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()