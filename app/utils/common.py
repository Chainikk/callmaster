import os


def get_env_path():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_file_path = os.path.abspath(os.path.join(current_directory, '.env'))
    return env_file_path
