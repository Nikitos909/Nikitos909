CREATE TABLE IF NOT EXISTS mainmenu (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL);


CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
login VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
psw TEXT NOT NULL,
time INTEGER NOT NULL);