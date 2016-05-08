
.. _ref-ModbusmaDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-ModbusmaDO>` and child element nodes :ref:`DO<ref-ModbusmaDO>` are used to create DO information objects for sending control commands to the downstream outstation.
Each created DO can be used as a destination for any DO information object defined in the IO table of any Slave protocol instance.
Command execution procedure is as follows: Slave protocol instance receives a control command from the upstream Master station and forwards to the destination DO object.
Current communication protocol instance validates and sends a command to the outstation based on the DO settings configured below.
Please refer to the section :ref:`docref-IEC10xslDOTable` for more information on how to use DO as a destination.

.. tip:: \ :ref:`DOTable<ref-ModbusmaDO>` group and :ref:`DO<ref-ModbusmaDO>` element nodes are optional if hardcoded Modbus device :ref:`<ref-ModbusmaHardcodedType>` is used. DO information objects will be automatically initialized for these devices.

Please see sample :ref:`DOTable<ref-ModbusmaDO>` group and :ref:`DO<ref-ModbusmaDO>` child element nodes below.
There are 5 DO information objects configured using 4 :ref:`DO<ref-ModbusmaDO>` element nodes.

.. code-block:: none

   <DOTable>
	<DO Index="0" Qualifier="0x00"/>
	<DO Index="1" Qualifier="0x10"/>
	<DO Index="2" Qualifier="0x10"/>
	<DO Index="3" Qualifier="0x00" Total="2"/>
   </DOTable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`DO<ref-ModbusmaDO>`"

.. code-block:: none

   <DO Index="0" Qualifier="0x00" PulseDuration="500" Total="2" Name="Transducer mode" />

.. tip:: Attributes of the :ref:`DO<ref-ModbusmaDO>` element node can be arranged in any order, it will not affect XML file validation.         

DO attributes
^^^^^^^^^^^^^

.. _ref-ModbusmaDOAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master DO attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-ModbusmaDOIndex:" "DO"

   * :attr:     .. _ref-ModbusmaDOQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		:inlinetip:`Attribute is not implemented currently and reserved for future use.`

   * :attr:     .. _ref-ModbusmaDOPulseDuration:

                :xmlref:`PulseDuration`
     :val:      1...65535
     :def:      1500 msec
     :desc:     Digital output pulse duration in milliseconds.
		Digital output will be activated when command is sent and automatically released after configured number of milliseconds.

.. include-file:: sections/Include/Modbusma_Total.rstinc "" ".. _ref-ModbusmaDOTotal:" "DO" ":ref:`<ref-ModbusmaDOIndex>`" ":ref:`DO<ref-ModbusmaDO>`"

.. include-file:: sections/Include/Name.rstinc ""
