from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import groww_service
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_symbol_quote(request, symbol):
    """
    Get quote for a single symbol
    
    Args:
        symbol (str): Trading symbol (e.g., 'NIFTY', 'RELIANCE')
        
    Returns:
        JSON response with quote data
    """
    try:
        # Validate symbol parameter
        if not symbol or not isinstance(symbol, str):
            return Response(
                {"error": "Invalid symbol parameter"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get quote from Groww API
        quote_data = groww_service.get_quote(symbol.upper())
        
        return Response({
            "success": True,
            "symbol": symbol.upper(),
            "data": quote_data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        logger.error(f"Error in get_symbol_quote for {symbol}: {str(e)}")
        return Response(
            {
                "success": False,
                "error": f"Failed to get quote for {symbol}",
                "details": str(e)
            }, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_nifty_50_ltp(request):
    """
    Get LTP (Last Traded Price) for all Nifty 50 stocks
    
    Returns:
        JSON response with LTP data for all Nifty 50 stocks
    """
    try:
        # Get Nifty 50 LTP from Groww API
        ltp_data = groww_service.get_nifty_50_ltp()
        
        return Response({
            "success": True,
            "count": len(ltp_data) if isinstance(ltp_data, (list, dict)) else 0,
            "data": ltp_data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        logger.error(f"Error in get_nifty_50_ltp: {str(e)}")
        return Response(
            {
                "success": False,
                "error": "Failed to get Nifty 50 LTP data",
                "details": str(e)
            }, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint to verify API is working
    
    Returns:
        JSON response with API status
    """
    try:
        # Test the Groww API connection
        test_quote = groww_service.get_quote("NIFTY")
        
        return Response({
            "success": True,
            "status": "healthy",
            "message": "Groww API is working correctly",
            "timestamp": "2024-01-01T00:00:00Z"  # You can use timezone.now() here
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return Response(
            {
                "success": False,
                "status": "unhealthy",
                "error": "Groww API connection failed",
                "details": str(e)
            }, 
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )