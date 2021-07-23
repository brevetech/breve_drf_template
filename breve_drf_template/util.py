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
        f = open(f"{base}/docs/apidocs/{filename}.md", "r")
        return f.read()
    except FileNotFoundError:
        return None
