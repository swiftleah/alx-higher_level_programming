-- creates new user to MySQL server with password 'user_0d_1_pwd' if user doesn't already exist
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
