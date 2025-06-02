# AlphaSort Game

A word game where players arrange letters of words in alphabetical order.

**Proof-of-concept project using Cursor to build a small FastAPI API and a frontend for it.**

**Backend uses Python 3.12, MySQL (via Docker), SQLAlchemy, and Pydantic. Frontend uses TypeScript, React, and Tailwind.**

## Project Structure

```
alpharush/
├── api/                    # Backend API
│   ├── src/               # Source code
│   │   ├── main.py        # FastAPI application
│   │   ├── models.py      # Database models
│   │   ├── schemas.py     # Pydantic schemas
│   │   ├── database.py    # Database connection
│   │   └── config.py      # Configuration management
│   ├── migrations/        # Database migrations
│   ├── mysql/            # MySQL initialization scripts
│   ├── scripts/          # Utility scripts
│   ├── venv/             # Python virtual environment
│   ├── alembic.ini       # Alembic configuration
│   ├── docker-compose.yaml  # Docker configuration
│   └── requirements.txt   # Python dependencies
└── web/                  # Frontend application (to be implemented)
```

## Backend Setup

### Prerequisites

- Python 3.12.10
- Docker and Docker Compose
- MySQL 8.4.5 (via Docker)

### Installation

1. Create and activate virtual environment:
```bash
cd api
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

2. Start MySQL container:
```bash
docker-compose up -d
```

3. Verify database connection:
```bash
python scripts/setup_db.py
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Seed the database:
```bash
python src/seed.py
```

6. Start the API server:
```bash
uvicorn src.main:app --reload
```

The API will be available at http://localhost:8000

### API Endpoints

- `GET /api/phrases/random`: Get a random phrase to sort

## Frontend Setup

### Prerequisites

- Node.js 20.x or later
- npm 10.x or later

### Installation

1. Navigate to the frontend directory:
```bash
cd web
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:5173

### Development

- `npm run dev`: Start development server with hot reload
- `npm run build`: Build for production
- `npm run preview`: Preview production build locally
- `npm run lint`: Run ESLint
- `npm run type-check`: Run TypeScript type checking

### Environment Variables

Create a `.env` file in the `web` directory with the following variables:
```
VITE_API_URL=http://localhost:8000
```

## Development

### Database Migrations

To create a new migration:
```bash
cd api
alembic revision --autogenerate -m "description of changes"
```

To apply migrations:
```bash
alembic upgrade head
```

### Environment Variables

Create a `.env` file in the `api` directory with the following variables:
```
ENV=development
DATABASE_URL=mysql+pymysql://alphasort:alphasort_password@localhost/alphasort_dev
DEBUG=true
```

## License

MIT
