.. include:: global.roles

.. _docref-plc:
.. _xmlgroup-plcConfig: lelabel=PLCConfig

Internal PLC
============

This section describes how to enable basic PLC functionality and define internal data points and commands.
Only one :ref:`xmlelem-gpplc` instance can be defined, but it can contain points that use data from all available communication protocol instances.
Points are defined in the XML configuration file described in this section.

Name and location path of the XML configuration file is not predefined, it can be chosen freely.
File name 'myplc.xml' is used as a sample.
Enter name of the XML file in :ref:`xmlelem-gpplc`.\ :ref:`xmlattr-gpplcXMLpath` attribute of the PLC instance created in |leandcxml| as follows:
:ref:`xmlattr-gpplcXMLpath` \ ="myplc.xml" .
Location path doesn't have to be specified if the XML file is located in the default directory (|leandcdir|).

| PLC configuration file (e.g. 'myplc.xml') must have a root node :ref:`xmlgroup-PLCConfig` which cosists of:
| 1 mandatory group :ref:`xmlelem-VersionControl`;
| 1 optional settings group :ref:`xmlgroup-plcSettings`;
| 1 optional condition group :ref:`xmlgroup-plcConditionTable`;
| 1 optional data point group :ref:`xmlgroup-plcPointTable`;
| Please see the sample below.

.. code-block:: none

 <PLCConfig xmlns="http://www.londelec.com/xmlschemas/leandc/plc" … version="1.00">
   <VersionControl conf="1.00" date="2023-03-01" time="12:00:13"/>
    <Settings>
     <Timeouts InApplication="8" OutApplication="7" CmdForward="6"/>
   </Settings>
   <ConditionTable>
     <Range CondId="1" OnMin="0.0001" OnMax="10e20" OffMin="0" OffMax="-inf"/>
         …
   </ConditionTable>
   <PointTable>
     <PNT Index="0" PlcType="or" SrcDevices="10" SrcIndexes="0" SrcTypes="DI"/>
         …
   </PointTable>
 </PLCConfig>


.. _xmlgroup-plcSettings: lelabel=Settings

Settings group
--------------

Various settings of the basic PLC instance are defined in the :ref:`xmlgroup-plcSettings` group as shown below.

.. code-block:: none

 <Settings>
   <Timeouts … />
 </Settings>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.


.. _xmlelem-plcTimeouts:

Timeouts
^^^^^^^^

PLC command processing timeouts are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-plcTimeouts`"

.. code-block:: none

   <Timeouts InApplication="8" OutApplication="7" CmdForward="6"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-plcTimeouts" "PLC Timeouts attributes" ":spec: |C{0.12}|C{0.1}|C{0.1}|S{0.68}|"

   * :attr:	:xmlattr:`InApplication`
     :val:	1...2\ :sup:`32`\  - 1
     :def:	30 sec
     :desc:	Application timeout is a delay in seconds for the received (incoming) PLC command processing.
		This timeout applies to commands received from upstream (Slave) protocol instance e.g. SCADA.
		Command fails if the PLC instance can't complete the command (i.e. command is forwarded to Master protocol instance(s) but no valid responses received) within a configured number of seconds.
		If the PLC instance forwards commands to several Master protocol instance(s) all commands must be completed (and valid responses received) within a configured number of seconds.

   * :attr:	:xmlattr:`OutApplication`
     :val:	1...2\ :sup:`32`\  - 1
     :def:	10 sec
     :desc:	Application timeout is a delay in seconds for the outgoing (PLC generated / forwarded) command processing.
		This timeout applies to commands PLC instance sends to downstream (Master) protocol instance(s).
		Command fails if the PLC instance can't complete the command (i.e. command is sent to outstation(s) but no valid responses received) within a configured number of seconds.
		In general this timeout is used to terminate pending commands, if communication to outstation(s) is lost.

.. include-file:: sections/Include/CmdForwardTimeout.rstinc


.. _xmlgroup-plcPointTable: lelabel=PointTable
.. _xmlelem-plcPNT: lelabel=PNT

PointTable group
----------------

| :ref:`xmlgroup-plcPointTable` group and its elements :ref:`xmlelem-plcPNT` are used to create an internal point table.
  Each :ref:`xmlelem-plcPNT` element needs one or more sources of data to perform a logic or arithmetic operation.
  DI/AI information objects defined in IO table of any Master protocol instance can be used as data sources for internal PLC points.
| The result of the logic or aritmetic operation becomes value of the internal data point.
  This result can be used by linking the internal point :ref:`xmlelem-plcPNT` to DI/AI information object (one or more) defined in the IO table of a Slave protocol instance.
  Please refer to the :ref:`docref-IEC10xslDI` and :ref:`docref-IEC10xslAI` sections of a Slave protocol instance for more information on how to link an internal data point.

Please see sample :ref:`xmlgroup-plcPointTable` group and :ref:`xmlelem-plcPNT` elements below.
There are 2 data points defined with 2 :ref:`xmlelem-plcPNT` elements.

.. code-block:: none

 <PointTable>
   <PNT Index="0" PlcType="or" SrcDevices="10" SrcIndexes="0" SrcTypes="DI"/>
   <PNT Index="1" PlcType="add" SrcDevices="10,11" SrcIndexes="0,2" SrcTypes="AI,AI"/>
 </PointTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-plcPNT`"

