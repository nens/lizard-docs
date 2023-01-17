
=========
Datatypes
=========

Lizard can store & accelerate three types of data: vectors, rasters and time series.
These data types are a digital representation of the physical environment.
We also distinguish wms layers, scenarios and labels.

Rasters
=======

Introduction
------------

Rasters in Lizard represent continuous information about the physical environment across an area.
Rasters can be static or temporal. Examples of static data are digital elevation models and land cover maps.
Temporal raster datasets, or raster series, consist of a series of rasters for a certain time interval.
Examples of temporal raster datasets are radar measurements of precipitation, air quality or hydrodynamic model results such as flood depths. 

.. _why_rasterstores:

Why Rasterstores
-----------------

The rasterstore is a library designed for quick data retrieval. Rasters provide a simple structure for data analyis.

Main functionalities:

* Retrieve values for a specific location or area
* Analyse data for a particular period or moment in time
* Map visualisation in the lizard Viewer
* Exporting to a geotiff file
* Connecting with external applications via WMS
* Base block for on-the-fly map calculations and conversions
* API interactions: list, create, (partial) update, retrieve and delete

Raster data
------------

A rasters is a grid of cells organized into rows and columns. Each cell contains a value that represents real-world phenomena, such as water depth. The values can be continuous (e.g. 28.5 degrees) or integer numbers. Integer numbers can represent classes (e.g. 1: Water, 2: Land).

Rasterstore data can be static or temporal. Examples of static data are a digital elevation model and a land cover map. Temporal rasterstores consist of multiple timesteps. The data can be stored in time using an origin (e.g. 2019-01-01) and an interval (e.g. every day). Examples are weather predictions and timeseries of 3Di model results.

Requirements 
--------------

Your raster data has to be in the format of a single band, georeferenced TIFF (geotiff), with the following requirements: 

* **Geotiff should have valid projection** including transformation (EPSG code). All projections supported by proj4 are supported.
* **Geotiff should have a NODATA value**.
* **Geotiff should be single band**. RGB or multi-band is not supported. 
* **Temporal raster datasets** with multiple timesteps **should be supplied with a single geotiff per timestamp**

Raster metadata
----------------

Characteristics of rasters are stored in the attributes of a rasterstore. The attributes are used to indicate the function, purpose and meaning of data. The main attributes are listed below.

* Organisation
* Name
* Description
* Aggregation type
* Observation type
* Colormap
* Supplier name
* Supplier code
* Temporal behaviour

.. _vector_data_types:

Vectors
=======

Vectors in Lizard represent physical or abstract objects in time and space.
Lizard offers an extensive library of vector data models that can be used to represent objects (physical or abstract) in the physical environment. 
Per data model, there are columns defined with certain data_types.
Some are obligatory, such as the id, some are optional. Below you find the available columns per data model. 

.. csv-table:: "administrative boundaries": "https://demo.lizard.net/api/v4/boundaries/"
    :header: column_name, data_type	
	
	id,	integer
	code,	character varying
	type,	smallint
	name,	character varying
	created,	timestamp with time zone
	geometry,	USER-DEFINED
	last_modified,	timestamp with time zone

.. csv-table:: "bridges": "https://demo.lizard.net/api/v4/bridges/"
    :header: column_name, data_type

    id, integer
    organisation_id, integer
    created, timestamp with time zone
    code, character varying
    name, character varying
    type, character varying
    width, double precision
    length, double precision
    height, double precision
    image_url, character varying
    geometry, USER-DEFINED
    end, timestamp with time zone
    start, timestamp with time zone
    last_modified, timestamp with time zone

.. csv-table:: "buildings": "https://demo.lizard.net/api/v4/buildings/"
    :header: column_name, data_type

    id,	integer
	created,	timestamp with time zone
	start,	timestamp with time zone
	end,	timestamp with time zone
	image_url,	character varying
	code,	character varying
	build_year,	integer
	geometry,	USER-DEFINED
	organisation_id,	integer
	last_modified,	timestamp with time zone

.. csv-table:: "culverts": "https://demo.lizard.net/api/v4/culverts/"
    :header: column_name, data_type
    
    id, integer
    organisation_id, integer
    created, timestamp with time zone
    code, character varying
    type, character varying
    bed_level_upstream, double precision
    bed_level_downstream, double precision
    width, double precision
    length, double precision
    allowed_flow_direction, integer
    height, double precision
    material, integer
    shape, integer
    description, text
    image_url, character varying
    geometry, USER-DEFINED
    end, timestamp with time zone
    start, timestamp with time zone
    num_timeseries, integer
    last_modified, timestamp with time zone

