
.. _ref-IEC103maAITable:
.. _ref-IEC103maAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-IEC103maAITable>` and child element nodes :ref:`AI<ref-IEC103maAI>` are used to create AI information objects to receive analog information from the downstream outstation.
Each created AI information object can be used as source of information for any AI information object defined in IO table of the Slave protocol instances.
If used as a source, analog information received from an outstation will be forwarded to AI information object of the Slave protocol instance and then to the upstream Master station.
Please refer to the section :ref:`docref-IEC10xslAITable` for more information on how to use AI information object as a source.

In order to receive an analog information from downstream outstation [:lectext1:`FUNCTION TYPE`] and [:lectext1:`INFORMATION NUMBER`]
has to be specified in :ref:`<ref-IEC103maAIFUN>` \ and :ref:`<ref-IEC103maAIINF>` \ attributes.
It also essential to select particular measurement from the incoming message as IEC60870-5-103 station sends multiple measurands in one message.
Particular analog value is selected with :ref:`<ref-IEC103maAIMEA>` \ attribute.

Please see sample :ref:`AITable<ref-IEC103maAITable>` group and :ref:`AI<ref-IEC103maAI>` child element nodes below.
There are 5 AI information objects configured using 4 :ref:`AI<ref-IEC103maAI>` element nodes.

.. code-block:: none

   <AITable>
	<AI Index="0" FUN="1" INF="1" MEA="0" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" FUN="1" INF="1" MEA="5" Qualifier="0x00" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="2" FUN="85" INF="83" MEA="0" Qualifier="0x00" Coeff="-17.0" Percent="1.4"/>
	<AI Index="3" FUN="105" INF="103" MEA="0" Qualifier="0x00" Coeff="0.08" Total="2"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AI<ref-IEC103maAI>`"

.. code-block:: none

   <AI Index="0" FUN="85" INF="83" MEA="2" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" Total="2" Name="Feeder current" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`AI<ref-IEC103maAI>`"

AI attributes
^^^^^^^^^^^^^

.. _ref-IEC103maAIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-103 Master AI attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC103maAIIndex:" "AI"

.. include-file:: sections/Include/IEC103ma_FunInf.rstinc "" ".. _ref-IEC103maAIFUN:" ".. _ref-IEC103maAIINF:" "AI" "receive object from"

   * :attr:     .. _ref-IEC103maAIMEA:

                :xmlref:`MEA`
     :val:      0...31
     :def:      n/a
     :desc:     Number of the analog value in the received measurement message.
		Use value 0 to select first measurement in the received message.
		:inlinetip:`Numbers don't have to be arranged in an ascending order.`

   * :attr:     .. _ref-IEC103maAIQualifier:

                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC103maAIQualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/AI_Coeff.rstinc "" ".. _ref-IEC103maAICoeff:"

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ".. _ref-IEC103maAIDeadband:" ".. _ref-IEC103maAIPercent:"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ".. _ref-IEC103maAIStartOffset:" ".. _ref-IEC103maAIZeroDeadband:" ".. _ref-IEC103maAIOffset:" ".. _ref-IEC103maAIOffsetDeadband:" ".. _ref-IEC103maAINonZeroOffset:"

.. include-file:: sections/Include/Total.rstinc "" ".. _ref-IEC103maAITotal:" ":ref:`<ref-IEC103maAIIndex>` and :ref:`<ref-IEC103maAIMEA>`" ":ref:`AI<ref-IEC103maAI>`" "254"

.. include-file:: sections/Include/Name.rstinc ""

.. tip::

   \* Please refer to annex :ref:`docref-ReceivedAIProcessing` for additional information on AI processing 
   options and application examples using :ref:`Deadband<ref-IEC103maAIDeadband>` \ and :ref:`Percent<ref-IEC103maAIPercent>` \ attributes.
   Annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` for additional information on AI scaling.

AI.Qualifier
^^^^^^^^^^^^

.. _ref-IEC103maAIQualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-103 Master AI internal Qualifier" ":ref:`<ref-IEC103maAIQualifier>`" "AI internal qualifier"

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
     :desc:	Event is generated if an AI object is received from outstation with a **'spontaneous'** Cause Of Transmission ([:lectext1:`COT`] = 1)
		or received value exceeds deadband/percent limit.

   * :(attr):
     :val:      xxxx.x1xx
     :desc:	Event is generated **every time** AI object is received from outstation regardless of the Cause Of Transmission.
		Also invalid [:lectext1:`IV`] flag is automatically cleared when outstation goes online which ensures this AI object is always valid.
		:inlinetip:`This option is only used for backward compatibility.`

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

   * :attr:     Bits 0;3;4;5
     :val:      Any
     :desc:     Bits reserved for future use
