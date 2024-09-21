from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 