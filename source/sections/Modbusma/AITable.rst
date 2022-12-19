
.. _xmlgroup-ModbusmaAI: lelabel=AITable
.. _xmlelem-ModbusmaAI: lelabel=AI

AITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-ModbusmaAI`" ":ref:`xmlelem-ModbusmaAI`" ":numref:`tabid-ModbusmaAI`" ":ref:`docref-IEC10xslAI`" "AI" "analog information" "outstation"

.. tip:: \ :ref:`xmlgroup-ModbusmaAI` group and :ref:`xmlelem-ModbusmaAI` nodes are optional if :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` is used. AI information objects are initialized automatically for hardcoded devices.

Please see sample :ref:`xmlgroup-ModbusmaAI` group and :ref:`xmlelem-ModbusmaAI` element nodes below.
There are 5 analog information objects defined with 4 :ref:`xmlelem-ModbusmaAI` element nodes.

.. code-block:: none

   <AITable>
	<AI Index="0" PollMsg="1" RegOffset="0" Type="33" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" PollMsg="1" RegOffset="1" Type="33" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" PollMsg="1" RegOffset="2" Type="65" Coeff="-17.0" Percent="1.4"/>
	<AI Index="3" PollMsg="1" RegOffset="4" Type="33" Coeff="0.08" Total="2"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaAI`"

.. code-block:: none

   <AI Index="0" PollMsg="1" RegOffset="0" Type="33" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" Total="1" Name="Voltage" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-ModbusmaAI`"

AI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaAI" "Modbus Master AI attributes" ":spec: |C{0.18}|C{0.16}|C{0.1}|S{0.56}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "AI"

.. include-file:: sections/Include/Modbusma_PollMsg.rstinc ""

   * :attr:	:xmlattr:`RegOffset`
     :val:	0...63 or 0x00...0x3F
     :def:	0
     :desc:	Offset of the register to read the analog information from.
		See :numref:`tabid-ModbusmaRegOffset` for examples of offset values.
		:inlineimportant:`Attribute is optional only if` :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` :inlineimportant:`is used.`

   * :attr:	:xmlattr:`Type`
     :val:	See :numref:`tabid-ModbusAIType`
     :def:	33
     :desc:	Select format of the received data.
		:inlineimportant:`Attribute is optional only if` :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` :inlineimportant:`is used.`

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-ModbusmaAIQualifier`"

.. include-file:: sections/Include/AI_Coeff.rstinc ""

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ":ref:`xmlattr-ModbusmaAIDeadband`" ":ref:`xmlattr-ModbusmaAIPercent`" ":ref:`xmlelem-ModbusmaApp`.\ :ref:`xmlattr-ModbusmaAppAIDeadband`" ":ref:`xmlelem-ModbusmaApp`.\ :ref:`xmlattr-ModbusmaAppAIPercent`"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ":ref:`xmlattr-ModbusmaAIStartOffset`" ":ref:`xmlattr-ModbusmaAIZeroDeadband`" ":ref:`xmlattr-ModbusmaAIOffset`" ":ref:`xmlattr-ModbusmaAIOffsetDeadband`" ":ref:`xmlattr-ModbusmaAINonZeroOffset`"

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-ModbusmaAIIndex` and :ref:`xmlattr-ModbusmaAIRegOffset`" ":ref:`xmlelem-ModbusmaAI`" "254"

.. include-file:: sections/Include/Name.rstinc ""

.. include-file:: sections/Include/ma_AI_Annex.rstinc "" ":ref:`xmlattr-ModbusmaAIDeadband`" ":ref:`xmlattr-ModbusmaAIPercent`"

AI.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-ModbusmaAIQualifier" "Modbus Master AI internal qualifier" ":ref:`xmlattr-ModbusmaAIQualifier`" "AI internal qualifier"

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	**Deocode** maximal integer value normally based on the selected :ref:`xmlelem-ModbusmaAI`.\ :ref:`xmlattr-ModbusmaAIType`.

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	| **Substitute** maximal integer value received from outstation with 0.
		| Maximal integer value (to be substituted with 0) depends on the selected :ref:`xmlattr-ModbusmaAIType`:
		| 65536 (0xFFFF) for 16bit Unsigned Integer :ref:`xmlattr-ModbusmaAIType`\ ="33,35" 
		| 32767 (0x7FFF) for 16bit Signed Integer :ref:`xmlattr-ModbusmaAIType`\ ="34,36" 
		| 4294967295 (0xFFFFFFFF) for 32bit Unsigned Integer :ref:`xmlattr-ModbusmaAIType`\ ="37,39,41,43" 
		| 2147483647 (0x7FFFFFFF) for 32bit Signed Integer :ref:`xmlattr-ModbusmaAIType`\ ="38,40,42,44" 

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	**Deocode** minimal integer value normally based on the selected :ref:`xmlelem-ModbusmaAI`.\ :ref:`xmlattr-ModbusmaAIType`.

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	| **Substitute** minimal integer value received from outstation with 0. This applies only to Signed Integers.
		| Minimal integer value (to be substituted with 0) depends on the selected :ref:`xmlattr-ModbusmaAIType`:
		| -32768 (0x8000) for 16bit Signed Integer :ref:`xmlattr-ModbusmaAIType`\ ="34,36" 
		| -2147483648 (0x80000000) for 32bit Signed Integer :ref:`xmlattr-ModbusmaAIType`\ ="38,40,42,44" 

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	AI is **enabled** and will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AI is **disabled** and will be discarded when received

   * :attr:	Bits 0,3..6
     :val:	Any
     :desc:	Bits reserved for future use


