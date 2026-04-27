"""Web mercator XYZ tile utilities"""

from collections import namedtuple
from functools import reduce
import math
import sys
import warnings
import operator

if sys.version_info < (3,):
    warnings.warn(
        "Python versions < 3 will not be supported by mercantile 2.0.",
        UserWarning,
    )
    from collections import Sequence

    def lru_cache(maxsize=None):
        """Does nothing. We do not cache for Python < 3."""
        def fake_decorator(func):
            pass

        pass


else:
    from collections.abc import Sequence
    from functools import lru_cache


__version__ = "1.2.1"

__all__ = [
    "Bbox",
    "LngLat",
    "LngLatBbox",
    "Tile",
    "bounding_tile",
    "bounds",
    "children",
    "feature",
    "lnglat",
    "neighbors",
    "parent",
    "quadkey",
    "quadkey_to_tile",
    "simplify",
    "tile",
    "tiles",
    "ul",
    "xy_bounds",
    "minmax",
]


R2D = 180 / math.pi
RE = 6378137.0
CE = 2 * math.pi * RE
EPSILON = 1e-14
LL_EPSILON = 1e-11


class Tile(namedtuple("Tile", ["x", "y", "z"])):
    """An XYZ web mercator tile

    Attributes
    ----------
    x, y, z : int
        x and y indexes of the tile and zoom level z.

    """

    def __new__(cls, x, y, z):
        """A new instance"""
        lo, hi = minmax(z)
        if not lo <= x <= hi or not lo <= y <= hi:
            warnings.warn(
                "Mercantile 2.0 will require tile x and y to be within the range (0, 2 ** zoom)",
                FutureWarning,
            )
        return tuple.__new__(cls, [x, y, z])


LngLat = namedtuple("LngLat", ["lng", "lat"])
"""A longitude and latitude pair

Attributes
----------
lng, lat : float
    Longitude and latitude in decimal degrees east or north.
"""


LngLatBbox = namedtuple("LngLatBbox", ["west", "south", "east", "north"])
"""A geographic bounding box

Attributes
----------
west, south, east, north : float
    Bounding values in decimal degrees.
"""


Bbox = namedtuple("Bbox", ["left", "bottom", "right", "top"])
"""A web mercator bounding box

Attributes
----------
left, bottom, right, top : float
    Bounding values in meters.
"""


class MercantileError(Exception):
    """Base exception"""


class InvalidLatitudeError(MercantileError):
    """Raised when math errors occur beyond ~85 degrees N or S"""


class InvalidZoomError(MercantileError):
    """Raised when a zoom level is invalid"""


class ParentTileError(MercantileError):
    """Raised when a parent tile cannot be determined"""


class QuadKeyError(MercantileError):
    """Raised when errors occur in computing or parsing quad keys"""


class TileArgParsingError(MercantileError):
    """Raised when errors occur in parsing a function's tile arg(s)"""


class TileError(MercantileError):
    """Raised when a tile can't be determined"""


def _parse_tile_arg(*args):
    """parse the *tile arg of module functions

    Parameters
    ----------
    tile : Tile or sequence of int
        May be be either an instance of Tile or 3 ints, X, Y, Z.

    Returns
    -------
    Tile

    Raises
    ------
    TileArgParsingError

    """
    pass


def ul(*tile):
    """Returns the upper left longitude and latitude of a tile

    Parameters
    ----------
    tile : Tile or sequence of int
        May be be either an instance of Tile or 3 ints, X, Y, Z.

    Returns
    -------
    LngLat

    Examples
    --------

    >>> ul(Tile(x=0, y=0, z=1))
    LngLat(lng=-180.0, lat=85.0511287798066)

    >>> mercantile.ul(1, 1, 1)
    LngLat(lng=0.0, lat=0.0)

    """
    pass


def bounds(*tile):
    """Returns the bounding box of a tile

    Parameters
    ----------
    tile : Tile or tuple
        May be be either an instance of Tile or 3 ints (X, Y, Z).

    Returns
    -------
    LngLatBbox

    """
    pass


