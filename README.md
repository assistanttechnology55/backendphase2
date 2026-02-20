# Todo Application Backend

This is the backend for the Todo Application, built with FastAPI and SQLModel.

## Features

- User authentication (signup, login, JWT-based)
- Task management (CRUD operations)
- Role-based access control
- RESTful API design
- Type safety with Pydantic models
- Async database operations with SQLModel

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL (via SQLModel)
- **Authentication**: JWT with bcrypt hashing
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Async Support**: asyncio for concurrent operations

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login and get JWT token
- `POST /api/v1/auth/logout` - Logout user

### Tasks
- `GET /api/v1/tasks/` - Get all tasks for current user
- `POST /api/v1/tasks/` - Create a new task
- `GET /api/v1/tasks/{id}` - Get a specific task
- `PUT /api/v1/tasks/{id}` - Update a specific task
- `DELETE /api/v1/tasks/{id}` - Delete a specific task
- `PATCH /api/v1/tasks/{id}/complete` - Toggle task completion status

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL database

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with the following:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/todo_db
   SECRET_KEY=your-super-secret-jwt-key-change-this-in-production
   ```

5. Run the application:
   ```bash
   python start_server.py
   ```

The server will start on `http://localhost:8000`. Visit `http://localhost:8000/docs` for the interactive API documentation.

## Environment Variables

- `DATABASE_URL`: Connection string for the PostgreSQL database
- `SECRET_KEY`: Secret key for JWT token signing (use a strong random key in production)
- `ALGORITHM`: Algorithm used for JWT encoding (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes (default: 30)

## Project Structure

```
backend/
├── app/
│   └── main.py          # Main FastAPI application
├── api/
│   ├── api.py           # Main API router
│   └── routers/         # Individual API routers
│       ├── auth.py      # Authentication endpoints
│       └── tasks.py     # Task management endpoints
├── models/              # Database models
│   └── user.py          # User and Task models
├── schemas/             # Pydantic schemas for request/response validation
├── database.py          # Database connection and session management
├── core/                # Core application settings
│   └── config.py        # Configuration settings
├── utils/               # Utility functions
│   ├── auth.py          # Authentication utilities
│   └── common.py        # Common utility functions
├── requirements.txt     # Python dependencies
└── start_server.py      # Application startup script
```

## Running Tests

To run the tests:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.