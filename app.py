import os
from flask import Flask
from scraper import EpicStore
from steam import special_offer

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit


@app.route('/')
def homepage():
    return "No, not here, you are wrong"


@app.route('/epic/free_games')
def epic_free_games():
    scrape = EpicStore()
    data = scrape.get_free_games()
    if data:
        return data
    else:
        return {"error": "Failed to fetch free games"}, 500


@app.route('/steam/special_offer')
def steam_special_offer():
    data = {
        "code": 200,
        "message": "",
        "data": []
    }

    data["message"] = "Steam Special Offer"
    data["data"] = special_offer()

    return data


if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
