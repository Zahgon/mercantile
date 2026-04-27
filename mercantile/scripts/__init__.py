"""Mercantile command line interface
"""

import json
import logging
import sys

import click

import mercantile


def configure_logging(verbosity):
    """Configure logging level

    Parameters
    ----------
    verbosity : int
        The number of `-v` options from the command line.

    Returns
    -------
    None
    """
    pass


logger = logging.getLogger(__name__)

RS = u"\x1e"


def normalize_input(input):
    """Normalize file or string input."""
    pass


def iter_lines(lines):
    """Iterate over lines of input, stripping and skipping."""
    pass


# The CLI command group.
@click.group(help="Command line interface for the Mercantile Python package.")
@click.option("--verbose", "-v", count=True, help="Increase verbosity.")
@click.option("--quiet", "-q", count=True, help="Decrease verbosity.")
@click.version_option(version=mercantile.__version__, message="%(version)s")
@click.pass_context
def cli(ctx, verbose, quiet):
    """Execute the main mercantile command"""
    pass


# Commands are below.

# The shapes command.
@cli.command(short_help="Print the shapes of tiles as GeoJSON.")
# This input is either a filename, stdin, or a string.
@click.argument("input", default="-", required=False)
# Coordinate precision option.
@click.option(
    "--precision", type=int, default=None, help="Decimal precision of coordinates."
)
# JSON formatting options.
@click.option(
    "--indent", default=None, type=int, help="Indentation level for JSON output"
)
@click.option(
    "--compact/--no-compact", default=False, help="Use compact separators (',', ':')."
)
# Geographic (default) or Mercator switch.
@click.option(
    "--geographic",
    "projected",
    flag_value="geographic",
    default=True,
    help="Output in geographic coordinates (the default).",
)
@click.option(
    "--mercator",
    "projected",
    flag_value="mercator",
    help="Output in Web Mercator coordinates.",
)
@click.option(
    "--seq",
    is_flag=True,
    default=False,
    help="Write a RS-delimited JSON sequence (default is LF).",
)
# GeoJSON feature (default) or collection switch. Meaningful only
# when --x-json-seq is used.
@click.option(
    "--feature",
    "output_mode",
    flag_value="feature",
    default=True,
    help="Output as sequence of GeoJSON features (the default).",
)
@click.option(
    "--bbox",
    "output_mode",
    flag_value="bbox",
    help="Output as sequence of GeoJSON bbox arrays.",
)
@click.option(
    "--collect",
    is_flag=True,
    default=False,
    help="Output as a GeoJSON feature collections.",
)
# Optionally write out bboxen in a form that goes
# straight into GDAL utilities like gdalwarp.
@click.option(
    "--extents/--no-extents",
    default=False,
    help="Write shape extents as ws-separated strings (default is " "False).",
)
# Optionally buffer the shapes by shifting the x and y values of each
# vertex by a constant number of decimal degrees or meters (depending
# on whether --geographic or --mercator is in effect).
@click.option(
    "--buffer",
    type=float,
    default=None,
    help="Shift shape x and y values by a constant number",
)
@click.pass_context
def shapes(
    ctx,
    input,
    precision,
    indent,
    compact,
    projected,
    seq,
    output_mode,
    collect,
    extents,
    buffer,
):

    """Print tiles as GeoJSON feature collections or sequences.

    Input may be a compact newline-delimited sequences of JSON or
    a pretty-printed ASCII RS-delimited sequence of JSON (like
    https://tools.ietf.org/html/rfc8142 and
    https://tools.ietf.org/html/rfc7159).

    Tile descriptions may be either an [x, y, z] array or a JSON
    object of the form

      {"tile": [x, y, z], "properties": {"name": "foo", ...}}

    In the latter case, the properties object will be used to update
    the properties object of the output feature.

	Example:

	\b
	echo "[486, 332, 10]" | mercantile shapes --precision 4 --bbox
	[-9.1406, 53.1204, -8.7891, 53.3309]

    """
    pass


# The tiles command.
@cli.command(
    short_help="Print tiles that overlap or contain a lng/lat point, "
    "bounding box, or GeoJSON objects."
)
# Mandatory Mercator zoom level argument.
@click.argument("zoom", type=int, default=-1)
# This input is either a filename, stdin, or a string.
# Has to follow the zoom arg.
@click.argument("input", default="-", required=False)
@click.option(
    "--seq/--lf",
    default=False,
    help="Write a RS-delimited JSON sequence (default is LF).",
)
@click.pass_context
def tiles(ctx, zoom, input, seq):
    """Lists Web Mercator tiles at ZOOM level intersecting
    GeoJSON [west, south, east, north] bounding boxen, features, or
    collections read from stdin. Output is a JSON
    [x, y, z] array.

    Input may be a compact newline-delimited sequences of JSON or
    a pretty-printed ASCII RS-delimited sequence of JSON (like
    https://tools.ietf.org/html/rfc8142 and
    https://tools.ietf.org/html/rfc7159).

    Example:

    \b
    $ echo "[-105.05, 39.95, -105, 40]" | mercantile tiles 12
    [852, 1550, 12]
    [852, 1551, 12]
    [853, 1550, 12]
    [853, 1551, 12]

    """
    def feature_gen():
        pass

    def feature_gen():
        pass

    pass


