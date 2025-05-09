from dataclasses import dataclass, asdict
from datetime import datetime
import requests


@dataclass
class Game:
    title: str
    url: str
    price: str
    description: str
    image_url: str
    original_price: int
    discount_price: int
    end_date: datetime = None


class EpicStore:
    def __init__(self):
        self.url = "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=ID&allowCountries=ID"

    def get_free_games(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            data = data.get("data", {}).get("Catalog", {}).get(
                "searchStore", {}).get("elements", [])

            FREE_GAMES = []

            for game in data:
                if game.get("price", {}).get("totalPrice", {}).get("discountPrice") != 0:
                    continue

                if not game.get("catalogNs", {}).get("mappings"):
                    continue

                # Extract the product slug from the game data
                product_slug = game.get("catalogNs", {}).get(
                    "mappings", [{}])[0].get("pageSlug")
                if not product_slug:
                    product_slug = game.get("productSlug")

                tall_image = None
                # Find the image URL for the game
                # Check if the game has a key image of type "OfferImageTall" / "Thumbnail"
                for image_data in game.get("keyImages", []):
                    if image_data.get("type") == "OfferImageTall":
                        tall_image = image_data.get("url")
                        break

                free_game = Game(
                    title=game.get("title"),
                    url=f"https://store.epicgames.com/en-US/p/{product_slug}",
                    price=game.get("price", {}).get(
                        "totalPrice", {}).get("fmtPrice").get("discountPrice"),
                    description=game.get("description"),
                    image_url=tall_image,
                    original_price=game.get("price", {}).get(
                        "totalPrice", {}).get("originalPrice"),
                    discount_price=game.get("price", {}).get(
                        "totalPrice", {}).get("discount"),
                )
                free_game.end_date = game.get("promotions", {}).get("promotionalOffers", [{}])[
                    0].get("promotionalOffers", [{}])[0].get("endDate")
                FREE_GAMES.append(asdict(free_game))

            print(f"Fetched {len(FREE_GAMES)} free games.")
            if not FREE_GAMES:
                print("No free games available.")
                return None
            return FREE_GAMES
        except requests.exceptions.RequestException as e:
            print(f"Error fetching free games: {e}")
            return None
