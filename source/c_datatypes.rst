=========
Datatypes
=========

Lizard can store & accelerate three types of data: vectors, rasters and time series.
These data types are a digital representation of the physical environment.

.. _vector_data_types:

Vectors
=======

Vectors in Lizard represent physical or abstract objects in time and space.
Lizard offers an extensive library of vector data models that can be used to represent objects (physical or abstract) in the physical environment. 
Per data model, there are columns defined with certain data_types.
Some are obligatory, such as the id, some are optional. Below you find the available columns per data model. 

.. csv-table:: "administrative boundaries": "https://demo.lizard.net/api/v3/bridges/"
    :header: column_name, data_type	
	
	id,	integer
	code,	character varying
	type,	smallint
	name,	character varying
	created,	timestamp with time zone
	geometry,	USER-DEFINED
	last_modified,	timestamp with time zone

.. csv-table:: "bridges": "https://demo.lizard.net/api/v3/bridges/"
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

.. csv-table:: "buildings": "https://demo.lizard.net/api/v3/buildings/"
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

.. csv-table:: "channels": "https://demo.lizard.net/api/v3/channel/"
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	type,	character varying
	bed_level,	double precision
	comment,	text
	name,	character varying
	talud_left,	double precision
	talud_right,	double precision
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone
	
.. csv-table:: "channelsurface": "https://demo.lizard.net/api/v3/channelsurface/"
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	image_url,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone

.. csv-table:: "crosspofile": "https://demo.lizard.net/api/v3/crossprofile/"
    :header: column_name, data_type

	id,	integer
	type,	integer
	tables,	character varying
	created,	timestamp with time zone
	last_modified,	timestamp with time zone

.. csv-table:: "crosssection": "https://demo.lizard.net/api/v3/crosssection"
    :header: column_name, data_type

	id,	integer
	cross_profile_id,	integer
	channel_id,	integer
	friction_type,	integer
	friction_value,	integer
	distance_on_channel,	numeric
	bed_level,	double precision
	bed_width,	double precision
	width,	double precision
	slope_left,	double precision
	slope_right,	double precision
	reclamation,	double precision
	created,	timestamp with time zone
	geometry,	USER-DEFINED
	last_modified,	timestamp with time zone


.. csv-table:: "culverts": "https://demo.lizard.net/api/v3/culverts/"
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

.. csv-table:: "domains": "https://demo.lizard.net/api/v3/domains/"
    :header: column_name, data_type
    
    id, integer
    created, timestamp with time zone
    name, character varying
    description, character varying
    last_modified, timestamp with time zone

.. csv-table:: "filters": "https://demo.lizard.net/api/v3/filters/"
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

.. csv-table:: "fixeddrainagelevelareas":"https://demo.lizard.net/api/v3/fixeddrainagelevelareas/"    
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

.. csv-table:: "groundwaterstations": "https://demo.lizard.net/api/v3/groundwaterstations/",
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

.. csv-table:: "impervioussurface": "https://demo.lizard.net/api/v3/impervioussurface/",
    :header: column_name, data_type	

	id	integer
	organisation_id	integer
	created	timestamp with time zone
	code	character varying
	surface_class	character varying
	surface_sub_class	character varying
	street_name	character varying
	connection	character varying
	pipe_id	integer
	sewerage_inflow_parameter_id	integer
	inhabitants	double precision
	function	character varying
	dry_water_flow_production	double precision
	surface_inclination	character varying
	image_url	character varying
	geometry	USER-DEFINED
	end	timestamp with time zone
	start	timestamp with time zone
	surface_area	double precision
	last_modified	timestamp with time zone

.. csv-table:: "leveecrosssections": "https://demo.lizard.net/api/v3/leveecrosssections/",
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

.. csv-table:: "leveereferencepoints": "https://demo.lizard.net/api/v3/leveereferencepoints/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	reference_point_type,	integer
	image_url,	character varying
	distance_to_reference,	integer
	geometry,	USER-DEFINED
	end	timestamp, with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone
    
.. csv-table:: "leveerings": "https://demo.lizard.net/api/v3/leveerings/",
    :header: column_name, data_type

	id,	integer
	created,	timestamp with time zone
	image_url,	character varying
	code,	character varying
	organisation_id,	integer
	name,	character varying
	levee_ring_type,	integer
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone

.. csv-table:: "levees": "https://demo.lizard.net/api/v3/levees/",
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
    
.. csv-table:: "leveesections": "https://demo.lizard.net/api/v3/leveesections/",
    :header: column_name, data_type

	id,	integer
	created,	timestamp with time zone
	image_url,	character varying
	code,	character varying
	organisation_id,	integer
	distance_end,	integer
	distance_start,	integer
	levee_id,	integer
	levee_section_type,	integer
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone

