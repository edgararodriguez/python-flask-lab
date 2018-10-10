from flask import Flask, jsonify, request
app = Flask(__name__)
#objects
Athletes = [{'name' : 'Lebron James'}, {'name' : 'Odell Beckham Jr'}, {'name' : 'Josh Norman'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'Hello World'})
#get request that gets athletes
@app.route('/ath' , methods=['GET'])
def returnall():
    return jsonify({'Athletes' : Athletes})
#Get request on a single name
@app.route('/ath/<string:name>', methods=['GET'])
def returnOne(name):
    athl = [athlete for athlete in Athletes if athlete['name'] == name]
    return jsonify({'athlete' : athl[0]})
#Post request
#Use Postman to edit
@app.route('/ath' , methods=['POST'])
def addOne():
    athlete = {'name' : request.json['name']}
    Athletes.append(athlete)
    return jsonify({'Athletes' : Athletes})
#put request
#Use Postman to edit
@app.route('/ath/<string:name>', methods=['PUT'])
def editOne(name):
    athl = [athlete for athlete in Athletes if athlete['name'] == name]
    athl[0]['names'] = request.json['name']
    return jsonify({'athlete' : athl[0]})
#Delete request
#Use Postman to delete
@app.route('/ath/<string:name>', methods=['DELETE'])
def removeOne(name):
    athl = [athlete for athlete in Athletes if athlete['name'] == name]
    Athletes.remove(athl[0])
    return jsonify({'Athletes' : Athletes})