# The bounding-tile command.
@cli.command(
    "bounding-tile",
    short_help="Print the bounding tile of a lng/lat point, "
    "bounding box, or GeoJSON objects.",
)
# This input is either a filename, stdin, or a string.
@click.argument("input", default="-", required=False)
@click.option(
    "--seq/--lf",
    default=False,
    help="Write a RS-delimited JSON sequence (default is LF).",
)
@click.pass_context
def bounding_tile(ctx, input, seq):
    """Print the Web Mercator tile at ZOOM level bounding
    GeoJSON [west, south, east, north] bounding boxes, features, or
    collections read from stdin.

    Input may be a compact newline-delimited sequences of JSON or
    a pretty-printed ASCII RS-delimited sequence of JSON (like
    https://tools.ietf.org/html/rfc8142 and
    https://tools.ietf.org/html/rfc7159).

    Example:

    \b
    echo "[-105.05, 39.95, -105, 40]" | mercantile bounding-tile
    [426, 775, 11]

    """
    def feature_gen():
        pass

    def feature_gen():
        pass

    pass


# The children command.
@cli.command(short_help="Print the children of the tile.")
@click.argument("input", default="-", required=False)
@click.option(
    "--depth",
    type=int,
    default=1,
    help="Number of zoom levels to traverse (default is 1).",
)
@click.pass_context
def children(ctx, input, depth):
    """Takes [x, y, z] tiles as input and writes children to stdout
    in the same form.

    Input may be a compact newline-delimited sequences of JSON or
    a pretty-printed ASCII RS-delimited sequence of JSON (like
    https://tools.ietf.org/html/rfc8142 and
    https://tools.ietf.org/html/rfc7159).

    Example:

    \b
    echo "[486, 332, 10]" | mercantile children
    [972, 664, 11]
    [973, 664, 11]
    [973, 665, 11]
    [972, 665, 11]

    """
    pass


# The parent command.
@cli.command(short_help="Print the parent tile.")
@click.argument("input", default="-", required=False)
@click.option(
    "--depth",
    type=int,
    default=1,
    help="Number of zoom levels to traverse (default is 1).",
)
@click.pass_context
def parent(ctx, input, depth):
    """Takes [x, y, z] tiles as input and writes parents to stdout
    in the same form.

    Input may be a compact newline-delimited sequences of JSON or
    a pretty-printed ASCII RS-delimited sequence of JSON (like
    https://tools.ietf.org/html/rfc8142 and
    https://tools.ietf.org/html/rfc7159).

    Example:

    \b
    echo "[486, 332, 10]" | mercantile parent
    [243, 166, 9]

    """
    pass


# The neighbors command.
@cli.command(short_help="Print the neighbors of the tile.")
@click.argument("input", default="-", required=False)
@click.pass_context
def neighbors(ctx, input):
    """Takes [x, y, z] tiles as input and writes adjacent
    tiles on the same zoom level to stdout in the same form.

    There are no ordering guarantees for the output tiles.

    Input may be a compact newline-delimited sequences of JSON or
    a pretty-printed ASCII RS-delimited sequence of JSON (like
    https://tools.ietf.org/html/rfc8142 and
    https://tools.ietf.org/html/rfc7159).

    Example:

    \b
    echo "[486, 332, 10]" | mercantile neighbors
    [485, 331, 10]
    [485, 332, 10]
    [485, 333, 10]
    [486, 331, 10]
    [486, 333, 10]
    [487, 331, 10]
    [487, 332, 10]
    [487, 333, 10]

    """
    pass


@cli.command(short_help="Convert to/from quadkeys.")
@click.argument("input", default="-", required=False)
@click.pass_context
def quadkey(ctx, input):
    """Takes [x, y, z] tiles or quadkeys as input and writes
    quadkeys or a [x, y, z] tiles to stdout, respectively.

    Input may be a compact newline-delimited sequences of JSON or
    a pretty-printed ASCII RS-delimited sequence of JSON (like
    https://tools.ietf.org/html/rfc8142 and
    https://tools.ietf.org/html/rfc7159).

    Examples:

    \b
    echo "[486, 332, 10]" | mercantile quadkey
    0313102310

    \b
    echo "0313102310" | mercantile quadkey
    [486, 332, 10]

    """
    pass
