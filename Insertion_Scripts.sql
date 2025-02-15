INSERT INTO users (user_name, mobile_number, user_email, user_pancard, bank_acc_number, dob) VALUES
('Amit Shah', '9876543210', 'amit.shah@email.com', 'ABCDE1234F', '123456789012', '1985-04-23'),
('Priya Mehta', '9123456789', 'priya.mehta@email.com', 'FGHIJ5678K', '234567890123', '1990-07-15'),
('Rajesh Gupta', '9012345678', 'rajesh.gupta@email.com', 'LMNOP9876Z', '345678901234', '1995-12-10');


INSERT INTO login (login_id, login_password) VALUES
(1, 'password123'),
(2, 'securepass'),
(3, 'rajesh@987');


INSERT INTO stock_indices (index_symbol, index_name) VALUES
('NIFTY50', 'Nifty 50'),
('SENSEX', 'BSE Sensex'),
('NASDAQ', 'NASDAQ Composite');


INSERT INTO stock (stock_symbol, stock_name, stock_price, opening_price, closing_price, stock_type, index_symbol) VALUES
('RELIANCE', 'Reliance Industries', 2800.50, 2750.00, 2785.00, 'Equity', 'NIFTY50'),
('TCS', 'Tata Consultancy Services', 3500.75, 3450.00, 3495.00, 'Equity', 'NIFTY50'),
('AAPL', 'Apple Inc.', 175.60, 172.50, 174.80, 'Technology', 'NASDAQ');


INSERT INTO portfolio (portfolio_type, purchased_price, quantity_owned, user_id, asset_symbol, asset_type) VALUES
('Long Term', 2750.00, 10, 1, 'RELIANCE', 'Stock'),
('Short Term', 3450.00, 5, 2, 'TCS', 'Stock'),
('Forex Investment', 1.12, 1000, 3, 'USD', 'Currency');

INSERT INTO favourite (user_id, stock_symbol, status) VALUES
(1, 'RELIANCE', TRUE),
(2, 'TCS', TRUE),
(3, 'AAPL', FALSE);

INSERT INTO news (news_title, author, news_source, stock_symbol) VALUES
('Reliance Q3 Earnings Beat Estimates', 'Economic Times', 'ET Now', 'RELIANCE'),
('TCS Expands AI Capabilities', 'CNBC India', 'CNBC', 'TCS'),
('Apple Launches New MacBook', 'Bloomberg', 'Bloomberg', 'AAPL');

INSERT INTO currency (currency_symbol, currency_name, conversion_rate) VALUES
('USD', 'US Dollar', 83.12),
('EUR', 'Euro', 90.45),
('INR', 'Indian Rupee', 1.00);

INSERT INTO commodity (commodity_name, commodity_type, last_traded_price) VALUES
('Gold', 'Precious Metal', 60000.00),
('Crude Oil', 'Energy', 5800.50),
('Silver', 'Precious Metal', 72000.75);