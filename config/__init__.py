import os 
import json 

from dotenv import load_dotenv
load_dotenv()

env = os.environ.get('ENV')

if env:
    with open('./config/' + env + '.json') as f:
        config = json.load(f)
else:
    with open('./config/default.json') as f:
        config = json.load(f)