.. code-block:: none

   <PNT Index="0" PlcType="or" SrcDevices="10" SrcIndexes="0" SrcTypes="DI" CondIds="1" Deadband="12" Percent="5.4" ExcludeMask="0x80" CmdIndex="0" Action="1" Name="OR point"/>

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
     :val:	or / and / add / mult
     :desc:	Logic or arithmetic operation of the data point.
		This operation will be perfomed on a source data values and the result of the operation will become value of the internal data point.
		See :numref:`tabid-PlcPntType` for more information.

   * :attr:	:xmlattr:`SrcDevices` \**
     :val:	|gpindexrange|
     :desc:	Index of the source communication protocol instance, any Master protocol instance listed in :ref:`xmlgroup-CommunicationCfg` group.
		Use value of the :ref:`xmlattr-gp101maIndex` attribute in order to select Master protocol instance as a source.
		Internal PLC instance can also be used as a source, in this case use the :ref:`xmlelem-gpplc`.\ :ref:`xmlattr-gpplcIndex` attribute of the PLC instance itself.
		Normally multiple data sources are required in order to perform a logic operation, therefore multiple Master protocol instances can be specified in this attribute.
		A list of up to 32 protocol instances separated by commas are allowed e.g. :ref:`xmlattr-plcPNTSrcDevices`\ ="10,17,20".

   * :attr:	:xmlattr:`SrcIndexes` \**
     :val:	|maindexrange|
     :desc:	Index of the source DI/AI object.
		Any DI/AI element of the selected Master protocol instance can be used as a source.
		Use value of the :ref:`xmlelem-IEC10xmaDI`.\ :ref:`xmlattr-IEC10xmaDIIndex` attribute of any object listed in the IO table of the selected Master protocol instance.
		Normally multiple data sources are required in order to perform a logic operation, therefore multiple object indexes can be specified in this attribute.
		A list of up to 32 DI/AI object indexes separated by commas are allowed e.g. :ref:`xmlattr-plcPNTSrcIndexes`\ ="0,1,6".

   * :attr:	:xmlattr:`SrcTypes` \**
     :val:	DI / AI
     :desc:	Type of the source object.
		DI/AI objects can be used as a source for a data point.
		Normally multiple data sources are required in order to perform a logic or artithmetic operation, therefore multiple object types can be specified in this attribute.
		A list of up to 32 object types separated by commas are allowed e.g. :ref:`xmlattr-plcPNTSrcTypes`\ ="DI,DI,AI".

   * :attr:	:xmlattr:`CondIds` \**
     :val:	0...65535
     :desc:	Identifier of the condition defined in the :ref:`xmlgroup-plcConditionTable` group.
		Currently used to set conditions only for source AI objects.
		A list of up to 32 identifiers separated by commas can be specified in this attribute e.g. :ref:`xmlattr-plcPNTCondIds`\ ="0,1,9".
		Value 0 - no condition used.
		|optinalattr|

   * :attr:	:xmlattr:`Deadband` \*
     :val:	0 or +1.18×10\ :sup:`-38` \ ... +3.4×10\ :sup:`38`\
     :desc:	Absolute (static) deadband applicable only to analog point value.
		Internal point value will be updated and event will be generated if the latest analog value (calculated from source AI values) exceeds value stored in the database plus/minus :ref:`xmlattr-plcPNTDeadband`.
		Defined :ref:`xmlattr-plcPNTDeadband` is added and subtracted from old analog value stored in the database in order to create the absolute deadband range.
		Limits of this range are calculated as follows: Lower = (oldvalue - deadband); Upper = (oldvalue + deadband).
		Analog values of the PLC point are checked against the deadband range and event is generated if a new value is outside the limit.
		Value 0 disables the deadband feature.
		|optinalattr|

   * :attr:	:xmlattr:`Percent` \*
     :val:	0 or +1.18×10\ :sup:`-38` \ ... +3.4×10\ :sup:`38`\
     :desc:	Percent (dynamic) deadband applicable only to analog point value.
		Internal point value will be updated and event will be generated if the latest analog value (calculated from source AI values) exceeds value stored in the database plus/minus :ref:`xmlattr-plcPNTPercent`.
		Defined :ref:`xmlattr-plcPNTPercent` is used to calculate the dynamic deadband range based on the old analog value stored in the database.
		Limits of this range are calculated as follows: Lower = (oldvalue - (oldvalue * percent / 100)); Upper = (oldvalue + (oldvalue * percent / 100)).
		Analog values of the PLC point are checked against the deadband range and event is generated if a new value is outside the limit.
		Value 0 disables the percent feature.
		|optinalattr|

   * :attr:	:xmlattr:`ExcludeMask`
     :val:	|flags8range|
     :desc:	Exclude source DI/AI values from processing based on their quality.
		See :numref:`tabid-PlcPntExcludeMask` for more information.
		|optinalattr|

   * :attr:	:xmlattr:`CmdIndex`
     :val:	|maindexrange|
     :desc:	Index of the PLC command element.
		Any :ref:`xmlelem-plcCMD` element can be selected.
		Use value of the :ref:`xmlelem-plcCMD`.\ :ref:`xmlattr-plcCMDIndex` attribute.
		:inlineimportant:`This attribute must be used only if the PLC data point needs to generate a control command automatically based on its value.`

   * :attr:	:xmlattr:`Action`
     :val:	0...255
     :desc:	Action that PLC data point performs automatically.
		See :numref:`tabid-plcAction` for description.

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. important::

	\** It is essential to specify equal number of parameters in attributes :ref:`xmlattr-plcPNTSrcDevices`; :ref:`xmlattr-plcPNTSrcIndexes`; :ref:`xmlattr-plcPNTSrcTypes` and :ref:`xmlattr-plcPNTCondIds`.
	For example if 2 DI information objects are used as an internal data point sources, each of these attributes must have 2 parameters e.g.
	:ref:`xmlattr-plcPNTSrcDevices`\ ="10,10"; :ref:`xmlattr-plcPNTSrcIndexes`\ ="0,1"; :ref:`xmlattr-plcPNTSrcTypes`\ ="DI,AI" and :ref:`xmlattr-plcPNTCondIds`\ ="0,1".

