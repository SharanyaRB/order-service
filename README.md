# order-service
```
https://github.com/SharanyaRB/order-service
```

## [View Design Decisions and Trade Off](DESIGN_DECISION.md)

## [View REMOTE SERVER SETUP](REMOTE_SERVER_SETUP.md)

Backend Python Service to interact with MySQL DB for order processing

## 🛠 Setting Up Virtual Environment & Installing Requirements
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Database Setup Commands
Install MySQL and then run the following commands:

```sql
CREATE DATABASE app;
CREATE USER 'temp_user'@'localhost' IDENTIFIED BY 'temp_pass';
GRANT ALL PRIVILEGES ON app.* TO 'temp_user'@'localhost';
FLUSH PRIVILEGES;
```

## 🔄 Running Migrations
Ensure that migrations are correctly applied to the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## 🚀 Running App Locally for Debugging
Start the Flask application on the default port **5000**:
```bash
python app.py
```

## 📌 API Endpoints
## 📌 API Documentation
### **1️⃣ Ping API (No Authentication Required)**
#### **HTTP Request:**
- **GET** `/ping`

#### **cURL Command:**
For **HTTP**:
```bash
curl -X GET "http://3.27.70.158/ping"
```
For **HTTPS**:
```bash
curl -k -X GET "https://3.27.70.158/ping"
```
#### **Response Example:**
```json
{"message": "success"}
```

### **2️⃣ Create Order (Requires Basic Authentication)**
#### **HTTP Request:**
- **POST** `/orders`

#### **cURL Command:**
```bash
curl -u admin:securepassword -X POST "http://3.27.70.158/orders" \
     -H "Content-Type: application/json" \
     -d '{"order_id": 123, "user_id": 456, "item_ids": [1, 2, 3], "total_amount": 150.75}'
```
#### **Response Examples:**
✅ **Success Response:**
```json
{"message": "Order received", "order_id": 123}
```

❌ **Duplicate Order ID Request Example:**
```bash
curl -u admin:securepassword -X POST "http://3.27.70.158/orders" \
     -H "Content-Type: application/json" \
     -d '{"order_id": 123, "user_id": 456, "item_ids": [1, 2, 3], "total_amount": 150.75}'
```
❌ **Duplicate Order ID Response:**
```json
{"error": "Duplicate order_id. This order already exists."}
```

❌ **Missing Required Field (`user_id`) Request Example:**
```bash
curl -u admin:securepassword -X POST "http://3.27.70.158/orders" \
     -H "Content-Type: application/json" \
     -d '{"order_id": 124, "item_ids": [1, 2, 3], "total_amount": 150.75}'
```
❌ **Missing Required Field (`user_id`) Response:**
```json
{
  "error": {
    "user_id": [
      "Missing data for required field."
    ]
  }
}
```

❌ **Authentication Failure Request Example:**
```bash
curl -u wronguser:wrongpassword -X POST "http://3.27.70.158/orders" \
     -H "Content-Type: application/json" \
     -d '{"order_id": 125, "user_id": 789, "item_ids": [4, 5, 6], "total_amount": 99.99}'
```
❌ **Authentication Failure Response:**
```json
{
  "error": "Unauthorized access. Invalid credentials."
}
```

### **3️⃣ Get Order Status (Requires Basic Authentication)**
#### **HTTP Request:**
- **GET** `/orders/<order_id>`

#### **cURL Command:**
```bash
curl -u admin:securepassword -X GET "http://3.27.70.158/orders/123"
```
#### **Response Example:**
```json
{"order_id": 123, "status": "Processing"}
```

### **4️⃣ Fetch Order Processing Metrics (Requires Basic Authentication)**
#### **HTTP Request:**
- **GET** `/metrics`

#### **cURL Command:**
```bash
curl -u admin:securepassword -X GET "http://3.27.70.158/metrics"
```
#### **Response Example:**
```json
{
    "total_orders": 100,
    "pending_orders": 5,
    "processing_orders": 10,
    "completed_orders": 85,
    "avg_processing_time_seconds": 1.25
}
```