.. csv-table:: "filters": "https://demo.lizard.net/api/v4/filters/"
    :header: column_name, data_type
    
    id, integer
    created, timestamp with time zone
    filter_top_level, double precision
    filter_bottom_level, double precision
    aquifer_confiment, text
    litology, text
    code, character varying
    groundwater_station_id, integer
    top_level, double precision
    high_groundwater_level, double precision
    low_groundwater_level, double precision
    last_modified, timestamp with time zone

.. csv-table:: "fixeddrainagelevelareas":"https://demo.lizard.net/api/v4/fixeddrainagelevelareas/"    
    :header: column_name, data_type

    id, integer
    organisation_id, integer
    created, timestamp with time zone
    code, character varying
    name, character varying
    type, integer
    water_level_summer, double precision
    water_level_winter, double precision
    water_level_fixed, double precision
    image_url, character varying
    geometry, USER-DEFINED
    end, timestamp with time zone
    start, timestamp with time zone
    num_timeseries, integer
    last_modified, timestamp with time zone

.. csv-table:: "groundwaterstations": "https://demo.lizard.net/api/v4/groundwaterstations/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	image_url,	character varying
	code,	character varying
	name,	character varying
	surface_level,	double precision
	top_level,	double precision
	bottom_level,	double precision
	station_type,	integer
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	scale,	integer
	status,	integer
	last_modified,	timestamp with time zone

.. csv-table:: "leveecrosssections": "https://demo.lizard.net/api/v4/leveecrosssections/",
    :header: column_name, data_type

	id,	integer
	created,	timestamp with time zone
	start,	timestamp with time zone
	end,	timestamp with time zone
	image_url,	character varying
	code,	character varying
	name,	character varying
	distance_to_reference,	integer
	geometry,	USER-DEFINED
	levee_id,	integer
	organisation_id,	integer
	last_modified,	timestamp with time zone

.. csv-table:: "levees": "https://demo.lizard.net/api/v4/levees/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	recurrence_time,	integer
	material,	character varying
	coating,	character varying
	crest_height,	double precision
	image_url,	character varying
	name,	character varying
	category,	integer
	levee_ring_id,	integer
	levee_type,	integer
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	last_modified,	timestamp with time zone
    
.. csv-table:: "locations": "https://demo.lizard.net/api/v4/locations/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	code,	character varying
	name,	character varying
	object_type_id,	integer
	object_id,	integer
	created,	timestamp with time zone
	access_modifier,	integer
	last_modified,	timestamp with time zone
	last_modified_by,	character varying
	extra_metadata,	text
	ddsc_icon_url,	character varying
	ddsc_show_on_map,	boolean
	geometry,	USER-DEFINED
	uuid,	uuid
	node_id,	integer
	supplier_id,	integer

.. csv-table:: "manholes": "https://demo.lizard.net/api/v4/manholes/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	surface_level,	double precision
	drainage_area,	integer
	material,	character varying
	width,	double precision
	length,	double precision
	shape,	character varying
	bottom_level,	double precision
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	water_consumption,	double precision
	last_modified,	timestamp with time zone
    
.. csv-table:: "measuringstations": "https://demo.lizard.net/api/v4/measuringstations/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	name,	character varying
	region,	character varying
	station_type,	integer
	category,	character varying
	frequency,	character varying
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	last_modified,	timestamp with time zone

.. csv-table:: "monitoringwells": "https://demo.lizard.net/api/v4/monitoringwells/",
    :header: column_name, data_type

	id,	integer
	created,	timestamp with time zone
	start,	timestamp with time zone
	end,	timestamp with time zone
	image_url,	character varying
	code,	character varying
	num_timeseries,	integer
	well_top_level,	double precision
	well_bottom_level,	double precision
	geometry,	USER-DEFINED
	levee_crosssection_id,	integer
	organisation_id,	integer
	last_modified,	timestamp with time zone

.. csv-table:: "orifices": "https://demo.lizard.net/api/v4/orifices/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	start_point_id,	integer
	end_point_id,	integer
	connection_serial,	integer
	crest_width,	double precision
	crest_level,	double precision
	shape,	character varying
	initial_opening_height,	double precision
	code,	character varying
	name,	character varying
	flow_type,	integer
	angle,	double precision
	contraction_coeff,	double precision
	lat_contr_coeff,	double precision
	negative_flow_limit,	double precision
	positive_flow_limit,	double precision
	allowed_flow_direction,	integer
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone

.. csv-table:: "outlets": "https://demo.lizard.net/api/v4/outlets/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	manhole_id,	integer
	connection_serial,	integer
	open_water_level_average,	double precision
	open_water_level_summer,	double precision
	open_water_level_winter,	double precision
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone
    
