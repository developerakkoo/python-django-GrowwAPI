from growwapi import GrowwAPI
import pyotp
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class GrowwAPIService:
    """
    Singleton service to manage Groww API connection with token caching
    """
    _instance = None
    _groww_api = None
    _access_token = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GrowwAPIService, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._groww_api is None:
            self._initialize_api()
    
    def _initialize_api(self):
        """Initialize the Groww API with access token"""
        try:
            # Generate TOTP token
            api_totp_gen = pyotp.TOTP(settings.TOTP_SECRET)
            token = api_totp_gen.now()
            
            # Get access token
            self._access_token = GrowwAPI.get_access_token(settings.API_KEY, token)
            
            # Initialize Groww API
            self._groww_api = GrowwAPI(self._access_token)
            
            logger.info("Groww API initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize Groww API: {str(e)}")
            raise
    
    @property
    def api(self):
        """Get the Groww API instance"""
        if self._groww_api is None:
            self._initialize_api()
        return self._groww_api
    
    def get_quote(self, symbol):
        """
        Get quote for a single symbol
        
        Args:
            symbol (str): Trading symbol (e.g., 'NIFTY', 'RELIANCE')
            
        Returns:
            dict: Quote response
        """
        try:
            response = self.api.get_quote(
                exchange=self.api.EXCHANGE_NSE,
                segment=self.api.SEGMENT_CASH,
                trading_symbol=symbol
            )
            return response
        except Exception as e:
            logger.error(f"Error getting quote for {symbol}: {str(e)}")
            raise
    
    def get_nifty_50_ltp(self):
        """
        Get LTP for all Nifty 50 stocks
        
        Returns:
            dict: LTP response for all Nifty 50 stocks
        """
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
        
        try:
            response = self.api.get_ltp(
                segment=self.api.SEGMENT_CASH,
                exchange_trading_symbols=nifty_50_symbols
            )
            return response
        except Exception as e:
            logger.error(f"Error getting Nifty 50 LTP: {str(e)}")
            raise

# Global instance
groww_service = GrowwAPIService()
