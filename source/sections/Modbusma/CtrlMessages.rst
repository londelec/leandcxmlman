
.. _ref-CtrlMessages:

CtrlMessages group and MSG node
-------------------------------

Group node :ref:`CtrlMessages<ref-CtrlMessages>` and child element nodes :ref:`MSG<ref-CtrlMessages>` contain messages for writing data to outstation.
Use :ref:`DO<ref-ModbusmaDO>` node to specify which control message has to be sent to outstation when command is received.

.. tip:: \ :ref:`CtrlMessages<ref-CtrlMessages>` group and :ref:`MSG<ref-CtrlMessages>` nodes are optional if :ref:`<ref-ModbusmaHardcoded>`.\ :ref:`<ref-ModbusmaHardcodedType>` is used. Messages required to send data to a hardcoded device are set-up automatically.

Please see sample :ref:`CtrlMessages<ref-CtrlMessages>` group and :ref:`MSG<ref-CtrlMessages>` child element nodes below.
There are 2 Modbus messages configured using 2 :ref:`MSG<ref-CtrlMessages>` element nodes.

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="6" Reg="0x0055" Type="1" />
	<MSG CtrlMsg="2" Func="16" Reg="0x0003" Data="0x0001" Type="0" />
   </CtrlMessages>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`MSG<ref-CtrlMessages>`"

.. code-block:: none

   <MSG CtrlMsg="1" Func="6" Reg="0x0100" Data="0x1122" FollowCtrlMsg="2" Type="0" Name="Write Registers message" />

.. tip:: Attributes of the :ref:`MSG<ref-CtrlMessages>` element node can be arranged in any order, it will not affect XML file validation.

MSG attributes
^^^^^^^^^^^^^^

.. _docref-CtrlMessageAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master Control message attributes" ":spec: |C{0.16}|C{0.16}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/Modbusma_Msgid.rstinc "" ".. _ref-CtrlMsgId:" ":xmlref:`CtrlMsg`"

.. include-file:: sections/Include/Modbusma_Func.rstinc "" ".. _ref-CtrlMsgFunc:" "See table :numref:`docref-ModbusmaCtrlFuncTab`"

.. include-file:: sections/Include/Modbusma_Reg.rstinc "" ".. _ref-CtrlMsgReg:" "Data will be written to or read from this register."

