from flask import Flask, jsonify, request

app = Flask(__name__)

informations = [
    {
        'id': 1,
        'name': u'Ashutosh',
        'contact': u'0123456789',
        'done': False
    },
    {
        'id': 1,
        'name': u'Atharva',
        'contact': u'9876543210',
        'done': False
    }
]

@app.route('/add-data', methods = ['POST'])

def add_information():
    return jsonify(
        {
            'status': 'error',
            'message': 'Please provide the data!'
        }, 400
    )

    information = {
        'id': tasks[-1][id] + 1,
        'name': request.json['name'],
        'contact': request.json['contact'],
        'done': False
    }

    informations.append(information)
    return jsonify(
        {
            'status': 'success',
            'message': 'Information added successfully!'
        }
    )

if(__name__ == '__main__'):
    app.run(debug = True)