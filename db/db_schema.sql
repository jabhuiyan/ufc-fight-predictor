CREATE TABLE IF NOT EXISTS fighters (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    height_cm REAL,
    weight_kg REAL,
    reach_cm REAL,
    stance TEXT,
    wins INTEGER,
    losses INTEGER,
    draws INTEGER,
    strikes_per_min REAL,
    striking_accuracy REAL,
    takedown_avg REAL,
    takedown_accuracy REAL,
    takedown_defense REAL,
    submission_avg REAL
);
