import abc

import collections

from yapylib.gis.coord_transform_utils import EPSGProjection, wgs84togcj02, wgs84tobd09
from yapylib.gis.measure_utils import haversine, pnt_in_polygon


class GeometryCollection(abc.ABC):
    """
    用于存放多个Geometry
    """
    pass


class Geometry(abc.ABC):
    pass


class Point(collections.abc.Iterable, Geometry):
    """
    用于存放Point
    """

    def __init__(self, lng, lat, coord=EPSGProjection.WGS84):
        self.center_point = []
        if coord is EPSGProjection.WGS84:
            self.wgs84_lng = lng
            self.wgs84_lat = lat
            self.gcj02_lng, self.gcj02_lat = wgs84togcj02(self.wgs84_lng, self.wgs84_lat)
            self.bd09_lng, self.bd09_lat = wgs84tobd09(self.wgs84_lng, self.wgs84_lat)
            self.center_point = [self.wgs84_lng, self.wgs84_lat]
            pass
        elif coord is EPSGProjection.GCJ02:
            pass
        elif coord is EPSGProjection.BD09:
            pass
        pass

    def distance(self, poi_obj):
        return haversine(poi_obj.wgs_lng, poi_obj.wgs_lat, EPSGProjection.WGS84)

    def __iter__(self):
        return iter(self.center_point)


class Polygon(collections.abc.Iterable, Geometry):

    def __init__(self, points, coord=EPSGProjection.WGS84):
        self.center_points = []
        if points and len(points) > 3:
            # TODO : 初始化相关参数
            if points[0] == points[-1]:
                pass
            else:
                points.append(points[0])
            for p in points:
                x, y = p
                self.center_points.append([x, y])
        else:
            raise Exception("请检查参数")

    def __contains__(self, point):
        if not isinstance(point, Point):
            raise Exception("参数必须为 Point 类型")
        else:
            return pnt_in_polygon(point, self.center_points)

    def __iter__(self):
        return iter(self.center_point)
