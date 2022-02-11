import environ

from django.conf import settings


def read_docs_md(filename, root=None):
    """
    Retrieves an apidoc markdown file to be implemented in swagger_auto_schema
    :param(str) root: root base dir, settings.BASE_DIR as default
    :param(str) filename: the filename to be retrieved without the .md file type
    :return: the content of the md file, None if not found
    """
    base = root or settings.BASE_DIR
    try:
        f = open(f"{base}/apidocs/{filename}.md", "r")
        return f.read()
    except FileNotFoundError:
        return None


def get_env_reader(levels):
    """
    Creates a django-environ reader setting root from the specified levels, for level 1 being .env
    in the same folder than the .py file, so on and so forth
    :param(int) levels: the levels that the root will be placed relative to the .py file reference
    :return: env reader.
    """

    root = environ.Path(start=__file__) - levels
    env = environ.Env()
    env.read_env('.env')

    return env


def extract_errors(errors_dict, parent_name=""):
    """
    Plains a validation errors dict into a list with 'Error in field: error' message strings recursively
    :param(dict) errors_dict: the error dict
    :param(str) parent_name: the parent name (optional), defaults to ""
    :return: the plain error messages strings list
    :rtype: list
    """
    error_list = []
    for field in errors_dict:
        if isinstance(errors_dict[field], dict):
            error_list += extract_errors(
                errors_dict[field],
                parent_name=(f"{parent_name}.{field}" if parent_name else field),
            )
        else:
            error_list += [
                f"Error in field {f'{parent_name}.' if parent_name else ''}{field}: {error}"
                for error in errors_dict[field]
            ]
    return error_list
