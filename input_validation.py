def is_valid_number(value):
    """Check if the input value can be converted to a float."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
