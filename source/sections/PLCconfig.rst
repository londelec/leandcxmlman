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
     :val:	or / and / add / mult
     :desc:	Logic or arithmetic operation of the data point.
		This operation will be perfomed on a source data values and the result of the operation will become value of the internal data point.
		See :numref:`tabid-PlcType` for more information.

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
		Normally multiple data sources are required in order to perform a logic or artithmetic operation, therefore multiple object types can be specified in this attribute.
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
	For example if 2 DI information objects are used as an internal data point sources, each of these attributes must have 2 parameters e.g.
	:ref:`xmlattr-plcPNTSrcDevices`\ ="10,10"; :ref:`xmlattr-plcPNTSrcIndexes`\ ="0,1"; :ref:`xmlattr-plcPNTSrcTypes`\ ="DI,AI" and :ref:`xmlattr-plcPNTCondIds`\ ="0,1".

PLC operation types
^^^^^^^^^^^^^^^^^^^

| There are 4 types of logic and arithmetic operations that can be performed on a DI/AI data received from outstation.
  These are summarized in the table below.


.. field-list-table:: PLC logic or arithmetic operations
   :class: table table-condensed table-bordered longtable
   :name: tabid-PlcType
   :spec: |C{0.16}|S{0.84}|
   :header-rows: 1

   * :attr,10,center:	:ref:`xmlattr-plcPNTPlcType`
     :desc,90:		Description

   * :attr:	or
     :desc:	| Perform logic OR operation based on a DI object state position.
		  DI object can have 4 states - INTER; OFF; ON; INVALID but only ON and OFF (distinctive position) states are used to perform a PLC operation.
		  If state of any of the source DI objects is INTER or INVALID the PLC data point will also have an INTER or INVALID state.
		  Quality bits of all source DI objects are added together meaning that if any of the source DI objects have [:lemonobgtext:`IV`] bit set or
		  outstation (where DI is received from) goes offline, the resulting PLC data point will also have [:lemonobgtext:`IV`] bit.
		  The PLC data point is valid only if all source DI objects are valid.
		  There are at least 2 source DI objects required to perform a logic OR operation.
		  The resulting state of the PLC data point based on the distinctive position states (ON or OFF) of the 2 source DI objects is shown below:
		| DI1 DI2 => PLC point:
		| OFF OFF => OFF
		| ON OFF => ON
		| OFF ON => ON
		| ON ON => ON

   * :attr:	and
     :desc:	| Perform logic AND operation based on a DI object state position.
		  DI object can have 4 states - INTER; OFF; ON; INVALID but only ON and OFF (distinctive position) states are used to perform a PLC operation.
		  If state of any of the source DI objects is INTER or INVALID the PLC data point will also have an INTER or INVALID state.
		  Quality bits of all source DI objects are added together meaning that if any of the source DI objects have [:lemonobgtext:`IV`] bit set or
		  outstation (where DI is received from) goes offline, the resulting PLC data point will also have [:lemonobgtext:`IV`] bit.
		  The PLC data point is valid only if all source DI objects are valid.
		  There are at least 2 source DI objects required to perform a logic AND operation.
		  The resulting state of the PLC data point based on the distinctive position states (ON or OFF) of the 2 source DI objects is shown below:
		| DI1 DI2 => PLC point:
		| OFF OFF => OFF
		| ON OFF => OFF
		| OFF ON => OFF
		| ON ON => ON

   * :attr:	add
     :desc:	Addition of AI object values.
		2 or more AI values received from oustation can be added together and the sum will become value of the PLC data point.
		Quality bits of all source AI objects are added together meaning that if any of the source AI objects have [:lemonobgtext:`IV`] bit set or
		outstation (where AI is received from) goes offline, the resulting PLC data point will also have [:lemonobgtext:`IV`] bit.
		The PLC data point is valid only if all source AI objects are valid.
		Addition takes place after AI value scaling i.e. after coefficient (if any) specified in the source protocol instance is applied.

   * :attr:	mult
     :desc:	Multiplication of AI object values.
		2 or more AI values received from oustation can be multiplied together and the product will become value of the PLC data point.
		Quality bits of all source AI objects are added together meaning that if any of the source AI objects have [:lemonobgtext:`IV`] bit set or
		outstation (where AI is received from) goes offline, the resulting PLC data point will also have [:lemonobgtext:`IV`] bit.
		The PLC data point is valid only if all source AI objects are valid.
		Multiplication takes place after AI value scaling i.e. after coefficient (if any) specified in the source protocol instance is applied.


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


