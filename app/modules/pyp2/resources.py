"""
RESTful API GeoAPI resources
--------------------------
"""

import geopy.distance
import pyproj
from app.modules.geoapi import GeoApiNamespace
from flask import request
from flask_restplus import Namespace, Resource, abort
from flask_restplus import fields
from functools import partial
from geopy import Point as GeopyPoint, distance
from http import HTTPStatus
from shapely.geometry import Polygon, LineString
from shapely.ops import transform
import urllib
import geojson


api = Namespace('pyp2', description=GeoApiNamespace.description)

@api.route('/hexgrid/')
class HexGrid(Resource):
    """
    Return hexagonal grid.
    """

    @api.doc(id='hex_grid')
    def get(self):
        """
        Return hexagonal grid.
        """
        try:
            with open("app/modules/pyp2/data/malla.geojson") as f:
                data = geojson.load(f)
            return data
        except Exception:
            pass

        abort(HTTPStatus.BAD_REQUEST,
              message="Please provide a valid query e.g. with the following url arguments: "
                      "http://127.0.0.1:4000/api/geoapi/point/distance/?start_lng=8.83546&start_lat=53.071124&end_lng=10.006168&end_lat=53.549926")

