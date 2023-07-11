.. include:: global.roles

.. _docref-plc:
.. _xmlgroup-plcConfig: lelabel=PLCConfig

Internal PLC
============

This section describes how to enable basic PLC functionality and define internal data points.
Only one :ref:`xmlelem-gpplc` instance can be defined, but it can contain points that use data from all available communication protocol instances.
Points are defined in the XML configuration file described in this section.

Name and location path of the XML configuration file is not predefined, it can be chosen freely.
File name 'myplc.xml' is used as a sample.
Enter name of the XML file in :ref:`xmlelem-gpplc`.\ :ref:`xmlattr-gpplcXMLpath` attribute of the PLC instance created in |leandcxml| as follows:
:ref:`xmlattr-gpplcXMLpath` \ ="myplc.xml" .
Location path doesn't have to be specified if the XML file is located in the default directory (|leandcdir|).

| PLC configuration file (e.g. 'myplc.xml') must have a root node :ref:`xmlgroup-PLCConfig` which cosists of:
| 1 mandatory group :ref:`xmlelem-VersionControl`;
| 1 optional condition group :ref:`xmlgroup-plcConditionTable`.
| 1 optional data point group :ref:`xmlgroup-plcPointTable`.
| Please see the sample below.

.. code-block:: none

 <PLCConfig xmlns="http://www.londelec.com/xmlschemas/leandc/plc" … version="1.00">
   <VersionControl conf="1.00" date="2023-03-01" time="12:00:13"/>
   <ConditionTable>
     <Range CondId="1" OnMin="0.0001" OnMax="10e20" OffMin="0" OffMax="-inf"/>
         …
   </ConditionTable>
   <PointTable>
     <PNT Index="0" PlcType="or" SrcDevices="10" SrcIndexes="0" SrcTypes="DI"/>
         …
   </PointTable>
 </PLCConfig>


.. _xmlgroup-plcPointTable: lelabel=PointTable
.. _xmlelem-plcPNT: lelabel=PNT

PointTable group
----------------

| :ref:`xmlgroup-plcPointTable` group and its elements :ref:`xmlelem-plcPNT` are used to create internal point table.
  Each :ref:`xmlelem-plcPNT` element needs one or more sources of data to perform a logic operation.
  DI/AI information objects defined in the IO table of any Master protocol instance are used as data sources for internal PLC points.
| The result of the logic operation becomes value of the internal point itself and can be used by linking the internal point :ref:`xmlelem-plcPNT` to DI information objects (one or more) defined in the IO table of a Slave protocol instance.
  Please refer to the :ref:`docref-IEC10xslDI` section of a Slave protocol instance for more information on how to link an internal data point.

Please see sample :ref:`xmlgroup-plcPointTable` group and :ref:`xmlelem-plcPNT` elements below.
There are 2 data points defined with 2 :ref:`xmlelem-plcPNT` elements.

.. code-block:: none

 <PointTable>
   <PNT Index="0" PlcType="or" SrcDevices="10" SrcIndexes="0" SrcTypes="DI"/>
   <PNT Index="1" PlcType="and" SrcDevices="10,11" SrcIndexes="0,2" SrcTypes="DI,DI"/>
 </PointTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-plcPNT`"

.. code-block:: none

   <PNT Index="0" PlcType="or" SrcDevices="10" SrcIndexes="0" SrcTypes="DI" CondIds="1" DstDevice="11" DstIndex="0" Action="1" Name="OR point"/>

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-plcPNT`"

PNT attributes
^^^^^^^^^^^^^^

