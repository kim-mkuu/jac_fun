"""Python validation utilities"""

def validate_title(title: str) -> bool:
    "Validator used across multiple projects"
    return len(title) > 3

def get_sample_title():
    """Helper to load sample data"""
    return "Build API"