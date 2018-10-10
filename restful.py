from flask import Flask, jsonify, request
app = Flask(__name__)

Athletes = [{'name' : 'Lebron James'}, {'name' : 'Odell Beckham Jr'}, {'name' : 'Josh Norman'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'Hello World'})

@app.route('/ath' , methods=['GET'])
def returnall():
    return jsonify({'Athletes' : Athletes})

@app.route('/ath/<string:name>', methods=['GET'])
def returnOne(name):
    athl = [athlete for athlete in Athletes if athlete['name'] == name]
    return jsonify({'athlete' : athl[0]})

@app.route('/ath' , methods=['POST'])
def addOne():
    athlete = {'name' : request.json['name']}
    Athletes.append(athlete)
    return jsonify({'Athletes' : Athletes})
