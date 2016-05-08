
.. _ref-ModbusmaAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-ModbusmaAI>` and child element nodes :ref:`AI<ref-ModbusmaAI>` are used to create AI information objects to receive analog information from the downstream outstation.
Each created AI can be used as a source for any AI information object defined in the IO table of any Slave protocol instance.
Analog data received from the outstation will be forwarded to the AI information object of the Slave protocol instance and then to the upstream Master station.
Please refer to the section :ref:`docref-IEC10xslAITable` for more information on how to use AI information object as a source.

.. tip:: \ :ref:`AITable<ref-ModbusmaAI>` group and :ref:`AI<ref-ModbusmaAI>` element nodes are optional if hardcoded Modbus device :ref:`<ref-ModbusmaHardcodedType>` is used. AI information objects will be automatically initialized for these devices.

Please see sample :ref:`AITable<ref-ModbusmaAI>` group and :ref:`AI<ref-ModbusmaAI>` child element nodes below.
There are 5 AI information objects configured using 4 :ref:`AI<ref-ModbusmaAI>` element nodes.

.. code-block:: none

   <AITable>
	<AI Index="0" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" Qualifier="0x00" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" Qualifier="0x00" Coeff="-17.0" Percent="1.4"/>
	<AI Index="3" Qualifier="0x00" Coeff="0.08" Total="2"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AI<ref-ModbusmaAI>`"

.. code-block:: none

   <AI Index="0" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" Total="2" Name="Feeder current" />

.. tip:: Attributes of the :ref:`AI<ref-ModbusmaAI>` element node can be arranged in any order, it will not affect XML file validation.         

AI attributes
^^^^^^^^^^^^^

.. _ref-ModbusmaAIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master AI attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-ModbusmaAIIndex:" "AI"

   * :attr:     .. _ref-ModbusmaAIQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		:inlinetip:`Attribute is not implemented currently and reserved for future use.`

.. include-file:: sections/Include/AI_Coeff.rstinc "" ".. _ref-ModbusmaAICoeff:"

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ".. _ref-ModbusmaAIDeadband:" ".. _ref-ModbusmaAIPercent:"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ".. _ref-ModbusmaAIStartOffset:" ".. _ref-ModbusmaAIZeroDeadband:" ".. _ref-ModbusmaAIOffset:" ".. _ref-ModbusmaAIOffsetDeadband:" ".. _ref-ModbusmaAINonZeroOffset:"

.. include-file:: sections/Include/Modbusma_Total.rstinc "" ".. _ref-ModbusmaAITotal:" "AI" ":ref:`<ref-ModbusmaAIIndex>`" ":ref:`AI<ref-ModbusmaAI>`"

.. include-file:: sections/Include/Name.rstinc ""

.. tip::

   \* Please refer to annex :ref:`docref-ReceivedAIProcessing` for additional information on AI processing 
   options and application examples using :ref:`<ref-ModbusmaAIDeadband>` \ and :ref:`<ref-ModbusmaAIPercent>` \ attributes.
   Annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` for additional information on AI scaling.
