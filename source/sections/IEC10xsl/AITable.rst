
.. _docref-IEC10xslAITable:
.. _ref-IEC10xslAITable:
.. _ref-IEC10xslAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-IEC10xslAITable>` and child element nodes :ref:`AI<ref-IEC10xslAI>` are used to create AI information objects to send static 
analogue values and analog events to the upstream Master station.
Each created AI information object needs to have a source of information.
The source is created by linking AI information object to an :ref:`AI<ref-IEC10xslAI>` node of any Master protocol instance.
(Master protocol instances are defined in :ref:`CommunicationCfg<ref-CommunicationCfg>` group in **leandc.xml** file)

The link is created using :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAIDevice>` \ and :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAIIndex>` \ attributes.
The first step is to select the **source Master protocol instance**, use value of the :ref:`<ref-IEC101maIndex>` attribute of any Master protocol instance.
The next step is to select the source AI object, use value of the :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAIIndex>` \ attribute of any AI object listed in the IO object table of a Master protocol instance.
Enter the selected values of **source Master protocol instance** in :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAIDevice>` \
attribute and **source AI object** in :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAIIndex>` \ attribute.

Information address (IOA) to send AI information object upstream is specified in :ref:`<ref-IEC10xslAIInfAddr>` \ attribute.

Please see sample :ref:`AITable<ref-IEC10xslAITable>` group and :ref:`AI<ref-IEC10xslAI>` child element nodes below.
There are 5 AI information objects configured using 4 :ref:`AI<ref-IEC10xslAI>` element nodes.

.. code-block:: none

   <AITable>
	<AI Device="10" Index="0" InfAddr="1" qualifier="0x20" Coeff="1.0" Offset="28.0" … /> 
	<AI Device="10" Index="1" InfAddr="2" qualifier="0x00" ZeroDeadband="1.0" … />
	<AI Device="10" Index="2" InfAddr="3" qualifier="0x01" Coeff="0.05" GroupMask="0x0002" … />
	<AI Device="10" Index="3" InfAddr="4" qualifier="0x00" Coeff="1.0" Offset="2.0" Total="2" … />
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AI<ref-IEC10xslAI>`"

.. code-block:: none

   <AI Device="10" Index="2" InfAddr="3" qualifier="0" Coeff="100.0" StartOffset="6554" ZeroDeadband="5.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" GroupMask="0x0002" TypeID="13" Total="2" Name="Feeder current" />

.. tip:: Attributes of the :ref:`AI<ref-IEC10xslAI>` element node can be arranged in any order, it will not affect the XML file validation.         

AI attributes
^^^^^^^^^^^^^

.. _ref-IEC10xslAIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101/104 Slave AI attributes"

.. include-file:: sections/Include/IEC10xsl_Device.rstinc "" ".. _ref-IEC10xslAIDevice:" "AI" "source" "Source"

   * :attr:     .. _ref-IEC10xslAIIndex:

                :xmlref:`Index`
     :val:      0...2\ :sup:`32`\  - 1
     :def:      n/a
     :desc:     Source AI object. Any AI element node of the selected Master protocol instance can be used as a source.
		Use value of the :ref:`AI<ref-IEC10xmaAI>`.\ :ref:`<ref-IEC10xmaAIIndex>` \ attribute of any AI object listed in the IO table of the selected Master protocol instance.
		:inlinetip:`Indexes don't have to be arranged in ascending order.`

