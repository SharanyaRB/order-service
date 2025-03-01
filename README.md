# order-service
Mock Service to interact with MySQL DB for order processing

# DB Set Up Commands
Install mysql

```
CREATE DATABASE app;
CREATE USER 'temp_user'@'localhost' IDENTIFIED BY 'temp_pass';
GRANT ALL PRIVILEGES ON app.* TO 'temp_user'@'localhost';
```

# Runinng Migration
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

# Running app locally for deebugging  on default port 5000
`python app.py`

