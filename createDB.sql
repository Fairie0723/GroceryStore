-- create database
create database Store;

-- create table
-- customers table
create table customers(
customer_id int not null auto_increment primary key,
customer_fname varchar(255) not null,
customer_lname varchar(255) not null,
customer_email varchar(255)
);
-- products table
create	table products(
product_id int not null AUTO_INCREMENT primary KEY, 
product_name VARCHAR(255) NOT NULL,
product_description VARCHAR(255),
product_price DECIMAL(10,2) NOT NULL
);

-- orders table
create table orders(
order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
customer_id int NOT NULL,
order_total decimal(10,2),
order_status varchar(40),
foreign key (customer_id) references Customers(customer_id) 
);

