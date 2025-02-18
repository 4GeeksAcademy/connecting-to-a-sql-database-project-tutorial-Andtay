import os 
import pandas as pd
from sqlalchemy import create_engine

def connect():
    global engine
    try:
        connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        print("Starting the connection...")
        engine = create_engine(connection_string, isolation_level="AUTOCOMMIT")
        engine.connect()
        print("Connected successfully!")
        return engine
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    
engine = connect() # Connection to the db
print(engine)
if(engine == None):
    exit()