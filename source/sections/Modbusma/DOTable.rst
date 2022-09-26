
.. _xmlgroup-ModbusmaDO: lelabel=DOTable
.. _xmlelem-ModbusmaDO: lelabel=DO

DOTable group
-------------

.. include-file:: sections/Include/ma_DOAO_table.rstinc "" ":ref:`xmlgroup-ModbusmaDO`" ":ref:`xmlelem-ModbusmaDO`" ":numref:`tabid-ModbusmaDO`" ":ref:`docref-IEC10xslDO`" "DO" "control" "outstation"

.. tip:: \ :ref:`xmlgroup-ModbusmaDO` group and :ref:`xmlelem-ModbusmaDO` nodes are optional if :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` is used. DO information objects are initialized automatically for hardcoded devices.

Please see sample :ref:`xmlgroup-ModbusmaDO` group and :ref:`xmlelem-ModbusmaDO` element nodes below.
There are 5 control commands defined with 4 :ref:`xmlelem-ModbusmaDO` element nodes.

.. code-block:: none

   <DOTable>
	<DO Index="0" CtrlMsg="1" BitOffset="0"/>
	<DO Index="1" CtrlMsg="1" BitOffset="1"/>
	<DO Index="2" CtrlMsg="1" BitOffset="2" Qualifier="0x01"/>
	<DO Index="3" CtrlMsg="1" BitOffset="4" Total="2"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaDO`"

.. code-block:: none

   <DO Index="0" CtrlMsg="1" BitOffset="0" Qualifier="0x00" PulseDuration="500" Step="1" Total="1" Name="Output 1" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-ModbusmaDO`"

DO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaDO" "Modbus Master DO attributes" ":spec: |C{0.14}|C{0.14}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "DO"

.. include-file:: sections/Include/Modbusma_CtrlMsg.rstinc ""
		:inlineimportant:`Attribute is optional only if` :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` :inlineimportant:`is used.`

   * :attr:	:xmlattr:`BitOffset`
     :val:	0...1023 or 0x00...0x3FF
     :def:	0
     :desc:	Offset of the bit that is to send control.
		See :numref:`tabid-ModbusmaBitOffset` for examples of offset values.
		:inlineimportant:`Attribute is optional only if` :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` :inlineimportant:`is used.`

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-ModbusmaDOQualifier`"

   * :attr:	:xmlattr:`PulseDuration`
     :val:	1...65535
     :def:	1500 msec
     :desc:	Digital output pulse duration in milliseconds.
		Digital output will be activated when command is sent and automatically released after configured number of milliseconds.
		:inlinetip:`This attribute applies only to LEIODC series units.`

   * :attr:	:xmlattr:`Step`
     :val:	0 or 1.18×10\ :sup:`-38` \ ... 3.4×10\ :sup:`38`\
     :def:	0
     :desc:	Step value to add to/subtract from initial data value.
		Contents of this attribute will be mathematically added to (if ON command is received from upstream station) or subtracted from (if OFF command is received from upstream station) initial data value and the result will be sent to outstation.
		Initial data can either be read from outstation with a read message or contents of the :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgData` attribute can be used.
		:inlinetip:`See compatibility` :numref:`tabid-ModbusmaCtrlMsgCompatibility` :inlinetip:`to check how this attribute is used for different control message types.`

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-ModbusmaDOIndex` and :ref:`xmlattr-ModbusmaDOBitOffset`" ":ref:`xmlelem-ModbusmaDO`" "254"

.. include-file:: sections/Include/Name.rstinc ""

DO.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-ModbusmaDOQualifier" "Modbus Master DO internal qualifier" ":ref:`xmlattr-ModbusmaDOQualifier`" "DO internal qualifier"

   * :attr:	:bitdef:`0`
     :val:	xxxx.xxx0
     :desc:	DO object **will not** be inverted (ON = 1; OFF = 0)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	DO object **will** be inverted (ON = 0; OFF = 1)

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	DO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	DO is **disabled**, command will not be sent to outstation

   * :attr:	Bits 1..6
     :val:	Any
     :desc:	Bits reserved for future use

.. _docref-ModbusmaDOsamples:

DO samples
^^^^^^^^^^

**Example 1:**

