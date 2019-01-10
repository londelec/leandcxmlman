
.. _ref-ModbusmaDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-ModbusmaDO>` and child element nodes :ref:`DO<ref-ModbusmaDO>` are used to create DO information objects for sending control commands to outstation.
Each created DO can be used as a destination for any DO information object defined in the IO table of any Slave protocol instance.
Command execution procedure is as follows: Slave protocol instance receives a control command from the upstream Master station and forwards to the destination DO object.
Current communication protocol instance validates and sends a command to the outstation based on the DO settings configured below.
Please refer to the section :ref:`docref-IEC10xslDOTable` for more information on how to use DO as a destination.

.. tip:: \ :ref:`DOTable<ref-ModbusmaDO>` group and :ref:`DO<ref-ModbusmaDO>` nodes are optional if :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` is used. DO information objects are initialized automatically for hardcoded devices.

Please see sample :ref:`DOTable<ref-ModbusmaDO>` group and :ref:`DO<ref-ModbusmaDO>` child element nodes below.
There are 5 DO information objects configured using 4 :ref:`DO<ref-ModbusmaDO>` element nodes.

.. code-block:: none

   <DOTable>
	<DO Index="0" CtrlMsg="1" BitOffset="0"/>
	<DO Index="1" CtrlMsg="1" BitOffset="1"/>
	<DO Index="2" CtrlMsg="1" BitOffset="2" Qualifier="0x01"/>
	<DO Index="3" CtrlMsg="1" BitOffset="4" Total="2"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DO<ref-ModbusmaDO>`"

.. code-block:: none

   <DO Index="0" CtrlMsg="1" BitOffset="0" Qualifier="0x00" PulseDuration="500" Total="1" Name="Output 1" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`DO<ref-ModbusmaDO>`"

DO attributes
^^^^^^^^^^^^^

.. _docref-ModbusmaDOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master DO attributes" ":spec: |C{0.14}|C{0.14}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-ModbusmaDOIndex:" "DO"

   * :attr:     .. _ref-ModbusmaDOCtrlMsg:

                :xmlref:`CtrlMsg`
     :val:      1...65534
     :def:      0
     :desc:     Identifier of the message that is used to poll data from outstation.
		Use value of the :ref:`MSG<ref-CtrlMessages>`.\ :ref:`<ref-CtrlMsgId>` attribute.
		Value 0 means no poll message is selected.
		:inlineimportant:`Attribute is optional only if` :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` :inlineimportant:`is used.`

   * :attr:     .. _ref-ModbusmaDOBitOffset:

                :xmlref:`BitOffset`
     :val:      0...1023 or 0x00...0x3FF
     :def:      0
     :desc:     Offset of the bit that is to send control.
		See table :numref:`docref-ModbusmaBitOffsetTab` for examples of offset values.
		:inlineimportant:`Attribute is optional only if` :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` :inlineimportant:`is used.`

   * :attr:     .. _ref-ModbusmaDOQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`docref-ModbusmaDOqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-ModbusmaDOPulseDuration:

                :xmlref:`PulseDuration`
     :val:      1...65535
     :def:      1500 msec
     :desc:     Digital output pulse duration in milliseconds.
		Digital output will be activated when command is sent and automatically released after configured number of milliseconds.
		:inlinetip:`This attribute applies only to LEIODC series units.`

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-ModbusmaDOTotal:" ":ref:`<ref-ModbusmaDOIndex>` and :ref:`<ref-ModbusmaDOBitOffset>`" ":ref:`DO<ref-ModbusmaDO>`" "254"

.. include-file:: sections/Include/Name.rstinc ""

DO.Qualifier
^^^^^^^^^^^^

.. _docref-ModbusmaDOqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Modbus Master DO internal qualifier" ":ref:`<ref-ModbusmaDOQualifier>`" "DO internal qualifier"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     DO object **will not** be inverted (ON = 1; OFF = 0)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     DO object **will** be inverted (ON = 0; OFF = 1)

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     DO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     DO is **disabled**, command will not be sent to outstation

   * :attr:     Bits 1..6
     :val:      Any
     :desc:     Bits reserved for future use

