
.. _ref-ModbusmaAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-ModbusmaAI>` and child element nodes :ref:`AI<ref-ModbusmaAI>` are used to create AI information objects to receive analog information from outstation.
Each created AI can be used as a source for any AI information object defined in the IO table of any Slave protocol instance.
Analog data received from outstation will be forwarded to the AI information object of the Slave protocol instance and then to the upstream Master station.
Please refer to the section :ref:`docref-IEC10xslAITable` for more information on how to use AI information object as a source.

.. tip:: \ :ref:`AITable<ref-ModbusmaAI>` group and :ref:`AI<ref-ModbusmaAI>` nodes are optional if :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` is used. AI information objects are initialized automatically for hardcoded devices.

Please see sample :ref:`AITable<ref-ModbusmaAI>` group and :ref:`AI<ref-ModbusmaAI>` child element nodes below.
There are 5 AI information objects configured using 4 :ref:`AI<ref-ModbusmaAI>` element nodes.

.. code-block:: none

   <AITable>
	<AI Index="0" PollMsg="1" RegOffset="0" Type="33" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" PollMsg="1" RegOffset="1" Type="33" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" PollMsg="1" RegOffset="2" Type="65" Coeff="-17.0" Percent="1.4"/>
	<AI Index="3" PollMsg="1" RegOffset="4" Type="33" Coeff="0.08" Total="2"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AI<ref-ModbusmaAI>`"

.. code-block:: none

   <AI Index="0" PollMsg="1" RegOffset="0" Type="33" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" Total="1" Name="Voltage" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`AI<ref-ModbusmaAI>`"

AI attributes
^^^^^^^^^^^^^

.. _docref-ModbusmaAIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master AI attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-ModbusmaAIIndex:" "AI"

   * :attr:     .. _ref-ModbusmaAIPollMsg:

                :xmlref:`PollMsg`
     :val:      1...65534
     :def:      0
     :desc:     Identifier of the message that is used to poll data from outstation.
		Use value of the :ref:`MSG<ref-PollMessages>`.\ :ref:`<ref-PollMsgId>` attribute.
		Value 0 means no poll message is selected.
		:inlineimportant:`Attribute is optional only if` :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` :inlineimportant:`is used.`

   * :attr:     .. _ref-ModbusmaAIRegOffset:

                :xmlref:`RegOffset`
     :val:      0...63 or 0x00...0x3F
     :def:      0
     :desc:     Offset of the register to read the analog information from.
		See table :numref:`docref-ModbusmaRegOffsetTab` for examples of offset values.
		:inlineimportant:`Attribute is optional only if` :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` :inlineimportant:`is used.`

   * :attr:     .. _ref-ModbusmaAIType:

                :xmlref:`Type`
     :val:      See table :numref:`docref-ModbusAITypeTab`
     :def:      33
     :desc:     Select format of the received data.
		:inlineimportant:`Attribute is optional only if` :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` :inlineimportant:`is used.`

   * :attr:     .. _ref-ModbusmaAIQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`docref-ModbusmaAIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/AI_Coeff.rstinc "" ".. _ref-ModbusmaAICoeff:"

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ".. _ref-ModbusmaAIDeadband:" ".. _ref-ModbusmaAIPercent:"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ".. _ref-ModbusmaAIStartOffset:" ".. _ref-ModbusmaAIZeroDeadband:" ".. _ref-ModbusmaAIOffset:" ".. _ref-ModbusmaAIOffsetDeadband:" ".. _ref-ModbusmaAINonZeroOffset:"

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-ModbusmaAITotal:" ":ref:`<ref-ModbusmaAIIndex>` and :ref:`<ref-ModbusmaAIRegOffset>`" ":ref:`AI<ref-ModbusmaAI>`" "254"

.. include-file:: sections/Include/Name.rstinc ""

.. tip::

   \* Please refer to annex :ref:`docref-ReceivedAIProcessing` for additional information on AI processing
   options and application examples using :ref:`<ref-ModbusmaAIDeadband>` \ and :ref:`<ref-ModbusmaAIPercent>` \ attributes.
   Annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` for additional information on AI scaling.


AI.Qualifier
^^^^^^^^^^^^

.. _docref-ModbusmaAIqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Modbus Master AI internal qualifier" ":ref:`<ref-ModbusmaAIQualifier>`" "AI internal qualifier"

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     AI is **enabled** and will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     AI is **disabled** and will be discarded when received

   * :attr:     Bits 0..6
     :val:      Any
     :desc:     Bits reserved for future use


AI.Type
^^^^^^^

.. _docref-ModbusAITypeTab:

.. field-list-table:: Modbus Master AI decode types
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.10}|S{0.90}|
   :header-rows: 1

   * :val,10:   Type value
     :desc,90:  Description

   * :val:	0
     :desc:	Not used

   * :val:      33
     :desc:     Decode data as 16bit Unsigned Integer big endian.
		For example received Modbus data {01 04 ... **FF 11** ...} will be decoded as '65297'

   * :val:      34
     :desc:     Decode data as 16bit Signed Integer big endian.
		For example received Modbus data {01 04 ... **FF 11** ...} will be decoded as '-239'

   * :val:      35
     :desc:     Decode data as 16bit Unsigned Integer little endian.
		For example received Modbus data {01 04 ... **11 FF** ...} will be decoded as '65297'

   * :val:      36
     :desc:     Decode data as 16bit Signed Integer little endian.
		For example received Modbus data {01 04 ... **11 FF** ...} will be decoded as '-239'

   * :val:      65
     :desc:     Decode data as Short floating point number byte order [3210].
		For example received Modbus data {01 04 ... **40 00 10 80** ...} will be decoded as '2.001007'

   * :val:      66
     :desc:     Decode data as Short floating point number byte order [1032].
		For example received Modbus data {01 04 ... **10 80 40 00** ...} will be decoded as '2.001007'

   * :val:      67
     :desc:     Decode data as Short floating point number byte order [2301].
		For example received Modbus data {01 04 ... **00 40 80 10** ...} will be decoded as '2.001007'

   * :val:      68
     :desc:     Decode data as Short floating point number byte order [0123].
		For example received Modbus data {01 04 ... **80 10 00 40** ...} will be decoded as '2.001007'

   * :val:	Other
     :desc:	Not used


Table below shows position of a sample value '341' (0x0155) in a Modbus message and the :ref:`<ref-ModbusmaAIRegOffset>` required to read this value.

.. _docref-ModbusmaRegOffsetTab:

.. field-list-table:: Modbus Master Register Offset sample values
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.10}|S{0.90}|
   :header-rows: 1

   * :val,10:   RegOffset
     :desc,90:  Modbus Message

   * :val:      0
     :desc:     {01 04 ... **01 55** 00 00 ...}

   * :val:      1
     :desc:     {01 04 ... 00 00 **01 55** ...}

