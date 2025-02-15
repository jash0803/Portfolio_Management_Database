CREATE SCHEMA portfolio;
USE portfolio;

CREATE TABLE users (
    user_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(15) UNIQUE NOT NULL,
    user_email VARCHAR(255) UNIQUE NOT NULL,
    user_pancard VARCHAR(20) UNIQUE NOT NULL,
    bank_acc_number VARCHAR(20) UNIQUE NOT NULL,
    dob DATE NOT NULL
);

CREATE TABLE login (
    login_id BIGINT PRIMARY KEY,
    login_password VARCHAR(255) NOT NULL,
    FOREIGN KEY (login_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE stock_indices (
    index_symbol VARCHAR(50) PRIMARY KEY,
    index_name VARCHAR(255) NOT NULL
);

CREATE TABLE stock (
    stock_symbol VARCHAR(50) PRIMARY KEY,
    stock_name VARCHAR(255) NOT NULL,
    stock_price DECIMAL(10,2) NOT NULL,
    opening_price DECIMAL(10,2) NOT NULL,
    closing_price DECIMAL(10,2) NOT NULL,
    stock_type VARCHAR(100),
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    index_symbol VARCHAR(50),
    FOREIGN KEY (index_symbol) REFERENCES stock_indices(index_symbol) ON DELETE SET NULL
);

CREATE TABLE portfolio (
    portfolio_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    portfolio_type VARCHAR(100) NOT NULL,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    purchased_price DECIMAL(10,2) NOT NULL,
    quantity_owned INT NOT NULL,
    user_id BIGINT,
    asset_symbol VARCHAR(50),
    asset_type ENUM('Stock', 'Currency', 'Commodity') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE favourite (
    user_id BIGINT,
    stock_symbol VARCHAR(50),
    status BOOLEAN,
    PRIMARY KEY (user_id, stock_symbol),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (stock_symbol) REFERENCES stock(stock_symbol) ON DELETE CASCADE
);

CREATE TABLE news (
    news_id INT PRIMARY KEY AUTO_INCREMENT,
    news_title VARCHAR(255) NOT NULL,
    news_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author VARCHAR(100) NOT NULL,
    news_source VARCHAR(255),
    stock_symbol VARCHAR(50),
    FOREIGN KEY (stock_symbol) REFERENCES stock(stock_symbol) ON DELETE CASCADE
);

CREATE TABLE currency (
    currency_symbol VARCHAR(10) PRIMARY KEY,
    currency_name VARCHAR(100) NOT NULL,
    conversion_rate DECIMAL(10,4) NOT NULL,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE commodity (
    commodity_name VARCHAR(100) PRIMARY KEY,
    commodity_type VARCHAR(100),
    last_traded_price DECIMAL(10,2) NOT NULL,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);