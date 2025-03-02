📌 Design Decisions and Assumptions
===================================

**1️⃣ Design Decisions and Trade-offs**
---------------------------------------

### **Architecture and Scalability**

*   **Flask with Gunicorn:** Chosen for its simplicity and ability to handle concurrent requests efficiently.
    
*   **Nginx as a Reverse Proxy:** Used to serve requests and forward them to Gunicorn, improving security and request handling.
    
*   **MySQL Database:** Structured storage with ACID compliance ensures data consistency.
    
*   **In-Memory Queue:** Python's queue.Queue was used to simulate an asynchronous order processing system without external dependencies like Redis.
    

### **API Design**

*   **RESTful APIs:** Structured for easy interaction and scalability.
    
*   **Basic Authentication:** Implemented via Flask-HTTPAuth for secured endpoints.
    
*   **Input Validation:** Marshmallow was used to enforce correct request formats and data integrity.
    

### **Trade-offs Made**

*   **Queueing Strategy:** Instead of RabbitMQ or Kafka, a Python in-memory queue was used for simplicity, limiting horizontal scalability.
    
*   **Database Choice:** MySQL ensures structured data consistency, but NoSQL (e.g., MongoDB) could offer more flexibility.
    
*   **Authentication Simplicity:** Basic Auth was chosen over OAuth2 or JWT for rapid implementation.
    
*   **Self-Signed SSL:** Since no domain was used, HTTPS was configured with a self-signed certificate instead of Let's Encrypt.
    

**2️⃣ Assumptions Made During Development**
-------------------------------------------

### **Order Processing**

*   Orders are **processed asynchronously** using an in-memory queue.
    
*   An order transitions from Pending → Processing → Completed when picked up by the queue.
    
*   Orders **cannot be modified** once submitted.
    

### **API Behavior**

*   order\_id is **assumed unique**, and duplicate orders with the same ID are rejected.
    
*   The user\_id field is **mandatory**, and an error is returned if missing.
    
*   Requests without authentication to secured endpoints return a 401 Unauthorized response.
    
*   The /ping endpoint is **publicly accessible** without authentication for health checks.
    

### **Deployment & Networking**

*   The application is **hosted on an AWS EC2 instance**.
    
*   **Gunicorn runs as a daemon**, ensuring continuous request handling.
    
*   **Nginx is configured for both HTTP and HTTPS**, with SSL enabled via a self-signed certificate.
    
*   Security groups allow traffic on **ports 80 (HTTP) and 443 (HTTPS)**, while **Gunicorn listens on port 8000** internally.