
.. _xmlgroup-ModbusmaInitMessages: lelabel=InitMessages
.. _xmlelem-ModbusmaInitMsg: lelabel=MSG

InitMessages group
------------------

Group node :ref:`xmlgroup-ModbusmaInitMessages` and child element nodes :ref:`xmlelem-ModbusmaInitMsg` contain messages that are being sent to outstation during an initialization stage.
Outstation replies can be checked against the pre-defined data to ensure correct outstation is connected during the initialization stage.
Modbus Write messages can be used to change settings of the outstation during the initialization stage, if necessary.

.. tip:: \ :ref:`xmlgroup-ModbusmaInitMessages` group and :ref:`xmlelem-ModbusmaInitMsg` nodes are optional if :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` is used. Messages required for initialization of hardcoded devices are set-up automatically.

Please see sample :ref:`xmlgroup-ModbusmaInitMessages` group and :ref:`xmlelem-ModbusmaInitMsg` child element nodes below.
There are 2 Modbus messages configured using 2 :ref:`xmlelem-ModbusmaInitMsg` element nodes.

.. code-block:: none

   <InitMessages>
	<MSG InitMsg="1" Func="17" Data="0x00"/>
	<MSG InitMsg="2" Func="4" Reg="0x0003" Count="1" Data="0x00" />
   </InitMessages>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaInitMsg`"

.. code-block:: none

   <MSG InitMsg="1" Func="4" Reg="0x0100" Count="1" Data="0xAA BB CC DD 05 03" Flags="0x00" Name="Read Input Registers message" />

.. tip:: Attributes of the :ref:`xmlelem-ModbusmaInitMsg` element node can be arranged in any order, it will not affect XML file validation.

Init MSG attributes
^^^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaInitMsg" "Modbus Master Initialization message attributes" ":spec: |C{0.1}|C{0.16}|C{0.1}|S{0.64}|"

.. include-file:: sections/Include/serma_Msgid.rstinc "" ":xmlattr:`InitMsg`"

.. include-file:: sections/Include/Modbusma_Func.rstinc "" "See :numref:`tabid-ModbusmaInitMsgFunc`"

.. include-file:: sections/Include/Modbusma_Reg.rstinc "" "Data will be written to or read from this register."
		:inlinetip:`See` :numref:`tabid-ModbusmaInitMsgFunc` :inlinetip:`to check if attribute is optional.`

.. include-file:: sections/Include/Modbusma_Count.rstinc "" "read from"
		:inlinetip:`Attribute is used only for read messages` :ref:`xmlattr-ModbusmaInitMsgFunc`\ ="3" :inlinetip:`or` :ref:`xmlattr-ModbusmaInitMsgFunc`\ ="4"

.. include-file:: sections/Include/Modbusma_Data.rstinc "" ":ref:`xmlattr-ModbusmaInitMsgReg`" " or expected in a reply from outstation" " / reading" " / read from"

   * :attr:	:xmlattr:`Flags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Message flags to customize processing.
		See :numref:`tabid-ModbusInitMsgFlags` for available flags.
		:inlinetip:`Attribute is optional and doesn’t have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Name.rstinc ""

Init MSG.Func
^^^^^^^^^^^^^

Table below shows supported values of the :ref:`xmlattr-ModbusmaInitMsgFunc` attribute and
whether :ref:`xmlattr-ModbusmaInitMsgReg` attribute must be specified when particular Modbus function is used.

.. field-list-table:: Modbus Master Initialization message functions
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusmaInitMsgFunc
   :spec: |C{0.07}|C{0.10}|S{0.83}|
   :header-rows: 1

   * :val,8:	:ref:`xmlattr-ModbusmaInitMsgFunc`
     :reg,10:	:ref:`xmlattr-ModbusmaInitMsgReg` required
     :name,82:	Function Name

   * :val:	3
     :reg:	Yes
     :name:	[:lemonobgtext:`Read Holding Registers`] message reads contents of one or more outstation registers.
		Number of registers to read is set by the :ref:`xmlattr-ModbusmaInitMsgCount` attribute.

   * :val:	4
     :reg:	Yes
     :name:	[:lemonobgtext:`Read Input Registers`] message reads contents of one or more outstation registers.
		Number of registers to read is set by the :ref:`xmlattr-ModbusmaInitMsgCount` attribute.

   * :val:	5
     :reg:	Yes
     :name:	[:lemonobgtext:`Force Single Coil`] message writes data to a single outstation register (2 bytes).

   * :val:	6
     :reg:	Yes
     :name:	[:lemonobgtext:`Preset Single Register`] message writes data to a single outstation register (2 bytes).

   * :val:	16
     :reg:	Yes
     :name:	[:lemonobgtext:`Preset Multiple Registers`] message writes data to multiple outstation registers (up to 126 bytes).
		Number of registers to write is determined by the :ref:`xmlattr-ModbusmaInitMsgData` attribute.

   * :val:	17
     :reg:	No
     :name:	[:lemonobgtext:`Report Slave ID`] message reads Modbus device ID.

   * :val:	Other
     :reg:	---
     :name:	Function is not supported

Init MSG.Flags
^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-ModbusInitMsgFlags" "Modbus Initialization message flags" ":ref:`xmlattr-ModbusmaInitMsgFlags`" "Message flags"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	Data received from outstation has to match contents of the :ref:`xmlattr-ModbusmaInitMsgData` attribute **exactly**

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	Data received from outstation has to **contain** contents of the :ref:`xmlattr-ModbusmaInitMsgData` attribute.
		This option is normally used with :lemonobgtext:`Report Server ID [17]` message and 
		enables to check only portion of the received reply.
		For example if :ref:`xmlattr-ModbusmaInitMsgData`\="41 42 43" (represents string "ABC") a reply from outstation
		{01 17 08 41 42 43 20 56 31 2E 30 ...} (represents string "ABC V1.0") is considered valid.

