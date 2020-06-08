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
import requests


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


@api.route('/isochrone_otp/')
class Isochrone(Resource):
    """
    Return isochrone with Open Trip Planner API
    """

    @api.doc(id='isochrone_otp')
    def post(self):
        """
        Return isochrone with Open Trip Planner API
        """
        locations = request.json['locations']
        costing = request.json['costing']
        contours = request.json['contours']
        fromPlace = str(locations[0]["lat"])+','+str(locations[0]["lon"])
        mode="WALK"
        if costing == "bicycle":
            mode = "BICYCLE"
        elif costing== "bus":    
            mode = "WALK, TRANSIT"
        #params = {"locations": locations, "costing":costing,"contours":contours, "generalize":30}
        params = {
            'fromPlace': fromPlace,
            'mode': mode,
            'date' : '11-14-2020',
            'time':'8:00am',
            'maxWalkDistance': '500',
            'cutoffSec': contours[0]["time"]*60,
            'locale':'es'
        }
        otpurl = 'http://201.159.223.152/otp/routers/default'
        #http://localhost:8080/otp/routers/default/plan?fromPlace=-2.8878374918762115%2C-79.02036666870117&toPlace=-2.902581526675543%2C-79.00766372680663&time=5%3A48pm&date=04-26-2020&mode=BICYCLE&maxWalkDistance=804.672&arriveBy=false&wheelchair=false&optimize=TRIANGLE&triangleTimeFactor=0.38271604938271603&triangleSlopeFactor=0.26336672107399556&triangleSafetyFactor=0.35391722954328847&locale=en
        print(params)
        r = requests.get(
            otpurl+'/isochrone',
            params=params)
        return r.json()

@api.route('/isochrone_valhalla/')
class Isochrone(Resource):
    """
    Return isochrone Valhalla API
    """

    @api.doc(id='isocrhone')
    def post(self):
        """
        Return isochrone Valhalla API
        """
        locations = request.json['locations']
        costing = request.json['costing']
        contours = request.json['contours']

        params = {"locations": locations, "costing":costing,"contours":contours, "generalize":30}
        r = requests.post(
                'http://localhost:8002/isochrone',
                json=params
        )
 
        return r.json()

