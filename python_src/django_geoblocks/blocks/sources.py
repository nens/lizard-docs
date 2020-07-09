# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
"""
Module containing geometry sources.
"""

class GeoDjangoSource:
    """Query a geodjango model.

    :param app_label: The django app label
    :param model_name: Name of the django model
    :param fields: a mapping ``{<model field name>: <column name>, ...}``
    :param geometry_field_name: geometry field name. Default `'geometry'``.
    :param start_field_name: field name to use as start. Default None.
    :param end_field_name: field name to use as end. Default None.
    :param filters: filters to apply to the model to select the records to add,
      of the form: ``{<field lookup>: <value>, ...}``

    :type app_label: string
    :type model_name: string
    :type fields: dict
    :type geometry_field_name: string
    :type start_field_name: string
    :type end_field_name: string
    :type filters: dict

    If ``fields`` is empty, only the geometry field is added by default. If
    ``start_field_name`` and ``end_field_name`` are not given, this source will
    not use a temporal filters.
    """
    pass


class AddDjangoFields:
    """ Add a column to a GeometryBlock with data from a django model.

    :param source: the data source to add extra properties to
    :param app_label: the django app label
    :param model_name: the name of the django model
    :param filters: filters to apply to the model to select the records to add,
      of the form: ``{<field lookup>: <value>, ...}``
    :param lookup: a single mapping to match the data from the source to the
      data being added: ``{<field name>: <column name>}``
    :param fields: determines what fields will be added and how these will be
      named: ``{<field name>: <column name>, ...}``
    :param start_field_name: field name to use as start
    :param end_field_name: field name to use as end

    :type source: GeometryBlock
    :type app_label: string
    :type model_name: string
    :type filters: dict
    :type lookup: dict
    :type fields: dict
    :type start_field_name: string
    :type end_field_name: string

    The filters and lookup should be such that every existing geometry is
    matched to exactly one django model instance. If this is not the case,
    an arbitrary record will be taken.

    If ``start_field_name`` and ``end_field_name`` are not given, this source
    will not use a temporal filters.
    """
    pass
