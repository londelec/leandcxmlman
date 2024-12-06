
.. _xmlgroup-ModbusmaDI: lelabel=DITable
.. _xmlelem-ModbusmaDI: lelabel=DI

DITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-ModbusmaDI`" ":ref:`xmlelem-ModbusmaDI`" ":numref:`tabid-ModbusmaDI`" ":ref:`docref-IEC10xslDI`" "DI" "status information" "outstation"

.. tip:: \ :ref:`xmlgroup-ModbusmaDI` group and :ref:`xmlelem-ModbusmaDI` nodes are optional if :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` is used. DI information objects are initialized automatically for hardcoded devices.

Please see sample :ref:`xmlgroup-ModbusmaDI` group and :ref:`xmlelem-ModbusmaDI` element nodes below.
There are 5 status information objects defined with 4 :ref:`xmlelem-ModbusmaDI` element nodes.

.. code-block:: none

   <DITable>
	<DI Index="0" PollMsg="1" BitOffset="0" Type="1" />
	<DI Index="1" PollMsg="1" BitOffset="1" Type="1" />
	<DI Index="2" PollMsg="1" BitOffset="2" Type="1" Qualifier="0x01"/>
	<DI Index="3" PollMsg="1" BitOffset="4" Type="1" Total="2"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaDI`"

.. code-block:: none

   <DI Index="0" PollMsg="1" BitOffset="0" Type="1" Qualifier="0" ChatterFilter="100" OnValues="0x01 0x02" OffValues="5,6" OnDelay="0" OffDelay="0" AndMask="0" OrMask="0" Total="1" Name="Input 1" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-ModbusmaDI`"

DI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaDI" "Modbus Master DI attributes" ":spec: |C{0.14}|C{0.14}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DI"

.. include-file:: sections/Include/Modbusma_PollMsg.rstinc ""

   * :attr:	:xmlattr:`BitOffset`
     :val:	0...1023 or 0x00...0x3FF
     :def:	0
     :desc:	Offset of the bit that carries status information.
		See :numref:`tabid-ModbusmaBitOffset` for examples of offset values.
		:inlineimportant:`Attribute is optional only if` :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` :inlineimportant:`is used.`

   * :attr:	:xmlattr:`Type`
     :val:	See :numref:`tabid-ModbusDIType`
     :def:	1
     :desc:	Select format of the received data.
		:inlineimportant:`Attribute is optional only if` :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` :inlineimportant:`is used.`

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-ModbusmaDIQualifier`"

   * :attr:	:xmlattr:`ChatterFilter`
     :val:	1...65535
     :def:	50 msec
     :desc:	Chatter filter in milliseconds for Digital Inputs.
		State change of the digital input will be reported only if it remains stable for the period that exceeds configured filter.
		:inlinetip:`This attribute applies only to LEIODC series units.`

   * :attr:	:xmlattr:`OnValues`
     :val:	0...65535 or 0x00...0xFFFF (up to 32)
     :def:	n/a
     :desc:	Values received from station will result in a DI state ON.
		The DI will have ON state, if a register data received from station matches one of the values specified in this attribute.
		Up to 32 values can be specified in decimal or hexadecimal notation separated by whitespaces or commas
		e.g. "2,3 0x05 0xf1".
		:inlineimportant:`Either`
		:ref:`xmlattr-ModbusmaDIOnValues`
		:inlineimportant:`or`
		:ref:`xmlattr-ModbusmaDIOffValues`
		:inlineimportant:`attribute must be specified if`
		:ref:`xmlelem-ModbusmaDI`.\ :ref:`xmlattr-ModbusmaDIType`\ 
		:inlineimportant:`="5" is used.`
		:inlinetip:`If`
		:ref:`xmlattr-ModbusmaDIOffValues`
		:inlinetip:`attribute is not used, any value received from station that is not included in`
		:ref:`xmlattr-ModbusmaDIOnValues`
		:inlinetip:`list will result in a DI state OFF. If`
		:ref:`xmlattr-ModbusmaDIOffValues`
		:inlinetip:`attribute is used, any value received from station that is not included in either attributes will result in a DI state INTER.`

   * :attr:	:xmlattr:`OffValues`
     :val:	0...65535 or 0x00...0xFFFF (up to 32)
     :def:	n/a
     :desc:	Values received from station will result in a  DI state OFF.
		The DI will have OFF state, if a register data received from station matches one of the values specified in this attribute.
		Up to 32 values can be specified in decimal or hexadecimal notation separated by whitespaces or commas
		e.g. "2,3 0x05 0xf1"
		:inlineimportant:`Either`
		:ref:`xmlattr-ModbusmaDIOnValues`
		:inlineimportant:`or`
		:ref:`xmlattr-ModbusmaDIOffValues`
		:inlineimportant:`attribute must be specified if`
		:ref:`xmlelem-ModbusmaDI`.\ :ref:`xmlattr-ModbusmaDIType`\ 
		:inlineimportant:`="5" is used.`
		:inlinetip:`If`
		:ref:`xmlattr-ModbusmaDIOnValues`
		:inlinetip:`attribute is not used, any value received from station that is not included in`
		:ref:`xmlattr-ModbusmaDIOffValues`
		:inlinetip:`list will result in a DI state ON. If`
		:ref:`xmlattr-ModbusmaDIOnValues`
		:inlinetip:`attribute is used, any value received from station that is not included in either attributes will result in a DI state INTER.`

.. include-file:: sections/Include/DI_Odelays.rstinc ""

   * :attr:	:xmlattr:`AndMask`
     :val:	0...65535 or 0x00...0xFFFF
     :def:	0xFFFF
     :desc:	Logic AND function for the received value.
		Perform logic AND operation on the received data with this attribute before checking for matching values in :ref:`xmlattr-ModbusmaDIOnValues` and :ref:`xmlattr-ModbusmaDIOffValues` attributes.
		This attribute has a higher priority than :ref:`xmlattr-ModbusmaDIOrMask`.
		:inlinetip:`This attribute is used only if list of ON/OFF values is specified and` :ref:`xmlattr-ModbusmaDIType` :inlinetip:`="5".`

   * :attr:	:xmlattr:`OrMask`
     :val:	0...65535 or 0x00...0xFFFF
     :def:	0
     :desc:	Logic OR function for the received value.
		Perform logic OR operation on the received data with this attribute before checking for matching values in :ref:`xmlattr-ModbusmaDIOnValues` and :ref:`xmlattr-ModbusmaDIOffValues` attributes.
		This attribute has a lower priority than :ref:`xmlattr-ModbusmaDIAndMask`.
		:inlinetip:`This attribute is used only if list of ON/OFF values is specified and` :ref:`xmlattr-ModbusmaDIType` :inlinetip:`="5".`

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-ModbusmaDIIndex` and :ref:`xmlattr-ModbusmaDIBitOffset`" ":ref:`xmlelem-ModbusmaDI`" "254"

