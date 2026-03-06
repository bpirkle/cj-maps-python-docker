# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Mabel!'

@app.route('/mabel')
def mabel():
        return 'Mabel<br><b>Mabel</b><br><em>Mabel!</em><br>Good girl.'

@app.route('/down')
def here_mabel():
    file_path = 'down.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
