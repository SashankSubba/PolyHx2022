DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS encounter;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    phoneNumber TEXT NOT NULL
);

CREATE TABLE contacts (
    selfNumber TEXT NOT NULL
        REFERENCES user(phoneNumber),
    emergencyNumber TEXT NOT NULL
);

CREATE TABLE encounter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER NOT NULL
        REFERENCES user(id),
    transcribedAudio TEXT,
    sentimentTags TEXT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    resolved BOOLEAN NOT NULL,
    isPrivate BOOLEAN NOT NULL
);