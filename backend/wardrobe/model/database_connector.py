import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

class DataBaseConnector:
    def __init__(self):
        engine = create_engine(os.environ['DATABASE_URL'])
        Session = sessionmaker(bind=engine)
        self.session = Session()
    