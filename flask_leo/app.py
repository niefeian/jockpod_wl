from flask import Flask, jsonify, request
from flask_cors import CORS

from api.leo_api import *

app = Flask(__name__,
            template_folder="../front_vue/dist",
            static_folder="../front_vue/dist/static")
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
#
@app.route('/verify_correct', methods=['GET', 'POST'])
def verify_correct_():
    token = request.args.get('token')
    return jsonify(verify_correct(token,10))

@app.route('/silent_login', methods=['GET', 'POST'])
def gsilent_login():
    token = request.args.get('token')
    return jsonify(silent_login(token))

@app.route('/balances', methods=['GET', 'POST'])
def balances_api():
    token = request.args.get('token')
    return jsonify(getBalance(token))


@app.route('/balances_no', methods=['GET', 'POST'])
def balances_api_no():
    return jsonify(getBalanceNo())

@app.route('/login', methods=['GET', 'POST'])
def login_api():
    address = request.args.get('address')
    chain = request.args.get('chain')
    return jsonify(login(address,chain,None))

@app.route('/will_betting', methods=['GET', 'POST'])
def will_betting_():
    token = request.args.get('token')
    return will_betting(token,10)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=4999)
