import os
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask
from flask_migrate import Migrate
from sqlalchemy import create_engine, text
from models.student_model import db
from students.routes import students_bp


# Load settings
load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# CORS
CORS(app)

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)

# Create table if not exists
with app.app_context():
    db.create_all()


# Routes
app.register_blueprint(students_bp)


def create_engine_with_retry():
    db_config = {
        'host': os.getenv('DB_HOST', 'mysql'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'rootpassword'),
        'database': os.getenv('DB_NAME', 'mydatabase'),
        'port': 3306
    }
    
    db_url = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    
    print(f"🔗 Intentando conectar a: {db_config['host']}:{db_config['port']}")
    
    engine = create_engine(db_url)
    
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Conexión exitosa a MySQL!")
            return engine
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        raise

if __name__ == '__main__':
    app.run(debug=True)

