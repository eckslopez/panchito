# Project Context for AI Assistants

## Purpose
Flask-based data ingestion and API service for real estate data. Demonstrates production Python patterns: async tasks (Celery), data validation (Pydantic), RESTful API design.

## Current State
Phase I complete (foundation). Phase II in progress (core data model). Migrating from MariaDB to PostgreSQL for pg-multitenant integration. Issue backlog tracked in GitHub.

## Key Files
- `README.md` - Architecture and quick start
- `CLAUDE.md` - Detailed development guide for AI assistants
- `backend/app/` - Flask application structure
- `docker-compose.yaml` - Local development environment
- GitHub Issues - Feature tracking and phase milestones

## Working With This Repo

**Local development:**
```bash
# Start all services
docker compose up -d

# View logs
docker compose logs -f backend

# Run tests (once Phase II complete)
docker compose run --rm backend pytest

# Database migrations
docker compose exec backend flask db upgrade
```

**Project structure:**
```
backend/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── config.py          # Environment configuration
│   ├── models/            # SQLAlchemy models
│   ├── api/v1/            # REST API endpoints
│   ├── services/          # Business logic
│   ├── tasks/             # Celery tasks
│   └── schemas/           # Pydantic validation
├── tests/                 # Test suite (structure ready)
├── migrations/            # Alembic migrations
└── requirements.txt       # Dependencies
```

## Architecture

**Technology Stack:**
- Flask 3.1 with app factory pattern
- SQLAlchemy 2.0 ORM
- PostgreSQL database (migrating from MariaDB)
- Celery + Redis for async tasks
- Pydantic for data validation
- Docker Compose for local dev

**Service Architecture:**
```
Nginx (port 80) → Flask (port 8000)
                   ↓
                PostgreSQL
                   ↓
                Celery Workers ← Redis
```

**API Endpoints (Phase II):**
- `GET /api/v1/health` - Health check
- `GET /api/v1/health/ready` - Readiness probe
- `GET /api/v1/listings` - List all listings (paginated)
- `GET /api/v1/listings/{id}` - Get single listing
- `POST /api/v1/ingest/trigger` - Trigger ETL job
- `GET /api/v1/ingest/status/{job_id}` - Job status

## Related Repos
- **zavestudios** - Parent documentation hub
- **platform-pipelines** - CI/CD workflows (Python test/lint)
- **pg-multitenant** - Target database platform
- **thehouseguy** - Consumer application (Rails app)

## CI/CD
GitHub Actions workflows:
- `test.yml` - pytest with PostgreSQL service container
- `security.yml` - gitleaks secret scanning

---

## Maintaining This File

**When to update:**
- Phase milestones reached (update Current State)
- API endpoints added (update Architecture section)
- Database migration complete (remove "migrating from MariaDB")
- New services added to docker-compose
- Major dependency changes

**What NOT to include:**
- Detailed API documentation (belongs in README.md)
- Database schema details (self-documenting in models/)
- Development workflows (belongs in README.md)
- Phase implementation details (belongs in GitHub Issues)

**Keep it under 100 lines total.**
