import os


def get_environment_type():
    return os.getenv('APP_ENVIRONMENT') == 'PRD'