.. include-file:: sections/Include/ma_AI_Annex.rstinc "" ":ref:`xmlattr-plcPNTDeadband`" ":ref:`xmlattr-plcPNTPercent`"


PLC operation types
^^^^^^^^^^^^^^^^^^^

| There are 6 types of logic and arithmetic operations that can be performed on a DI/AI data received from outstation.
  These are summarized in the table below.

.. field-list-table:: PLC logic or arithmetic operations
   :class: table table-condensed table-bordered longtable
   :name: tabid-PlcPntType
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10,center:	:ref:`xmlattr-plcPNTPlcType`
     :desc,90:		Description

   * :attr:	or
     :desc:	| Perform logic OR operation based on a DI object state position.
		  DI object can have 4 states - INTER; OFF; ON; INVALID but only ON and OFF (distinctive position) states are used to perform a PLC operation.
		  If state of any of the source DI objects is INTER or INVALID the PLC data point will also have an INTER or INVALID state.
.. include-file:: sections/Include/plc_ai_exclude.rstinc "" "DI"
		  At least 2 source DI objects required to perform a logic OR operation.
		  The resulting state of the PLC data point based on the distinctive position states (ON or OFF) of 2 source DI objects is shown below:
		| DI1 DI2 => PLC point:
		| OFF OFF => OFF
		| ON OFF => ON
		| OFF ON => ON
		| ON ON => ON

   * :attr:	and
     :desc:	| Perform logic AND operation based on a DI object state position.
		  DI object can have 4 states - INTER; OFF; ON; INVALID but only ON and OFF (distinctive position) states are used to perform a PLC operation.
		  If state of any of the source DI objects is INTER or INVALID the PLC data point will also have an INTER or INVALID state.