AI.Type
^^^^^^^

.. field-list-table:: Modbus Master AI decode types
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusAIType
   :spec: |C{0.07}|S{0.93}|
   :header-rows: 1

   * :val,10,center:	:ref:`xmlattr-ModbusmaAIType`
     :desc,90:		Description

   * :val:	0
     :desc:	Not used

   * :val:	33
     :desc:	Decode data as 16bit Unsigned Integer big endian.
		For example received Modbus data {01 04 ... **FF 11** ...} will be decoded as '65297'

   * :val:	34
     :desc:	Decode data as 16bit Signed Integer big endian.
		For example received Modbus data {01 04 ... **FF 11** ...} will be decoded as '-239'

   * :val:	35
     :desc:	Decode data as 16bit Unsigned Integer little endian.
		For example received Modbus data {01 04 ... **11 FF** ...} will be decoded as '65297'

   * :val:	36
     :desc:	Decode data as 16bit Signed Integer little endian.
		For example received Modbus data {01 04 ... **11 FF** ...} will be decoded as '-239'

   * :val:	37
     :desc:	Decode data as 32bit Unsigned Integer byte order [3210].
		For example received Modbus data {01 04 ... **00 01 00 05** ...} will be decoded as '65541'

   * :val:	38
     :desc:	Decode data as 32bit Signed Integer byte order [3210].
		For example received Modbus data {01 04 ... **FF FF 01 05** ...} will be decoded as '-65275'

   * :val:	39
     :desc:	Decode data as 32bit Unsigned Integer byte order [1032].
		For example received Modbus data {01 04 ... **00 01 00 05** ...} will be decoded as '327681'

   * :val:	40
     :desc:	Decode data as 32bit Signed Integer byte order [1032].
		For example received Modbus data {01 04 ... **01 05 FF FF** ...} will be decoded as '-65275'

   * :val:	41
     :desc:	Decode data as 32bit Unsigned Integer byte order [2301].
		For example received Modbus data {01 04 ... **00 01 00 05** ...} will be decoded as '16778496'

   * :val:	42
     :desc:	Decode data as 32bit Signed Integer byte order [2301].
		For example received Modbus data {01 04 ... **FF FF 01 05** ...} will be decoded as '-64255'

   * :val:	43
     :desc:	Decode data as 32bit Unsigned Integer byte order [0123].
		For example received Modbus data {01 04 ... **00 01 00 05** ...} will be decoded as '83886336'

   * :val:	44
     :desc:	Decode data as 32bit Signed Integer byte order [0123].
		For example received Modbus data {01 04 ... **01 05 FF FF** ...} will be decoded as '-64255'

   * :val:	65
     :desc:	Decode data as Short floating point number byte order [3210].
		For example received Modbus data {01 04 ... **40 00 10 80** ...} will be decoded as '2.001007'

   * :val:	66
     :desc:	Decode data as Short floating point number byte order [1032].
		For example received Modbus data {01 04 ... **10 80 40 00** ...} will be decoded as '2.001007'

   * :val:	67
     :desc:	Decode data as Short floating point number byte order [2301].
		For example received Modbus data {01 04 ... **00 40 80 10** ...} will be decoded as '2.001007'

   * :val:	68
     :desc:	Decode data as Short floating point number byte order [0123].
		For example received Modbus data {01 04 ... **80 10 00 40** ...} will be decoded as '2.001007'

   * :val:	97
     :desc:	Decode data as 16bit Binary Coded Decimal (BCD) big endian.
		For example received Modbus data {01 04 ... **12 34** ...} will be decoded as '1234'

   * :val:	98
     :desc:	Decode data as 16bit Binary Coded Decimal (BCD) little endian.
		For example received Modbus data {01 04 ... **12 34** ...} will be decoded as '3412'

   * :val:	Other
     :desc:	Not used


Table below shows position of a sample value '341' (0x0155) in a Modbus message and the :ref:`xmlattr-ModbusmaAIRegOffset` required to read this value.

.. field-list-table:: Modbus Master Register Offset sample values
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusmaRegOffset
   :spec: |C{0.12}|S{0.5}|
   :header-rows: 1

   * :val,10,center:	:ref:`xmlattr-ModbusmaAIRegOffset`
     :desc,90:		Modbus Message

   * :val:	0
     :desc:	{01 04 ... **01 55** 00 00 ...}

   * :val:	1
     :desc:	{01 04 ... 00 00 **01 55** ...}

