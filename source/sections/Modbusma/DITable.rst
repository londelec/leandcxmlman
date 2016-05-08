
.. _ref-ModbusmaDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-ModbusmaDI>` and child element nodes :ref:`DI<ref-ModbusmaDI>` are used to create DI information objects to receive status information from the downstream outstation.
Each created DI can be used as a source for any DI information object defined in the IO table of any Slave protocol instance.
Data received from the outstation will be forwarded to the DI information object of the Slave protocol instance and then to the upstream Master station.
Please refer to the section :ref:`docref-IEC10xslDITable` for more information on how to use DI information object as a source.

.. tip:: \ :ref:`DITable<ref-ModbusmaDI>` group and :ref:`DI<ref-ModbusmaDI>` element nodes are optional if hardcoded Modbus device :ref:`<ref-ModbusmaHardcodedType>` is used. DI information objects will be automatically initialized for these devices.

Please see sample :ref:`DITable<ref-ModbusmaDI>` group and :ref:`DI<ref-ModbusmaDI>` child element nodes below.
There are 5 DI information objects configured using 4 :ref:`DI<ref-ModbusmaDI>` element nodes.

.. code-block:: none

   <DITable>
	<DI Index="0" Qualifier="0x00"/>
	<DI Index="1" Qualifier="0x10"/>
	<DI Index="2" Qualifier="0x10"/>
	<DI Index="3" Qualifier="0x00" Total="2"/>
   </DITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DI<ref-ModbusmaDI>`"

.. code-block:: none

   <DI Index="0" Qualifier="0" ChatterFilter="100" Total="2" Name="Transducer mode" />

.. tip:: Attributes of the :ref:`DI<ref-ModbusmaDI>` element node can be arranged in any order, it will not affect XML file validation.

DI attributes
^^^^^^^^^^^^^

.. _ref-ModbusmaDIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master DI attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-ModbusmaDIIndex:" "DI"

   * :attr:     .. _ref-ModbusmaDIQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		:inlinetip:`Attribute is not implemented currently and reserved for future use.`

   * :attr:     .. _ref-ModbusmaDIChatterFilter:

                :xmlref:`ChatterFilter`
     :val:      1...65535
     :def:      50 msec
     :desc:     Chatter filter in milliseconds for Digital Inputs.
		State change of the digital input will be reported only if remains stable for the period that exceeds configured filter.

.. include-file:: sections/Include/Modbusma_Total.rstinc "" ".. _ref-ModbusmaDITotal:" "DI" ":ref:`<ref-ModbusmaDIIndex>`" ":ref:`DI<ref-ModbusmaDI>`"

.. include-file:: sections/Include/Name.rstinc ""
