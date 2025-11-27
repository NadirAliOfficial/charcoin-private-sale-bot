# CharCoin Private Sale Bot

An automated Python bot to control and execute private sale token releases for CHAR Coin. Designed to enforce structured, price-based selling post-launch to protect token value and ensure fair distribution.

---

## 🚀 Features

* Load investor wallet info, token allocation, and staking percentage
* Multi-stage sell plan with customizable target prices
* Sell in 20 fractions per stage for smoother release
* Real-time price tracking (CoinGecko or Pyth)
* On-chain swap execution via Jupiter Aggregator
* Dry-run simulation and live execution modes
* Secure handling of wallet private keys (encrypted JSON)

---

## 📁 Repository Structure

```
charcoin-private-sale-bot/
├── investors.json           # Investor wallet + stage config
├── private_keys.json        # Secure wallet key storage (never commit)
├── .env                     # API keys, Solana RPC
├── bot.py                   # Main bot logic
├── utils/
│   ├── pricing.py           # Price feed handlers
│   └── jupiter.py           # Swap execution via Jupiter
└── logs/                    # Execution logs
```

---

## ⚙️ Configuration

1. **investors.json**

   ```json
   [
     {
       "wallet": "InakiZubizarreta.sol",
       "total_tokens": 50400000,
       "staking_percentage": 0.30,
       "stages": [
         { "stage_number": 1, "percentage_to_sell": 0.06, "target_price_usd": 0.0024 },
         { "stage_number": 2, "percentage_to_sell": 0.06, "target_price_usd": 0.0030 }
       ]
     }
   ]
   ```

2. **.env**

   ```env
   RPC_URL=https://api.mainnet-beta.solana.com
   COINGECKO_API_KEY=your_api_key
   ```

3. **private\_keys.json**

   ```json
   {
     "InakiZubizarreta.sol": "private-key-string-here"
   }
   ```

---

## 🧪 Bot Modes

| Mode      | Description                                      |
| --------- | ------------------------------------------------ |
| `dry-run` | Simulates selling logic, no transactions sent    |
| `live`    | Executes swaps on Jupiter when price targets hit |

---

## 📌 Example Log Output

```
✅ Stage 2 triggered at $0.0030 for InakiZubizarreta.sol
🔁 Selling 30240 CHAR in 20 parts (~1512 per swap)
✅ Remaining CHAR: 201600
```

---

## 🔐 Security Notice

* Never commit or upload `private_keys.json` to any public repo.
* Use per-investor wallets to limit exposure.
* Production deployments should encrypt and lock access to key files.

---

## 📅 Development Timeline

* ✅ Phase 1: Simulation logic + CLI alerts
* ✅ Phase 2: Real price feeds + Jupiter integration
* 🔜 Phase 3: Admin dashboard / monitoring panel

---

## 🤝 Credits

**Lead Developer:** Nadir Ali Khan
**Bot Strategy & Oversight:** Jorge Martinez
**Developed By:** Team NAK (Blockchain | Automation | AI)

---

## 📄 License

MIT License — intended for internal use by the CharCoin Foundation.
<!-- updated: 2026-06-18 -->

