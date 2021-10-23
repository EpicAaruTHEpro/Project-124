from logging import error
from flask import Flask, jsonify, request
app =Flask(__name__)

@app.route("/")
def helloWorld():
    return "Tasks Program: change route to add /get-data to see tasks and /add-data to add tasks"

tasks = [ { 'id': 1, 'title': u'Practice Instrument', 'description': u'Play through all of the Concert Scales', 'done': False, 'name': 'Johnathan' }, 
{ 'id': 2, 'title': u'Learn Calculus', 'description': u'Need to find a good Calculus course on the web', 'done': False, 'name': 'Johnathan' } ]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify(
            {"status": "error", "message":"Please provide the data in .json format"}, 400
        )
    task = {
        "id": tasks[-1]["id"]+1, 'title': request.json['title'],'name':request.json['name'], 'description': request.json.get('description', ""), "done": False
    }

    tasks.append(task)

    return jsonify(
            {"status": "success", "message":"Task added successfully"}, 200
        )

@app.route("/get-data")
def getTask():
    return jsonify({
        "data": tasks
    })


if (__name__ == "__main__"):
    app.run(debug=True)
