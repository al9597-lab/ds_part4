import os
from dotenv import load_dotenv

# read .env
load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DB = os.getenv("PG_DB")

MODEL_PATH = os.getenv("MODEL_PATH")
MODEL_VERSION = os.getenv("MODEL_VERSION")
