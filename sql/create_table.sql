CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,  -- Manually assigned ID
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('admin', 'user'))
);
