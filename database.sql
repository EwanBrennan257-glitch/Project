--enables foreign keys--
PRAGMA foreign_keys = ON;

CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE Product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    stock INT NOT NULL CHECK (stock >= 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0.00),
    imageurl VARCHAR(255) NOT NULL,
    created_by INT NOT NULL,
    product_type VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES User(id) ON DELETE CASCADE
);

