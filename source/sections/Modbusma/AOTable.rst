
.. _xmlgroup-ModbusmaAO: lelabel=AOTable
.. _xmlelem-ModbusmaAO: lelabel=AO

AOTable group
-------------

.. include-file:: sections/Include/ma_DOAO_table.rstinc "" ":ref:`xmlgroup-ModbusmaAO`" ":ref:`xmlelem-ModbusmaAO`" ":numref:`tabid-ModbusmaAO`" ":ref:`docref-IEC10xslAO`" "AO" "setpoint" "outstation"

Please see sample :ref:`xmlgroup-ModbusmaAO` group and :ref:`xmlelem-ModbusmaAO` element nodes below.
There are 4 setpoint commands defined with 4 :ref:`xmlelem-ModbusmaAO` element nodes.

.. code-block:: none

   <AOTable>
	<AO Index="0" CtrlMsg="1" Coeff="1"/>
	<AO Index="1" CtrlMsg="1" Coeff="*1"/>
	<AO Index="2" CtrlMsg="1" Qualifier="0x01" />
	<AO Index="3" CtrlMsg="1" Coeff="4.2"/>
   </AOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaAO`"

.. code-block:: none

   <AO Index="0" CtrlMsg="1" Qualifier="0x00" Coeff="1.2" Name="Regulate 1" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-ModbusmaAO`"

AO attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaAO" "Modbus Master AO attributes" ":spec: |C{0.14}|C{0.14}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "AO"

