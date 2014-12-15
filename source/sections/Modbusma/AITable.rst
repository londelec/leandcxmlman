
.. _ref-ModbusmaAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-ModbusmaAI>` and child element nodes :ref:`AI<ref-ModbusmaAI>` are used to create AI information objects to receive analog 
information from downstream outstation. Each created AI information object can be used as source of 
information for any AI information object defined in IO table of the Slave protocol instances. If used as a source, 
analog information received from an outstation will be forwarded to AI information object of the Slave protocol 
instance and then to the upstream Master station. Please refer to
section :ref:`docref-IEC10xslAITable` for more information on how to use AI information object as a source.

.. tip:: \ :ref:`AITable<ref-ModbusmaAI>` group and :ref:`AI<ref-ModbusmaAI>` element nodes are optional if hardcoded Modbus device :ref:`Type<ref-ModbusmaHardcodedType>` is used. AI information objects will be automatically initialized for these devices.

Please see sample :ref:`AITable<ref-ModbusmaAI>` group node and :ref:`AI<ref-ModbusmaAI>` child element nodes below. There are 5 AI information objects 
configured using 4 :ref:`AI<ref-ModbusmaAI>` element nodes.

.. code-block:: none

   <AITable> 
	<AI Index="0" qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" qualifier="0x00" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" qualifier="0x00" Coeff="-17.0" Percent="1.4"/>
	<AI Index="3" qualifier="0x00" Coeff="0.08" Total="2"/>
   </AITable>
   
Please see sample :ref:`AI<ref-ModbusmaAI>` element node below listing all available attributes.
            
.. code-block:: none
            
   <AI  Index="0"
	qualifier="0x20"
	Coeff="1.0"
	Deadband="0.5"
	Percent="0"
	StartOffset="6554"
	ZeroDeadband="3.0"
	Offset="-2.0"
	OffsetDeadband="2.0"
	NonZeroOffset="200.0"
	Total="2"
	Name="Feeder current" />
      
.. tip:: Attributes of the :ref:`AI<ref-ModbusmaAI>` element node can be arranged in any order, it will not affect XML file validation.         

AI attributes
^^^^^^^^^^^^^

.. _ref-ModbusmaAIAttributes:

.. field-list-table:: Modbus Master AI attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-ModbusmaAIIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the AI object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-ModbusmaAIqualifier:
   
               :xmlref:`qualifier`
     :val:     0...255
     :desc:    Internal object qualifier to enable customized data processing. (default value 0) :inlinetip:`Attribute is not implemented currently and reserved for future use.`

   * :attr:    .. _ref-ModbusmaAICoeff:
   
               :xmlref:`Coeff`
     :val:     ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Coefficient to multiply the value of incoming analog object. (default value 1) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ".. _ref-ModbusmaAIDeadband:" ".. _ref-ModbusmaAIPercent:" ":xmlref:`Deadband\*`" ":xmlref:`Percent\*`"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ".. _ref-ModbusmaAIStartOffset:" ".. _ref-ModbusmaAIZeroDeadband:" ".. _ref-ModbusmaAIOffset:" ".. _ref-ModbusmaAIOffsetDeadband:" ".. _ref-ModbusmaAINonZeroOffset:"

   * :attr:    .. _ref-ModbusmaAITotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Sequence of identical AI objects. Attribute is used to create sequence of information objects with consecutive :ref:`Index<ref-ModbusmaAIIndex>` attributes. This eliminates the need to create individual :ref:`AI<ref-ModbusmaAI>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`AI<ref-ModbusmaAI>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-ModbusmaAIName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

.. tip::

   \* Please refer to annex :ref:`docref-ReceivedAIProcessing` for additional information on AI processing 
   options and application examples using :ref:`Deadband<ref-ModbusmaAIDeadband>`\; 
   :ref:`Percent<ref-ModbusmaAIPercent>` attributes.
   Annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` for additional information on AI scaling.

   
