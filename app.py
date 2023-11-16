from fastapi import FastAPI, Request, Response
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
import yfinance


app = FastAPI()


class Stock(BaseModel):
    stockName: str
    currentPrice: float
    changePercent: float
    bidPrice: float
    askPrice: float
    volume: int


@app.get("/stocks/{stockName}")
def get_quote(stockName: str) -> Stock:
    """Get the quote for a single stock."""

    # Get the stock quote from Yahoo Finance.
    stock = yfinance.Ticker(stockName)
    quote = stock.info

    # Convert the quote to a Stock object.
    stock_object = Stock(
        stockName=quote["symbol"],
        currentPrice=quote["currentPrice"],
        changePercent=quote["changePercent"],
        bidPrice=quote["bidPrice"],
        askPrice=quote["askPrice"],
        volume=quote["volume"],
    )

    return stock_object


@app.get("/stocks")
def get_quotes(stockNames: list[str]) -> list[Stock]:
    """Get the quotes for a list of stocks."""

    # Get the stock quotes from Yahoo Finance.
    stocks = [yfinance.Ticker(stockName).info for stockName in stockNames]

    # Convert the quotes to Stock objects.
    stock_objects = [
        Stock(
            stockName=quote["symbol"],
            currentPrice=quote["currentPrice"],
            changePercent=quote["changePercent"],
            bidPrice=quote["bidPrice"],
            askPrice=quote["askPrice"],
            volume=quote["volume"],
        )
        for quote in stocks
    ]

    return stock_objects


@app.openapi
def custom_openapi():
    """
    Overrides the default OpenAPI document.

    This is useful for adding additional metadata to the OpenAPI document,
    such as the version number and contact information.
    """

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Stock Quotes API",
        version="1.0.0",
        description="A simple API for getting stock quotes.",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return openapi_schema


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
