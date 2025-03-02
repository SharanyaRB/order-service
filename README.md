# order-service
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
### 1️⃣ **Create Order**
- **Endpoint:** `POST /orders`
- **Description:** Accepts an order and adds it to the processing queue all the fields are mandotry with validations in place for datatypes and order duplication.
- **Request Body:**
  ```json
  {
      "order_id": 123,
      "user_id": 456,
      "item_ids": [1, 2, 3],
      "total_amount": 150.75
  }
  ```
- **Response:**
  ```json
  {"message": "Order received", "order_id": 123}
  ```
- **Request Body:**
  ```json
  {
      "order_id": 123,
      "user_id": 456,
      "item_ids": [1, 2, 3],
      "total_amount": 150.75
  }
  ```
- **Response:**
 ```json
  {"error": "Duplicate order_id. This order already exists."}
  ```
- **Request Body:**
  ```json
  {
      "order_id": 123,
      "item_ids": [1, 2, 3],
      "total_amount": 150.75
  }
  ```
- **Response:**
 ```json
 {
  "error": {
    "user_id": [
      "Missing data for required field."
    ]
  }
}
 ```


### 2️⃣ **Get Order Status**
- **Endpoint:** `GET /orders/<order_id>`
- **Description:** Fetches the current status of an order.
- **Response Example:**
  ```json
  {"order_id": 123, "status": "Processing"}
  ```

### 3️⃣ **Fetch Order Processing Metrics**
- **Endpoint:** `GET /metrics`
- **Description:** Returns aggregated statistics about order processing.
- **Response Example:**
  ```json
  {
      "total_orders": 100,
      "pending_orders": 5,
      "processing_orders": 10,
      "completed_orders": 85,
      "avg_processing_time_seconds": 1.25
  }
  ```

