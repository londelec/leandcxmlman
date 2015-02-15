
.. _docref-IEC10xslAITable:
.. _ref-IEC10xslAITable:
.. _ref-IEC10xslAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-IEC10xslAITable>` and child element nodes :ref:`AI<ref-IEC10xslAI>` are used to create AI information objects to send static 
analogue values and analog events to the upstream Master station. Each created AI information object needs to 
have a source of information. The source is created by linking AI information object to an :ref:`AI<ref-IEC10xslAI>` node of any Master 
protocol instance that is defined in leandc. (Master protocol instances are defined under :ref:`CommunicationCfg<ref-CommunicationCfg>` 
node in **leandc.xml** file)

The link is created using :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Device<ref-IEC10xslAIDevice>` \ and :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Index<ref-IEC10xslAIIndex>` \ attributes. The first step is to select the **source Master 
protocol instance**, use value of the :ref:`Index<ref-IEC101maIndex>` attribute of any Master protocol instance. The next step is to select 
the source AI object, use value of the :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Index<ref-IEC10xslAIIndex>` \ attribute of any AI object listed in the IO object table of a 
Master protocol instance. Enter the selected values of **source Master protocol instance** in :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Device<ref-IEC10xslAIDevice>` \ 
attribute and **source AI object** in :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Index<ref-IEC10xslAIIndex>` \ attribute.

Information address (IOA) for sending AI information object upstream is entered in :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Device<ref-IEC10xslAIInfAddr>` \ attribute.

Please see sample :ref:`AITable<ref-IEC10xslAITable>` group node and :ref:`AI<ref-IEC10xslAI>` child element nodes below. There are 5 AI information objects 
configured using 4 :ref:`AI<ref-IEC10xslAI>` element nodes.

.. code-block:: none

   <AITable>
	<AI Device="10" Index="0" InfAddr="1" qualifier="0x20" Coeff="1.0" Offset="28.0" … /> 
	<AI Device="10" Index="1" InfAddr="2" qualifier="0x00" ZeroDeadband="1.0" … />
	<AI Device="10" Index="2" InfAddr="3" qualifier="0x01" Coeff="0.05" GroupMask="0x0002" … />
	<AI Device="10" Index="3" InfAddr="4" qualifier="0x00" Coeff="1.0" Offset="2.0" Total="2" … />
   </AITable>
   
Please see sample :ref:`AI<ref-IEC10xslAI>` element node below listing all available attributes.
            
.. code-block:: none
            
   <AI  Device="10"
  	Index="2"
	InfAddr="3"
	qualifier="0"
	Coeff="100.0"
	StartOffset="6554"
	ZeroDeadband="5.0"
	Offset="-2.0"
	OffsetDeadband="2.0"
	NonZeroOffset="200.0"
	GroupMask="0x0002"
	TypeID="13"
	Total="2"
	Name="Feeder current" />
      
.. tip:: Attributes of the :ref:`AI<ref-IEC10xslAI>` element node can be arranged in any order, it will not affect the XML file validation.         

AI attributes
^^^^^^^^^^^^^

.. _ref-IEC10xslAIAttributes:

.. field-list-table:: IEC 60870-5-101/104 Slave AI attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC10xslAIDevice:
               
               :xmlref:`Device`
     :val:     1...254
     :desc:    Source communication protocol instance. Any Master protocol instance listed in :ref:`CommunicationCfg<ref-CommunicationCfg>` group can be used as a source. Use value of the Master protocol instance :ref:`Index<ref-IEC101maIndex>` attribute in order to link AI to it. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`IEC101sl<ref-IEC101sl>`.\ :ref:`Source<ref-IEC101slSource>` \ or :ref:`IEC104sl<ref-IEC104sl>`.\ :ref:`Source<ref-IEC104slSource>` \ :inlinetip:`attributes will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAIIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Source AI object. Any AI element node of the selected Master protocol instance can be used as a source. Use value of the :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`Index<ref-IEC10xmaAIIndex>` \ attribute of any AI object listed in the IO table of the selected Master protocol instance. :inlinetip:`Indexes don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xslAIInfAddr:
   
               :xmlref:`InfAddr`
     :val:     1...16777215
     :desc:    Information Object Address (IOA) of the AI object. This IOA will be used to send object to upstream Master station. :inlinetip:`Addresses don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xslAIqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC10xslAIqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC10xslAIqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAICoeff:
   
               :xmlref:`Coeff`
     :val:     ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Coefficient to multiply the analog object value before sending to upstream Master station. (default value 1) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAIStartOffset:
   
               :xmlref:`StartOffset`\*
     :val:     0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Scale start offset to compensate e.g. 4-20mA transducer output range. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAIZeroDeadband:
   
               :xmlref:`ZeroDeadband`\*
     :val:     0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Zero Deadband allows to filter noise by forcing small fluctuating AI values to 0. If an absolute value (+/-) of the received AI is less than :xmlref:`ZeroDeadband` attribute, AI value will be forced to 0. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAIOffset:
   
               :xmlref:`Offset`\*
     :val:     0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Offset AI value **after** :xmlref:`ZeroDeadband` has been applied. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAIOffsetDeadband:
   
               :xmlref:`OffsetDeadband`\*
     :val:     0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Offset Zero Deadband allows to filter noise around 0 value **after** applying :xmlref:`Offset`. If an absolute value (+/-) after offsetting is less than :xmlref:`OffsetDeadband` attribute, AI value will be forced to 0. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAINonZeroOffset:
   
               :xmlref:`NonZeroOffset`\*
     :val:     0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Offset only non-zero values **after** :xmlref:`ZeroDeadband`; :xmlref:`Offset` and :xmlref:`OffsetDeadband` has been applied. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAIGroupMask:
   
               :xmlref:`GroupMask`
     :val:     0...0xFFFF
     :desc:    Include object in Interrogation group/groups. Each bit of the group mask attribute needs to be set in order to include object in a particular interrogation group. Please refer to the table :numref:`ref-IEC10xslGroupMask` for more information. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAITypeID:
   
               :xmlref:`TypeID`
     :val:     See table :numref:`ref-IEC10xslAITypeIDValues` for description
     :desc:    Use this ASDU Type to send a AI event. Attribute also affects ASDU type of the static data (e.g. Normalized, Scaled, Short floating point value) being reported to General interrogation request (default value depends on the protocol type, refer to table :numref:`ref-IEC10xslAITypeIDValues`). :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAITotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Index<ref-IEC10xslAIIndex>` \ and :ref:`AI<ref-IEC10xslAI>`.\ :ref:`InfAddr<ref-IEC10xslAIInfAddr>` \ attribute values without a need to create individual :ref:`AI<ref-IEC10xslAI>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`AI<ref-IEC10xslAI>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAIName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

.. tip::

   \* Please refer to annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` 
   for additional information on AI scaling and application examples using :ref:`AI<ref-IEC10xslAI>`.\ :ref:`StartOffset<ref-IEC10xslAIStartOffset>` \; 
   :ref:`AI<ref-IEC10xslAI>`.\ :ref:`ZeroDeadband<ref-IEC10xslAIZeroDeadband>` \; :ref:`AI<ref-IEC10xslAI>`.\ :ref:`Offset<ref-IEC10xslAIOffset>` \; :ref:`AI<ref-IEC10xslAI>`.\ :ref:`OffsetDeadband<ref-IEC10xslAIOffsetDeadband>` \; :ref:`AI<ref-IEC10xslAI>`.\ :ref:`NonZeroOffset<ref-IEC10xslAINonZeroOffset>` \ attributes.

