from django.core.exceptions import ValidationError

def validate_file_size(file):
    MAX_SIZE = 100
    if file.size > MAX_SIZE * 1024:
        raise ValidationError(f"Max file size is {MAX_SIZE}KB")