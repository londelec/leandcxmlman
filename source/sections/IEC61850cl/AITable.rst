
.. _xmlgroup-IEC61850clAI: lelabel=AITable
.. _xmlelem-IEC61850clAI: lelabel=AI

AITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-IEC61850clAI`" ":ref:`xmlelem-IEC61850clAI`" ":numref:`tabid-IEC61850clAI`" ":ref:`docref-IEC10xslAI`" "AI" "analog information" "IED"

Please see sample :ref:`xmlgroup-IEC61850clAI` group and :ref:`xmlelem-IEC61850clAI` element nodes below.
There are 2 analog information objects defined in this sample.

.. code-block:: none

   <AITable>
	<AI Index="0" ldInst="LD0" prefix="CPH" lnClass="MMXU" lnInst="1" doName="A.phsA" fc="MX" Coeff="1.0" Deadband="0.5" Percent="0"/>
	<AI Index="1" ldInst="LD0" prefix="CPH" lnClass="MMXU" lnInst="1" doName="A.phsB" fc="MX"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clAI`"

.. code-block:: none

   <AI Index="0" ldInst="LD0" prefix="CPH" lnClass="MMXU" lnInst="1" doName="A.phsA" fc="MX" Qualifier="0x20" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" daName="cVal.mag.f" DSref="ABCLD/LLN0.myds" DSflags="0x00" TrgOps="0x00" intgPd="0" Name="Feeder current" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-IEC61850clAI`"

AI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clAI" "IEC61850 Client AI attributes" ":spec: |C{0.18}|C{0.16}|C{0.12}|S{0.54}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "AI"

.. include-file:: sections/Include/IEC61850cl_SCL.rstinc "" "'CPH'" "'MMXU'" "'Pos'" "'A.phsA'" "'MX'"

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-IEC61850clAIQualifier`"

.. include-file:: sections/Include/AI_Coeff.rstinc ""

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ":ref:`xmlattr-IEC61850clAIDeadband`" ":ref:`xmlattr-IEC61850clAIPercent`" ":ref:`xmlelem-IEC61850clApp`.\ :ref:`xmlattr-IEC61850clAppAIDeadband`" ":ref:`xmlelem-IEC61850clApp`.\ :ref:`xmlattr-IEC61850clAppAIPercent`"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ":ref:`xmlattr-IEC61850clAIStartOffset`" ":ref:`xmlattr-IEC61850clAIZeroDeadband`" ":ref:`xmlattr-IEC61850clAIOffset`" ":ref:`xmlattr-IEC61850clAIOffsetDeadband`" ":ref:`xmlattr-IEC61850clAINonZeroOffset`"

.. include-file:: sections/Include/hidden_qtname.rstinc "internal"

.. include-file:: sections/Include/IEC61850cl_DIAI.rstinc "" ":numref:`tabid-IEC61850clAIDSflags`" ":numref:`tabid-IEC61850clTrgOps`" "cVal.mag.f"

.. include-file:: sections/Include/Name.rstinc ""

.. include-file:: sections/Include/ma_AI_Annex.rstinc "" ":ref:`xmlattr-IEC61850clAIDeadband`" ":ref:`xmlattr-IEC61850clAIPercent`"

AI.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clAIQualifier" "IEC61850 Client AI internal qualifier" ":ref:`xmlattr-IEC61850clAIQualifier`" "AI internal qualifier"

   * :attr:	Bit 3
     :val:	xxxx.0xxx
     :desc:	**Use original** timetag when event is received from IED

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	**Substitute** timetag with local time when event is received from IED

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	AI is **enabled** and will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AI is **disabled** and will be discarded when received

   * :attr:	Bits 0...2;4...6
     :val:	Any
     :desc:	Bits reserved for future use

AI.DSflags
^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clAIDSflags" "IEC61850 Client AI Dataset flags" ":ref:`xmlattr-IEC61850clAIDSflags`" "Dataset flags"

   * :attr:	Bits 1;0
     :val:	xxxx.xx00
     :desc:	Dataset that is linked to **unbuffered** Report Block is required for this AI object

   * :(attr):
     :val:	xxxx.xx01
     :desc:	Dataset that is linked to **buffered** Report Block is required for this AI object

   * :(attr):
     :val:	xxxx.xx10
     :desc:	Dataset that is linked to **any** Report Block can be used for this AI object

   * :(attr):
     :val:	xxxx.xx11
     :desc:	Reserved for future use

   * :attr:	Bit 5
     :val:	xx0x.xxxx
     :desc:	Use **any** dataset that contains this AI object.

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	Use **referenced only** dataset, that is set by :ref:`xmlattr-IEC61850clAIDSref` attribute.
		No other dataset will be used even if :ref:`xmlattr-IEC61850clAIDSref` dataset doesn't contain this AI object.

   * :attr:	Bits 2;3;6;7
     :val:	Any
     :desc:	Bits reserved for future use