.. include-file:: sections/Include/plc_ai_exclude.rstinc "" "DI"
		  At least 2 source DI objects are required to perform a logic AND operation.
		  The resulting state of the PLC data point based on the distinctive position states (ON or OFF) of 2 source DI objects is shown below:
		| DI1 DI2 => PLC point:
		| OFF OFF => OFF
		| ON OFF => OFF
		| OFF ON => OFF
		| ON ON => ON

   * :attr:	add
     :desc:	  Addition of AI object values.
		  2 or more AI values received from outstation can be added together and the sum will become value of the PLC data point.
.. include-file:: sections/Include/plc_ai_exclude.rstinc "" "AI"
		  Addition takes place after AI value scaling i.e. after coefficient (if any) specified in the source protocol instance is applied.

   * :attr:	mult
     :desc:	  Multiplication of AI object values.
		  2 or more AI values received from outstation can be multiplied together and the product will become value of the PLC data point.
.. include-file:: sections/Include/plc_ai_exclude.rstinc "" "AI"
		  Multiplication takes place after AI value scaling i.e. after coefficient (if any) specified in the source protocol instance is applied.

   * :attr:	avgany
     :desc:	  Get average of AI object values.
		  Average of 2 or more AI values received from outstation can be calculated and will become value of the PLC data point.
		  If the source analog value is 0, it is included in calculation.
.. include-file:: sections/Include/plc_ai_exclude.rstinc "" "AI"
		  If any of the source AI values are excluded from processing based on quality by the :ref:`xmlattr-plcPNTExcludeMask` attribute,
		  the average is calculated only from those AI values that are available and online.

   * :attr:	avgnonzero
     :desc:	  Get average of non-zero AI object values.
		  Average of 2 or more AI values received from outstation can be calculated and will become value of the PLC data point.
		  If the source analog value is 0, it is excluded and average is calculated only from non-zero values.
.. include-file:: sections/Include/plc_ai_exclude.rstinc "" "AI"
		  If any of the source AI values are excluded from processing based on quality by the :ref:`xmlattr-plcPNTExcludeMask` attribute,
		  the average is calculated only from those AI values that are available and online.


