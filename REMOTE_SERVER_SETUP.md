## 📌 Remote Server Setup with Nginx and Gunicorn

### ** Start Gunicorn Server**
Run Gunicorn in daemon mode:
```bash
gunicorn --workers 4 --bind 0.0.0.0:8000 app:app --daemon
```
Verify that Gunicorn is running:
```bash
ps aux | grep gunicorn
```

### ** Configure Nginx as Reverse Proxy**
Create a new Nginx configuration file:
```bash
sudo nano /etc/nginx/sites-available/order-service
```
Add the following configuration:
```nginx
server {
    listen 80;
    server_name 3.27.70.158;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

server {
    listen 443 ssl;
    server_name 3.27.70.158;

    ssl_certificate /etc/nginx/ssl/selfsigned.crt;
    ssl_certificate_key /etc/nginx/ssl/selfsigned.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
Save and exit (`CTRL + X`, then `Y`, then `ENTER`).

### ** Enable and Restart Nginx**
```bash
sudo ln -s /etc/nginx/sites-available/order-service /etc/nginx/sites-enabled/
sudo nginx -t  # Test configuration
sudo systemctl restart nginx
sudo systemctl enable nginx
```

### ** Test the Deployment**
Verify API endpoints:
```bash
curl -X GET "http://3.27.70.158/ping"
curl -k -X GET "https://3.27.70.158/ping"
```

### ** Restart Services if Needed**
If Gunicorn stops working:
```bash
pkill gunicorn
nohup gunicorn --workers 4 --bind 0.0.0.0:8000 app:app &
```
If Nginx needs a restart:
```bash
sudo systemctl restart nginx
```

