CREATE SCHEMA portfolio;
USE portfolio;

CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    user_name VARCHAR(255),
    mobile_number BIGINT,
    user_email VARCHAR(255),
    user_pancard VARCHAR(255) UNIQUE,
    bank_acc_number BIGINT UNIQUE,
    dob DATE
);

CREATE TABLE login (
    login_id BIGINT PRIMARY KEY,
    login_password VARCHAR(255),
    FOREIGN KEY (login_id) REFERENCES users(user_id)
);

CREATE TABLE stock_indices (
    index_symbol VARCHAR(50) PRIMARY KEY,
    index_name VARCHAR(255)
);

CREATE TABLE stock (
    stock_symbol VARCHAR(50) UNIQUE,
    stock_name VARCHAR(255),
    stock_price INT,
    opening_price INT,
    closing_price INT,
    stock_type VARCHAR(100),
    stock_gain_loss INT,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    index_symbol VARCHAR(50),
    PRIMARY KEY (stock_symbol),
    FOREIGN KEY (index_symbol) REFERENCES stock_indices(index_symbol)
);

CREATE TABLE portfolio (
    portfolio_id INT PRIMARY KEY,
    portfolio_type VARCHAR(100),
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    purchased_price INT,
    quantity_owned INT,
    user_id BIGINT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE favourite (
    user_id BIGINT,
    stock_symbol VARCHAR(50),
    status BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (stock_symbol) REFERENCES stock(stock_symbol)
);

CREATE TABLE news (
    news_id INT UNIQUE,
    news_title VARCHAR(255),
    news_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author VARCHAR(255),
    news_source VARCHAR(255),
    stock_symbol VARCHAR(50),
    PRIMARY KEY (news_id),
    FOREIGN KEY (stock_symbol) REFERENCES stock(stock_symbol)
);

CREATE TABLE currency (
    currency_symbol VARCHAR(50) PRIMARY KEY,
    currency_name VARCHAR(255),
    conversion_rate INT,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE commodity (
    commodity_name VARCHAR(100) PRIMARY KEY,
    commodity_type VARCHAR(100),
    last_traded_price INT,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contains_commodity (
    portfolio_id INT PRIMARY KEY,
    commodity_name VARCHAR(100),
    FOREIGN KEY (portfolio_id) REFERENCES portfolio(portfolio_id),
    FOREIGN KEY (commodity_name) REFERENCES commodity(commodity_name)
);

CREATE TABLE contains_currency (
    portfolio_id INT PRIMARY KEY,
    currency_symbol VARCHAR(50),
    FOREIGN KEY (portfolio_id) REFERENCES portfolio(portfolio_id),
    FOREIGN KEY (currency_symbol) REFERENCES currency(currency_symbol)
);

CREATE TABLE contains_stock (
    portfolio_id INT PRIMARY KEY,
    stock_symbol VARCHAR(50),
    FOREIGN KEY (portfolio_id) REFERENCES portfolio(portfolio_id),
    FOREIGN KEY (stock_symbol) REFERENCES stock(stock_symbol)
);
