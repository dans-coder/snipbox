# SnipBox Backend API

SnipBox is a short note saving application that allows users to save and organize notes with tags. This repository contains the backend API built with Django Rest Framework.

## Features

- JWT Authentication
- CRUD operations for snippets
- Tag management
- User-specific snippets
- RESTful API endpoints

## Prerequisites

- Python 3.8+
- PostgreSQL
- Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd snipbox
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure your settings:
```bash
cp .env.example .env  # On Windows: copy .env.example .env
```
Edit the `.env` file to set your SECRET_KEY, DEBUG, ALLOWED_HOSTS, and database settings as needed.

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Documentation

### Authentication Endpoints

1. Login API
```bash
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

2. Refresh Token API
```bash
POST /api/token/refresh/
{
    "refresh": "your_refresh_token"
}
```

### Snippet Endpoints

1. Overview API
```bash
GET /api/snippets/
```

2. Create Snippet
```bash
POST /api/snippets/
{
    "title": "Snippet Title",
    "note": "Snippet content",
    "tags": ["tag1", "tag2"]
}
```

3. Detail API
```bash
GET /api/snippets/{id}/
```

4. Update API
```bash
PUT /api/snippets/{id}/
{
    "title": "Updated Title",
    "note": "Updated content",
    "tags": ["tag1", "tag3"]
}
```

5. Delete API
```bash
DELETE /api/snippets/{id}/
```

### Tag Endpoints

1. List Tags
```bash
GET /api/tags/
```

2. Tag Detail
```bash
GET /api/tags/{id}/
```

## Docker Deployment

1. Build the Docker image:
```bash
docker-compose build
```

2. Run the containers:
```bash
docker-compose up -d
```

## Database Schema

The application uses the following models:

1. User (Django's built-in User model)
2. Tag
   - title (unique)
3. Snippet
   - title
   - note
   - created_at
   - updated_at
   - user (ForeignKey to User)
   - tags (ManyToMany to Tag)

## Testing

Run the test suite:
```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 