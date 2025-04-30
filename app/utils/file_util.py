import os

def read_sql_file(filename: str, path: str = __file__) -> str:
    current_dir = os.path.dirname(path)
    sql_path = os.path.join(current_dir, '..', 'sql', filename)
    with open(sql_path, 'r', encoding='utf-8') as file:
        return file.read()