import os, sys

INTERP = ""

#If we are not in Production
# - then it loads the Python Path from the .env file

if os.environ['HOME'] == '/home/dh_3aiepx':
        INTERP = os.path.join(os.environ['HOME'], 'assistant.tokenizeme.io', 'venv', 'bin', 'python3')
else:   
        from dotenv import load_dotenv
        load_dotenv()
        if (os.environ.get('INTERP')):
                INTERP = os.environ.get('INTERP')

if sys.executable != INTERP:
        print("INTERP: ",INTERP)
        print("sys.argv: ",sys.argv)
        print("os.environ['HOME']:", os.environ['HOME'])
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())



from flask import Flask
application = Flask(__name__)
sys.path.append('app')
from app import app as application

