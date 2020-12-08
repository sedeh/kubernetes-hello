import os
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return {
        os.environ['HOSTNAME']: 'hello from ' + os.environ['CONTAINER_NAME']
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
