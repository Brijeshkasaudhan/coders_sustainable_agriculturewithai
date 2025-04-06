-- Farmers Table
CREATE TABLE IF NOT EXISTS farmers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    soil_type TEXT,
    crop_history TEXT
);

-- Advisors Table
CREATE TABLE IF NOT EXISTS advisors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    expertise TEXT
);

-- Weather Data Table
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    date TEXT NOT NULL,
    temperature REAL,
    rainfall REAL,
    humidity REAL
);

-- Market Data Table
CREATE TABLE IF NOT EXISTS market (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT NOT NULL,
    price REAL,
    demand INTEGER
);

-- Recommendations Table
CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    farmer_id INTEGER,
    recommendation TEXT,
    date TEXT,
    FOREIGN KEY (farmer_id) REFERENCES farmers (id)
);
