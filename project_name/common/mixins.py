class ReadWriteSerializerMixin:
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.
    Set read_serializer_class and write_serializer_class attributes on a
    viewset.
    """

    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        """Gets the serializer class

        :return: serializer class
        """
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        """Gets read serializer class"""
        assert self.read_serializer_class is not None, (
            f"{self.__class__.__name__} should either include a `read_serializer_class` attribute,"
            "or override the `get_read_serializer_class()` method."
        )
        return self.read_serializer_class

    def get_write_serializer_class(self):
        """Gets write serializer class"""
        assert self.write_serializer_class is not None, (
            f"{self.__class__.__name__} should either include a `write_serializer_class` attribute,"
            "or override the `get_write_serializer_class()` method."
        )
        return self.write_serializer_class


class MultiSerializerMixin:
    """
    Defines a different serializer for each method of a viewset.
    Implement list_serializer_class, create_serializer_class, update_serializer_class,
    partial_update_serializer_class and retrieve_serializer_class if methods implemented.
    """

    list_serializer_class = None
    create_serializer_class = None
    update_serializer_class = None
    partial_update_serializer_class = None
    retrieve_serializer_class = None

    def get_serializer_class(self):
        """Gets the serializer class"""
        if self.action == "create":
            return self.get_create_serializer_class()
        if self.action == "update":
            return self.get_update_serializer_class()
        if self.action == "partial_update":
            return self.get_partial_update_serializer_class()
        if self.action == "list":
            return self.get_list_serializer_class()

        return self.get_retrieve_serializer_class()

    def get_retrieve_serializer_class(self):
        """Returns the serializer class to use for the retrieve action."""
        assert self.retrieve_serializer_class is not None, (
            f"{self.__class__.__name__} should either include a `read_serializer_class` attribute,"
            "or override the `get_read_serializer_class()` method."
        )
        return self.retrieve_serializer_class

    def get_create_serializer_class(self):
        """Returns the serializer class to use for the create action."""
        assert self.create_serializer_class is not None, (
            f"{self.__class__.__name__} should either include a "
            "`create_serializer_class` attribute,"
            "or override the `get_create_serializer_class()` method."
        )
        return self.create_serializer_class

    def get_update_serializer_class(self):
        """Returns the serializer class to use for the update action."""
        assert self.update_serializer_class is not None, (
            f"{self.__class__.__name__} should either include a "
            "`update_serializer_class` attribute,"
            "or override the `get_update_serializer_class()` method."
        )
        return self.update_serializer_class

    def get_partial_update_serializer_class(self):
        """Returns the serializer class to use for the partial update action."""
        assert self.partial_update_serializer_class is not None, (
            f"{self.__class__.__name__} should either include a "
            "`partial_update_serializer_class` attribute,"
            "or override the `get_partial_update_serializer_class()` method."
        )
        return self.partial_update_serializer_class

    def get_list_serializer_class(self):
        """Returns the serializer class to use for the list action."""
        assert self.list_serializer_class is not None, (
            f"{self.__class__.__name__} should either include a "
            "`destroy_serializer_class` attribute,"
            "or override the `get_destroy_serializer_class()` method."
        )
        return self.list_serializer_class
