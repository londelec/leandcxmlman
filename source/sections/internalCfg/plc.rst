
.. _xmlelem-gpplc:

PLC
^^^

Internal data processing and basic PLC functionality is provided by :ref:`xmlelem-gpplc` instance.
This allows to perform logic operations such as 'OR' and 'AND' on the received data values.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gpplc`"

.. code-block:: none

   <PLC Index="99" XMLpath="myplc.xml" Name="PLC instance"/>


.. field-list-table:: PLC attributes
   :class: table table-condensed table-bordered longtable
   :name: tabid-plc
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:	Attribute
     :val,15:	Values or range
     :desc,75:	Description

   * :attr:	:xmlattr:`Index`
     :val:	|gpindexrange|
     :desc:	Index is a unique identifier of the PLC instance.
		It is used to reference data points defined in the PLC instance from other configuration files e.g. IO object tables
		(please see :ref:`xmlelem-IEC10xslDI`.\ :ref:`xmlattr-IEC10xslDIDevice`\; :ref:`xmlelem-IEC10xslAI`.\ :ref:`xmlattr-IEC10xslAIDevice`\; :ref:`xmlelem-IEC10xslDO`.\ :ref:`xmlattr-IEC10xslDODevice`\; :ref:`xmlelem-IEC10xslAO`.\ :ref:`xmlattr-IEC10xslAODevice` \ attributes of the Slave protocol instance).
		:inlineimportant:`Make sure the selected value doesn't overlap with communication protocol instance indexes.`

   * :attr:	:xmlattr:`XMLpath`
     :val:	Max 100 chars
     :desc:	XML configuration file name and path.
		This file contains PLC data point table and other settings.
		Path may be omitted if the XML file is stored in the default directory (|leandcapp|)
		:inlineimportant:`Attribute is case sensitive, observe case of the path and file name when specifying.`

.. include-file:: sections/Include/Name_wodef.rstinc ""

PLC data point tables are defined in a separate XML file specified in :ref:`xmlattr-gpplcXMLpath` attribute.
Contents of this XML file are described in the section :ref:`docref-plc`.
