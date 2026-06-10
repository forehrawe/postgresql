from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "postgresql+psycopg://hadi:1234@localhost/mydb" # postgresql+psycopg://{user}:{password}@localhost/{db name}
)
Base = declarative_base()
Session = sessionmaker(bind=engine)