
import os
import json
import time
import requests
from dotenv import load_dotenv
from solana.rpc.api import Client
from solana.keypair import Keypair
from utils.pricing import get_char_price
from utils.jupiter import execute_jupiter_swap

# Load environment variables
load_dotenv()
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
RPC_URL            = os.getenv("RPC_URL")
JUPITER_API        = os.getenv("JUPITER_API")  # Jupiter quote endpoint

# Bot settings
PRICE_CHECK_INTERVAL = 30  # seconds between price checks
FRACTIONS_PER_STAGE   = 20  # micro-sells per stage

# Initialize Solana RPC client
client = Client(RPC_URL)

# Load investor configurations
with open("investors.json") as f:
    investors = json.load(f)


def get_char_price():
    # Fetch current CHAR/USDC price from CoinGecko
    resp = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={
            "ids": "char-coin",
            "vs_currencies": "usd",
            "x_cg_pro_api_key": COINGECKO_API_KEY
        },
        timeout=10
    )
    data = resp.json()
    return data.get("char-coin", {}).get("usd", 0.0)


def load_private_key(wallet_address):
    # Load the private key for a given wallet
    with open("private_keys.json") as f:
        keys = json.load(f)
    secret = keys.get(wallet_address)
    return Keypair.from_secret_key(bytes(secret))


def process_investor(inv):
    total     = inv["total_tokens"]
    staked    = total * inv["staking_percentage"]
    available = total - staked

    for stage in inv["stages"]:
        if stage.get("completed"):
            continue

        current_price = get_char_price()
        target_price  = stage["target_price_usd"]
        if current_price >= target_price:
            to_sell  = available * stage["percentage_to_sell"]
            fraction = to_sell / FRACTIONS_PER_STAGE
            keypair  = load_private_key(inv["wallet"])

            # Execute micro-sells
            for _ in range(FRACTIONS_PER_STAGE):
                execute_jupiter_swap(keypair, fraction)
                time.sleep(1)

            stage["completed"] = True
            # Persist progress
            with open("investors.json", "w") as wf:
                json.dump(investors, wf, indent=2)
            print(f"✅ Stage {stage['stage_number']} done for {inv['wallet']}")
            break


def main():
    print("🚀 CharCoin Private Sale Bot started")
    while True:
        for investor in investors:
            process_investor(investor)
        time.sleep(PRICE_CHECK_INTERVAL)


if __name__ == "__main__":
    main()