PNT exclusion based on quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| DI/AI values that are used as sources for PLC points can be excluded (ignored) if any of their quality bits are set or
  the source outstation where DI/AI object originates is offline.
  By default all source DI/AI values are used in PLC point processing and the resulting PLC point will have the same quality bits
  as all of the source DI/AI objects combined (logic OR is performed to quality bits of all source DI/AI objects).

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-PlcPntExcludeMask" " Source DI/AI quality exclusion bits" :ref:`xmlattr-plcPNTExcludeMask` "Exclusion mask"

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	Last available value of the source DI/AI will be **used** for PLC point processing if a source DI/AI object is not received from outstation
		or outstation is OFFLINE.
		The resulting PLC point will be marked offline if any of the source DI/AI objects are offline.

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Source DI/AI value will be **excluded** from PLC point processing if a source DI/AI object is not received from outstation or
		outstation is OFFLINE.
		Any source DIs/AIs originating from outstation that is offline will not affect PLC point processing (their values will be ignored)
		and the resulting PLC point's value will be based only on those source DI/AI values that are available and online.

   * :attr:	Bit 3
     :val:	xxxx.0xxx
     :desc:	Invalid [:lemonobgtext:`IV`] bit of the resulting PLC point **will not be** set if all source DI/AI objects are excluded from processing because of their quality or
		are not online i.e. not received from outstation.
		If all source DI/AI values are excluded from processing the resulting AI PLC point will have a valid 0 value and the resulting DI PLC point will have a valid OFF value.

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	Invalid [:lemonobgtext:`IV`] bit of the resulting PLC point **will be** set if all source DI/AI objects are excluded from processing because of their quality or
		are not online i.e. not received from outstation.

   * :attr:	Bit 4
     :val:	xxx0.xxxx
     :desc:	Source DI/AI values with set Blocked [:lemonobgtext:`BL`] bit will be **included** in PLC point processing
		and the resulting PLC point will also have a set Blocked [:lemonobgtext:`BL`] bit.

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	Source DI/AI values with set Blocked [:lemonobgtext:`BL`] bit will be **excluded** from PLC point processing.

   * :attr:	Bit 5
     :val:	xx0x.xxxx
     :desc:	Source DI/AI values with set Substituted [:lemonobgtext:`SB`] bit will be **included** in PLC point processing
		and the resulting PLC point will also have a set Substituted [:lemonobgtext:`SB`] bit.

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	Source DI/AI values with set Substituted [:lemonobgtext:`SB`] bit will be **excluded** from PLC point processing.

   * :attr:	Bit 6
     :val:	x0xx.xxxx
     :desc:	Source DI/AI values with set Not Topical [:lemonobgtext:`NT`] bit will be **included** in PLC point processing
		and the resulting PLC point will also have a set Not Topical [:lemonobgtext:`NT`] bit.

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	Source DI/AI values with set Not Topical [:lemonobgtext:`NT`] bit will be **excluded** from PLC point processing.

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	Source DI/AI values with set Invalid [:lemonobgtext:`IV`] bit will be **included** in PLC point processing
		and the resulting PLC point will also have a set Invalid [:lemonobgtext:`IV`] bit.

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	Source DI/AI values with set Invalid [:lemonobgtext:`IV`] bit will be **excluded** from PLC point processing.

   * :attr:	Bits 0,1
     :val:	Any
     :desc:	Bits reserved for future use


PNT actions
^^^^^^^^^^^

| Point actions are primarily used to trigger commands based on a value of the PLC data point.
  Available actions are summarized in the table below.


.. field-list-table:: PLC Action values
   :class: table table-condensed table-bordered longtable
   :name: tabid-plcAction
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10,center:	:ref:`xmlattr-plcPNTAction`
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


.. _xmlgroup-plcCommandTable: lelabel=CommandTable
.. _xmlelem-plcCMD: lelabel=CMD

CommandTable group
------------------

| :ref:`xmlgroup-plcCommandTable` group and its elements :ref:`xmlelem-plcCMD` are used to create an internal command table.
| The main purpose of the :ref:`xmlelem-plcCMD` elements is to generate and send multiple commands to one or more Master protocol instances
  when command is received from Slave protocol instance.
  :ref:`xmlelem-plcCMD` can be used as a destination for any DO/AO information object defined in the IO table of a Slave protocol instance.
  Please refer to the :ref:`docref-IEC10xslDO` and :ref:`docref-IEC10xslAO` sections of a Slave protocol instance for more information on how
  to use PLC :ref:`xmlelem-plcCMD` element as a destination for control commands.
| Each :ref:`xmlelem-plcCMD` element needs one or more command destinations to forward the received command to.
  DO/AO information objects defined in the IO table of any Master protocol instance can be used as a command destination.

