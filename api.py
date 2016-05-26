from flask import Flask, request
import re, json

app = Flask(__name__)

pattern = []
response = {
    'GET': [],
    'POST': [],
    'PUT': [],
    'DELETE': [],
}

NOFOUND = '{"status": 0, "msg": "no found this resources"}'

@app.route('/api/<path:objs>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def doGet(objs):
    result = None
    for x in response[request.method]:
        found = re.findall(x['pt'], objs)
        if found:
            result = x['response']
            
    if result:
        return result
    else:
        return NOFOUND, 404


if __name__ == '__main__':
    pattern = json.loads(open('api.txt', 'r').read())
    
    for x in pattern:
        x['response'] = open(x['result'], 'r').read()
        response[x['type']].append(x)

    app.run()