.. csv-table:: "overflows": "https://demo.lizard.net/api/v4/overflows/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	start_point_id,	integer
	end_point_id,	integer
	connection_serial,	integer
	crest_width,	double precision
	crest_level,	double precision
	open_water_level_average,	double precision
	open_water_level_summer,	double precision
	open_water_level_winter,	double precision
	angle,	double precision
	allowed_flow_direction,	integer
	image_url,	character varying
	code,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	sensor_level,	double precision
	surface_level,	double precision
	name,	character varying
	last_modified,	timestamp with time zone
    
.. csv-table:: "parcels": "https://demo.lizard.net/api/v4/parcels/",
    :header: column_name, data_type

	id,	integer
	created,	timestamp with time zone
	start,	timestamp with time zone
	end,	timestamp with time zone
	image_url,	character varying
	code,	character varying
	name,	character varying
	external_id,	character varying
	geometry,	USER-DEFINED
	organisation_id,	integer
	num_timeseries,	integer
	last_modified,	timestamp with time zone

.. csv-table:: "pipes": "https://demo.lizard.net/api/v4/pipes/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	start_point_id,	integer
	end_point_id,	integer
	connection_serial,	integer
	invert_level_start_point,	double precision
	invert_level_end_point,	double precision
	length,	double precision
	type,	character varying
	material,	character varying
	width,	double precision
	height,	double precision
	shape,	character varying
	number_of_inhabitants,	integer
	dwa_definition,	character varying
	impervious_surfaces,	text
	allowed_flow_direction,	integer
	image_url,	character varying
	code,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone

.. csv-table:: "polders": "https://demo.lizard.net/api/v4/polders/",
    :header: column_name, data_type

	id,	integer
	created,	timestamp with time zone
	image_url,	character varying
	code,	character varying
	name,	character varying
	organisation_id,	integer
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone

.. csv-table:: "pressurepipes": "https://demo.lizard.net/api/v4/pressurepipes/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	length,	double precision
	material,	character varying
	diameter,	double precision
	shape,	character varying
	year_of_construction,	integer
	image_url,	character varying
	type,	integer
	name,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone

.. csv-table:: "pumpeddrainageareas": "https://demo.lizard.net/api/v4/pumpeddrainageareas/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	name,	character varying
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	connected_impervious_surface,	double precision
	downstream_pumped_drainage_area_id,	integer
	extraneous_water,	double precision
	inhabitants,	integer
	minimum_overflow_crest_level,	double precision
	pollution_equivalent,	double precision
	population_equivalent,	double precision
	pump_station_id,	integer
	sanitary_load,	double precision
	sewer_system,	integer
	upstream_load,	double precision
	water_consumption,	double precision
	water_retention_capacity,	double precision
	area_type,	integer
	connected_impervious_surface_mixed,	double precision
	connected_impervious_surface_rainwater,	double precision
	num_timeseries,	integer
	pump_overcapacity,	double precision
	last_modified,	timestamp with time zone

.. csv-table:: "pumps": "https://demo.lizard.net/api/v4/pumps/",
    :header: column_name, data_type

	id,	integer
	pump_station_id,	integer
	code,	character varying
	serial,	integer
	capacity,	double precision
	start_level,	double precision
	stop_level,	double precision
	name,	character varying
	type,	character varying
	reduction_factor_no_levels,	double precision
	reduction_factor,	double precision
	characteristics,	character varying
	allowed_flow_direction,	integer
	start_level_delivery_side,	double precision
	stop_level_delivery_side,	double precision
	created,	timestamp with time zone
	last_modified,	timestamp with time zone
    
.. csv-table:: "pumpstations": "https://demo.lizard.net/api/v4/pumpstations/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	type,	character varying
	start_point_id,	integer
	end_point_id,	integer
	connection_serial,	integer
	capacity,	double precision
	start_level,	double precision
	stop_level,	double precision
	name,	character varying
	allowed_flow_direction,	integer
	start_level_delivery_side,	double precision
	stop_level_delivery_side,	double precision
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	last_modified,	timestamp with time zone
    
.. csv-table:: "roads": "https://demo.lizard.net/api/v4/roads/",
    :header: column_name, data_type
    
	id,	integer
	created,	timestamp with time zone
	name,	character varying
	type,	integer
	use,	integer
	geometry,	USER-DEFINED
	code,	character varying
	end,	timestamp with time zone
	image_url,	character varying
	organisation_id,	integer
	start,	timestamp with time zone
	region_id,	integer
	last_modified,	timestamp with time zone

