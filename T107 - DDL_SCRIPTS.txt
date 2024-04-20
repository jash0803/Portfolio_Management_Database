create schema dbms;
set search_path to dbms;


create table users(
        user_id bigint primary key,
        user_name varchar,
        mobile_number bigint,
        user_email varchar,
        user_pancard varchar unique,
        bank_acc_number bigint unique,
        dob date
);


create table login(
        login_id int primary key,
        login_password varchar,
        Foreign key(login_id) references users(user_id)
);


create table stock_indices(
        index_symbol varchar primary key,
        index_name varchar
);


create table stock(
        stock_symbol varchar unique,
        stock_name varchar ,
        stock_price int,
        opening_price int,
        closing_price int,
        stock_type varchar,
        stock_gain_loss int,
        date_time timestamp ,
        index_symbol varchar ,
        primary key(stock_symbol),
        foreign key(index_symbol) references stock_indices(index_symbol)
);


create table portfolio(
        portfolio_id int primary key,
        portfolio_type varchar,
        date_time timestamp,
        purchased_price int,
        quantity_owned int,
        user_id int ,
        foreign key(user_id) references users(user_id)
);


create table favourite (
        user_id int,
        stock_symbol varchar,
        status bool,
        foreign key(user_id) references users(user_id),
        foreign key(stock_symbol) references stock(stock_symbol)
);


create table news(
        news_id int unique,
        news_title varchar,
        news_date timestamp,
        author varchar,
        news_source varchar,
        stock_symbol varchar,
        primary key(news_id),
        foreign key(stock_symbol) references stock(stock_symbol)
);


create table currency(
        currency_symbol varchar primary key,
        currency_name varchar,
        conversion_rate int,
        date_time timestamp
);


create table commodity(
        commodity_name varchar primary key,
        commodity_type varchar,
        last_traded_price int,
        date_time timestamp
);


create table contains_commodity(
        portfolio_id int primary key,
        commodity_name varchar,
        foreign key(portfolio_id) references portfolio(portfolio_id),
        foreign key(commodity_name) references commodity(commodity_name)
);


create table contains_currency(
        portfolio_id int primary key,
        currency_symbol varchar,
        foreign key(portfolio_id) references portfolio(portfolio_id),
        foreign key(currency_symbol) references currency(currency_symbol)
);


create table contains_stock(
        portfolio_id int primary key,
        stock_symbol varchar ,
        foreign key(portfolio_id) references portfolio(portfolio_id),
        foreign key(stock_symbol) references stock(stock_symbol)
);