Please see sample :ref:`xmlgroup-plcCommandTable` group and :ref:`xmlelem-plcCMD` elements below.
There are 2 commands defined with 2 :ref:`xmlelem-plcCMD` elements.

.. code-block:: none

 <CommandTable>
   <CMD Index="0" PlcType="direct" DstDevices="10" DstIndexes="0" DstTypes="DO"/>
   <CMD Index="1" PlcType="divproportion" DstDevices="10,11" DstIndexes="0,2" DstTypes="AO,AO"/>
 </CommandTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-plcCMD`"

.. code-block:: none

   <CMD Index="0" PlcType="direct" DstDevices="10" DstIndexes="0" DstTypes="DO" CondIds="1" Name="Direct command"/>

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-plcCMD`"

CMD attributes
^^^^^^^^^^^^^^

.. field-list-table:: PLC command attributes
   :class: table table-condensed table-bordered longtable
   :name: tabid-plcCMD
   :spec: |C{0.16}|C{0.12}|S{0.72}|
   :header-rows: 1

   * :attr,10,center:	Attribute
     :val,15,center:	Values or range
     :desc,75:		Description

   * :attr:	:xmlattr:`Index`
     :val:	|maindexrange|
     :desc:	Index is a unique identifier of the PLC command.
		:inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order.
		This restriction has been put in place because insertion of a new index affects mapping to Slave communication protocol instances.`

   * :attr:	:xmlattr:`PlcType`
     :val:	direct / divproportion
     :desc:	Command pre-processing before forwarding.
		Type of processing can be defined in this attribute before command is forwarded to its destination station(s).
		See :numref:`tabid-PlcCmdType` for more information.

   * :attr:	:xmlattr:`DstDevices` \*
     :val:	|gpindexrange|
     :desc:	Index of the destination communication protocol instance, any Master protocol instance listed in :ref:`xmlgroup-CommunicationCfg` group.
		Use value of the :ref:`xmlattr-gp101maIndex` attribute in order to select Master protocol instance as a destination.
		Multiple Master protocol instances can be specified in this attribute.
		A list of up to 32 protocol instances separated by commas are allowed e.g. :ref:`xmlattr-plcCMDDstDevices`\ ="10,17,20".

   * :attr:	:xmlattr:`DstIndexes` \*
     :val:	|maindexrange|
     :desc:	Index of the destination DO/AO object.
		Any DO/AO element of the selected Master protocol instance can be used as a destination.
		Use value of the :ref:`xmlelem-IEC10xmaDO`.\ :ref:`xmlattr-IEC10xmaDOIndex` attribute of any object listed in the IO table of the selected Master protocol instance.
		Multiple object indexes can be specified in this attribute.
		A list of up to 32 DO/AO object indexes separated by commas are allowed e.g. :ref:`xmlattr-plcCMDDstIndexes`\ ="0,1,6".

   * :attr:	:xmlattr:`DstTypes` \*
     :val:	DO / AO
     :desc:	Type of the destination object.
		DO/AO objects can be used as a destination for a PLC command.
		Multiple object types can be specified in this attribute.
		A list of up to 32 object types separated by commas are allowed e.g. :ref:`xmlattr-plcCMDDstTypes`\ ="DO,DO,AO".

   * :attr:	:xmlattr:`CondIds` \*
     :val:	0...65535
     :desc:	Identifier of the condition defined in the :ref:`xmlgroup-plcConditionTable` group.
		Currently used to set conditions only for destination AO objects.
		A list of up to 32 identifiers separated by commas can be specified in this attribute e.g. :ref:`xmlattr-plcCMDCondIds`\ ="0,1,9".
		Only :ref:`xmlelem-plcSubstitution` and :ref:`xmlelem-plcScaling` conditions can be used for a PLC command.
		Value 0 - no condition used.
		|optinalattr|

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. important::

	\* It is essential to specify equal number of parameters in attributes :ref:`xmlattr-plcCMDDstDevices`; :ref:`xmlattr-plcCMDDstIndexes`; :ref:`xmlattr-plcCMDDstTypes` and :ref:`xmlattr-plcCMDCondIds`.
	For example if 2 AO information objects are used as a destination, each of these attributes must have 2 parameters e.g.
	:ref:`xmlattr-plcCMDDstDevices`\ ="10,10"; :ref:`xmlattr-plcCMDDstIndexes`\ ="0,1"; :ref:`xmlattr-plcCMDDstTypes`\ ="AO,AO" and :ref:`xmlattr-plcCMDCondIds`\ ="0,1".


PLC command types
^^^^^^^^^^^^^^^^^

| There are 2 types of pre-processing that can take place before command is forwarded to the destionation protocol instance(s).
  These are summarized in the table below.


.. field-list-table:: PLC command pre-processing
   :class: table table-condensed table-bordered longtable
   :name: tabid-PlcCmdType
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10,center:	:ref:`xmlattr-plcCMDPlcType`
     :desc,90:		Description

   * :attr:	direct
     :desc:	Forward control command to destination protocol instance without modifying its qualifier or setpoint value.

   * :attr:	divproportion
     :desc:	Divide AO setpoint value by the number of defined PLC command destinations.
		For example, if a PLC command has 2 destination AO objects, the received value 6 will be divided by 2 and
		value 3 will be sent to each destination AO object.
		This setting applies only to AO commands.


.. _xmlgroup-plcConditionTable: lelabel=ConditionTable

ConditionTable group
--------------------

| :ref:`xmlgroup-plcConditionTable` group is used to define conditions for processing and modifying PLC analog values.
  There are 3 condition types available:
| Range of analog values defined using the :ref:`xmlelem-plcRange` element;
| Analog value scaling with the :ref:`xmlelem-plcScaling` element;
| Analog value substitution with the :ref:`xmlelem-plcSubstitution` element.

Please see sample :ref:`xmlgroup-plcConditionTable` group below.
There are 5 conditions defined with 2 :ref:`xmlelem-plcRange`, 1 :ref:`xmlelem-plcScaling` and 2 :ref:`xmlelem-plcSubstitution` elements.

.. code-block:: none

 <ConditionTable>
   <Range CondId="1" OnMin="0" OnMax="10e4" OffMin="-5" OffMax="-inf"/>
   <Range CondId="2" OnMin="100" OnMax="200"/>
   <Scaling CondId="3" Min="-5" Max="11e6" Offset="1.1" Coeff="14"/>
   <Substitution CondId="4" Min="-5" Max="11e6" Values="1.1 -4e-5" Result="14" NextCondId="5"/>
   <Substitution CondId="5" Min="0" Max="200" Values="3,4,5" Result="0"/>
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

   <Range CondId="1" OnMin="0" OnMax="10e4" OffMin="-5" OffMax="-99999.9" Name="AI to DI conversion"/>

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

.. include-file:: sections/Include/Name_wodef.rstinc ""


.. _xmlelem-plcScaling: lelabel=Scaling

Scaling element
---------------

| :ref:`xmlelem-plcScaling` element is used to change (multiply, offset) analog values.
  Whenever received analog value falls within a defined range it will be scaled based on specified atributes.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-plcScaling`"

