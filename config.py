from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ.get('TOKEN')
DBNAME = os.environ.get('DBNAME')
DBUSER = os.environ.get('DBUSER')
DBPASSWORD = os.environ.get('DBPASSWORD')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')