Configuration below has a [:lemonobgtext:`Preset Single Register`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="1".
DO inversion is not enabled, which means Bit 0 of the initial data value 0x0000 will be set.
The resulting data 0x0001 will be written to outstation register 0x0305.

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="6" Reg="0x0305" Type="1" Name="Write register 0x0305"/>
   </CtrlMessages>
   <DOTable>
	<DO Index="0" CtrlMsg="1" BitOffset="0" Name="DO sets Bit 0"/>
   </DOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 06 03 05 00 01 ...
   COMM -> 01 06 03 05 00 01 ...

|
| **Example 2:**

Configuration below has a [:lemonobgtext:`Preset Single Register`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="1".
DO inversion is enabled, which means Bit 1 of the initial data value 0xFFFF will be cleared.
The resulting data 0xFFFD will be written to outstation register 0x0305.

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="6" Reg="0x0305" Type="1" Name="Write register 0x0305"/>
   </CtrlMessages>
   <DOTable>
	<DO Index="0" CtrlMsg="1" BitOffset="1" Qualifier="0x01" Name="DO clears Bit 1"/>
   </DOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 06 03 05 FF FD ...
   COMM -> 01 06 03 05 FF FD ...

|
| **Example 3:**

Configuration below has a [:lemonobgtext:`Preset Single Register`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="1" that follows a [:lemonobgtext:`Read Holding Registers`] message.
Initial data will be read from outstation before modifying the bit. Data read from outstation is 0xAA00 in this example.
DO inversion is not enabled, which means Bit 7 of the initial data value 0xAA00 will be set.
The resulting data 0xAA80 will be written to outstation register 0x0305.

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="3" Reg="0x0305" Count="1" Name="Read register 0x0305"/>
	<MSG CtrlMsg="2" Func="6" Reg="0x0305" Type="1" FollowCtrlMsg="1" Name="Write register 0x0305"/>
   </CtrlMessages>
   <DOTable>
	<DO Index="0" CtrlMsg="1" BitOffset="7" Name="DO sets Bit 7"/>
   </DOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 03 03 05 00 01 ...
   COMM -> 01 03 02 AA 00 ...
   COMM <- 01 06 03 05 AA 80 ...
   COMM -> 01 06 03 05 AA 80 ...

|
| **Example 4:**

Configuration below has a [:lemonobgtext:`Preset Single Register`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="33" that follows a [:lemonobgtext:`Read Holding Registers`] message.
Initial data will be read from outstation before adding/subtracting step value. Data read from outstation 0xAA00 in this example will be decoded as 16bit Unsigned Integer '43520'.
If DO ON command is received, step value '4' will be added to '43520'.
The result '43524' will be encoded as 16bit Unsigned Integer 0xAA04 and written to outstation register 0x0305.

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="3" Reg="0x0305" Count="1" Name="Read register 0x0305"/>
	<MSG CtrlMsg="2" Func="6" Reg="0x0305" Type="33" FollowCtrlMsg="1" Name="Write register 0x0305"/>
   </CtrlMessages>
   <DOTable>
	<DO Index="0" CtrlMsg="1" Step="4" Name="DO ON adds 4, DO OFF subtracts 4"/>
   </DOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 03 03 05 00 01 ...
   COMM -> 01 03 02 AA 00 ...
   COMM <- 01 06 03 05 AA 04 ...
   COMM -> 01 06 03 05 AA 04 ...

|
| **Example 5:**

Configuration below has a [:lemonobgtext:`Preset Multiple Registers`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="37" that follows a [:lemonobgtext:`Read Holding Registers`] message.
Initial data will be read from outstation before adding/subtracting step value. Data read from outstation 0x0000AA00 in this example will be decoded as 32bit Unsigned Integer '43520'.
If DO OFF command is received, step value '4' will be subtracted from '43520'.
The result '43516' will be encoded as 32bit Unsigned Integer 0x0000A9FC and written to outstation registers 0x0305 and 0x0306.
.. include-file:: sections/Include/Modbusma_CtrlData.rstinc ""

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="3" Reg="0x0305" Count="2" Name="Read registers 0x0305 and 0x0306"/>
	<MSG CtrlMsg="2" Func="16" Reg="0x0305" Data="0x00000000" Type="37" FollowCtrlMsg="1" Name="Write registers 0x0305 and 0x0306"/>
   </CtrlMessages>
   <DOTable>
	<DO Index="0" CtrlMsg="1" Step="4" Name="DO ON adds 4, DO OFF subtracts 4"/>
   </DOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 03 03 05 00 02 ...
   COMM -> 01 03 04 00 00 AA 00 ...
   COMM <- 01 10 03 05 00 02 04 00 00 A9 FC ...
   COMM -> 01 10 03 05 00 02 ...

|
| **Example 6:**

Configuration below has a [:lemonobgtext:`Preset Single Register`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="0" which is followed by a [:lemonobgtext:`Read Holding Registers`] message.
Contents of the :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgData` attribute will be written to outstation register 0x0305.
.. include-file:: sections/Include/Modbusma_verify.rstinc "" "0xAA55"

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="6" Reg="0x0305" Type="0" Data="0xAA55" Name="Write register 0x0305"/>
	<MSG CtrlMsg="2" Func="3" Reg="0x0305" Count="1" FollowCtrlMsg="1" Name="Read and Verify register 0x0305"/>
   </CtrlMessages>
   <DOTable>
	<DO Index="0" CtrlMsg="1" Name="DO writes constant data"/>
   </DOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 06 03 05 AA 55 ...
   COMM -> 01 06 03 05 AA 55 ...
   COMM <- 01 03 03 05 00 01 ...
   COMM -> 01 03 02 AA 55 ...

|
| **Example 7:**

Configuration below has a [:lemonobgtext:`Preset Single Register`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="97" which is preceded and followed by [:lemonobgtext:`Read Holding Registers`] messages.
Initial data will be read from outstation before adding/subtracting step value. Data read from outstation 0x0198 in this example will be decoded as 16bit Binary Coded Decimal '198'.
If DO ON command is received, step value '15' will be added to '198'.
The result '213' will be encoded as 16bit Binary Coded Decimal 0x0213 and written to outstation register 0x0305.
.. include-file:: sections/Include/Modbusma_verify.rstinc "" "0x0213"

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="3" Reg="0x0305" Count="1" Name="Read register 0x0305"/>
	<MSG CtrlMsg="2" Func="6" Reg="0x0305" Type="97" FollowCtrlMsg="1" Name="Write register 0x0305"/>
	<MSG CtrlMsg="3" Func="3" Reg="0x0305" Count="1" FollowCtrlMsg="2" Name="Read and Verify register 0x0305"/>
   </CtrlMessages>
   <DOTable>
	<DO Index="0" CtrlMsg="1" Step="15" Name="DO ON adds 15, DO OFF subtracts 15"/>
   </DOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 03 03 05 00 01 ...
   COMM -> 01 03 02 01 98 ...
   COMM <- 01 06 03 05 02 13 ...
   COMM -> 01 06 03 05 02 13 ...
   COMM <- 01 03 03 05 00 01 ...
   COMM -> 01 03 02 02 13 ...

