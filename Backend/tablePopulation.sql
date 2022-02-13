INSERT INTO user (email, password, firstName, lastName, phoneNumber) VALUES
('test@gmail.com', 'password', 'Ali', 'MHZ', '5141111111');

INSERT INTO contacts (selfNumber, emergencyNumber) VALUES
('5141111111', '5148261505'),
('5141111111', '5142488420'),
('5141111111', '5148132924');

INSERT INTO encounter (userId, transcribedAudio, sentimentTags, latitude, longitude, resolved, isPrivate) VALUES
(1, 'transcribed audio', 'sentiment-tags', 45.500847, -73.585306, false, true);
