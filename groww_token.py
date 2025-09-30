from growwapi import GrowwAPI
import pyotp

api_key = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjI1NDc0NTgyMzEsImlhdCI6MTc1OTA1ODIzMSwibmJmIjoxNzU5MDU4MjMxLCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCJiOWMzYzMwYS1lOGNkLTQxZGItODQyZS1lZjg5YzQ4YmExYzhcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiM2UwZDljNzItMjI2NC00ZDBjLWExZmEtNjAyM2NhZDAyNTc0XCIsXCJkZXZpY2VJZFwiOlwiODkxMGFlM2YtYWU0YS01YWE5LTg2N2QtNWU1ODIwMzY5ZGQ4XCIsXCJzZXNzaW9uSWRcIjpcIjBkYWM3YTg3LTllYWQtNDJlNi1hY2MzLWI5ZjVhYTBhZTIzYlwiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYktlUXRyaDFVSmpNK2pLdDBzRzhUbVJSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcImF1dGgtdG90cFwiLFwic291cmNlSXBBZGRyZXNzXCI6XCIyNDAxOjQ5MDA6MWMxNjoyM2MyOmM5YzE6YWIxNzphYzNkOmYzNmYsMTcyLjY4LjIzOS4yMjUsMzUuMjQxLjIzLjEyM1wiLFwidHdvRmFFeHBpcnlUc1wiOjI1NDc0NTgyMzE2OTd9IiwiaXNzIjoiYXBleC1hdXRoLXByb2QtYXBwIn0.U_NoPRg4YPkmcWljNuJ36G0kBVpZeTwiaYrFIPmoV3-iAOpVEUMiC0vuUEGYt9ws9heY2hBx9FMD3w3X045FAg"
api_topt_gen = pyotp.TOTP("NBPTIVC2YPAP72PHLENMT4OV7BWRVRIF")

token = api_topt_gen.now()
print(token)

access_token = GrowwAPI.get_access_token(api_key, token)
print(access_token)

groww_api = GrowwAPI(access_token)

# Get Last Traded Price (LTP) for NSE NIFTY
ltp_response = groww_api.get_ltp(
    segment=groww_api.SEGMENT_CASH,
    exchange_trading_symbols="NSE_NIFTY"
)
print("LTP Response:", ltp_response)

# Nifty 50 symbols
nifty_50_symbols = (
    "NSE_RELIANCE", "NSE_TCS", "NSE_HDFCBANK", "NSE_ICICIBANK", "NSE_HINDUNILVR",
    "NSE_ITC", "NSE_KOTAKBANK", "NSE_LTI", "NSE_SBIN", "NSE_BHARTIARTL",
    "NSE_ASIANPAINT", "NSE_AXISBANK", "NSE_MARUTI", "NSE_HCLTECH", "NSE_ULTRACEMCO",
    "NSE_SUNPHARMA", "NSE_TITAN", "NSE_WIPRO", "NSE_NESTLEIND", "NSE_POWERGRID",
    "NSE_NTPC", "NSE_COALINDIA", "NSE_JSWSTEEL", "NSE_TATAMOTORS", "NSE_BAJFINANCE",
    "NSE_BAJAJFINSV", "NSE_INDUSINDBK", "NSE_DRREDDY", "NSE_TECHM", "NSE_APOLLOHOSP",
    "NSE_TATASTEEL", "NSE_CIPLA", "NSE_ADANIPORTS", "NSE_BPCL", "NSE_GRASIM",
    "NSE_HEROMOTOCO", "NSE_EICHERMOT", "NSE_DIVISLAB", "NSE_HDFCLIFE", "NSE_SBILIFE",
    "NSE_BRITANNIA", "NSE_UPL", "NSE_ONGC", "NSE_TATACONSUM", "NSE_BAJAJHLDNG",
    "NSE_M&M", "NSE_LUPIN", "NSE_ADANIENT", "NSE_HINDALCO", "NSE_BAJAJ"
)

# Get LTP for all Nifty 50 stocks
nifty_50_ltp_response = groww_api.get_ltp(
    segment=groww_api.SEGMENT_CASH,
    exchange_trading_symbols=nifty_50_symbols
)
print("Nifty 50 LTP Response:", nifty_50_ltp_response)

# Get quote for single symbol (NIFTY)
quote_response = groww_api.get_quote(
    exchange=groww_api.EXCHANGE_NSE,
    segment=groww_api.SEGMENT_CASH,
    trading_symbol="NIFTY"
)
print("Quote Response:", quote_response)