.. include-file:: sections/Include/IEC10xsl_IOA.rstinc "" ".. _ref-IEC10xslAIInfAddr:" "AI" "send object to"

   * :attr:     .. _ref-IEC10xslAIqualifier:

                :xmlref:`qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC10xslAIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAICoeff:

                :xmlref:`Coeff`
     :val:      0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\
     :def:      1
     :desc:     Coefficient to multiply the analog object value before sending to upstream Master station.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAIStartOffset:

		:xmlref:`StartOffset`

		\*
     :val:      0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\
     :def:      0
     :desc:     Start offset is normally used to adjust 4-20mA transducer output range, e.g. offset by a value that represents 4mA.
		AI will be forced to 0 and Invalid [IV] bit set if the received value is smaller than this offset.
		:xmlref:`StartOffset` will be subtracted from the received value if the received value is greater or equal to this offset.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAIZeroDeadband:

		:xmlref:`ZeroDeadband`

		\*
     :val:      0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\
     :def:      0
     :desc:     Zero Deadband is used to filter noise by forcing low AI values to 0.
		AI will be forced to 0 if its real-time absolute value (+/-) falls below :xmlref:`ZeroDeadband` attribute.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAIOffset:

		:xmlref:`Offset`

		\*
     :val:      0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\
     :def:      0
     :desc:     Offset AI value **after** :xmlref:`ZeroDeadband` has been applied.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAIOffsetDeadband:

		:xmlref:`OffsetDeadband`

		\*
     :val:      0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\
     :def:      0
     :desc:     Offset Zero Deadband is used to filter noise around 0 value **after** applying :xmlref:`Offset`.
		AI will be forced to 0 if its absolute value (+/-) after offsetting falls below :xmlref:`OffsetDeadband` attribute.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAINonZeroOffset:

		:xmlref:`NonZeroOffset`

		\*
     :val:      0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\
     :def:      0
     :desc:     Offset only non-zero values **after** :xmlref:`ZeroDeadband`; :xmlref:`Offset` and :xmlref:`OffsetDeadband` has been applied.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:     .. _ref-IEC10xslAIGroupMask:

                :xmlref:`GroupMask`
     :val:      0...65535 or 0x0000...0xFFFF
     :def:      0x0000
     :desc:     Include object in Interrogation group/groups.
		Each bit of the group mask attribute needs to be set in order to include object in a particular interrogation group.
		Please refer to the table :numref:`ref-IEC10xslGroupMask` for more information.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAITypeID:

                :xmlref:`TypeID`
     :val:      See table :numref:`ref-IEC10xslAITypeIDValues`
     :def:      14 [M_ME_TC_1] or 36 [M_ME_TF_1]
     :desc:     Use this ASDU Type to send a AI event.
		Attribute also affects ASDU type of the static data (e.g. Normalized, Scaled, Short floating point value) being reported to General interrogation request
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/IEC60870_Total.rstinc "" ".. _ref-IEC10xslAITotal:" ":ref:`Index<ref-IEC10xslAIIndex>`" ":ref:`InfAddr<ref-IEC10xslAIInfAddr>`" ":ref:`AI<ref-IEC10xslAI>`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

.. tip::

   \* Please refer to annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` 
   for additional information on AI scaling and application examples using
   :ref:`<ref-IEC10xslAIStartOffset>` \; :ref:`<ref-IEC10xslAIZeroDeadband>` \; :ref:`<ref-IEC10xslAIOffset>` \; :ref:`<ref-IEC10xslAIOffsetDeadband>` \; :ref:`<ref-IEC10xslAINonZeroOffset>` \ attributes.

AI.qualifier
^^^^^^^^^^^^
.. _ref-IEC10xslAIqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-101/104 Slave AI internal qualifier" ":ref:`<ref-IEC10xslAIqualifier>`" "AI internal qualifier"

   * :attr:     Bit 0\*
     :val:      xxxx.xxx0
     :desc:     :ref:`StartOffset<ref-IEC10xslAIStartOffset>` \ attribute will be used for AI scaling.

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     Fixed offset (6554) will be loaded to :ref:`StartOffset<ref-IEC10xslAIStartOffset>` \ attribute in order to compensate 4-20mA transducer output offset.
		Applies to positive or negative AI values.

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     Additional 'Zero' AI event generation **disabled**

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     Additional 'Zero' AI event generation **enabled**. A value 0 event will be internally generated following every sent AI event sent with nonzero value. AI object will always have 0 value in interrogation responses.

   * :attr:     Bit 2
     :val:      xxxx.x0xx
     :desc:     AI events **enabled**. AI event will be sent upstream if event is received from the source communication protocol instance

   * :(attr):
     :val:      xxxx.x1xx
     :desc:     AI events **disabled**

   * :attr:     Bit 3
     :val:      xxxx.0xxx
     :desc:     AI object will be **included** in General Interrogation response

   * :(attr):
     :val:      xxxx.1xxx
     :desc:     AI object will be **excluded** from General Interrogation response

   * :attr:     Bit 6
     :val:      x0xx.xxxx
     :desc:     Send AI events upstream with their original value and use **the same value** for Interrogation response and periodic reporting

   * :(attr):
     :val:      x1xx.xxxx
     :desc:     Send AI events upstream with their original value, but use **value 0** for Interrogation response and periodic reporting

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     AI is **enabled** and will be sent upstream

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     AI is **disabled** and will not be sent upstream

   * :attr:     Bits 4;5
     :val:      Any
     :desc:     Bits reserved for future use

.. tip::

   \* Please refer to annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` 
   for additional information on AI scaling and application examples using :ref:`<ref-IEC10xslAIqualifier>` \ Bit[0].

.. include-file:: sections/Include/IEC60870_AI_TypeID.rstinc "" ".. _ref-IEC10xslAITypeIDValues:" "IEC60870-5-101/104 Slave AI TypeID"
