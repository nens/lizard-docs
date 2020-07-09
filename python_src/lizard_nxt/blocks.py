# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans, see LICENSE.rst.


class LizardRasterSource:
    """A RasterBlock that interfaces a Lizard RasterSource model instance

    :param uuid: the UUID of the RasterSource object
    :type uuid: string
    """
    pass


class LizardRasterGroup:
    """A raster source that groups Lizard RasterLayers

    Args:
      *args (uuid): uuids of RasterLayers to group

    Values in the contributing rasters are stacked left to right. Therefore
    values from rasters that are more 'to the left' are shadowed by values
    from rasters more 'to the right'. However, 'no data' values are
    transparent and do not shadow underlying data values.

    The temporal behavior of this block is different than the Group
    geoblock:

    - if a single time instance is requested, all frames nearest to the
      requested time are grouped into one raster
    - if no time is requested, all most recent frames are grouped into
      one raster
    - if a time period is requested a NotImplementedError is raised

    This block also returns a raster containing the primary keys of the
    data origins. Use LizardRasterId to use that data.
    """
    pass


class LizardRasterId:
    """This geoblock should be combined with LizardRasterGroup to obtain the
    id (primary key) of the RasterStore from which the data is coming.

    :param source: grouped Lizard rasters to obtain origins from
    :type source: GroupLizardRaster
    """
    pass
