import os
from flask import Flask
from scraper import EpicStore

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

@app.route('/')
def homepage():
    return "Welcome to the Epic Store Free Games API!"

@app.route('/epic/free_games')
def epic_free_games():
    scrape = EpicStore()
    data = scrape.get_free_games()
    if data:
        return data
    else:
        return {"error": "Failed to fetch free games"}, 500


if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
