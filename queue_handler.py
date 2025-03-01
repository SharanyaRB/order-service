# Logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Queue Handler
import queue
import threading
import time
import random
from models import db, Order
from services.order_service import update_order_status

order_queue = queue.Queue()

def process_orders(app):
    with app.app_context():
        logger.info("Queue has started processing orders...")
        while True:
            order_id = order_queue.get()
            if order_id is None:
                break  # Exit condition
            try:
                start_time = time.time()
                
                # Update order status to Processing using service method
                update_order_status(order_id, 'processing')
                
                time.sleep(random.uniform(0, 0.2))  # Simulating random processing time between 0 - 200 ms
                
                # Calculate processing time
                processing_time = time.time() - start_time
                
                # Update order status to Completed using service method
                update_order_status(order_id, 'completed', processing_time)
                
                order_queue.task_done()
                logger.info(f"Order {order_id} processed in {processing_time:.2f} seconds.")
            except Exception as e:
                logger.error(f"Error processing order {order_id}: {str(e)}")
                db.session.rollback()

def start_order_processing(app):
    thread = threading.Thread(target=process_orders, args=(app,), daemon=True)
    thread.start()