
.. _ref-IEC10xmaAITable:
.. _ref-IEC10xmaAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-IEC10xmaAITable>` and child element nodes :ref:`AI<ref-IEC10xmaAI>` are used to create AI information objects to receive analog information from the downstream outstation.
Each created AI can be used as a source for any AI information object defined in the IO table of any Slave protocol instance.
Analog data received from the outstation will be forwarded to the AI information object of the Slave protocol instance and then to the upstream Master station.
Please refer to the section :ref:`docref-IEC10xslAITable` for more information on how to use AI information object as a source.

In order to receive analog information from the downstream outstation information object address (IOA) needs to be
specified in the :ref:`<ref-IEC10xmaAIInfAddr>` \ attribute.
Analog information is processed when received with any of the following ASDU types:
5 [:lemonobgtext:`M_ST_NA_1`]; 6 [:lemonobgtext:`M_ST_TA_1`]; 32 [:lemonobgtext:`M_ST_TB_1`];
9 [:lemonobgtext:`M_ME_NA_1`]; 10 [:lemonobgtext:`M_ME_TA_1`]; 34 [:lemonobgtext:`M_ME_TD_1`];
11 [:lemonobgtext:`M_ME_NB_1`]; 12 [:lemonobgtext:`M_ME_TB_1`]; 35 [:lemonobgtext:`M_ME_TE_1`];
13 [:lemonobgtext:`M_ME_NC_1`]; 14 [:lemonobgtext:`M_ME_TC_1`]; 36 [:lemonobgtext:`M_ME_TF_1`]

Please see sample :ref:`AITable<ref-IEC10xmaAITable>` group and :ref:`AI<ref-IEC10xmaAI>` child element nodes below.
There are 5 AI information objects configured using 4 :ref:`AI<ref-IEC10xmaAI>` element nodes.

.. code-block:: none

   <AITable>
	<AI Index="0" InfAddr="1" qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" InfAddr="2" qualifier="0x00" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" InfAddr="3" qualifier="0x00" Coeff="-17.0" Deadband="0" Percent="1.4" TypeID="36"/>
	<AI Index="3" InfAddr="4" qualifier="0x00" Coeff="0.08" Deadband="8" Percent="3" Total="2"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AI<ref-IEC10xmaAI>`"

.. code-block:: none

   <AI Index="0" InfAddr="1" qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" TypeID="36" Total="2" Name="Feeder current" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`AI<ref-IEC10xmaAI>`"

AI attributes
^^^^^^^^^^^^^

.. _docref-IEC10xmaAIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101/104 Master AI attributes" ":spec: |C{0.18}|C{0.16}|C{0.12}|S{0.54}|"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC10xmaAIIndex:" "AI"

.. include-file:: sections/Include/IEC10xma_IOA.rstinc "" ".. _ref-IEC10xmaAIInfAddr:" "AI" "receive object from"

   * :attr:     .. _ref-IEC10xmaAIqualifier:

                :xmlref:`qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`docref-IEC10xmaAIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/AI_Coeff.rstinc "" ".. _ref-IEC10xmaAICoeff:"

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ".. _ref-IEC10xmaAIDeadband:" ".. _ref-IEC10xmaAIPercent:"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ".. _ref-IEC10xmaAIStartOffset:" ".. _ref-IEC10xmaAIZeroDeadband:" ".. _ref-IEC10xmaAIOffset:" ".. _ref-IEC10xmaAIOffsetDeadband:" ".. _ref-IEC10xmaAINonZeroOffset:"

   * :attr:     .. _ref-IEC10xmaAITypeID:

		:xmlref:`TypeID`
     :val:      See table :numref:`docref-IEC10xmaAITypeIDValues`
     :def:      transparent
     :desc:     Use this ASDU type to send a DI object upstream, if transparent ASDUs are enabled in Slave protocol instance with :ref:`<ref-IEC101slASDUSettings>`.\ :ref:`<ref-IEC101slASDUSettingsTranspTypes>` \ attribute.
		This ASDU type will be used to report object regardless of the received ASDU type.
		There is no default value, attribute must not be specified if not used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration.
		ASDU type received from outstation will be used to report object upstream if transparent ASDUs are enabled in Slave protocol instance with` :ref:`<ref-IEC101slASDUSettings>`.\ :ref:`<ref-IEC101slASDUSettingsTranspTypes>` \ :inlinetip:`attribute.`

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-IEC10xmaAITotal:" ":ref:`<ref-IEC10xmaAIIndex>` and :ref:`<ref-IEC10xmaAIInfAddr>`" ":ref:`AI<ref-IEC10xmaAI>`" "16777214"

.. include-file:: sections/Include/Name.rstinc ""

.. include-file:: sections/Include/ma_AI_Annex.rstinc "" ":ref:`<ref-IEC10xmaAIDeadband>`" ":ref:`<ref-IEC10xmaAIPercent>`"

AI.qualifier
^^^^^^^^^^^^

.. _docref-IEC10xmaAIqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-101/104 Master AI internal qualifier" ":ref:`<ref-IEC10xmaAIqualifier>`" "AI internal qualifier"

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     Additional 'Zero' AI event generation **disabled**

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     | Additional 'Zero' AI event generation **enabled**. New 0 value event will be generated internally following every:
		| / event with a nonzero value received from outstation and
		| / event with a nonzero value resulted from a deadband/percent or scaling processing.
		| Static AI object will be set to value 0, static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.

   * :attr:     Bit 2
     :val:      xxxx.x0xx
     :desc:	Event is generated if an AI object is received from outstation with a **'spontaneous'** Cause Of Transmission ([:lemonobgtext:`COT`] = 3)
		or received value exceeds deadband/percent limit.

   * :(attr):
     :val:      xxxx.x1xx
     :desc:	Event is generated **every time** AI object is received from outstation regardless of the Cause Of Transmission.
		Also invalid [:lemonobgtext:`IV`] flag is automatically cleared when outstation goes online which ensures this AI object is always valid.
		:inlinetip:`This option is only used for backward compatibility.`

   * :attr:     Bit 3
     :val:      xxxx.0xxx
     :desc:     **Use original** timetag when event is received from outstation

   * :(attr):
     :val:      xxxx.1xxx
     :desc:     **Substitute** timetag with local time when event is received from outstation

   * :attr:     Bit 6
     :val:      x0xx.xxxx
     :desc:     Process events received from outstation with their original AI value and store **original** value in the static database. Static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.

   * :(attr):
     :val:      x1xx.xxxx
     :desc:     Process events received from outstation with their original value, but store **0 value** in the static database. Static value is used when Slave protocol instance responds to an Interrogation or sends AI periodically.

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     AI is **enabled** and will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     AI is **disabled** and will be discarded when received

   * :attr:     Bits 0;4;5
     :val:      Any
     :desc:     Bits reserved for future use

.. include-file:: sections/Include/IEC60870_AI_TypeID.rstinc "" ".. _docref-IEC10xmaAITypeIDValues:" "IEC60870-5-101/104 Master AI TypeID"
