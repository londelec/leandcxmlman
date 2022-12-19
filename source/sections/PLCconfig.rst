.. include:: global.roles

.. _docref-plc:
.. _xmlgroup-plcConfig: lelabel=PLCConfig

Internal PLC
============

This section describes how to enable basic PLC functionality and define internal data points.
Only one :ref:`xmlelem-gpplc` instance can be defined, but it can contain points that use data values from all available communication protocol instances.
Points are defined in the XML configuration file described in this section.

Name and location path of the XML configuration file is not predefined, it can be chosen freely.
File name 'myplc.xml' is used as a sample.
Enter name of the XML file in :ref:`xmlelem-gpplc`.\ :ref:`xmlattr-gpplcXMLpath` attribute of the PLC instance created in |leandcxml| as follows:
:ref:`xmlattr-gpplcXMLpath` \ ="myplc.xml" .
Location path doesn't have to be specified if the XML file is located in the default directory (|leandcdir|).

| PLC configuration file (e.g. 'myplc.xml') must have a root node :ref:`xmlgroup-PLCConfig` which cosists of:
| 1 mandatory group :ref:`xmlelem-VersionControl`;
| 1 optional data point group :ref:`xmlgroup-plcPointTable`.
| Please see the sample below.

.. code-block:: none

 <PLCConfig xmlns="http://www.londelec.com/xmlschemas/leandc/plc" … version="1.00">
   <VersionControl conf="1.00" date="2022-06-01" time="12:00:13"/>
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
  Each :ref:`xmlelem-plcPNT` element can be linked to DI information objects (one or more) defined in the IO table of a Slave protocol instance.
| Please refer to the :ref:`docref-IEC10xslDI` section of a Slave protocol instance for more information on how to link data point.

Please see sample :ref:`xmlgroup-plcPointTable` group and :ref:`xmlelem-plcPNT` elements below.
There are 2 data points defined with 2 :ref:`xmlelem-plcPNT` elements.

.. code-block:: none

 <PointTable>
   <PNT Index="0" PlcType="or" SrcDevices="10" SrcIndexes="0" SrcTypes="DI"/>
   <PNT Index="1" PlcType="and" SrcDevices="10,11" SrcIndexes="0,2" SrcTypes="DI,DI"/>
 </PointTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-plcPNT`"

.. code-block:: none

   <PNT Index="0" PlcType="or" SrcDevices="10" SrcIndexes="0" SrcTypes="DI" DstDevice="11" DstIndex="0" Action="1" Name="OR point"/>

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
		This logic operation will be perfomed on the source data values and the result of the operation will be value of this data point.

   * :attr:	:xmlattr:`SrcDevices` \*
     :val:	|gpindexrange|
     :desc:	Index of the source communication protocol instance, any Master protocol instance listed in :ref:`xmlgroup-CommunicationCfg` group.
		Use value of the :ref:`xmlattr-gp101maIndex` attribute in order to select Master protocol instance as a source.
		Normally multiple data values are required in order to perform a logic operation.
		A list of up to 32 source instances separated by commas can be specified in this attribute e.g. :ref:`xmlattr-plcPNTSrcDevices`\ ="10,17,20".

   * :attr:	:xmlattr:`SrcIndexes` \*
     :val:	|maindexrange|
     :desc:	Index of the source DI object.
		Any DI element of the selected Master protocol instance can be used as a source.
		Use value of the :ref:`xmlelem-IEC10xmaDI`.\ :ref:`xmlattr-IEC10xmaDIIndex` attribute of any DI object listed in the IO table of the selected Master protocol instance.
		Normally multiple data values are required in order to perform a logic operation.
		A list of up to 32 source DI objext separated by commas can be specified in this attribute e.g. :ref:`xmlattr-plcPNTSrcIndexes`\ ="0,1,6".

   * :attr:	:xmlattr:`SrcTypes` \*
     :val:	DI
     :desc:	Type of the source object.
		Only DI objects can be used as a source for a data point.
		Normally multiple data values are required in order to perform a logic operation.
		A list of up to 32 source types separated by commas can be specified in this attribute e.g. :ref:`xmlattr-plcPNTSrcTypes`\ ="DI,DI,DI".

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

	\* It is essential to specify equal number of values in source attributes :ref:`xmlattr-plcPNTSrcDevices`; :ref:`xmlattr-plcPNTSrcIndexes` and :ref:`xmlattr-plcPNTSrcTypes`.
	For example if 2 DI information objects are used as a data source, each of these attributes must have 2 values e.g.
	:ref:`xmlattr-plcPNTSrcDevices`\ ="10,10"; :ref:`xmlattr-plcPNTSrcIndexes`\ ="0,1" and :ref:`xmlattr-plcPNTSrcTypes`\ ="DI,DI".


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
     :desc:	Send control command to DO index specified in :ref:`xmlattr-plcPNTDstIndex` of the communication protocol instance specified in :ref:`xmlattr-plcPNTDstDevice` attribute
		every time the PLC point state transitions from OFF to ON.
		Outgoing control command will have qualifier ON.

   * :attr: 	2...255
     :desc:	Reserved for future use. 
