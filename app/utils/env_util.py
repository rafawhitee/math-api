import os
from utils.bool_util import to_bool

def get_prefix():
    prefix_from_env = get_env_value("PREFIX")
    if prefix_from_env == None or prefix_from_env == "":
        return ""
    return prefix_from_env if prefix_from_env.startswith('/') else f"/{prefix_from_env}"

def get_env_value_as_bool(key, default_value = False):
    env_value = get_env_value(key)
    return to_bool(env_value) if env_value != None else default_value

def get_env_value_as_int(key, default_value: int | None = None):
    env_value = get_env_value(key)
    return int(env_value) if env_value != None else default_value

def get_env_value(key, default_value = None):
    env_value = os.getenv(key)
    return env_value if env_value != None else default_value