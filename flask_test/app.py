from flask import Flask

from note import create_note

app = Flask(__name__)


@app.route('/note', methods=['POST'])
def post_note():
    response_data = create_note()

    # ! READ THIS (about response)
    # https://flask.palletsprojects.com/en/2.2.x/quickstart/?highlight=response#about-responses
    return response_data


if __name__ == "__main__":
    app.run(debug=True)
