from bs4 import BeautifulSoup

def sanitize_query_params(query_params):
    sanitized_params = {}
    if has_query_params(query_params):
        for key, value in query_params.items():
            sanitized_params[key] = remove_html_tags_and_scripts_styles(value)
            if value and str(value).strip() == 'null':
                sanitized_params[key] = ''
    return sanitized_params

def has_query_params(query_params) -> bool:
    if query_params:
        for next_item in query_params.items():
            return next_item != None
    return False

def remove_html_tags_and_scripts_styles(text):
    soup = BeautifulSoup(text, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose() 
    return soup.get_text()