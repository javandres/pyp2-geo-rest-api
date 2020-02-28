# encoding: utf-8

from app import api_v1


class GeoApiNamespace:
    namespace = "pyp2"
    description = "PyP2 GeoAPI"


def init_app(app, **kwargs):
    """
    Init the PyP2 GeoAPI module.
    """

    # Load the underlying module
    from . import resources

    api_v1.add_namespace(resources.api)