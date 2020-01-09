======
Labels
======

Labels consist of three elements that are available through our API: LabelTypes, Labels and LabelParameters.
Labels are always linked to an organisation.
Each element is explained below.

LabelTypes
==========

LabelTypes can be found on the LabelType-endpoint `<demo.lizard.net/api/v3/labeltypes>`_ and describe the type of Label.
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
======

The Labels related to a specific LabelType can be found on the Labels-endpoint `<demo.lizard.net/api/v3/labels>`_.
Labels contain the follow fields:

* label_value: the index value of the Label
* object_type: the type of Asset related to the Label
* object_id: id of the Asset
* created: date when the label was created
* start: start of the validity of the Label (history of the Label)
* end: end of the validity of the Label (history of the Label)
* extra: this field can be used to show variables related to the definition of the Label (for instance a threshold value related to the Label)

LabelParameters
===============

The Label parameters is developed to store parameters that are used in the computation of the Label.
LabelParameters are linked to LabelTypes and Assets and can be found on the LabelParameters-endpoint `<demo.lizard.net/api/v3/labelparameters>`_.
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
================

With the count filter on the Labels endpoint it is possible to query a histogram of all Labels of a certain LabelType or a histogram of Labels within a region (e.g. municipality).