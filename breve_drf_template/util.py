from django.core.files.storage import default_storage


def read_docs_md(filename):
    """
    Retrieves an apidoc markdown file to be implemented in swagger_auto_schema
        Parameters:
            filename (str): the filename to be retrieved without the .md file type

        Returns:
            file_content (str): the content of the md file, None if not found
    """
    try:
        f = default_storage.open(f"docs/apidocs/{filename}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None