.. field-list-table:: Data point attributes
   :class: table table-condensed table-bordered longtable
   :name: tabid-plcPNT
   :spec: |C{0.16}|C{0.12}|S{0.72}|
   :header-rows: 1

   * :attr,10,center:	Attribute
     :val,15,center:	Values or range
     :desc,75:		Description

   * :attr:	:xmlattr:`Index`
     :val:	|maindexrange|
     :desc:	Index is a unique identifier of the data point.
		:inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order.
		This restriction has been put in place because insertion of a new index affects mapping to Slave communication protocol instances.`

   * :attr:	:xmlattr:`PlcType`
     :val:	or / and
     :desc:	Logic operation of the data point.
		This logic operation will be perfomed on the source data values and the result of the operation will become value of the internal data point.

   * :attr:	:xmlattr:`SrcDevices` \*
     :val:	|gpindexrange|
     :desc:	Index of the source communication protocol instance, any Master protocol instance listed in :ref:`xmlgroup-CommunicationCfg` group.
		Use value of the :ref:`xmlattr-gp101maIndex` attribute in order to select Master protocol instance as a source.
		Normally multiple data sources are required in order to perform a logic operation, therefore multiple Master protocol instances can be specified in this attribute.
		A list of up to 16 protocol instances separated by commas are allowed e.g. :ref:`xmlattr-plcPNTSrcDevices`\ ="10,17,20".

   * :attr:	:xmlattr:`SrcIndexes` \*
     :val:	|maindexrange|
     :desc:	Index of the source DI/AI object.
		Any DI/AI element of the selected Master protocol instance can be used as a source.
		Use value of the :ref:`xmlelem-IEC10xmaDI`.\ :ref:`xmlattr-IEC10xmaDIIndex` attribute of any object listed in the IO table of the selected Master protocol instance.
		Normally multiple data sources are required in order to perform a logic operation, therefore multiple object indexes can be specified in this attribute.
		A list of up to 16 DI/AI object indexes separated by commas are allowed e.g. :ref:`xmlattr-plcPNTSrcIndexes`\ ="0,1,6".

   * :attr:	:xmlattr:`SrcTypes` \*
     :val:	DI / AI
     :desc:	Type of the source object.
		DI/AI objects can be used as a source for a data point.
		Normally multiple data sources are required in order to perform a logic operation, therefore multiple object types can be specified in this attribute.
		A list of up to 16 object types separated by commas are allowed e.g. :ref:`xmlattr-plcPNTSrcTypes`\ ="DI,DI,AI".

   * :attr:	:xmlattr:`CondIds` \*
     :val:	0...65535
     :desc:	Identifier of the condition defined in the :ref:`xmlgroup-plcConditionTable` group.
		Currently used to set conditions only for source AI objects.
		A list of up to 16 identifiers separated by commas can be specified in this attribute e.g. :ref:`xmlattr-plcPNTCondIds`\ ="0,1,9".
		Value 0 - no condition used.
		|optinalattr|

   * :attr:	:xmlattr:`DstDevice`
     :val:	|gpindexrange|
     :desc:	Index of the destination communication protocol instance, any Master protocol instance listed in :ref:`xmlgroup-CommunicationCfg` group.
		Use value of the :ref:`xmlattr-gp101maIndex` attribute in order to select Master protocol instance as a destination.
		:inlinetip:`This attribute is only used if the PLC data point is automatically sending a control command.`

   * :attr:	:xmlattr:`DstIndex`
     :val:	|maindexrange|
     :desc:	Index of the destination DO object.
		Any DO element of the selected Master protocol instance can be used as a destination.
		Use value of the :ref:`xmlelem-IEC10xmaDO`.\ :ref:`xmlattr-IEC10xmaDOIndex` attribute of any DO object listed in the IO table of the selected Master protocol instance.
		:inlinetip:`This attribute is only used if the PLC data point is automatically sending a control command.`

   * :attr:	:xmlattr:`Action`
     :val:	0...255
     :desc:	Action that PLC data point performs automatically.
		See :numref:`tabid-plcAction` for description.

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. important::

	\* It is essential to specify equal number of parameters in attributes :ref:`xmlattr-plcPNTSrcDevices`; :ref:`xmlattr-plcPNTSrcIndexes`; :ref:`xmlattr-plcPNTSrcTypes` and :ref:`xmlattr-plcPNTCondIds`.
	For example if 2 DI information objects are used as internal data point sources, each of these attributes must have 2 parameters e.g.
	:ref:`xmlattr-plcPNTSrcDevices`\ ="10,10"; :ref:`xmlattr-plcPNTSrcIndexes`\ ="0,1"; :ref:`xmlattr-plcPNTSrcTypes`\ ="DI,AI" and :ref:`xmlattr-plcPNTCondIds`\ ="0,1".


.. field-list-table:: PLC Action values
   :class: table table-condensed table-bordered longtable
   :name: tabid-plcAction
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10,center:	Action Values
     :desc,90:		Description

   * :attr:	0
     :desc:	No Action.

   * :attr:	1
.. include-file:: sections/Include/plc_action_event.rstinc "" "OFF to ON"

   * :attr:	2
.. include-file:: sections/Include/plc_action_event.rstinc "" "ON to OFF"

   * :attr:	3
.. include-file:: sections/Include/plc_action_cont.rstinc "" "ON"

   * :attr:	4
.. include-file:: sections/Include/plc_action_cont.rstinc "" "OFF"

   * :attr: 	5...255
     :desc:	Reserved for future use.


.. _xmlgroup-plcConditionTable: lelabel=ConditionTable

ConditionTable group
--------------------

| :ref:`xmlgroup-plcConditionTable` group is used to define conditions for analog values of the AI objects that are used as internal data point sources.
  There is only one condition type available at the moment - the range of analog values defined using the :ref:`xmlelem-plcRange` element.

Please see sample :ref:`xmlgroup-plcConditionTable` group and :ref:`xmlelem-plcRange` element below.
There are 2 conditions defined with 2 :ref:`xmlelem-plcRange` elements.

.. code-block:: none

 <ConditionTable>
   <Range CondId="1" OnMin="0" OnMax="10e4" OffMin="-5" OffMax="-inf"/>
   <Range CondId="2" OnMin="100" OnMax="200"/>
 </ConditionTable>

Condition types and their attributes are described in the following sections.


.. _xmlelem-plcRange: lelabel=Range

Range element
-------------

| :ref:`xmlelem-plcRange` element is used to define 2 ranges for analog values.
  Whenever received analog value falls within a defined range, the position change event ON or OFF is generated.
  These ON and OFF positions are used as a source for internal points to perform a logic operation.
  Effectively the :ref:`xmlelem-plcRange` element is used to convert ranges of AI object values into DI with ON and OFF positions.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-plcRange`"

