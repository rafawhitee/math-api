import re

def has_headers(text: str) -> bool:
    return re.search(r'##\s*.*?\s*##', text) != None

def remove_headers(text: str, new_text: str = '') -> str:
    return re.sub(r'##\s*.*?\s*##', new_text, text)

def remove_nulls(text: str, new_text: str = " ") -> str:
    return replace(text, "\x00", new_text)

def remove_lines_breaks(text: str, new_text: str = " ") -> str:
    return replace(text, "\n", new_text)

def remove_tabs(text: str, new_text: str = " ") -> str:
    return replace(text, "\t", new_text)

def replace(text: str, old: str, new: str) -> str:
    return text.replace(old, new)
