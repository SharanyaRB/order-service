from flask import Flask
from config import Config
from models import db, migrate
from routes import api_bp
from queue_handler import start_order_processing

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

# Register Blueprints
app.register_blueprint(api_bp)

# Start queue processing thread inside app context
with app.app_context():
    start_order_processing(app)

if __name__ == '__main__':
    app.run(debug=True)
