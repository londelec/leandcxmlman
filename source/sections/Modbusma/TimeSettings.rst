.. _xmlelem-ModbusmaTime:

TimeSettings
^^^^^^^^^^^^

Time settings node is used to construct a message for synchronizing Modbus device's clock.
Modbus communication standard doesn't define a specific function for the purpose of time synchronization,
:lemonobgtext:`Write Multiple registers [16]` is normally used.
However encoding of the date and time in Modbus registers varies greatly from one device to another.
Attributes of the :ref:`xmlelem-ModbusmaTime` node below enable to build a custom Modbus message
where date and time values can be placed in any registers and each formatted in a different way.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaTime`"

.. code-block:: none

   <TimeSettings Func="0x10" Reg="0xAA55" Count="8" YearType="97" MonType="33" DomType="33" DowType="0" HourType="33" MinType="33" SecType="33" YearBitOffset="48" MonBitOffset="32" DomBitOffset="40" DowBitOffset="0" HourBitOffset="16" MinBitOffset="24" SecBitOffset="0"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaTime" "Modbus Master TimeSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/Modbusma_Func.rstinc "" "16"

.. include-file:: sections/Include/Modbusma_Reg.rstinc "" "Data will be written to this register."

.. include-file:: sections/Include/Modbusma_Count.rstinc "" "write to"

.. include-file:: sections/Include/Modbusma_TimeFormat.rstinc "" ":xmlattr:`YearType`" "year"

.. include-file:: sections/Include/Modbusma_TimeFormat.rstinc "" ":xmlattr:`MonType`" "month"

.. include-file:: sections/Include/Modbusma_TimeFormat.rstinc "" ":xmlattr:`DomType`" "day of month"

.. include-file:: sections/Include/Modbusma_TimeFormat.rstinc "" ":xmlattr:`DowType`" "day of week"

.. include-file:: sections/Include/Modbusma_TimeFormat.rstinc "" ":xmlattr:`HourType`" "hour"

.. include-file:: sections/Include/Modbusma_TimeFormat.rstinc "" ":xmlattr:`MinType`" "minute"

.. include-file:: sections/Include/Modbusma_TimeFormat.rstinc "" ":xmlattr:`SecType`" "second"

.. include-file:: sections/Include/Modbusma_Offset.rstinc "" ":xmlattr:`YearBitOffset`" "year"

.. include-file:: sections/Include/Modbusma_Offset.rstinc "" ":xmlattr:`MonBitOffset`" "month"

.. include-file:: sections/Include/Modbusma_Offset.rstinc "" ":xmlattr:`DomBitOffset`" "day of month"

.. include-file:: sections/Include/Modbusma_Offset.rstinc "" ":xmlattr:`DowBitOffset`" "day of week"

.. include-file:: sections/Include/Modbusma_Offset.rstinc "" ":xmlattr:`HourBitOffset`" "hour"

.. include-file:: sections/Include/Modbusma_Offset.rstinc "" ":xmlattr:`MinBitOffset`" "minute"

.. include-file:: sections/Include/Modbusma_Offset.rstinc "" ":xmlattr:`SecBitOffset`" "second"


Table below shows position of a sample value '85' (0x55) in a Modbus message depending on the BitOffset.

.. field-list-table:: Modbus Master Bit Offset sample values
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusmaTimeOffset
   :spec: |C{0.10}|S{0.90}|
   :header-rows: 1

   * :val,10,center:	BitOffset
     :desc,90:		Modbus Message

   * :val:	0
     :desc:	{01 10 ... **00 55** 00 00 ...}

   * :val:	1
     :desc:	{01 10 ... **00 AA** 00 00 ...}

   * :val:	2
     :desc:	{01 10 ... **01 54** 00 00 ...}

   * :val:	3
     :desc:	{01 10 ... **02 A8** 00 00 ...}

   * :val:	4
     :desc:	{01 10 ... **05 50** 00 00 ...}

   * :val:	8
     :desc:	{01 10 ... **55 00** 00 00 ...}

   * :val:	16
     :desc:	{01 10 ... 00 00 **00 55** ...}

   * :val:	24
     :desc:	{01 10 ... 00 00 **55 00** ...}


.. field-list-table:: Modbus Master Time variable encoding types
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusmaTimeTypes
   :spec: |C{0.10}|S{0.90}|
   :header-rows: 1

   * :val,10,center:	Type
     :desc,90:		Description

   * :val:	0
     :desc:	Value is not used

   * :val:	33
     :desc:	Encode value as 16bit Unsigned Integer big endian. 
		For example value '2018' will appear in Modbus message as follows: {01 10 ... **07 E2** ...}

   * :val:	35
     :desc:	Encode value as 16bit Unsigned Integer little endian.
		For example value '2018' will appear in Modbus message as follows: {01 10 ... **E2 07** ...}

   * :val:	97
     :desc:	Encode value as 16bit Binary Coded Decimal (BCD) big endian.
		For example value '2018' will appear in Modbus message as follows: {01 10 ... **20 18** ...}

   * :val:	98
     :desc:	Encode value as 16bit Binary Coded Decimal (BCD) little endian.
		For example value '2018' will appear in Modbus message as follows: {01 10 ... **18 20** ...}

   * :val:	Other
     :desc:	Value is not used

