
.. _docref-IEC10xslAI:
.. _xmlgroup-IEC10xslAI: lelabel=AITable
.. _xmlelem-IEC10xslAI: lelabel=AI

AITable group
-------------

.. include-file:: sections/Include/IEC10xsl_DIAI_table.rstinc "" ":ref:`xmlgroup-IEC10xslAI`" ":ref:`xmlelem-IEC10xslAI`" ":numref:`tabid-IEC10xslAI`" "AI" "analog information"

| The link is created using :ref:`xmlelem-IEC10xslAI`.\ :ref:`xmlattr-IEC10xslAIDevice` and :ref:`xmlelem-IEC10xslAI`.\ :ref:`xmlattr-IEC10xslAIIndex` attributes as follows:
| 1. Select the **source Master protocol instance** - use value of the :ref:`xmlattr-gp101maIndex` attribute of any Master protocol instance and enter this value in :ref:`xmlelem-IEC10xslAI`.\ :ref:`xmlattr-IEC10xslAIDevice` attribute.
| 2. Select the **source AI object** - use value of the :ref:`xmlelem-IEC10xmaAI`.\ :ref:`xmlattr-IEC10xmaAIIndex` attribute of any AI object listed in the IO object table of a Master protocol instance and enter this value in :ref:`xmlelem-IEC10xslAI`.\ :ref:`xmlattr-IEC10xslAIIndex` attribute.

Information object address (IOA) to send analog information object upstream is specified in :ref:`xmlattr-IEC10xslAIInfAddr` attribute.

Please see sample :ref:`xmlgroup-IEC10xslAI` group and :ref:`xmlelem-IEC10xslAI` element nodes below.
There are 5 analog information objects defined with 4 :ref:`xmlelem-IEC10xslAI` element nodes.

.. code-block:: none

   <AITable>
	<AI Device="10" Index="0" InfAddr="1" qualifier="0x20" Coeff="1.0" Offset="28.0" … /> 
	<AI Device="10" Index="1" InfAddr="2" qualifier="0x00" ZeroDeadband="1.0" … />
	<AI Device="10" Index="2" InfAddr="3" qualifier="0x01" Coeff="0.05" GroupMask="0x0002" … />
	<AI Device="10" Index="3" InfAddr="4" qualifier="0x00" Coeff="1.0" Offset="2.0" Total="2" … />
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC10xslAI`"

.. code-block:: none

   <AI Device="10" Index="2" InfAddr="3" qualifier="0" Coeff="100.0" StartOffset="6554" ZeroDeadband="5.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" GroupMask="0x0002" TypeID="13" Total="2" Name="Feeder current" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC10xslAI`"

AI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC10xslAI" "IEC60870-5-101/104 Slave AI attributes" ":spec: |C{0.18}|C{0.16}|C{0.15}|S{0.51}|"

.. include-file:: sections/Include/IEC10xsl_Device.rstinc "" ":xmlattr:`Device`" "source for this AI object" "Source"

   * :attr:	:xmlattr:`Index`
     :val:	|slindexrange|
     :def:	n/a
     :desc:	Source AI object. Any AI element of the selected Master protocol instance can be used as a source.
		Use value of the :ref:`xmlelem-IEC10xmaAI`.\ :ref:`xmlattr-IEC10xmaAIIndex` attribute of any AI object listed in the IO table of the selected Master protocol instance.
		:inlinetip:`Indexes don't have to be arranged in ascending order.`

.. include-file:: sections/Include/IEC10xsl_IOA.rstinc "" "AI" "send object to"

