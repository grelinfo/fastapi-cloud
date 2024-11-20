"""Grelmicro Synchronization Primitives Module."""

from grelmicro.sync.leaderelection import LeaderElection
from grelmicro.sync.lock import Lock

__all__ = ["Lock", "LeaderElection"]