.. include-file:: sections/Include/Modbusma_CtrlMsg.rstinc ""

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-ModbusmaAOQualifier`"

.. include-file:: sections/Include/AO_Coeff.rstinc ""

.. include-file:: sections/Include/hidden_ModbusAOPLCcondId.rstinc "internal"

.. include-file:: sections/Include/Name.rstinc ""

AO.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-ModbusmaAOQualifier" "Modbus Master AO internal qualifier" ":ref:`xmlattr-ModbusmaAOQualifier`" "AO internal qualifier"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	**Send** AO value to outstation

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	**Add/Subtract** AO value to the value received from outstation.
		In order to use this functionality current register value must be read from outstation with :ref:`xmlattr-ModbusmaCtrlMsgFunc`\ ="3" or :ref:`xmlattr-ModbusmaCtrlMsgFunc`\ ="4" message.

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	AO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AO is **disabled**, command will not be sent to outstation

   * :attr:	Bits 1..6
     :val:	Any
     :desc:	Bits reserved for future use

.. _docref-ModbusmaAOsamples:

AO samples
^^^^^^^^^^

**Example 1:**

Configuration below has a [:lemonobgtext:`Preset Single Register`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="33".
If a setpoint value e.g. '516' is received from upstream station, it will be encoded as 16bit Unsigned Integer 0x0204 and written to outstation register 0x0305.

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="6" Reg="0x0305" Type="33" Name="Write register 0x0305"/>
   </CtrlMessages>
   <AOTable>
	<AO Index="0" CtrlMsg="1" Name="AO as 16bit Integer"/>
   </AOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 06 03 05 02 04 ...
   COMM -> 01 06 03 05 02 04 ...

|
| **Example 2:**

Configuration below has a [:lemonobgtext:`Preset Multiple Registers`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="37".
If a setpoint value e.g. '516' is received from upstream station, it will be multiplied by coefficeint '2.5' first.
The result '1290' will be encoded as 32bit Unsigned Integer 0x0000050A and written to outstation registers 0x0305 and 0x0306.
.. include-file:: sections/Include/Modbusma_CtrlData.rstinc ""

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="16" Reg="0x0305" Data="0x00000000" Type="37" Name="Write registers 0x0305 and 0x0306"/>
   </CtrlMessages>
   <AOTable>
	<AO Index="0" CtrlMsg="1" Coeff="2.5" Name="AO as 32bit Integer"/>
   </AOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 10 03 05 00 02 04 00 00 05 0A ...
   COMM -> 01 10 03 05 00 02 ...

|
| **Example 3:**

Configuration below has a [:lemonobgtext:`Preset Single Register`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="35" that follows a [:lemonobgtext:`Read Holding Registers`] message.
A setpoint value received from upstream station will be added to initial data value received from outstation, because Add/Subtract bit is enabled :ref:`xmlattr-ModbusmaAOQualifier`\ ="0x01".
Data read from outstation 0x0602 in this example will be decoded as 16bit Unsigned Integer '518'.
If a setpoint value e.g. '5' is received from upstream station, it will be added to '518'.
The result '523' will be encoded as 16bit Unsigned Integer 0x0B02 and written to outstation register 0x0305.

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="3" Reg="0x0305" Count="1" Name="Read register 0x0305"/>
	<MSG CtrlMsg="2" Func="6" Reg="0x0305" Type="35" FollowCtrlMsg="1" Name="Write register 0x0305"/>
   </CtrlMessages>
   <AOTable>
	<AO Index="0" CtrlMsg="1" Qualifier="0x01" Name="AO add to 16bit Integer"/>
   </AOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 03 03 05 00 01 ...
   COMM -> 01 03 02 06 02 ...
   COMM <- 01 06 03 05 0B 02 ...
   COMM -> 01 06 03 05 0B 02 ...

|
| **Example 4:**

Configuration below has a [:lemonobgtext:`Preset Multiple Registers`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="65" which is followed by a [:lemonobgtext:`Read Holding Registers`] message.
If a setpoint value e.g. '3.4' is received from upstream station, it will be encoded as Short floating point number 0x4059999A and written to outstation registers 0x0305 and 0x0306.
.. include-file:: sections/Include/Modbusma_verify.rstinc "" "0x4059999A"
.. include-file:: sections/Include/Modbusma_CtrlData.rstinc ""

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="16" Reg="0x0305" Data="0x00000000" Type="65" Name="Write registers 0x0305 and 0x0306"/>
	<MSG CtrlMsg="2" Func="3" Reg="0x0305" Count="2" FollowCtrlMsg="1" Name="Read and Verify registers 0x0305 and 0x0306"/>
   </CtrlMessages>
   <AOTable>
	<AO Index="0" CtrlMsg="1" Name="AO as Short floating point number"/>
   </AOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 10 03 05 00 02 04 40 59 99 9A ...
   COMM -> 01 10 03 05 00 02 ...
   COMM <- 01 03 03 05 00 02 ...
   COMM -> 01 03 04 40 59 99 9A ...

|
| **Example 5:**

Configuration below has a [:lemonobgtext:`Preset Single Register`] message with :ref:`xmlelem-ModbusmaCtrlMsg`.\ :ref:`xmlattr-ModbusmaCtrlMsgType`\ ="34" which is preceded and followed by [:lemonobgtext:`Read Holding Registers`] messages.
A setpoint value received from upstream station will be added to initial data value received from outstation, because Add/Subtract bit is enabled :ref:`xmlattr-ModbusmaAOQualifier`\ ="0x01".
Data read from outstation 0xFFFE in this example will be decoded as 16bit Signed Integer '-2'.
If a setpoint value e.g. '6' is received from upstream station, it will be added to '-2'.
The result '4' will be encoded as 16bit Signed Integer 0x0004 and written to outstation register 0x0305.
.. include-file:: sections/Include/Modbusma_verify.rstinc "" "0x0004"

.. code-block:: none

   <CtrlMessages>
	<MSG CtrlMsg="1" Func="3" Reg="0x0305" Count="1" Name="Read register 0x0305"/>
	<MSG CtrlMsg="2" Func="6" Reg="0x0305" Type="34" FollowCtrlMsg="1" Name="Write register 0x0305"/>
	<MSG CtrlMsg="3" Func="3" Reg="0x0305" Count="1" FollowCtrlMsg="2" Name="Read and Verify register 0x0305"/>
   </CtrlMessages>
   <AOTable>
	<AO Index="0" CtrlMsg="1" Qualifier="0x01" Name="AO add to 16bit Integer"/>
   </AOTable>

Modbus RTU communication to outstation may contain the following:

.. code-block:: none

   COMM <- 01 03 03 05 00 01 ...
   COMM -> 01 03 02 FF FE ...
   COMM <- 01 06 03 05 00 04 ...
   COMM -> 01 06 03 05 00 04 ...
   COMM <- 01 03 03 05 00 01 ...
   COMM -> 01 03 02 00 04 ...