.. include-file:: sections/Include/Name.rstinc ""

DI.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-ModbusmaDIQualifier" "Modbus Master DI internal qualifier" ":ref:`xmlattr-ModbusmaDIQualifier`" "DI internal qualifier"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	DI object **will not** be inverted (ON = 1; OFF = 0)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DI object **will** be inverted (ON = 0; OFF = 1)

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DI is **enabled** and will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DI is **disabled** and will be discarded when received

   * :attr:	Bits 1..6
     :val:	Any
     :desc:	Bits reserved for future use


DI.Type
^^^^^^^

.. field-list-table:: Modbus Master DI decode types
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusDIType
   :spec: |C{0.07}|S{0.93}|
   :header-rows: 1

   * :val,10,center:	:ref:`xmlattr-ModbusmaDIType`
     :desc,90:		Description

   * :val:	0
     :desc:	Not used

   * :val:	1
     :desc:	Select one bit from the received data based on :ref:`xmlattr-ModbusmaDIBitOffset` attribute.
		See :numref:`tabid-ModbusmaBitOffset` for examples of offset values.

   * :val:	5
     :desc:	Values specified in :ref:`xmlattr-ModbusmaDIOnValues` and :ref:`xmlattr-ModbusmaDIOffValues` attributes will be used to determine the state of the DI object.

   * :val:	Other
     :desc:	Not used


Table below shows the selected bit '\ **B**\' based on the :ref:`xmlelem-ModbusmaDI`.\ :ref:`xmlattr-ModbusmaDIBitOffset` or :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOBitOffset` value.
The sample has 4 bytes of data in the order as it would be received from or sent to outstation.
Each byte is shown as 'xxxx.xxxx' where 'x' represents one bit of the byte.

.. field-list-table:: Modbus Master Bit Offset sample values
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusmaBitOffset
   :spec: |C{0.10}|S{0.50}|
   :header-rows: 1

   * :val,10,center:	:ref:`xmlattr-ModbusmaDIBitOffset`
     :desc,90:		Modbus Message

   * :val:	0
     :desc:	{... xxxx.xxxx xxxx.xxx\ **B** xxxx.xxxx xxxx.xxxx ...}

   * :val:	1
     :desc:	{... xxxx.xxxx xxxx.xx\ **B**\x xxxx.xxxx xxxx.xxxx ...}

   * :val:	2
     :desc:	{... xxxx.xxxx xxxx.x\ **B**\xx xxxx.xxxx xxxx.xxxx ...}

   * :val:	3
     :desc:	{... xxxx.xxxx xxxx.\ **B**\xxx xxxx.xxxx xxxx.xxxx ...}

   * :val:	4
     :desc:	{... xxxx.xxxx xxx\ **B**\.xxxx xxxx.xxxx xxxx.xxxx ...}

   * :val:	8
     :desc:	{... xxxx.xxx\ **B** xxxx.xxxx xxxx.xxxx xxxx.xxxx ...}

   * :val:	16
     :desc:	{... xxxx.xxxx xxxx.xxxx xxxx.xxxx xxxx.xxx\ **B** ...}

   * :val:	24
     :desc:	{... xxxx.xxxx xxxx.xxxx xxxx.xxx\ **B** xxxx.xxxx ...}

   * :val:	31
     :desc:	{... xxxx.xxxx xxxx.xxxx **B**\xxx.xxxx xxxx.xxxx ...}

