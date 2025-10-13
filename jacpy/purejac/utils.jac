"""Validation and AI utilities."""

def validate_title(title: str) -> bool {
    return len(title) > 3;
}

def generate_desc(title: str) -> str {
    return f"Task description for {title}";
} 