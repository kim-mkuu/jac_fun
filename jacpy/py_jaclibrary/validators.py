"""Python validation utilities"""

def validate_title(title: str) -> bool:
    "Title validator"
    return len(title) > 3