AI.qualifier
^^^^^^^^^^^^
.. _ref-IEC10xslAIqualifierBits:

.. field-list-table:: IEC 60870-5-101/104 Slave AI internal qualifier
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.25}|C{0.25}|S{0.5}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Values
     :desc,80: Description

   * :attr:    qualifier [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    AI internal qualifier has 8 data bits

   * :attr:    Bit 0\*
     :val:     xxxx.xxx0
     :desc:    :ref:`AI<ref-IEC10xslAI>`.\ :ref:`StartOffset<ref-IEC10xslAIStartOffset>` \ attribute will be used for AI scaling.

   * :(attr):
     :val:     xxxx.xxx1
     :desc:    Fixed offset (6554) will be loaded to :ref:`AI<ref-IEC10xslAI>`.\ :ref:`StartOffset<ref-IEC10xslAIStartOffset>` \ attribute in order to compensate 4-20mA transducer output offset. Applies to positive or negative AI values.

   * :attr:    Bit 1
     :val:     xxxx.xx0x
     :desc:    Additional 'Zero' AI event generation **disabled**

   * :(attr):
     :val:     xxxx.xx1x
     :desc:    Additional 'Zero' AI event generation **enabled**. A value 0 event will be internally generated following every sent AI event sent with nonzero value. AI object will always have 0 value in interrogation responses.

   * :attr:    Bit 2
     :val:     xxxx.x0xx
     :desc:    AI events **enabled**. AI event will be sent upstream if event is received from the source communication protocol instance

   * :(attr):
     :val:     xxxx.x1xx
     :desc:    AI events **disabled**

   * :attr:    Bit 3
     :val:     xxxx.0xxx
     :desc:    AI object will be **included** in General Interrogation response

   * :(attr):
     :val:     xxxx.1xxx
     :desc:    AI object will be **excluded** from General Interrogation response
 
   * :attr:    Bit 6
     :val:     x0xx.xxxx
     :desc:    Send AI events upstream with their original value and use **the same value** for Interrogation response and periodic reporting

   * :(attr):
     :val:     x1xx.xxxx
     :desc:    Send AI events upstream with their original value, but use **value 0** for Interrogation response and periodic reporting

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    AI is **enabled** and will be sent upstream

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    AI is **disabled** and will not be sent upstream

   * :attr:    Bits 4;5
     :val:     Any
     :desc:    Bits reserved for future use

.. tip::

   \* Please refer to annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` 
   for additional information on AI scaling and application examples using :ref:`AI<ref-IEC10xslAI>`.\ :ref:`qualifier<ref-IEC10xslAIqualifier>` \ Bit[0].

AI.TypeID
^^^^^^^^^

.. _ref-IEC10xslAITypeIDValues:

.. include:: IEC10xAITypeID.rst