def truncate_lnglat(lng, lat):
    pass


def xy(lng, lat, truncate=False):
    """Convert longitude and latitude to web mercator x, y

    Parameters
    ----------
    lng, lat : float
        Longitude and latitude in decimal degrees.
    truncate : bool, optional
        Whether to truncate or clip inputs to web mercator limits.

    Returns
    -------
    x, y : float
        y will be inf at the North Pole (lat >= 90) and -inf at the
        South Pole (lat <= -90).

    """
    pass


def lnglat(x, y, truncate=False):
    """Convert web mercator x, y to longitude and latitude

    Parameters
    ----------
    x, y : float
        web mercator coordinates in meters.
    truncate : bool, optional
        Whether to truncate or clip inputs to web mercator limits.

    Returns
    -------
    LngLat

    """
    pass


def neighbors(*tile, **kwargs):
    """The neighbors of a tile

    The neighbors function makes no guarantees regarding neighbor tile
    ordering.

    The neighbors function returns up to eight neighboring tiles, where
    tiles will be omitted when they are not valid e.g. Tile(-1, -1, z).

    Parameters
    ----------
    tile : Tile or sequence of int
        May be be either an instance of Tile or 3 ints, X, Y, Z.

    Returns
    -------
    list

    Examples
    --------
    >>> neighbors(Tile(486, 332, 10))
    [Tile(x=485, y=331, z=10), Tile(x=485, y=332, z=10), Tile(x=485, y=333, z=10), Tile(x=486, y=331, z=10), Tile(x=486, y=333, z=10), Tile(x=487, y=331, z=10), Tile(x=487, y=332, z=10), Tile(x=487, y=333, z=10)]

    """
    def valid(tile):
        pass

    pass


def xy_bounds(*tile):
    """Get the web mercator bounding box of a tile

    Parameters
    ----------
    tile : Tile or sequence of int
        May be be either an instance of Tile or 3 ints, X, Y, Z.

    Returns
    -------
    Bbox

    Notes
    -----
    Epsilon is subtracted from the right limit and added to the bottom
    limit.

    """
    pass


def _xy(lng, lat, truncate=False):

    pass


def tile(lng, lat, zoom, truncate=False):
    """Get the tile containing a longitude and latitude

    Parameters
    ----------
    lng, lat : float
        A longitude and latitude pair in decimal degrees.
    zoom : int
        The web mercator zoom level.
    truncate : bool, optional
        Whether or not to truncate inputs to limits of web mercator.

    Returns
    -------
    Tile

    """
    pass


def quadkey(*tile):
    """Get the quadkey of a tile

    Parameters
    ----------
    tile : Tile or sequence of int
        May be be either an instance of Tile or 3 ints, X, Y, Z.

    Returns
    -------
    str

    """
    pass


def quadkey_to_tile(qk):
    """Get the tile corresponding to a quadkey

    Parameters
    ----------
    qk : str
        A quadkey string.

    Returns
    -------
    Tile

    """
    pass


def tiles(west, south, east, north, zooms, truncate=False):
    """Get the tiles overlapped by a geographic bounding box

    Parameters
    ----------
    west, south, east, north : sequence of float
        Bounding values in decimal degrees.
    zooms : int or sequence of int
        One or more zoom levels.
    truncate : bool, optional
        Whether or not to truncate inputs to web mercator limits.

    Yields
    ------
    Tile

    Notes
    -----
    A small epsilon is used on the south and east parameters so that this
    function yields exactly one tile when given the bounds of that same tile.

    """
    pass


def parent(*tile, **kwargs):
    """Get the parent of a tile

    The parent is the tile of one zoom level lower that contains the
    given "child" tile.

    Parameters
    ----------
    tile : Tile or sequence of int
        May be be either an instance of Tile or 3 ints, X, Y, Z.
    zoom : int, optional
        Determines the *zoom* level of the returned parent tile.
        This defaults to one lower than the tile (the immediate parent).

    Returns
    -------
    Tile

    Examples
    --------
    >>> parent(Tile(0, 0, 2))
    Tile(x=0, y=0, z=1)
    >>> parent(Tile(0, 0, 2), zoom=0)
    Tile(x=0, y=0, z=0)

    """
    pass