.. csv-table:: "sluices": "https://demo.lizard.net/api/v4/sluices/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	name,	character varying
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	last_modified,	timestamp with time zone
    
.. csv-table:: "wastewatertreatmentplants": "https://demo.lizard.net/api/v4/wastewatertreatmentplants/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	name,	character varying
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	last_modified,	timestamp with time zone

.. csv-table:: "weirs": "https://demo.lizard.net/api/v4/weirs/",
    :header: column_name, data_type

    id	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	crest_type,	smallint
	crest_width,	double precision
	crest_level,	double precision
	name,	character varying
	lat_dis_coeff,	double precision
	angle,	double precision
	allowed_flow_direction,	integer
	controlled,	integer
	comment,	text
	discharge_coeff,	double precision
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	type,	smallint
	last_modified,	timestamp with time zone

Time Series
===========

Time series in Lizard represent in situ measurements and hindcasts/forecasts of processes in the physical environment.

A time series object is always related to a location object, which is in turn optionally linked to an asset.
By clicking an asset in the Lizard Viewer a list of related time series objects is fetched which can be visualised.

The storage of time series data and the presentation in the API are focussed on high performance and retrieving relevant information out of it.
There are multiple options for making aggregations and deriving statistics.

Value Types
-----------

Lizard time series can have different value types. The following value types are supported:

Numerical|Integer and float
Alphanumerical|Text
Images|PNG and JPG
Files|E.g. PDF

Series of numerical values and images can be visualised in the Lizard Viewer. Text values and Files can only be retrieved or downloaded from the API.

Aggregation options
-------------------

Time series can consist of many data points, making it difficult to handle when interested in longer periods of time.
The Lizard API has several options to aggregate the bulk data to make it manageable for presentation in clients or for analysis purposes.

In the API there are two parameters that can be used for aggregating time series.
First there is the window parameter to determine what is the interval of the retrieved (aggregated) data.
Options are:

- raw
- 5min
- hour
- day
- week
- month
- year

Field parameters
----------------

The timeseries events sub-endpoint returns the raw values. It is also possible to retrieve aggregated values, in the aggregates sub-endpoint.
With the fields parameter many statistics can be retrieved. Multiple fields can be requested in one call.

Options are:

- min
- min_timestamp
- max
- max_timestamp
- avg
- count
- first
- first_timestamp
- last
- last_timestamp
- nans
- sum

For more options in requesting time series see the API endpoint: https://demo.lizard.net/api/v4/timeseries/{timeseries_uuid}/aggregates/

Labels
======

Labels consist of three elements that are available through our API: LabelTypes, Labels and LabelParameters.
Labels are always linked to an organisation.
Each element is explained below.

LabelTypes
-----------

LabelTypes can be found on the LabelType-endpoint `<demo.lizard.net/api/v4/labeltypes>`_ and describe the type of Label.
LabelTypes contain the following fields:

* name: name of the LabelType
* description: description of the LabelType
* uuid: unique ID for the LabelType
* organisation: organisation that owns the LabelType
* created: date when LabelType was created
* object_type: the type of Asset related to the LabelType
* last_modified: date when LabelType was last updated
* source: source of the LabelType e.g. a GeoBlock

Labels
--------

The Labels related to a specific LabelType can be found on the Labels-endpoint `<demo.lizard.net/api/v4/labeltypes/{labeltype_uuid}/labels>`_.
Labels contain the follow fields:

* label_value: the index value of the Label
* object_type: the type of Asset related to the Label
* object_id: id of the Asset
* created: date when the label was created
* start: start of the validity of the Label (history of the Label)
* end: end of the validity of the Label (history of the Label)
* extra: this field can be used to show variables related to the definition of the Label (for instance a threshold value related to the Label)

LabelParameters
-----------------

The Label parameters is developed to store parameters that are used in the computation of the Label.
LabelParameters are linked to LabelTypes and Assets and can be found on the LabelParameters-endpoint `<demo.lizard.net/api/v4/labeltypes/{labeltype_uuid}/labelparameters>`_.
LabelParameters contain the following fields:

* label_type: the related LabelType
* value: value of the parameters
* name: name of the parameter
* object_type: the type of Asset related to the LabelParameter
* object_id: the ID of the Asset related to the LabelParameter
* created: date when LabelParameter was created
* start: start of the validity of the LabelParameter (history of the LabelParameter)
* end: end of the validity of the LabelParameter (history of the LabelParameter)

Label statistics
------------------

With the count filter on the Labels endpoint it is possible to query a histogram of all Labels of a certain LabelType or a histogram of Labels within a region (e.g. municipality).