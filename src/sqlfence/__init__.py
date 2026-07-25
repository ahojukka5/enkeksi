"""Public API for sqlfence."""

from .core import RenderOptions, SqlfenceError, render_markdown

# Compatibility name for code migrating from the pre-1.0 project.
EnkeksiError = SqlfenceError

__all__ = [
    "EnkeksiError",
    "RenderOptions",
    "SqlfenceError",
    "render_markdown",
]
__version__ = "1.0.0"
