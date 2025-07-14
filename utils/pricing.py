import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("COINGECKO_API_KEY")

def get_char_price():
    # Fetch current CHAR/USDC price from CoinGecko
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "char-coin",
            "vs_currencies": "usd",
            "x_cg_pro_api_key": API_KEY
        }
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        return data.get("char-coin", {}).get("usd", 0.0)
    except Exception as e:
        print(f"[price error] {e}")
        return 0.0