.. csv-table:: "leveezones": "https://demo.lizard.net/api/v3/leveezones/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	code,	character varying
	image_url,	character varying
	levee_zone_type,	integer
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	last_modified,	timestamp with time zone

.. csv-table:: "locations": "https://demo.lizard.net/api/v3/locations/",
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

.. csv-table:: "manholes": "https://demo.lizard.net/api/v3/manholes/",
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
    
.. csv-table:: "measuringstations": "https://demo.lizard.net/api/v3/measuringstations/",
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

.. csv-table:: "monitoringwells": "https://demo.lizard.net/api/v3/monitoringwells/",
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

.. csv-table:: "opticalfibers": "https://demo.lizard.net/api/v3/opticalfibers/",
    :header: column_name, data_type

	id,	integer
	organisation_id,	integer
	created,	timestamp with time zone
	image_url,	character varying
	code,	character varying
	length,	double precision
	access_modifier,	integer
	description,	text
	name,	character varying
	geometry,	USER-DEFINED
	end,	timestamp with time zone
	start,	timestamp with time zone
	num_timeseries,	integer
	uuid,	uuid
	supplier_id,	integer
	last_modified,	timestamp with time zone

.. csv-table:: "opticalfiberpart": "https://demo.lizard.net/api/v3/opticalfiberpart/",
    :header: column_name, data_type

	id,	integer
	fiber_id,	integer
	position,	double precision
	length,	double precision
	created,	timestamp with time zone
	index,	integer
	geometry,	USER-DEFINED
	last_modified,	timestamp with time zone
  
.. csv-table:: "orifices": "https://demo.lizard.net/api/v3/orifices/",
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

.. csv-table:: "outlets": "https://demo.lizard.net/api/v3/outlets/",
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
    
.. csv-table:: "overflows": "https://demo.lizard.net/api/v3/overflows/",
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
    
.. csv-table:: "parcels": "https://demo.lizard.net/api/v3/parcels/",
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

.. csv-table:: "pipes": "https://demo.lizard.net/api/v3/pipes/",
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

.. csv-table:: "polders": "https://demo.lizard.net/api/v3/polders/",
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

.. csv-table:: "pressurepipes": "https://demo.lizard.net/api/v3/pressurepipes/",
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

.. csv-table:: "pumpeddrainageareas": "https://demo.lizard.net/api/v3/pumpeddrainageareas/",
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

.. csv-table:: "pumps": "https://demo.lizard.net/api/v3/pumps/",
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
    
.. csv-table:: "pumpstations": "https://demo.lizard.net/api/v3/pumpstations/",
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
    
.. csv-table:: "regions": "https://demo.lizard.net/api/v3/regions/",
    :header: column_name, data_type

    id, integer
    
.. csv-table:: "roads": "https://demo.lizard.net/api/v3/roads/",
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

.. csv-table:: "sluices": "https://demo.lizard.net/api/v3/sluices/",
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
    
.. csv-table:: "wastewatertreatmentplants": "https://demo.lizard.net/api/v3/wastewatertreatmentplants/",
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

.. csv-table:: "weirs": "https://demo.lizard.net/api/v3/weirs/",
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

Time series in Lizard represent in situ measurements and forecasts of processes in the physical environment.
We also support time series with photos (.PNG, .JPG), video’s (.AVI, .WMV) or text files (.PDF, .CSV).

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
* Map visualization in the lizard portal
* Exporting to a geotiff file
* Connecting with external applications via WMS
* Base block for on-the-fly map calculations and conversions
* API interactions: list, create, (partial) update, retrieve and delete

Raster data
------------

A rasters is a grid of cells organized into rows and columns. Each cell contains a value that represents real-world phenomena, such as water depth. The values can be continuous (e.g. 28.5 degrees) or integer numbers. Integer numbers can represent classes (e.g. 1: Water, 2: Land).

Rasterstore data can be static or temporal. Examples of static data are a digital elevation model and a land cover map. Temporal rasterstores consist of multiple timesteps. The data can be stored in time using an origin (e.g. 2019-01-01) and an interval (e.g. every day). Examples are weather predictions and timeseries of 3Di model results.

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

Raster management
------------------

The data management interface for rasters can be used to upload, edit or remove rasters.
 

.. image:: /images/c_datatypes_01.jpg

The Data Management interface is available at: “{your_organisation}.lizard.net/management/”.

.. note::
	This functionality is available only to users with an admin, manager or supplier role.

After this screen, please click on ‘Data Management’, then ‘Rasters’ and, depending on if you want to manage a new or pre-existing raster, continue.

.. image:: /images/c_datatypes_02.jpg
.. image:: /images/c_datatypes_03.jpg
.. image:: /images/c_datatypes_04.jpg

Interested in the possibilities for your organisation? Please contact Joeri Verheijden via info@lizard.net.