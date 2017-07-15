import abc

from yapylib.gis.coord_transform_utils import EPSGProjection, wgs84togcj02, wgs84tobd09
from yapylib.gis.measure_utils import haversine


class GeometryCollection(abc.ABC):
    """
    用于存放多个Geometry
    """
    pass


class Geometry(abc.ABC):
    pass


class Point(Geometry):
    """
    用于存放Point
    """

    def __init__(self, lng, lat, coord=EPSGProjection.WGS84):
        if coord is EPSGProjection.WGS84:
            self.wgs84_lng = lng
            self.wgs84_lat = lat
            self.gcj02_lng, self.gcj02_lat = wgs84togcj02(self.wgs84_lng, self.wgs84_lat)
            self.bd09_lng, self.bd09_lat = wgs84tobd09(self.wgs84_lng, self.wgs84_lat)
            pass
        elif coord is EPSGProjection.GCJ02:
            pass
        elif coord is EPSGProjection.BD09:
            pass
        pass

    def distance(self, poi_obj):
        return haversine(poi_obj.wgs_lng, poi_obj.wgs_lat, EPSGProjection.WGS84)