.. code-block:: none

   <Substitution CondId="2" Min="-5" Max="11e6" Offset="5" Coeff="1.1" NextCondId="3" Name="AI/AO value scaling"/>

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-plcScaling`"

Scaling attributes
^^^^^^^^^^^^^^^^^^

.. field-list-table:: Scaling attributes
   :class: table table-condensed table-bordered longtable
   :name: tabid-plcScaling
   :spec: |C{0.16}|C{0.12}|S{0.72}|
   :header-rows: 1

   * :attr,10,center:	Attribute
     :val,15,center:	Values or range
     :desc,75:		Description

   * :attr:	:xmlattr:`CondId`
     :val:	1...65535
     :desc:	Condition identifier must be a unique number within a :ref:`xmlgroup-plcConditionTable` group.
		:inlineimportant:`Identifier numbering must start with 1 and identifiers must be arranged in an ascending order.`

.. include-file:: sections/Include/plc_cond_scale.rstinc "" ":xmlattr:`Min`" "Minimal"

.. include-file:: sections/Include/plc_cond_scale.rstinc "" ":xmlattr:`Max`" "Maximal"

   * :attr:	:xmlattr:`Offset`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`
     :desc:	Add value of this attribute to a PLC point or command.
		This attribute has a higher priority (applied before) :ref:`xmlattr-plcScalingCoeff` attribute.
		|optinalattr|

   * :attr:	:xmlattr:`Coeff`
     :val:	±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`
     :desc:	Multiply PLC point or command by the value of this attribute.
		This attribute has a lower priority (applied after) :ref:`xmlattr-plcScalingOffset` attribute.
		|optinalattr|

.. include-file:: sections/Include/plc_nextcond.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. _xmlelem-plcSubstitution: lelabel=Substitution

Substitution element
--------------------

| :ref:`xmlelem-plcSubstitution` element is used to substitute particular analog values with one specified value.
  Whenever received analog value falls within a defined range or matches one of the listed values, it will be substituted with a specified value.
  This functionality could be used to replace values that exceed a certain limit, for example, if a received value exceeds 100,
  :ref:`xmlelem-plcSubstitution` element can used to replace it with 100, so that the resulting value never exceeds 100.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-plcSubstitution`"

