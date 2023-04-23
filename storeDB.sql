-- create database
create database GROCERY_STORE;

-- drop database
drop database GROCERY_STORE;

-- create table
CREATE TABLE STORE
(item_id int primary key,
 item_name varchar(255),
 item_price decimal(10,2), 
 constraint chk_item_price check (item_price >= 0.00));
 
 -- insert into table
 insert into STORE values
 (1,'eggs',1.88);
 insert into STORE values
 (2,'milk',2.55);
 insert into STORE values
 (3,'cereal',1.76);
 insert into STORE values
 (4,'soda',3.50);
 insert into STORE values
 (5,'chicken breast',5.75);