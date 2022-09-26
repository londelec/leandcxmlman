
.. _xmlgroup-IEC103maAI: lelabel=AITable
.. _xmlelem-IEC103maAI: lelabel=AI

AITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-IEC103maAI`" ":ref:`xmlelem-IEC103maAI`" ":numref:`tabid-IEC103maAI`" ":ref:`docref-IEC10xslAI`" "AI" "analog information" "IED"

In order to receive an analog information from IED [:lemonobgtext:`FUNCTION TYPE`] and [:lemonobgtext:`INFORMATION NUMBER`] has to be specified in :ref:`xmlattr-IEC103maAIFUN` \ and :ref:`xmlattr-IEC103maAIINF` \ attributes.
It also essential to select index of a particular measurement because IEC60870-5-103 station sends multiple measurands in one message.
Index of a particular analog value is selected with :ref:`xmlattr-IEC103maAIMEA` \ attribute.

Please see sample :ref:`xmlgroup-IEC103maAI` group and :ref:`xmlelem-IEC103maAI` element nodes below.
There are 5 analog information objects defined with 4 :ref:`xmlelem-IEC103maAI` element nodes.

.. code-block:: none

   <AITable>
	<AI Index="0" FUN="1" INF="1" MEA="0" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" FUN="1" INF="1" MEA="5" Qualifier="0x00" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" FUN="85" INF="83" MEA="0" Qualifier="0x00" Coeff="-17.0" Percent="1.4"/>
	<AI Index="3" FUN="105" INF="103" MEA="0" Qualifier="0x00" Coeff="0.08" Total="2"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC103maAI`"

.. code-block:: none

   <AI Index="0" FUN="85" INF="83" MEA="2" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" DIAndIndex="0" LogicValue="1" Total="2" Name="Feeder current" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC103maAI`"

AI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC103maAI" "IEC60870-5-103 Master AI attributes" ":spec: |C{0.18}|C{0.16}|C{0.1}|S{0.56}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "AI"

.. include-file:: sections/Include/IEC103ma_FunInf.rstinc "" "AI" "receive object from"

   * :attr:	:xmlattr:`MEA`
     :val:	0...31
     :def:	n/a
     :desc:	Number of the analog value in the received measurement message.
		Use value 0 to select first measurement in the received message.
		:inlinetip:`Numbers don't have to be arranged in an ascending order.`

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-IEC103maAIQualifier`"

.. include-file:: sections/Include/AI_Coeff.rstinc ""

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ":ref:`xmlattr-IEC103maAIDeadband`" ":ref:`xmlattr-IEC103maAIPercent`" ":ref:`xmlelem-IEC103maAsdu`.\ :ref:`xmlattr-IEC103maAsduAIDeadband`" ":ref:`xmlelem-IEC103maAsdu`.\ :ref:`xmlattr-IEC103maAsduAIPercent`"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ":ref:`xmlattr-IEC103maAIStartOffset`" ":ref:`xmlattr-IEC103maAIZeroDeadband`" ":ref:`xmlattr-IEC103maAIOffset`" ":ref:`xmlattr-IEC103maAIOffsetDeadband`" ":ref:`xmlattr-IEC103maAINonZeroOffset`"

   * :attr:	:xmlattr:`DIAndIndex`
     :val:	0...65534
     :def:	n/a
     :desc:	Index of the DI object to perform logical conjunction (AND function).
		Use value of the :ref:`xmlelem-IEC103maDI`.\ :ref:`xmlattr-IEC103maDIIndex` attribute.
		Analog value will be stored in the database and event will be generated only if value of the DI object is the same as specified in :ref:`xmlattr-IEC103maAILogicValue` attribute.
		:inlinetip:`Attribute is optional and must not be specified in configuration if not used. There is no default value.`

   * :attr:	:xmlattr:`LogicValue`
     :val:	0...255
     :def:	0
     :desc:	Value of the object used for logical conjunction/disjunction (AND/OR function).
		Please note all DI values have to be treated as DPIs (ON = 2; OFF = 1) if used for logic functions.
		Quality flags (e.g. [:lemonobgtext:`IV`]) are not part of the logical processing, DI values are used regardless of state of the quality flags.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC103maAIIndex` and :ref:`xmlattr-IEC103maAIMEA`" ":ref:`xmlelem-IEC103maAI`" "254"

.. include-file:: sections/Include/Name.rstinc ""

.. include-file:: sections/Include/ma_AI_Annex.rstinc "" ":ref:`xmlattr-IEC103maAIDeadband`" ":ref:`xmlattr-IEC103maAIPercent`"

AI.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC103maAIQualifier" "IEC60870-5-103 Master AI internal Qualifier" ":ref:`xmlattr-IEC103maAIQualifier`" "AI internal qualifier"

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	Additional 'Zero' AI event generation **disabled**

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	| Additional 'Zero' AI event generation **enabled**. New 0 value event will be generated internally following every:
		| / event with a nonzero value received from outstation and
		| / event with a nonzero value resulted from a deadband/percent or scaling processing.
		| Static AI object will be set to value 0, static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.

   * :attr:	Bit 2
     :val:	xxxx.x0xx
     :desc:	Event is generated if an AI object is received from outstation with a **'spontaneous'** Cause Of Transmission ([:lemonobgtext:`COT`] = 1)
		or received value exceeds deadband/percent limit.

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Event is generated **every time** AI object is received from outstation regardless of the Cause Of Transmission.
		Also invalid [:lemonobgtext:`IV`] flag is automatically cleared when outstation goes online which ensures this AI object is always valid.
		:inlinetip:`This option is only used for backward compatibility.`

   * :attr:	Bit 6
     :val:	x0xx.xxxx
     :desc:	Process events received from outstation with their original AI value and store **original** value in the static database. Static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.

   * :(attr):
     :val:	x1xx.xxxx
     :desc:	Process events received from outstation with their original value, but store **0 value** in the static database. Static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	AI is **enabled** and will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AI is **disabled** and will be discarded when received

   * :attr:	Bits 0;3;4;5
     :val:	Any
     :desc:	Bits reserved for future use