.. include-file:: sections/Include/Modbusma_Data.rstinc "" ".. _ref-CtrlMsgData:" "" "" ""
		:inlinetip:`See compatibility table` :numref:`docref-ModbusmaCtrlFuncTab` :inlinetip:`to check if` :xmlref:`Data` :inlinetip:`attribute is optional.`

   * :attr:     .. _ref-ModbusmaFollowCtrlMsg:

                :xmlref:`FollowCtrlMsg`
     :val:      1...65534
     :def:      0
     :desc:     Identifier of the Control message which this message will follow.
		Current message will be sent after previous Control message with the identifier specified is complete.
		Value 0 means this message does not follow any previous messages.
		:inlinetip:`Attribute is optional and doesn’t have to be included in configuration.`


   * :attr:     .. _ref-CtrlMsgType:

                :xmlref:`Type`
     :val:      See table :numref:`docref-ModbusCtrlMsgTypeTab`
     :def:      0
     :desc:     Select format of outgoing data.
		:inlinetip:`Attribute is optional and doesn’t have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Name.rstinc ""

MSG.Func
^^^^^^^^

Table below shows supported values of the :ref:`<ref-CtrlMsgFunc>` attribute and 
whether :ref:`<ref-CtrlMsgData>` attribute must be specified when particular Modbus function is used.

.. _docref-ModbusmaCtrlFuncTab:

.. field-list-table:: Modbus Master Control message functions
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.10}|C{0.10}|C{0.14}|S{0.66}|
   :header-rows: 1

   * :val,10:   :ref:`<ref-CtrlMsgFunc>`
     :type,10:	:ref:`<ref-CtrlMsgType>`
     :data,13:	:ref:`<ref-CtrlMsgData>` required
     :name,67:  Description

   * :val:      3
     :type:	n/a
     :data:	No
     :name:     [:lemonobgtext:`Read Holding Registers`] message will be sent and
		data received from outstation can be modified and used for the following write message.
		This message should be followed by a write message with :ref:`<ref-CtrlMsgType>`\ ="1".

   * :val:      4
     :type:	n/a
     :data:	No
     :name:     [:lemonobgtext:`Read Input Registers`] message will be sent and
		data received from outstation can be modified and used for the following write message.
		This message should be followed by a write message with :ref:`<ref-CtrlMsgType>`\ ="1".

   * :val:      5
     :type:	0
     :data:	Yes
     :name:     [:lemonobgtext:`Force Single Coil`] message with contents of the :ref:`<ref-CtrlMsgData>` attribute will be sent.

   * :(val):
     :type:	1
     :data:	No
     :name:     [:lemonobgtext:`Force Single Coil`] message will contain data received from outstation in a previous read message and
		the bit specified in :ref:`DO<ref-ModbusmaDO>`.\ :ref:`<ref-ModbusmaDOBitOffset>` attribute will be set.
		If no read message is used, data is initialized to 0 and bit specified in :ref:`DO<ref-ModbusmaDO>`.\ :ref:`<ref-ModbusmaDOBitOffset>` attribute is set.

   * :val:      6
     :type:	0
     :data:	Yes
     :name:     [:lemonobgtext:`Preset Single Register`] message with contents of the :ref:`<ref-CtrlMsgData>` attribute will be sent.

   * :(val):
     :type:	1
     :data:	No
     :name:	[:lemonobgtext:`Preset Single Register`] message will contain data received from outstation in a previous read message and
		the bit specified in :ref:`DO<ref-ModbusmaDO>`.\ :ref:`<ref-ModbusmaDOBitOffset>` attribute will be set.
		If no read message is used, data is initialized to 0 and bit specified in :ref:`DO<ref-ModbusmaDO>`.\ :ref:`<ref-ModbusmaDOBitOffset>` attribute is set.

   * :val:      16
     :type:	0
     :data:	Yes
     :name:     [:lemonobgtext:`Preset Multiple Registers`] message with contents of the :ref:`<ref-CtrlMsgData>` attribute will be sent.

   * :(val):
     :type:	1
     :data:	No
     :name:     [:lemonobgtext:`Preset Multiple Registers`] message will contain data received from outstation in a previous read message and
		the bit specified in :ref:`DO<ref-ModbusmaDO>`.\ :ref:`<ref-ModbusmaDOBitOffset>` attribute will be set.
		If no read message is used, data is initialized to 0 and bit specified in :ref:`DO<ref-ModbusmaDO>`.\ :ref:`<ref-ModbusmaDOBitOffset>` attribute is set.

   * :val:      Other
     :type:	---
     :data:	---
     :name:     Function is not supported

MSG.Type
^^^^^^^^

.. _docref-ModbusCtrlMsgTypeTab:

.. field-list-table:: Modbus Master Control message types
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.10}|S{0.90}|
   :header-rows: 1

   * :val,10:   :ref:`<ref-CtrlMsgType>`
     :desc,90:  Description

   * :val:	0
     :desc:	Send contents of the :ref:`MSG<ref-CtrlMessages>`.\ :ref:`<ref-CtrlMsgData>` attribute to outstation.
		:ref:`DO<ref-ModbusmaDO>`.\ :ref:`<ref-ModbusmaDOBitOffset>` attribute is ignored

   * :val:	1
     :desc:	Set only one bit as specified in :ref:`DO<ref-ModbusmaDO>`.\ :ref:`<ref-ModbusmaDOBitOffset>` attribute.
		:ref:`MSG<ref-CtrlMessages>`.\ :ref:`<ref-CtrlMsgData>` attribute is ignored.

   * :val:	Other
     :desc:	Not used