.. include-file:: sections/Include/IEC60870_qualifier.rstinc "" ":numref:`tabid-IEC10xslAIqualifier`"

   * :attr:	:xmlattr:`Coeff`
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :def:	1
     :desc:	Coefficient to multiply the analog object value before sending to upstream Master station.
		|optinalattr|

   * :attr:	:xmlattr:`StartOffset` \*
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :def:	0
     :desc:	Start offset is normally used to adjust 4-20mA transducer output range, e.g. offset by a value that represents 4mA.
		AI will be forced to 0 and Invalid [:lemonobgtext:`IV`] bit set if the received value is smaller than this offset.
		:ref:`xmlattr-IEC10xslAIStartOffset` will be subtracted from the received value if the received value is greater or equal to this offset.
		|optinalattr|

   * :attr:	:xmlattr:`ZeroDeadband` \*
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :def:	0
     :desc:	Zero Deadband is used to filter noise by forcing low AI values to 0.
		AI will be forced to 0 if its real-time absolute value (+/-) falls below :ref:`xmlattr-IEC10xslAIZeroDeadband` attribute.
		|optinalattr|

   * :attr:	:xmlattr:`Offset` \*
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :def:	0
     :desc:	Offset AI value **after** :ref:`xmlattr-IEC10xslAIZeroDeadband` has been applied.
		|optinalattr|

   * :attr:	:xmlattr:`OffsetDeadband` \*
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :def:	0
     :desc:	Offset Zero Deadband is used to filter noise around 0 value **after** applying :ref:`xmlattr-IEC10xslAIOffset`.
		AI will be forced to 0 if its absolute value (+/-) after offsetting falls below :ref:`xmlattr-IEC10xslAIOffsetDeadband` attribute.
		|optinalattr|

   * :attr:	:xmlattr:`NonZeroOffset` \*
     :val:	0 or ±1.18×10\ :sup:`-38` \ ... ±3.4×10\ :sup:`38`\
     :def:	0
     :desc:	Offset only non-zero values **after** :ref:`xmlattr-IEC10xslAIZeroDeadband`; :ref:`xmlattr-IEC10xslAIOffset` and :ref:`xmlattr-IEC10xslAIOffsetDeadband` has been applied.
		|optinalattr|

.. include-file:: sections/Include/IEC10xsl_GroupMask.rstinc "" ":xmlattr:`GroupMask`" "object"

   * :attr:	:xmlattr:`TypeID`
     :val:	See :numref:`tabid-IEC10xslAITypeID`
     :def:	14 [:lemonobgtext:`M_ME_TC_1`] or 36 [:lemonobgtext:`M_ME_TF_1`]
     :desc:	Use this ASDU Type to send a AI event.
		Attribute also affects ASDU type of the static data (e.g. Normalized, Scaled, Short floating point value) being reported to General interrogation request
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC10xslAIIndex` and :ref:`xmlattr-IEC10xslAIInfAddr`" ":ref:`xmlelem-IEC10xslAI`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

.. tip::

   \* Please refer to annex :ref:`docref-AIScaling` for information on analog value scaling and application examples using
   :ref:`xmlattr-IEC10xslAIStartOffset` \; :ref:`xmlattr-IEC10xslAIZeroDeadband` \; :ref:`xmlattr-IEC10xslAIOffset` \; :ref:`xmlattr-IEC10xslAIOffsetDeadband` \; :ref:`xmlattr-IEC10xslAINonZeroOffset` \ attributes.

AI.qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC10xslAIqualifier" "IEC60870-5-101/104 Slave AI internal qualifier" ":ref:`xmlattr-IEC10xslAIqualifier`" "AI internal qualifier"

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	Additional 'Zero' AI event generation **disabled**

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	Additional 'Zero' AI event generation **enabled**. A value 0 event will be internally generated following every sent AI event sent with nonzero value. AI object will always have 0 value in interrogation responses.

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	AI events **enabled**. AI event will be sent upstream if event is received from the source communication protocol instance

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	AI events **disabled**

   * :attr:	Bit 3
     :val:	xxxx.0xxx
     :desc:	AI object will be **included** in General Interrogation response

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	AI object will be **excluded** from General Interrogation response

   * :attr:	Bit 6
     :val:	x0xx.xxxx
     :desc:	Send AI events upstream with their original value and use **the same value** for Interrogation response and periodic reporting

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	Send AI events upstream with their original value, but use **value 0** for Interrogation response and periodic reporting

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	AI is **enabled** and will be sent upstream

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AI is **disabled** and will not be sent upstream

   * :attr:	Bits 0;4;5
     :val:	Any
     :desc:	Bits reserved for future use

.. include-file:: sections/Include/IEC60870_AI_TypeID.rstinc "" "tabid-IEC10xslAITypeID" "IEC60870-5-101/104 Slave AI TypeID"