def children(*tile, **kwargs):
    """Get the children of a tile

    The children are ordered: top-left, top-right, bottom-right, bottom-left.

    Parameters
    ----------
    tile : Tile or sequence of int
        May be be either an instance of Tile or 3 ints, X, Y, Z.
    zoom : int, optional
        Returns all children at zoom *zoom*, in depth-first clockwise
        winding order.  If unspecified, returns the immediate (i.e. zoom
        + 1) children of the tile.

    Returns
    -------
    list

    Raises
    ------
    InvalidZoomError
        If the zoom level is not an integer greater than the zoom level
        of the input tile.

    Examples
    --------
    >>> children(Tile(0, 0, 0))
    [Tile(x=0, y=0, z=1), Tile(x=0, y=1, z=1), Tile(x=1, y=0, z=1), Tile(x=1, y=1, z=1)]
    >>> children(Tile(0, 0, 0), zoom=2)
    [Tile(x=0, y=0, z=2), Tile(x=0, y=1, z=2), Tile(x=0, y=2, z=2), Tile(x=0, y=3, z=2), ...]

    """
    pass


def simplify(tiles):
    """Reduces the size of the tileset as much as possible by merging leaves into parents.

    Parameters
    ----------
    tiles : Sequence of tiles to merge.

    Returns
    -------
    list

    """
    def merge(merge_set):
        pass

    pass


def rshift(val, n):
    pass


def bounding_tile(*bbox, **kwds):
    """Get the smallest tile containing a geographic bounding box

    NB: when the bbox spans lines of lng 0 or lat 0, the bounding tile
    will be Tile(x=0, y=0, z=0).

    Parameters
    ----------
    bbox : sequence of float
        west, south, east, north bounding values in decimal degrees.

    Returns
    -------
    Tile

    """
    pass


def _getBboxZoom(*bbox):
    pass


def feature(
    tile, fid=None, props=None, projected="geographic", buffer=None, precision=None
):
    """Get the GeoJSON feature corresponding to a tile

    Parameters
    ----------
    tile : Tile or sequence of int
        May be be either an instance of Tile or 3 ints, X, Y, Z.
    fid : str, optional
        A feature id.
    props : dict, optional
        Optional extra feature properties.
    projected : str, optional
        Non-standard web mercator GeoJSON can be created by passing
        'mercator'.
    buffer : float, optional
        Optional buffer distance for the GeoJSON polygon.
    precision : int, optional
        GeoJSON coordinates will be truncated to this number of decimal
        places.

    Returns
    -------
    dict

    """
    pass


def _coords(obj):
    """All coordinate tuples from a geometry or feature or collection

    Yields
    ------
    lng : float
        Longitude
    lat : float
        Latitude

    """
    pass


def geojson_bounds(obj):
    """Returns the bounding box of a GeoJSON object

    Parameters
    ----------
    obj : mapping
        A GeoJSON geometry, feature, or feature collection.

    Returns
    -------
    LngLatBbox

    """
    def func(bbox, coords):
        pass

    pass


@lru_cache(maxsize=28)
def minmax(zoom):
    """Minimum and maximum tile coordinates for a zoom level

    Parameters
    ----------
    zoom : int
        The web mercator zoom level.

    Returns
    -------
    minimum : int
        Minimum tile coordinate (note: always 0).
    maximum : int
        Maximum tile coordinate (2 ** zoom - 1).

    Raises
    ------
    InvalidZoomError
        If zoom level is not a positive integer.

    Examples
    --------
    >>> minmax(1)
    (0, 1)
    >>> minmax(-1)
    Traceback (most recent call last):
    ...
    InvalidZoomError: zoom must be a positive integer

    """
    pass
