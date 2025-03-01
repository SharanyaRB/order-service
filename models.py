from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    item_ids = db.Column(db.Text, nullable=False)  # Storing item IDs as a comma-separated string
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Auto-set on creation
    modified_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Auto-update on modification
    created_by = db.Column(db.Integer, nullable=True)  # User ID of the creator
    modified_by = db.Column(db.Integer, nullable=True)  # User ID of the last modifier
    deleted_at = db.Column(db.DateTime, nullable=True)  # Soft delete timestamp
    is_active = db.Column(db.Boolean, default=True)  # Mark active/inactive orders
    processing_time = db.Column(db.Float, nullable=True)  # Time taken to process (in seconds)