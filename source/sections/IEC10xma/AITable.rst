
.. _xmlgroup-IEC10xmaAI: lelabel=AITable
.. _xmlelem-IEC10xmaAI: lelabel=AI

AITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-IEC10xmaAI`" ":ref:`xmlelem-IEC10xmaAI`" ":numref:`tabid-IEC10xmaAI`" ":ref:`docref-IEC10xslAI`" "AI" "analog information" "outstation"

In order to receive analog information from outstation information object address (IOA) needs to be specified in the :ref:`xmlattr-IEC10xmaAIInfAddr` \ attribute.
Analog information is processed when received from oustation with any of the following ASDU types:
5 [:lemonobgtext:`M_ST_NA_1`]; 6 [:lemonobgtext:`M_ST_TA_1`]; 32 [:lemonobgtext:`M_ST_TB_1`];
9 [:lemonobgtext:`M_ME_NA_1`]; 10 [:lemonobgtext:`M_ME_TA_1`]; 34 [:lemonobgtext:`M_ME_TD_1`];
11 [:lemonobgtext:`M_ME_NB_1`]; 12 [:lemonobgtext:`M_ME_TB_1`]; 35 [:lemonobgtext:`M_ME_TE_1`];
13 [:lemonobgtext:`M_ME_NC_1`]; 14 [:lemonobgtext:`M_ME_TC_1`]; 36 [:lemonobgtext:`M_ME_TF_1`]

Please see sample :ref:`xmlgroup-IEC10xmaAI` group and :ref:`xmlelem-IEC10xmaAI` element nodes below.
There are 5 analog information objects defined with 4 :ref:`xmlelem-IEC10xmaAI` element nodes.

.. code-block:: none

   <AITable>
	<AI Index="0" InfAddr="1" qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" InfAddr="2" qualifier="0x00" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" InfAddr="3" qualifier="0x00" Coeff="-17.0" Deadband="0" Percent="1.4" TypeID="36"/>
	<AI Index="3" InfAddr="4" qualifier="0x00" Coeff="0.08" Deadband="8" Percent="3" Total="2"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC10xmaAI`"

.. code-block:: none

   <AI Index="0" InfAddr="1" qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" TypeID="36" Total="2" Name="Feeder current" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC10xmaAI`"

AI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC10xmaAI" "IEC60870-5-101/104 Master AI attributes" ":spec: |C{0.18}|C{0.16}|C{0.12}|S{0.54}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "AI"

.. include-file:: sections/Include/IEC10xma_IOA.rstinc "" "AI" "receive object from"

.. include-file:: sections/Include/IEC60870_qualifier.rstinc "" ":numref:`tabid-IEC10xmaAIqualifier`"

.. include-file:: sections/Include/AI_Coeff.rstinc ""

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ":ref:`xmlattr-IEC10xmaAIDeadband`" ":ref:`xmlattr-IEC10xmaAIPercent`" "IEC101ma and IEC104ma :ref:`xmlelem-IEC101maAsdu`.\ :ref:`xmlattr-IEC101maAsduAIDeadband`" "IEC101ma and IEC104ma :ref:`xmlelem-IEC101maAsdu`.\ :ref:`xmlattr-IEC101maAsduAIPercent`"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ":ref:`xmlattr-IEC10xmaAIStartOffset`" ":ref:`xmlattr-IEC10xmaAIZeroDeadband`" ":ref:`xmlattr-IEC10xmaAIOffset`" ":ref:`xmlattr-IEC10xmaAIOffsetDeadband`" ":ref:`xmlattr-IEC10xmaAINonZeroOffset`"

.. include-file:: sections/Include/IEC10xma_DIAI_TypeID.rstinc "" "AI" ":numref:`tabid-IEC10xmaAITypeID`"

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-IEC10xmaAIIndex` and :ref:`xmlattr-IEC10xmaAIInfAddr`" ":ref:`xmlelem-IEC10xmaAI`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

.. include-file:: sections/Include/ma_AI_Annex.rstinc "" ":ref:`xmlattr-IEC10xmaAIDeadband`" ":ref:`xmlattr-IEC10xmaAIPercent`"

AI.qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC10xmaAIqualifier" "IEC60870-5-101/104 Master AI internal qualifier" ":ref:`xmlattr-IEC10xmaAIqualifier`" "AI internal qualifier"

   * :attr:	Bit 1
     :val:	xxxx.xx0x
     :desc:	Additional 'Zero' AI event generation **disabled**

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	| Additional 'Zero' AI event generation **enabled**. New 0 value event will be generated internally following every:
		| / event with a nonzero value received from outstation and
		| / event with a nonzero value resulted from a deadband/percent or scaling processing.
		| Static AI object will be set to value 0, static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.

   * :attr:	:bitdef:`2`
     :val:	xxxx.x0xx
     :desc:	Event is generated if an AI object is received from outstation with a **'spontaneous'** Cause Of Transmission ([:lemonobgtext:`COT`] = 3)
		or received value exceeds deadband/percent limit.

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Event is generated **every time** AI object is received from outstation regardless of the Cause Of Transmission.
		Also invalid [:lemonobgtext:`IV`] flag is automatically cleared when outstation goes online which ensures this AI object is always valid.
		:inlinetip:`This option is only used for backward compatibility.`

   * :attr:	Bit 3
     :val:	xxxx.0xxx
     :desc:	**Use original** timetag when event is received from outstation

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	**Substitute** timetag with local time when event is received from outstation

   * :attr:	:bitdef:`5`
     :val:	xx0x.xxxx
     :desc:	**Process** analog value received from outstation in General Interrogation

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	**Ignore** analog value received from outstation in General Interrogation

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

   * :attr:	Bits 0;4
     :val:	Any
     :desc:	Bits reserved for future use

.. include-file:: sections/Include/IEC60870_AI_TypeID.rstinc "" "tabid-IEC10xmaAITypeID" "IEC60870-5-101/104 Master AI TypeID"
