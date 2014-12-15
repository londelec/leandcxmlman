
.. _ref-IEC103maAITable:
.. _ref-IEC103maAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-IEC103maAITable>` and child element nodes :ref:`AI<ref-IEC103maAI>` are used to create AI information objects to receive analog 
information from the downstream outstation. Each created AI information object can be used as source of 
information for any AI information object defined in IO table of the Slave protocol instances. If used as a source, 
analog information received from an outstation will be forwarded to AI information object of the Slave protocol 
instance and then to the upstream Master station. Please refer to the 
section :ref:`docref-IEC10xslAITable` for more information on how to use AI information object as a source.

In order to receive analog information from the downstream outstation function type (FUN) and information 
number (INF) need to be entered in :ref:`AI<ref-IEC103maAI>`.\ :ref:`FUN<ref-IEC103maAIFUN>` \ and :ref:`AI<ref-IEC103maAI>`.\ :ref:`INF<ref-IEC103maAIINF>` \ Attributes. It also essential to select particular 
measurement from the incoming message as IEC 60870-5-103 station sends number of measurands in the 
same message. Particular analog value is selected using :ref:`AI<ref-IEC103maAI>`.\ :ref:`FUN<ref-IEC103maAIMEA>` \ attribute.

Please see sample :ref:`AITable<ref-IEC103maAITable>` group node and :ref:`AI<ref-IEC103maAI>` child element nodes below. There are 5 AI information objects 
configured using 4 :ref:`AI<ref-IEC103maAI>` element nodes.

.. code-block:: none

   <AITable> 
	<AI Index="0" FUN="1" INF="1" MEA="0" qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" FUN="1" INF="1" MEA="5" qualifier="0x00" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" FUN="85" INF="83" MEA="0" qualifier="0x00" Coeff="-17.0" Percent="1.4"/>
	<AI Index="3" FUN="105" INF="103" MEA="0" qualifier="0x00" Coeff="0.08" Total="2"/>
   </AITable>
   
Please see sample :ref:`AI<ref-IEC103maAI>` element node below listing all available attributes.
            
.. code-block:: none
            
   <AI  Index="0"
	FUN="85"
	INF="83"
	MEA="2"
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
      
.. tip:: Attributes of the :ref:`AI<ref-IEC103maAI>` element node can be arranged in any order, it will not affect the XML file validation.         

AI attributes
^^^^^^^^^^^^^

.. _ref-IEC103maAIAttributes:

.. field-list-table:: IEC 60807-5-103 Master AI attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC103maAIIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the AI object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-IEC103maAIFUN:
   
               :xmlref:`FUN`
     :val:     0...255
     :desc:    Function Type (FUN) of the AI object. This FUN will be used to receive object from downstream outstation. :inlinetip:`Function types don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC103maAIINF:
   
               :xmlref:`INF`
     :val:     0...255
     :desc:    Information Number (INF) of the AI object. This INF will be used to receive object from downstream outstation. :inlinetip:`Information numbers don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC103maAIMEA:
   
               :xmlref:`MEA`
     :val:     0...31
     :desc:    Number of the analog value in the received measurement message. Use the :ref:`AI<ref-IEC103maAI>`.\ :ref:`FUN<ref-IEC103maAIMEA>` \ attribute value 0, in order to select the first analog value in the received measurement message. :inlinetip:`Numbers don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC103maAIqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC103maAIqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC103maAIqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC103maAICoeff:
   
               :xmlref:`Coeff`
     :val:     ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Coefficient to multiply the value of incoming analog object. (default value 1) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ".. _ref-IEC103maAIDeadband:" ".. _ref-IEC103maAIPercent:" ":xmlref:`Deadband\*`" ":xmlref:`Percent\*`"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ".. _ref-IEC103maAIStartOffset:" ".. _ref-IEC103maAIZeroDeadband:" ".. _ref-IEC103maAIOffset:" ".. _ref-IEC103maAIOffsetDeadband:" ".. _ref-IEC103maAINonZeroOffset:"

   * :attr:    .. _ref-IEC103maAITotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`AI<ref-IEC103maAI>`.\ :ref:`Index<ref-IEC103maAIIndex>` \ and :ref:`AI<ref-IEC103maAI>`.\ :ref:`MEA<ref-IEC103maAIMEA>` \ attribute values without a need to create individual :ref:`AI<ref-IEC103maAI>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`AI<ref-IEC103maAI>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC103maAIName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

.. tip::

   \* Please refer to annex :ref:`docref-ReceivedAIProcessing` for additional information on AI processing 
   options and application examples using :ref:`AI<ref-IEC103maAI>`.\ :ref:`Deadband<ref-IEC103maAIDeadband>`\; 
   :ref:`AI<ref-IEC103maAI>`.\ :ref:`Percent<ref-IEC103maAIPercent>` \ attributes.
   Annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` for additional information on AI scaling.

AI.qualifier
^^^^^^^^^^^^

.. _ref-IEC103maAIqualifierBits:

.. field-list-table:: IEC 60807-5-103 Master AI internal qualifier
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
     :desc:    AI event is **never** generated when object is received from outstation. This setting doesn't affect events resulting from deadband or percent processing.

   * :(attr):
     :val:     xxxx.x1xx
     :desc:    AI event is generated **every time** AI object is received from outstation. :inlinetip:`This option is only used for backward compatibility.`
 
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

   * :attr:    Bits 0;3;4;5
     :val:     Any
     :desc:    Bits reserved for future use
   
