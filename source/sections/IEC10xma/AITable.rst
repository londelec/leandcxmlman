
.. _ref-IEC10xmaAITable:
.. _ref-IEC10xmaAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-IEC10xmaAITable>` and child element nodes :ref:`AI<ref-IEC10xmaAI>` are used to create AI information objects to receive analog 
information from the downstream outstation. Each created AI information object can be used as source of 
information for any AI information object defined in IO table of the Slave protocol instances. If used as a source, 
analog information received from an outstation will be forwarded to AI information object of the Slave protocol 
instance and then to the upstream Master station. Please refer to the 
section :ref:`docref-IEC10xslAITable` for more information on how to use AI information object as a source.

In order to receive analog information from the downstream outstation information object address (IOA) needs 
to be entered in :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`InfAddr<ref-IEC10xmaAIInfAddr>` \ attribute. Analog information is processed when received with any of the following 
ASDU types:
5 [M_ST_NA_1]; 6 [M_ST_TA_1]; 32 [M_ST_TB_1]; 
9 [M_ME_NA_1]; 10 [M_ME_TA_1]; 34 [M_ME_TD_1];
11 [M_ME_NB_1]; 12 [M_ME_TB_1]; 35 [M_ME_TE_1];
13 [M_ME_NC_1]; 14 [M_ME_TC_1]; 36 [M_ME_TF_1]

Please see sample :ref:`AITable<ref-IEC10xmaAITable>` group node and :ref:`AI<ref-IEC10xmaAI>` child element nodes below. There are 5 AI information objects 
configured using 4 :ref:`AI<ref-IEC10xmaAI>` element nodes.

.. code-block:: none

   <AITable> 
	<AI Index="0" InfAddr="1" qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" InfAddr="2" qualifier="0x00" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" InfAddr="3" qualifier="0x00" Coeff="-17.0" Deadband="0" Percent="1.4" TypeID="36"/>
	<AI Index="3" InfAddr="4" qualifier="0x00" Coeff="0.08" Deadband="8" Percent="3" Total="2"/>
   </AITable>
   
Please see sample :ref:`AI<ref-IEC10xmaAI>` element node below listing all available attributes.
            
.. code-block:: none
            
   <AI  Index="0"
	InfAddr="1"
	qualifier="0x20"
	Coeff="1.0"
	Deadband="0.5"
	Percent="0"
	StartOffset="6554"
	ZeroDeadband="3.0"
	Offset="-2.0"
	OffsetDeadband="2.0"
	NonZeroOffset="200.0"
	TypeID="36"
	Total="2"
	Name="Feeder current" />
      
.. tip:: Attributes of the :ref:`AI<ref-IEC10xmaAI>` element node can be arranged in any order, it will not affect the XML file validation.         

AI attributes
^^^^^^^^^^^^^

.. _ref-IEC10xmaAIAttributes:

.. field-list-table:: IEC 60870-5-101/104 Master AI attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC10xmaAIIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the AI object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-IEC10xmaAIInfAddr:
   
               :xmlref:`InfAddr`
     :val:     1...16777215
     :desc:    Information Object Address (IOA) of the AI object. This IOA will be used to receive object from downstream outstation. :inlinetip:`Addresses don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xmaAIqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC10xmaAIqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC10xmaAIqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaAICoeff:
   
               :xmlref:`Coeff`
     :val:     ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Coefficient to multiply the value of incoming analog object. (default value 1) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ".. _ref-IEC10xmaAIDeadband:" ".. _ref-IEC10xmaAIPercent:" ":xmlref:`Deadband\*`" ":xmlref:`Percent\*`"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ".. _ref-IEC10xmaAIStartOffset:" ".. _ref-IEC10xmaAIZeroDeadband:" ".. _ref-IEC10xmaAIOffset:" ".. _ref-IEC10xmaAIOffsetDeadband:" ".. _ref-IEC10xmaAINonZeroOffset:"

   * :attr:    .. _ref-IEC10xmaAITypeID:
   
               :xmlref:`TypeID`
     :val:     See table :numref:`ref-IEC10xmaAITypeIDValues` for description
     :desc:    Use this ASDU type to send a AI object upstream, if transparent ASDU function is enabled in Slave protocol instance using :ref:`ASDUSettings<ref-IEC101slASDUSettings>`.\ :ref:`TranspTypes<ref-IEC101slASDUSettingsTranspTypes>` \ attribute. This ASDU type will be used to report object regardless of the received ASDU type. (There is no default value, attribute must not be specified if not used). :inlinetip:`Attribute is optional and doesn't have to be included in configuration.`

   * :attr:    .. _ref-IEC10xmaAITotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`Index<ref-IEC10xmaAIIndex>` \ and :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`InfAddr<ref-IEC10xmaAIInfAddr>` \ attribute values without a need to create individual :ref:`AI<ref-IEC10xmaAI>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`AI<ref-IEC10xmaAI>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaAIName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

.. tip::

   \* Please refer to annex :ref:`docref-ReceivedAIProcessing` for additional information on AI processing 
   options and application examples using :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`Deadband<ref-IEC10xmaAIDeadband>`\; 
   :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`Percent<ref-IEC10xmaAIPercent>` \ attributes.
   Annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` for additional information on AI scaling.

AI.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xmaAIqualifierBits:

.. field-list-table:: IEC 60870-5-101/104 Master AI internal qualifier
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Values
     :desc,80: Description

   * :attr:    qualifier [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    AI internal qualifier has 8 data bits

   * :attr:    Bit 1
     :val:     xxxx.xx0x
     :desc:    Additional 'Zero' AI event generation **disabled**

   * :(attr):
     :val:     xxxx.xx1x
     :desc:    Additional 'Zero' AI event generation **enabled**. New 0 value event will be generated internally following every:
               / event with a nonzero value received from outstation and
               / event with a nonzero value resulted from a deadband/percent or scaling processing.
               Static AI object will be set to value 0, static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.
   * :attr:    Bit 2
     :val:     xxxx.x0xx
     :desc:    AI event is generated **only** if AI object is received from outstation with a 'spontaneous' Cause Of Transmission ([COT] = 3)

   * :(attr):
     :val:     xxxx.x1xx
     :desc:    AI event is generated **every time** AI object is received from outstation regardless of the Cause Of Transmission. :inlinetip:`This option is only used for backward compatibility.`

   * :attr:    Bit 3
     :val:     xxxx.0xxx
     :desc:    **Use original** timetag when event is received from outstation

   * :(attr):
     :val:     xxxx.1xxx
     :desc:    **Substitute** timetag with local time when event is received from outstation
 
   * :attr:    Bit 6
     :val:     x0xx.xxxx
     :desc:    Process events received from outstation with their original AI value and store **original** value in the static database. Static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.

   * :(attr):
     :val:     x1xx.xxxx
     :desc:    Process events received from outstation with their original value, but store **0 value** in the static database. Static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    AI is **enabled** and will be processed when received

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    AI is **disabled** and will be discarded when received

   * :attr:    Bits 0;4;5
     :val:     Any
     :desc:    Bits reserved for future use

AI.TypeID
^^^^^^^^^

.. _ref-IEC10xmaAITypeIDValues:

.. include:: IEC10xAITypeID.rst
   
