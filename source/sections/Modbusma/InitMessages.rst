
.. _ref-InitMessages:

InitMessages group and MSG node
-------------------------------

Group node :ref:`InitMessages<ref-InitMessages>` and child element nodes :ref:`MSG<ref-InitMessages>` contain messages that are being sent to outstation during an initialization stage.
Outstation replies can be checked against the pre-defined data to ensure correct outstation is connected during the initialization stage.
Modbus Write messages can be used to change settings of the outstation during the initialization stage, if necessary.

.. tip:: \ :ref:`InitMessages<ref-InitMessages>` group and :ref:`MSG<ref-InitMessages>` nodes are optional if :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` is used. Messages required for initialization of hardcoded devices are set-up automatically.

Please see sample :ref:`InitMessages<ref-InitMessages>` group and :ref:`MSG<ref-InitMessages>` child element nodes below.
There are 2 Modbus messages configured using 2 :ref:`MSG<ref-InitMessages>` element nodes.

.. code-block:: none

   <InitMessages>
	<MSG InitMsg="1" Func="17" Data="0x00"/>
	<MSG InitMsg="2" Func="4" Reg="0x0003" Count="1" Data="0x00" />
   </InitMessages>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`MSG<ref-InitMessages>`"

.. code-block:: none

   <MSG InitMsg="1" Func="4" Reg="0x0100" Count="1" Data="0xAA BB CC DD 05 03" Flags="0x00" Name="Read Input Registers message" />

.. tip:: Attributes of the :ref:`MSG<ref-InitMessages>` element node can be arranged in any order, it will not affect XML file validation.

MSG attributes
^^^^^^^^^^^^^^

.. _docref-InitMessageAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master Initialization message attributes"

.. include-file:: sections/Include/Modbusma_Msgid.rstinc "" ".. _ref-InitMsgId:" ":xmlref:`InitMsg`"

.. include-file:: sections/Include/Modbusma_Func.rstinc "" ".. _ref-InitMsgFunc:" "See table :numref:`docref-ModbusmaInitFuncTab`"

.. include-file:: sections/Include/Modbusma_Reg.rstinc "" ".. _ref-InitMsgReg:" "Data will be written to or read from this register."
		:inlinetip:`See table` :numref:`docref-ModbusmaInitFuncTab` :inlinetip:`to check if` :xmlref:`Reg` :inlinetip:`attribute is optional.`

.. include-file:: sections/Include/Modbusma_Count.rstinc "" ".. _ref-InitMsgCount:" "read from"

.. include-file:: sections/Include/Modbusma_Data.rstinc "" ".. _ref-InitMsgData:" " or expected in a reply from outstation" " / reading" " / read from"

   * :attr:     .. _ref-ModbusmaMsgFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Message flags to customize processing.
		See table :numref:`docref-ModbusInitMsgFlagBits` for available flags.
		:inlinetip:`Attribute is optional and doesn’t have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Name.rstinc ""

MSG.Func
^^^^^^^^

Table below shows supported values of the :ref:`<ref-InitMsgFunc>` attribute and 
whether :ref:`<ref-InitMsgReg>` attribute must be specified when particular Modbus function is used.

.. _docref-ModbusmaInitFuncTab:

.. field-list-table:: Modbus Master Initialization message functions
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.10}|C{0.13}|S{0.77}|
   :header-rows: 1

   * :val,10:   :ref:`<ref-InitMsgFunc>`
     :reg,13:  	:ref:`<ref-InitMsgReg>` required
     :name,77:  Function Name

   * :val:      3
     :reg:	Yes
     :name:     [:lectext1:`Read Holding Registers`]

   * :val:      4
     :reg:	Yes
     :name:     [:lectext1:`Read Input Registers`]

   * :val:      5
     :reg:	Yes
     :name:     [:lectext1:`Force Single Coil`]

   * :val:      6
     :reg:	Yes
     :name:     [:lectext1:`Preset Single Register`]

   * :val:      16
     :reg:	Yes
     :name:     [:lectext1:`Preset Multiple Registers`]

   * :val:      17
     :reg:	No
     :name:     [:lectext1:`Report Slave ID`]

   * :val:      Other
     :reg:	---
     :name:     Function is not supported

MSG.Flags
^^^^^^^^^

.. _docref-ModbusInitMsgFlagBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Modbus Initialization message flags" ":ref:`<ref-ModbusmaMsgFlags>`" "Message flags"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	Data received from outstation has to match contents of the :ref:`<ref-InitMsgData>` attribute **exactly**

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	Data received from outstation has to **contain** contents of the :ref:`<ref-InitMsgData>` attribute.
		This option is normally used with :lectext1:`Report Server ID [17]` message and 
		enables to check only portion of the received reply.
		For example if :ref:`<ref-InitMsgData>`\="41 42 43" (represents string "ABC") a reply from outstation 
		{01 17 08 41 42 43 20 56 31 2E 30 ...} (represents string "ABC V1.0") is considered valid.

