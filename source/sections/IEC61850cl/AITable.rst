
.. _ref-IEC61850clAI:

AITable group and AI node
-------------------------

Group node :ref:`AITable<ref-IEC61850clAI>` and child element nodes :ref:`AI<ref-IEC61850clAI>` are used to create AI information objects to receive analog information from an IED.
Each created AI can be used as a source for any AI information object defined in the IO table of any Slave protocol instance.
Analog data received from an IED will be forwarded to the AI information object of the Slave protocol instance and then to the upstream Master station.
Please refer to the section :ref:`docref-IEC10xslAITable` for more information on how to use AI information object as a source.

Please see sample :ref:`AITable<ref-IEC61850clAI>` group and :ref:`AI<ref-IEC61850clAI>` child element nodes below.

.. code-block:: none

   <AITable>
	<AI Index="0" ldInst="LD0" prefix="CPH" lnClass="MMXU" lnInst="1" doName="A.phsA" fc="MX" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" ldInst="LD0" prefix="CPH" lnClass="MMXU" lnInst="1" doName="A.phsB" fc="MX"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`AI<ref-IEC61850clAI>`"

.. code-block:: none

   <AI Index="0" ldInst="LD0" prefix="CPH" lnClass="MMXU" lnInst="1" doName="A.phsA" fc="MX" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" daName="cVal.mag.f" DSnum="1" TrgOps="0x00" intgPd="0" Name="Feeder current" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`AI<ref-IEC61850clAI>`"

AI attributes
^^^^^^^^^^^^^

.. _ref-IEC61850clAIAttributes:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client AI attributes"

.. include-file:: sections/Include/ma_Index.rstinc "" ".. _ref-IEC61850clAIIndex:" "AI"

.. include-file:: sections/Include/IEC61850cl_SCL.rstinc "" "'CPH'" "'MMXU'" "'Pos'" "'A.phsA'" "'MX'"

   * :attr:     .. _ref-IEC61850clAIQualifier:
   
                :xmlref:`Qualifier`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Internal object qualifier to enable customized data processing.
		See table :numref:`ref-IEC61850clAIqualifierBits` for internal object qualifier description.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

.. include-file:: sections/Include/AI_Coeff.rstinc "" ".. _ref-IEC61850clAICoeff:"

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ".. _ref-IEC61850clAIDeadband:" ".. _ref-IEC61850clAIPercent:"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ".. _ref-IEC61850clAIStartOffset:" ".. _ref-IEC61850clAIZeroDeadband:" ".. _ref-IEC61850clAIOffset:" ".. _ref-IEC61850clAIOffsetDeadband:" ".. _ref-IEC61850clAINonZeroOffset:"

.. include-file:: sections/Include/hidden_qtname.rstinc "internal"

.. include-file:: sections/Include/IEC61850cl_DIAI.rstinc "" ".. _ref-IEC61850clAIDSnum:" ".. _ref-IEC61850clAITrgOps:" ".. _ref-IEC61850clAIintgPd:" ":numref:`ref-IEC61850clTrgOps`" "cVal.mag.f"

.. include-file:: sections/Include/Name.rstinc ""

.. tip::

   \* Please refer to annex :ref:`docref-ReceivedAIProcessing` for additional information on AI processing 
   options and application examples using :ref:`Deadband<ref-IEC61850clAIDeadband>` \ and :ref:`Percent<ref-IEC61850clAIPercent>` attributes.
   Annexes :ref:`docref-AIScalingWithoutStartOffset` and :ref:`docref-AIScalingWithStartOffset` for additional information on AI scaling.

AI.Qualifier
^^^^^^^^^^^^

.. _ref-IEC61850clAIqualifierBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC61850 Client AI internal qualifier" ":ref:`<ref-IEC61850clAIQualifier>`" "AI internal qualifier"

   * :attr:     Bit 3
     :val:      xxxx.0xxx
     :desc:     **Use original** timetag when event is received from IED

   * :(attr):
     :val:      xxxx.1xxx
     :desc:     **Substitute** timetag with local time when event is received from IED

   * :attr:     Bit 7
     :val:      0xxx.xxxx
     :desc:     AI is **enabled** and will be processed when received

   * :(attr):
     :val:      1xxx.xxxx
     :desc:     AI is **disabled** and will be discarded when received

   * :attr:     Bits 0...2;4...6
     :val:      Any
     :desc:     Bits reserved for future use
