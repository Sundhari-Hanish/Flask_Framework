Create database if not exists task_db;
use task_db;
create table if not exists tasks(
id int auto_increment primary key,
title varchar(255),
description text,
status varchar(50),
priority varchar(50),
due_date date);
