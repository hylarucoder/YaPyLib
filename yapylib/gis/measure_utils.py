from math import radians, cos, sin, asin, sqrt

from yapylib.gis.coord_transform_utils import EPSGProjection, bd09togcj02, gcj02towgs84, bd09towgs84


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
