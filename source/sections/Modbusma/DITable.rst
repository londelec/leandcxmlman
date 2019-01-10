
.. _ref-ModbusmaDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-ModbusmaDI>` and child element nodes :ref:`DI<ref-ModbusmaDI>` are used to create information objects to receive status information from outstation.
Each created DI can be used as a source for any DI information object defined in the IO table of any Slave protocol instance.
Data received from outstation will be forwarded to the DI information object of the Slave protocol instance and then to the upstream Master station.
Please refer to the section :ref:`docref-IEC10xslDITable` for more information on how to use DI information object as a source.

.. tip:: \ :ref:`DITable<ref-ModbusmaDI>` group and :ref:`DI<ref-ModbusmaDI>` nodes are optional if :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` is used. DI information objects are initialized automatically for hardcoded devices.

Please see sample :ref:`DITable<ref-ModbusmaDI>` group and :ref:`DI<ref-ModbusmaDI>` child element nodes below.
There are 5 DI information objects configured using 4 :ref:`DI<ref-ModbusmaDI>` element nodes.

.. code-block:: none

   <DITable>
	<DI Index="0" PollMsg="1" BitOffset="0" Type="1" />
	<DI Index="1" PollMsg="1" BitOffset="1" Type="1" />
	<DI Index="2" PollMsg="1" BitOffset="2" Type="1" Qualifier="0x01"/>
	<DI Index="3" PollMsg="1" BitOffset="4" Type="1" Total="2"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DI<ref-ModbusmaDI>`"

.. code-block:: none

   <DI Index="0" PollMsg="1" BitOffset="0" Type="1" Qualifier="0" ChatterFilter="100" Total="1" Name="Input 1" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`DI<ref-ModbusmaDI>`"

DI attributes
^^^^^^^^^^^^^

.. _docref-ModbusmaDIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master DI attributes" ":spec: |C{0.14}|C{0.14}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-ModbusmaDIIndex:" "DI"

   * :attr:     .. _ref-ModbusmaDIPollMsg:

                :xmlref:`PollMsg`
     :val:      1...65534
     :def:      0
     :desc:     Identifier of the message that is used to poll data from outstation.
		Use value of the :ref:`MSG<ref-PollMessages>`.\ :ref:`<ref-PollMsgId>` attribute.
		Value 0 means no poll message is selected.
		:inlineimportant:`Attribute is optional only if` :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` :inlineimportant:`is used.`

   * :attr:     .. _ref-ModbusmaDIBitOffset:

                :xmlref:`BitOffset`
     :val:      0...1023 or 0x00...0x3FF
     :def:      0
     :desc:     Offset of the bit that carries status information.
		See table :numref:`docref-ModbusmaBitOffsetTab` for examples of offset values.
		:inlineimportant:`Attribute is optional only if` :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` :inlineimportant:`is used.`

   * :attr:     .. _ref-ModbusmaDIType:

                :xmlref:`Type`
     :val:      See table :numref:`docref-ModbusDITypeTab`
     :def:      1
     :desc:     Select format of the received data.
		:inlineimportant:`Attribute is optional only if` :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` :inlineimportant:`is used.`

   * :attr:     .. _ref-ModbusmaDIQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`docref-ModbusmaDIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-ModbusmaDIChatterFilter:

                :xmlref:`ChatterFilter`
     :val:      1...65535
     :def:      50 msec
     :desc:     Chatter filter in milliseconds for Digital Inputs.
		State change of the digital input will be reported only if remains stable for the period that exceeds configured filter.
		:inlinetip:`This attribute applies only to LEIODC series units.`

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-ModbusmaDITotal:" ":ref:`<ref-ModbusmaDIIndex>` and :ref:`<ref-ModbusmaDIBitOffset>`" ":ref:`DI<ref-ModbusmaDI>`" "254"

.. include-file:: sections/Include/Name.rstinc ""

DI.Qualifier
^^^^^^^^^^^^

.. _docref-ModbusmaDIqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Modbus Master DI internal qualifier" ":ref:`<ref-ModbusmaDIQualifier>`" "DI internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DI object **will not** be inverted (ON = 1; OFF = 0)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DI object **will** be inverted (ON = 0; OFF = 1)

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DI is **enabled** and will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DI is **disabled** and will be discarded when received

   * :attr:     Bits 1..6
     :val:      Any
     :desc:     Bits reserved for future use


DI.Type
^^^^^^^

.. _docref-ModbusDITypeTab:

.. field-list-table:: Modbus Master DI decode types
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.10}|S{0.90}|
   :header-rows: 1

   * :val,10:   Type value
     :desc,90:  Description

   * :val:	0
     :desc:	Not used

   * :val:	1
     :desc:	Select one bit from the received data based on :ref:`<ref-ModbusmaDIBitOffset>` attribute.
		See table :numref:`docref-ModbusmaBitOffsetTab` for examples of offset values.

   * :val:	Other
     :desc:	Not used


Table below shows the selected bit '\ **B**\' based on the :ref:`DI<ref-ModbusmaDI>`.\ :ref:`<ref-ModbusmaDIBitOffset>` or :ref:`DO<ref-ModbusmaDO>`.\ :ref:`<ref-ModbusmaDOBitOffset>` value.
The sample has 4 bytes of data in the order as it would be received from or sent to outstation.
Each byte is shown as 'xxxx.xxxx' where 'x' represents one bit of the byte.

.. _docref-ModbusmaBitOffsetTab:

.. field-list-table:: Modbus Master Bit Offset sample values
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.10}|S{0.90}|
   :header-rows: 1

   * :val,10:   BitOffset
     :desc,90:  Modbus Message

   * :val:      0
     :desc:     {... xxxx.xxxx xxxx.xxx\ **B** xxxx.xxxx xxxx.xxxx ...}

   * :val:      1
     :desc:     {... xxxx.xxxx xxxx.xx\ **B**\x xxxx.xxxx xxxx.xxxx ...}

   * :val:      2
     :desc:     {... xxxx.xxxx xxxx.x\ **B**\xx xxxx.xxxx xxxx.xxxx ...}

   * :val:      3
     :desc:     {... xxxx.xxxx xxxx.\ **B**\xxx xxxx.xxxx xxxx.xxxx ...}

   * :val:      4
     :desc:     {... xxxx.xxxx xxx\ **B**\.xxxx xxxx.xxxx xxxx.xxxx ...}

   * :val:      8
     :desc:     {... xxxx.xxx\ **B** xxxx.xxxx xxxx.xxxx xxxx.xxxx ...}

   * :val:      16
     :desc:     {... xxxx.xxxx xxxx.xxxx xxxx.xxxx xxxx.xxx\ **B** ...}

   * :val:      24
     :desc:     {... xxxx.xxxx xxxx.xxxx xxxx.xxx\ **B** xxxx.xxxx ...}

   * :val:      31
     :desc:     {... xxxx.xxxx xxxx.xxxx **B**\xxx.xxxx xxxx.xxxx ...}