.. _xmlgroup-plcConditionTable: lelabel=ConditionTable

ConditionTable group
--------------------

| :ref:`xmlgroup-plcConditionTable` group is used to define conditions for analog values of the AI objects that are used as internal data point sources.
  There are 2 condition types available at the moment - the range of analog values defined using the :ref:`xmlelem-plcRange` element and
  AI value substitution with :ref:`xmlelem-plcSubstitution` element.

Please see sample :ref:`xmlgroup-plcConditionTable` group below.
There are 4 conditions defined with 2 :ref:`xmlelem-plcRange` and 2 :ref:`xmlelem-plcSubstitution` elements.

.. code-block:: none

 <ConditionTable>
   <Range CondId="1" OnMin="0" OnMax="10e4" OffMin="-5" OffMax="-inf"/>
   <Range CondId="2" OnMin="100" OnMax="200"/>
   <Substitution CondId="3" Min="-5" Max="11e6" Values="1.1 -4e-5" Result="14"/>
   <Substitution CondId="4" Min="0" Max="200" Values="3,4,5" Result="0"/>
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


.. _xmlelem-plcSubstitution: lelabel=Substitution

Substitution element
--------------------

| :ref:`xmlelem-plcSubstitution` element is used to substitute particular analog values with one specified value.
  Whenever received analog value falls within a defined range or matches one of the listed values, it will be substituted with a specified value.
  This functionality could be used to replace values that exceed a certain limit, for example, if a received value exceeds 100,
  :ref:`xmlelem-plcSubstitution` element can used to replace it with 100, so that the resulting value never exceeds 100.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-plcSubstitution`"

.. code-block:: none

   <Substitution CondId="2" Min="-5" Max="11e6" Values="1 -5.47 7e12 0.004" Result="14" Name="AI value substitution"/>

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

   * :attr:	:xmlattr:`Min`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`
     :desc:	Minimal (inclusive) analog value that will result in AI value substitution.
		Internal point :ref:`xmlelem-plcPNT` that uses AI as a data source will have :ref:`xmlattr-plcSubstitutionResult` value whenever received analog value is equal or exceeds this attribute and
		is less or equal to :ref:`xmlattr-plcSubstitutionMax` attribute.
		Positive and negative infinity values 'inf' and '-inf' can be specified.
		Note received AI value is compared to this attribute after scaling (e.g. when any coefficient in master instance is applied)
		|optinalattr|

   * :attr:	:xmlattr:`Max`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`
     :desc:	Maximal (inclusive) analog value that will result in AI value substitution.
		Internal point :ref:`xmlelem-plcPNT` that uses AI as a data source will have :ref:`xmlattr-plcSubstitutionResult` value whenever received analog value is less or equal to this attribute and
		is equal or exceeds :ref:`xmlattr-plcSubstitutionMin` attribute.
		Positive and negative infinity values 'inf' and '-inf' can be specified.
		Note received AI value is compared to this attribute after scaling (e.g. when any coefficient in master instance is applied)
		|optinalattr|

   * :attr:	:xmlattr:`Values`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38` (up to 16)
     :desc:	Match any analog value specified in this list.
		Internal point :ref:`xmlelem-plcPNT` that uses AI as a data source will have :ref:`xmlattr-plcSubstitutionResult` value whenever received analog value matches any of the values specified in this attibute.
		Up to 16 postive/negative floating point numbers in a standard decimal (1204.78) or scientific (3.5e3) notation can be specified separated by whitespaces or commas e.g. "1,-5.47,7e12,0.004".
		Note received AI value is compared to this attribute after scaling (e.g. when any coefficient in master instance is applied)
		|optinalattr|

   * :attr:	:xmlattr:`Result`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`
     :desc:	Substitution value for the internal point :ref:`xmlelem-plcPNT`.
		Value specified in this attribute will be used whenever received analog value falls within a range between :ref:`xmlattr-plcSubstitutionMin` and :ref:`xmlattr-plcSubstitutionMax` attributes or
		matches one of the :ref:`xmlattr-plcSubstitutionValues` attribute.
		:inlineimportant:`Positive and negative infinity values 'inf' and '-inf' must not be specified.`

.. include-file:: sections/Include/Name_wodef.rstinc ""