.. code-block:: none

   <Range CondId="0" OnMin="0" OnMax="10e4" OffMin="-5" OffMax="-99999.9" Name="AI to DI conversion"/>

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-plcRange`"

Range attributes
^^^^^^^^^^^^^^^^


.. field-list-table:: Range attributes
   :class: table table-condensed table-bordered longtable
   :name: tabid-plcRange
   :spec: |C{0.16}|C{0.12}|S{0.72}|
   :header-rows: 1

   * :attr,10,center:	Attribute
     :val,15,center:	Values or range
     :desc,75:		Description

   * :attr:	:xmlattr:`CondId`
     :val:	1...65535
     :desc:	Condition identifier must be a unique number within a :ref:`xmlgroup-plcConditionTable` group.
		:inlineimportant:`Identifier numbering must start with 1 and identifiers must be arranged in an ascending order.`

   * :attr:	:xmlattr:`OnMin`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :desc:	Minimal (inclusive) analog value that will result in a ON position.
		Internal point :ref:`xmlelem-plcPNT` that uses AI as a data source will get ON position whenever received analog value is equal or exceeds this attribute and
		is less or equal to :ref:`xmlattr-plcRangeOnMax` attribute.
		Positive and negative infinity values 'inf' and '-inf' can be specified.

   * :attr:	:xmlattr:`OnMax`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :desc:	Maximal (inclusive) analog value that will result in a ON position.
		Internal point :ref:`xmlelem-plcPNT` that uses AI as a data source will get ON position whenever received analog value is less or equal to this attribute and
		is equal or exceeds :ref:`xmlattr-plcRangeOnMin` attribute.
		Positive and negative infinity values 'inf' and '-inf' can be specified.

   * :attr:	:xmlattr:`OffMin`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :desc:	Minimal (inclusive) analog value that will result in a OFF position.
		Internal point :ref:`xmlelem-plcPNT` that uses AI as a data source will get OFF position whenever received analog value is equal or exceeds this attribute and
		is less or equal to :ref:`xmlattr-plcRangeOffMax` attribute.
		Positive and negative infinity values 'inf' and '-inf' can be specified.
		|optinalattr|
		:inlinetip:`Any analog value outside the range defined by` :ref:`xmlattr-plcRangeOnMin` :inlinetip:`and` :ref:`xmlattr-plcRangeOnMax` :inlinetip:`attributes will result in OFF position if this attribute is not used.`

   * :attr:	:xmlattr:`OffMax`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :desc:	Maximal (inclusive) analog value that will result in a OFF position.
		Internal point :ref:`xmlelem-plcPNT` that uses AI as a data source will get OFF position whenever received analog value is less or equal to this attribute and
		is equal or exceeds to :ref:`xmlattr-plcRangeOffMin` attribute.
		Positive and negative infinity values 'inf' and '-inf' can be specified.
		|optinalattr|
		:inlinetip:`Any analog value outside the range defined by` :ref:`xmlattr-plcRangeOnMin` :inlinetip:`and` :ref:`xmlattr-plcRangeOnMax` :inlinetip:`attributes will result in OFF position if this attribute is not used.`

