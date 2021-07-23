from django.conf import settings

root = settings.BASE_DIR


def read_docs_md(filename):
    """
    Retrieves an apidoc markdown file to be implemented in swagger_auto_schema

    :param(str) filename: the filename to be retrieved without the .md file type
    :return: the content of the md file, None if not found
    """
    try:
        f = open(f"{root}/docs/apidocs/{filename}.md", "r")
        return f.read()
    except FileNotFoundError:
        return None
