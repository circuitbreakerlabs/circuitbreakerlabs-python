"""A client library for accessing Circuit Breaker Labs API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