.. code-block:: none

   <Substitution CondId="2" Min="-5" Max="11e6" Values="1 -5.47 7e12 0.004" Result="14" NextCondId="3" Name="AI/AO value substitution"/>

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-plcSubstitution`"

Substitution attributes
^^^^^^^^^^^^^^^^^^^^^^^


.. field-list-table:: Substitution attributes
   :class: table table-condensed table-bordered longtable
   :name: tabid-plcSubstitution
   :spec: |C{0.16}|C{0.12}|S{0.72}|
   :header-rows: 1

   * :attr,10,center:	Attribute
     :val,15,center:	Values or range
     :desc,75:		Description

   * :attr:	:xmlattr:`CondId`
     :val:	1...65535
     :desc:	Condition identifier must be a unique number within a :ref:`xmlgroup-plcConditionTable` group.
		:inlineimportant:`Identifier numbering must start with 1 and identifiers must be arranged in an ascending order.`

.. include-file:: sections/Include/plc_cond_subst.rstinc "" ":xmlattr:`Min`" "Minimal"

.. include-file:: sections/Include/plc_cond_subst.rstinc "" ":xmlattr:`Max`" "Maximal"

   * :attr:	:xmlattr:`Values`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38` (up to 16)
     :desc:	Match any analog value specified in this list.
		The resulting value of a PLC point :ref:`xmlelem-plcPNT` or PLC command :ref:`xmlelem-plcCMD` will be substituted by the :ref:`xmlattr-plcSubstitutionResult` value
		whenever the source AI/AO value matches any of the values specified in this attibute.
		Up to 16 postive/negative floating point numbers in a standard decimal (1204.78) or scientific (3.5e3) notation can be specified separated by whitespaces or commas e.g. "1,-5.47,7e12,0.004".
		Note, received AI/AO values are compared to this attribute after scaling in the originating protocol instance is applied
		(e.g. coefficient in source Master instance in case of an AI and Slave instance in case of an AO)
		|optinalattr|

   * :attr:	:xmlattr:`Result`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`
     :desc:	Substitution value for the PLC point :ref:`xmlelem-plcPNT` or PLC command :ref:`xmlelem-plcCMD`.
		Value specified in this attribute will be used whenever received analog value falls within a range between :ref:`xmlattr-plcSubstitutionMin` and :ref:`xmlattr-plcSubstitutionMax` attributes or
		matches one of the :ref:`xmlattr-plcSubstitutionValues` attribute.
		:inlineimportant:`Positive and negative infinity values 'inf' and '-inf' must not be specified.`

.. include-file:: sections/Include/plc_nextcond.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""
