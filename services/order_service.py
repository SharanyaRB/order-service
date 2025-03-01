from models import db, Order
from datetime import datetime

def create_new_order(data):
    new_order = Order(
        order_id=data['order_id'],
        user_id=data['user_id'],
        item_ids=','.join(map(str, data['item_ids'])),
        total_amount=data['total_amount'],
        status='pending',
        created_by=data['user_id'],
        created_at=datetime.utcnow(),
        modified_at=datetime.utcnow(),
        is_active=True
    )
    db.session.add(new_order)
    db.session.commit()
    return new_order

def get_order_by_id(order_id):
    return Order.query.filter_by(order_id=order_id, is_active=True).first()

def get_order_metrics():
    total_orders = Order.query.count()
    pending_orders = Order.query.filter_by(status='Pending', is_active=True).count()
    processing_orders = Order.query.filter_by(status='Processing', is_active=True).count()
    completed_orders = Order.query.filter_by(status='Completed', is_active=True).count()
    
    completed_orders_data = Order.query.filter(Order.status == 'Completed', Order.is_active == True).all()
    avg_processing_time = (
        sum(order.processing_time for order in completed_orders_data) / len(completed_orders_data)
        if completed_orders_data else 0
    )

    return {
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'processing_orders': processing_orders,
        'completed_orders': completed_orders,
        'avg_processing_time_seconds': round(avg_processing_time, 2)
    }

def update_order_status(order_id, status, processing_time=None):
    order = Order.query.filter_by(order_id=order_id).first()
    if order:
        order.status = status
        if processing_time is not None:
            order.processing_time = processing_time
        db.session.commit()