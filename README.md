# WealthSync

WealthSync is a financial portfolio management system that helps users track stocks, commodities, and currencies in one place. The system provides real-time updates on financial assets and allows users to manage and analyze their investments effectively.

## Features

- **Stock Portfolio Management:** Track stocks with price updates and indices mapping.
- **Commodity Tracking:** Monitor commodities and their last traded price.
- **Currency Exchange:** Maintain real-time conversion rates for multiple currencies.
- **User Authentication:** Secure user login with password protection.
- **News Integration:** Stay updated with financial news linked to specific stocks.
- **Favorites & Custom Portfolio:** Users can create and manage their own investment portfolios.

## Database Schema

WealthSync uses a relational database with the following tables:

- **User & Login**: Stores user details and authentication credentials.
- **Portfolio**: Tracks user-owned financial assets.
- **Stock, Commodity, Currency**: Maintains financial market data.
- **Stock Indices**: Maps stocks to market indices.
- **News**: Stores financial news relevant to stocks.
- **Favorites & Portfolio Holdings**: Allows users to favorite and manage assets.

## Technologies Used

- **Database**: MySQL
- **Frontend & Backend**: Streamlit
