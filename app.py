from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def msg():
    dados = {'Mensagem': 'Seja bem vindo ao programa Flask'}
    return jsonify(dados)

@app.route('/users', methods = ["GET"])
def getUsers():
    dados = {'Mensagem': 'Seja bem vindo ao programa Flask'}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)