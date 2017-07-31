import pytest

from yapylib.gis.models.geometries import Point, Polygon

test_polygons = {
    "simple": [[2, 1], [3, 1], [4, 2], [4, 3], [4, 3], [3, 4], [2, 4], [1, 3], [1, 2]],
}


@pytest.mark.parametrize('test_pnt,test_polygon_name,expected', [
    ([1.5, 1.5], "simple", True),
    ([1.9, 1.1], "simple", False),
    ([1.5, 1.3], "simple", True),
    ([1.3, 1.5], "simple", False),
    ([4.9, 1.2], "simple", False),
    ([1.8, 1.1], "simple", False),
])
def test_pnt_in_polygon(test_pnt, test_polygon_name, expected):
    point = Point(test_pnt[0], test_pnt[1])
    polygon = Polygon(test_polygons[test_polygon_name])
    assert (point in polygon) is expected
