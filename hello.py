#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask('hello-flask')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yaml', methods=['POST', 'OPTIONS'])
def get_cloud_formation():

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    text_content = request.get_data(as_text=True)
    json_content = yaml.safe_load(text_content)
    default_yaml = amz.read_yaml(os.path.join(__location__, '../amazonia/defaults.yaml'))

    result = amz.generate_template(json_content, default_yaml)

    return Response(result, mimetype='Application/json')

if __name__ == '__main__':
    app.run('localhost')
