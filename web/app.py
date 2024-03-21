from flask import Flask
from dotenv import load_dotenv
import os

# Flask configuration

# Load default config and override config from an environment variable
load_dotenv()

app_version = "0.1.0"

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Smlouvy v. ' + app_version


@app.route('/contract/<int:contract_id>')
def show_contract(contract_id):
    return "<a href=" + os.environ.get('ABRAFLEXI_URL') + "/c/" + os.environ.get('ABRAFLEXI_COMPANY') + f'/smlouva/{contract_id}' + ">Contract " + str(contract_id) + "</a>"
