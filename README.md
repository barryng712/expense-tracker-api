# expense-tracker-api
An API for an expense tracker application, allow users to create, read, update, and delete expenses. 
# Expense Tracker API

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/expense-tracker-api.git
    cd expense-tracker-api
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables** in `.env` file:
    ```env
    FLASK_APP=wsgi.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=mysql+pymysql://username:password@localhost/dbname
    ```

5. **Run migrations**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

6. **Run the application**:
    ```bash
    flask run
    ```

## Docker Setup

1. **Build Docker image**:
    ```bash
    docker-compose build
    ```

2. **Run Docker container**:
    ```bash
    docker-compose up
    ```

## API Endpoints

### User Endpoints

- **Register**: `POST /api/users/register`
- **Login**: `POST /api/users/login`

### Expense Endpoints

- **Add Expense**: `POST /api/expenses`

## Running Tests

1. **Run unit tests**:
    ```bash
    pytest
    ```

## License

This project is licensed under the MIT License.




├── app/
│   ├── __init__.py            # Initialize Flask app and extensions
│   ├── config.py              # Configuration file (environment variables)
│   ├── api/
│   │   ├── __init__.py        # Initialize API blueprint
│   │   ├── expenses/          # Expenses module
│   │   │   ├── models.py      # Define database models
│   │   │   ├── routes.py      # Expense-related routes (API endpoints)
│   │   │   ├── serializers.py # Schema definitions (marshmallow or flask-restful)
│   │   │   ├── tests.py       # Unit tests for expenses
│   │   ├── users/             # User management
│   │   │   ├── models.py      # User models
│   │   │   ├── routes.py      # Authentication routes
│   │   │   ├── serializers.py # Serialize user data
│   │   │   ├── tests.py       # Unit tests for user management
│
├── migrations/               # Database migrations (Flask-Migrate)
├── tests/                    # End-to-end testing for the overall API
├── .env                      # Environment variables
├── Dockerfile                # Containerization for Flask app
├── docker-compose.yml        # Docker configuration for multi-service apps
├── README.md                 # Documentation for project
├── requirements.txt          # Python dependencies
├── wsgi.py                   # Entry point for the Flask app
