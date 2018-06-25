from math import radians, cos, sin, asin, sqrt

from yapylib.spatial.coord_transform_utils import EPSGProjection, gcj02towgs84, bd09towgs84


def haversine(lon1, lat1, lon2, lat2, default=EPSGProjection.WGS84):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    origin: https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
    """
    if default == EPSGProjection.WGS84:
        pass
    elif default == EPSGProjection.GCJ02:
        lon1, lat1 = gcj02towgs84(lon1, lat1)
        lon2, lat2 = gcj02towgs84(lon2, lat2)
        pass
    elif default == EPSGProjection.BD09:
        lon1, lat1 = bd09towgs84(lon1, lat1)
        lon2, lat2 = bd09towgs84(lon2, lat2)
    else:
        pass
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def pnt_in_polygon(point, polygon):
    """
    :param point:
    :param polygon:
    :return:

    ray-casting algorithm based on
    http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html
    应该是线性规划吧.....
    """
    inside = False
    x, y = point
    i = 0
    j = len(polygon) - 1
    while i < len(polygon):
        xi = polygon[i][0]
        yi = polygon[i][1]
        xj = polygon[j][0]
        yj = polygon[j][1]

        intersect = ((yi > y) != (yj > y)) and (
                x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
        j = i
        i += 1

    return inside
