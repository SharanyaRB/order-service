from flask import Blueprint, request, jsonify
from queue_handler import order_queue
from validator import OrderSchema 
from marshmallow import ValidationError
from services.order_service import create_new_order, get_order_by_id, get_order_metrics

api_bp = Blueprint('api', __name__)
order_schema = OrderSchema()  

@api_bp.route('/orders', methods=['POST'])
def create_order():
    try:
        # Validate incoming request
        data = order_schema.load(request.get_json())
        # Check if order_id already exists
        existing_order = get_order_by_id(data['order_id'])
        if existing_order:
            return jsonify({'error': 'Duplicate order_id. This order already exists.'}), 400
        new_order = create_new_order(data)
        order_queue.put(new_order.order_id)
        return jsonify({'message': 'Order received', 'order_id': new_order.order_id}), 201
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

@api_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order_status(order_id):
    try:
        order = get_order_by_id(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        return jsonify({'order_id': order.order_id, 'status': order.status})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify(get_order_metrics())
