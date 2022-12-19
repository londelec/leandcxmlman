
.. _xmlgroup-ModbusmaCtrlMessages: lelabel=CtrlMessages
.. _xmlelem-ModbusmaCtrlMsg: lelabel=MSG

CtrlMessages group
------------------

Group node :ref:`xmlgroup-ModbusmaCtrlMessages` and child element nodes :ref:`xmlelem-ModbusmaCtrlMsg` contain messages for writing data to outstation.
Use :ref:`xmlelem-ModbusmaDO` node to specify which control message has to be sent to outstation when command is received.

.. tip:: \ :ref:`xmlgroup-ModbusmaCtrlMessages` group and :ref:`xmlelem-ModbusmaCtrlMsg` nodes are optional if :ref:`xmlelem-ModbusmaHardcoded`.\ :ref:`xmlattr-ModbusmaHardcodedType` is used. Messages required to send data to a hardcoded device are set-up automatically.

Please see sample :ref:`xmlgroup-ModbusmaCtrlMessages` group and :ref:`xmlelem-ModbusmaCtrlMsg` child element nodes below.
There are 2 Modbus messages configured using 2 :ref:`xmlelem-ModbusmaCtrlMsg` element nodes.

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="6" Reg="0x0055" Type="1" />
	<MSG CtrlMsg="2" Func="16" Reg="0x0003" Data="0x0001" Type="0" />
   </CtrlMessages>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaCtrlMsg`"

.. code-block:: none

   <MSG CtrlMsg="1" Func="6" Reg="0x0100" Data="0x1122" Count="1" Type="0" FollowCtrlMsg="2" Name="Write Registers message" />

.. tip:: Attributes of the :ref:`xmlelem-ModbusmaCtrlMsg` element node can be arranged in any order, it will not affect XML file validation.

Ctrl MSG attributes
^^^^^^^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaCtrlMsg" "Modbus Master Control message attributes" ":spec: |C{0.16}|C{0.16}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/serma_Msgid.rstinc "" ":xmlattr:`CtrlMsg`"

.. include-file:: sections/Include/Modbusma_Func.rstinc "" "See :numref:`tabid-ModbusmaCtrlMsgFunc`"

.. include-file:: sections/Include/Modbusma_Reg.rstinc "" "Data will be written to or read from this register."

.. include-file:: sections/Include/Modbusma_Data.rstinc "" ":ref:`xmlattr-ModbusmaCtrlMsgReg`" "" "" ""
		:inlinetip:`See compatibility` :numref:`tabid-ModbusmaCtrlMsgCompatibility` :inlinetip:`to check how this attribute is used for different message types.`

.. include-file:: sections/Include/Modbusma_Count.rstinc "" "read from"
		:inlinetip:`Attribute is used only for read messages` :ref:`xmlattr-ModbusmaCtrlMsgFunc`\ ="3" :inlinetip:`and` :ref:`xmlattr-ModbusmaCtrlMsgFunc`\ ="4"

   * :attr:	:xmlattr:`Type`
     :val:	See :numref:`tabid-ModbusCtrlMsgType`
     :def:	0
     :desc:	Select format of outgoing data.
		:inlinetip:`Attribute is optional only for read messages` :ref:`xmlattr-ModbusmaCtrlMsgFunc`\ ="3" :inlinetip:`and` :ref:`xmlattr-ModbusmaCtrlMsgFunc`\ ="4"

.. include-file:: sections/Include/serma_FollowCtrlMsg.rstinc ""

.. include-file:: sections/Include/Name.rstinc ""

Ctrl MSG.Func
^^^^^^^^^^^^^

Table below shows supported values of the :ref:`xmlattr-ModbusmaCtrlMsgFunc` attribute and
whether :ref:`xmlattr-ModbusmaCtrlMsgCount` and :ref:`xmlattr-ModbusmaCtrlMsgType` attributes must be specified when particular Modbus function is used.

.. field-list-table:: Modbus Master Control message functions
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusmaCtrlMsgFunc
   :spec: |C{0.07}|C{0.10}|C{0.10}|S{0.73}|
   :header-rows: 1

   * :val,8,center:	:ref:`xmlattr-ModbusmaCtrlMsgFunc`
     :count,10,center:	:ref:`xmlattr-ModbusmaCtrlMsgCount` required
     :type,10,center:	:ref:`xmlattr-ModbusmaCtrlMsgType` required
     :name,72:		Function Name

   * :val:	3
     :count:	Yes
     :type:	No
     :name:	[:lemonobgtext:`Read Holding Registers`] message reads contents of one or more outstation registers.
		Number of registers to read is set by the :ref:`xmlattr-ModbusmaCtrlMsgCount` attribute.

   * :val:	4
     :count:	Yes
     :type:	No
     :name:	[:lemonobgtext:`Read Input Registers`] message reads contents of one or more outstation registers.
		Number of registers to read is set by the :ref:`xmlattr-ModbusmaCtrlMsgCount` attribute.

   * :val:	5
     :count:	No
     :type:	Yes
     :name:	[:lemonobgtext:`Force Single Coil`] message writes data to a single outstation register (2 bytes).

   * :val:	6
     :count:	No
     :type:	Yes
     :name:	[:lemonobgtext:`Preset Single Register`] message writes data to a single outstation register (2 bytes).

   * :val:	16
     :count:	No
     :type:	Yes
     :name:	[:lemonobgtext:`Preset Multiple Registers`] message writes data to multiple outstation registers (up to 126 bytes).
		Number of registers to write is determined by the :ref:`xmlattr-ModbusmaCtrlMsgData` attribute.

   * :val:	Other
     :count:	---
     :type:	---
     :name:	Function is not supported

Ctrl MSG.Type
^^^^^^^^^^^^^

.. field-list-table:: Modbus Master Control message types
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusCtrlMsgType
   :spec: |C{0.07}|S{0.93}|
   :header-rows: 1

   * :val,10,center:	:ref:`xmlattr-ModbusmaCtrlMsgType`
     :desc,90:		Description

   * :val:	0
     :desc:	Send contents of the :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgData` attribute to outstation.

   * :val:	1
     :desc:	| Set or Clear one bit in the initial data that's position is specified by the :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOBitOffset` attribute. Inversion enable :ref:`bitref-ModbusmaDOQualifierBit0` in :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOQualifier` selects if the bit is going to be set or cleared.
		| Inversion disabled (:ref:`bitref-ModbusmaDOQualifierBit0`\ |bitfalse| in :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOQualifier`) initial data value will be 0x0000 and one bit will be set.
		| Inversion enabled (:ref:`bitref-ModbusmaDOQualifierBit0`\ |bittrue| in :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOQualifier`) initial data value will be 0xFFFF and one bit will be cleared.
		| :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgData` attribute is ignored.
		| :inlineimportant:`This type can be used only for` :ref:`xmlelem-ModbusmaDO` :inlineimportant:`control messages, it is not supported for` :ref:`xmlelem-ModbusmaAO`\.

   * :val:	33
     :desc:	Encode data as 16bit Unsigned Integer big endian.
		For example value '65297' will be encoded to Modbus message as {01 06 ... **FF 11** ...}

   * :val:	34
     :desc:	Encode data as 16bit Signed Integer big endian.
		For example value '-239' will be encoded to Modbus message as {01 06 ... **FF 11** ...}

   * :val:	35
     :desc:	Encode data as 16bit Unsigned Integer little endian.
		For example value '65297' will be encoded to Modbus message as {01 06 ... **11 FF** ...}

   * :val:	36
     :desc:	Encode data as 16bit Signed Integer little endian.
		For example value '-239' will be encoded to Modbus message as {01 06 ... **11 FF** ...}

   * :val:	37
     :desc:	Encode data as 32bit Unsigned Integer byte order [3210].
		For example value '65541' will be encoded to Modbus message as {01 10 ... **00 01 00 05** ...}

   * :val:	38
     :desc:	Encode data as 32bit Signed Integer byte order [3210].
		For example value '-65275' will be encoded to Modbus message as {01 10 ... **FF FF 01 05** ...}

   * :val:	39
     :desc:	Encode data as 32bit Unsigned Integer byte order [1032].
		For example value '327681' will be encoded to Modbus message as {01 10 ... **00 01 00 05** ...}

   * :val:	40
     :desc:	Encode data as 32bit Signed Integer byte order [1032].
		For example value '-65275' will be encoded to Modbus message as {01 10 ... **01 05 FF FF** ...}

   * :val:	41
     :desc:	Encode data as 32bit Unsigned Integer byte order [2301].
		For example value '16778496' will be encoded to Modbus message as {01 10 ... **00 01 00 05** ...}

   * :val:	42
     :desc:	Encode data as 32bit Signed Integer byte order [2301].
		For example value '-64255' will be encoded to Modbus message as {01 10 ... **FF FF 01 05** ...}

   * :val:	43
     :desc:	Encode data as 32bit Unsigned Integer byte order [0123].
		For example value '83886336' will be encoded to Modbus message as {01 10 ... **00 01 00 05** ...}

   * :val:	44
     :desc:	Encode data as 32bit Signed Integer byte order [0123].
		For example value '-64255' will be encoded to Modbus message as {01 10 ... **01 05 FF FF** ...}

   * :val:	65
     :desc:	Encode data as Short floating point number byte order [3210].
		For example value '2.001007' will be encoded to Modbus message as {01 10 ... **40 00 10 80** ...}

   * :val:	66
     :desc:	Encode data as Short floating point number byte order [1032].
		For example value '2.001007' will be encoded to Modbus message as {01 10 ... **10 80 40 00** ...}

   * :val:	67
     :desc:	Encode data as Short floating point number byte order [2301].
		For example value '2.001007' will be encoded to Modbus message as {01 10 ... **00 40 80 10** ...}

   * :val:	68
     :desc:	Encode data as Short floating point number byte order [0123].
		For example value '2.001007' will be encoded to Modbus message as {01 10 ... **80 10 00 40** ...}

   * :val:	97
     :desc:	Encode data as 16bit Binary Coded Decimal (BCD) big endian.
		For example value '1234' will be encoded to Modbus message as {01 06 ... **12 34** ...}

   * :val:	98
     :desc:	Encode data as 16bit Binary Coded Decimal (BCD) little endian.
		For example value '3412' will be encoded to Modbus message as {01 06 ... **12 34** ...}

   * :val:	Other
     :desc:	Not used

.. important:: If read message (:ref:`xmlattr-ModbusmaCtrlMsgFunc`\ ="3" or :ref:`xmlattr-ModbusmaCtrlMsgFunc`\ ="4") is used, received data will be decoded based on
	 the :ref:`xmlattr-ModbusmaCtrlMsgType` attribute of the following/preceding write message. I.e. the same way as data would be encoded for the write message.
         :ref:`xmlattr-ModbusmaCtrlMsgType` attribute must not be used for read messages.

Compatibility
^^^^^^^^^^^^^

Table below shows compatibility between :ref:`xmlattr-ModbusmaCtrlMsgFunc` and :ref:`xmlattr-ModbusmaCtrlMsgType` attributes and
whether :ref:`xmlattr-ModbusmaCtrlMsgData` attribute must be specified when particular message type is used.

.. field-list-table:: Modbus Master Control message attribute compatibility
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusmaCtrlMsgCompatibility
   :spec: |C{0.07}|C{0.12}|C{0.12}|S{0.69}|
   :header-rows: 1

   * :val,10,center:	:ref:`xmlattr-ModbusmaCtrlMsgFunc`
     :type,10,center:	:ref:`xmlattr-ModbusmaCtrlMsgType`
     :data,10,center:	:ref:`xmlattr-ModbusmaCtrlMsgData`
     :name,70:		Description

   * :val:	3;4
     :type:	n/a
     :data:	n/a
     :name:	| Read message reads contents of the outstation register. Read message has 2 purposes depending on its relation to a write message:
		| 1/ Read message is followed by a write message. In this case data read from outstation can be modified and sent to outstation with the following write message.
		| 2/ Write message is followed by a read message. In this case data sent to outstation with a preceding write message can be verified with this read message.
		| Both options can be used in the same sequence, i.e. read-write-read(verify) sequence of messages is allowed.

   * :val:	5;6
     :type:	0
     :data:	Data to send
     :name:	Write message with contents of the :ref:`xmlattr-ModbusmaCtrlMsgData` attribute will be sent to outstation.

   * :(val):
     :type:	1
     :data:	n/a
     :name:	| :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="1" :inlineimportant:`can be used only for` :ref:`xmlelem-ModbusmaDO` :inlineimportant:`control messages, it is not supported for` :ref:`xmlelem-ModbusmaAO`\.
		| One bit in the initial data, that's position is specified by the :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOBitOffset` attribute, will be set or cleared. Initial data value (before modifying the bit) can either be received from outstation in a preceding read message or will be set up automatically depending on inversion enable :ref:`bitref-ModbusmaDOQualifierBit0` in :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOQualifier`.
		| Inversion disabled (:ref:`bitref-ModbusmaDOQualifierBit0`\ |bitfalse| in :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOQualifier`) initial data value will be 0x0000 and one bit will be set.
		| Inversion enabled (:ref:`bitref-ModbusmaDOQualifierBit0`\ |bittrue| in :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOQualifier`) initial data value will be 0xFFFF and one bit will be cleared.

   * :(val):
     :type:	33;34;35;36
     :data:	Optional
     :name:	| Behavior depends on whether the message is used for DO or AO:
		| :ref:`xmlelem-ModbusmaDO`\ : ON command adds :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents to the initial data value. OFF command subtracts :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents from the initial data value. Initial data value can either be received from outstation in a preceding read message or specified in the :ref:`xmlattr-ModbusmaCtrlMsgData` attribute e.g. :ref:`xmlattr-ModbusmaCtrlMsgData`\ ="0x0000".
		| :ref:`xmlelem-ModbusmaAO`\ : value received from upstream station will be written to outstation.
		| Outgoing data will be encoded as a 16bit Integer, see :numref:`tabid-ModbusCtrlMsgType` for details.

   * :(val):
     :type:	97;98
     :data:	Optional
     :name:	| Behavior depends on whether the message is used for DO or AO:
		| :ref:`xmlelem-ModbusmaDO`\ : ON command adds :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents to the initial data value. OFF command subtracts :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents from the initial data value. Initial data value can either be received from outstation in a preceding read message or specified in the :ref:`xmlattr-ModbusmaCtrlMsgData` attribute e.g. :ref:`xmlattr-ModbusmaCtrlMsgData`\ ="0x0000".
		| :ref:`xmlelem-ModbusmaAO`\ : value received from upstream station will be written to outstation.
		| Outgoing data will be encoded as a 16bit Binary Coded Decimal (BCD), see :numref:`tabid-ModbusCtrlMsgType` for details.

   * :val:	16
     :type:	0
     :data:	Data to send
     :name:	Write message with contents of the :ref:`xmlattr-ModbusmaCtrlMsgData` attribute will be sent to outstation.

   * :(val):
     :type:	1
     :data:	n/a
     :name:	| :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="1" :inlineimportant:`can be used only for` :ref:`xmlelem-ModbusmaDO` :inlineimportant:`control messages, it is not supported for` :ref:`xmlelem-ModbusmaAO`\.
		| One bit in the initial data, that's position is specified by the :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOBitOffset` attribute, will be set or cleared. Initial data value (before modifying the bit) can either be received from outstation in a preceding read message or will be set up automatically depending on inversion enable :ref:`bitref-ModbusmaDOQualifierBit0` in :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOQualifier`.
		| Inversion disabled (:ref:`bitref-ModbusmaDOQualifierBit0`\ |bitfalse| in :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOQualifier`) initial data value will be 0x0000 and one bit will be set.
		| Inversion enabled (:ref:`bitref-ModbusmaDOQualifierBit0`\ |bittrue| in :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOQualifier`) initial data value will be 0xFFFF and one bit will be cleared.

   * :(val):
     :type:	33;34;35;36
     :data:	Optional
     :name:	| Behavior depends on whether the message is used for DO or AO:
		| :ref:`xmlelem-ModbusmaDO`\ : ON command adds :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents to the initial data value. OFF command subtracts :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents from the initial data value. Initial data value can either be received from outstation in a preceding read message or specified in the :ref:`xmlattr-ModbusmaCtrlMsgData` attribute e.g. :ref:`xmlattr-ModbusmaCtrlMsgData`\ ="0x0000".
		| :ref:`xmlelem-ModbusmaAO`\ : value received from upstream station will be written to outstation.
		| Outgoing data will be encoded as a 16bit Integer, see :numref:`tabid-ModbusCtrlMsgType` for details.

   * :(val):
     :type:	37;38;39;40;41;42;43;44
     :data:	0x00000000
     :name:	| Behavior depends on whether the message is used for DO or AO:
		| :ref:`xmlelem-ModbusmaDO`\ : ON command adds :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents to the initial data value. OFF command subtracts :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents from the initial data value. Initial data value can either be received from outstation in a preceding read message or specified in the :ref:`xmlattr-ModbusmaCtrlMsgData` attribute e.g. :ref:`xmlattr-ModbusmaCtrlMsgData`\ ="0x0000".
		| :ref:`xmlelem-ModbusmaAO`\ : value received from upstream station will be written to outstation.
		| Outgoing data will be encoded as a 32bit Integer, see :numref:`tabid-ModbusCtrlMsgType` for details.
		| :ref:`xmlattr-ModbusmaCtrlMsgData` :inlineimportant:`attribute must always be present for these message types. Even if its contents are not used, the length of data (2 registers or 4 bytes) instructs Modbus master instance that 2 registers need to be written.`

   * :(val):
     :type:	65;66;67;68
     :data:	0x00000000
     :name:	| Behavior depends on whether the message is used for DO or AO:
		| :ref:`xmlelem-ModbusmaDO`\ : ON command adds :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents to the initial data value. OFF command subtracts :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents from the initial data value. Initial data value can either be received from outstation in a preceding read message or specified in the :ref:`xmlattr-ModbusmaCtrlMsgData` attribute e.g. :ref:`xmlattr-ModbusmaCtrlMsgData`\ ="0x0000".
		| :ref:`xmlelem-ModbusmaAO`\ : value received from upstream station will be written to outstation.
		| Outgoing data will be encoded as a Short floating point number, see :numref:`tabid-ModbusCtrlMsgType` for details.
		| :ref:`xmlattr-ModbusmaCtrlMsgData` :inlineimportant:`attribute must always be present for these message types. Even if its contents are not used, the length of data (2 registers or 4 bytes) instructs Modbus master instance that 2 registers need to be written.`

   * :(val):
     :type:	97;98
     :data:	Optional
     :name:	| Behavior depends on whether the message is used for DO or AO:
		| :ref:`xmlelem-ModbusmaDO`\ : ON command adds :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents to the initial data value. OFF command subtracts :ref:`xmlelem-ModbusmaDO`.\ :ref:`xmlattr-ModbusmaDOStep` attribute contents from the initial data value. Initial data value can either be received from outstation in a preceding read message or specified in the :ref:`xmlattr-ModbusmaCtrlMsgData` attribute e.g. :ref:`xmlattr-ModbusmaCtrlMsgData`\ ="0x0000".
		| :ref:`xmlelem-ModbusmaAO`\ : value received from upstream station will be written to outstation.
		| Outgoing data will be encoded as a 16bit Binary Coded Decimal (BCD), see :numref:`tabid-ModbusCtrlMsgType` for details.

   * :val:	Other
     :type:	---
     :data:	---
     :name:	Function is not supported

.. tip::

   Please refer to sections :ref:`docref-ModbusmaDOsamples` and :ref:`docref-ModbusmaAOsamples` for configuration and Modbus message samples.

