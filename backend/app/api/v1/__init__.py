"""API v1 blueprint."""
from flask import Blueprint

# Create the v1 API blueprint
api_v1_bp = Blueprint('api_v1', __name__)

# Import routes to register them with the blueprint
from app.api.v1 import health as health  # noqa: E402
from app.api.v1 import listings as listings  # noqa: E402

__all__ = ("api_v1_bp", "health", "listings")
