
.. _xmlgroup-SpabusmaAI: lelabel=AITable
.. _xmlelem-SpabusmaAI: lelabel=AI

AITable group
-------------

.. include-file:: sections/Include/ma_DIAI_table.rstinc "" ":ref:`xmlgroup-SpabusmaAI`" ":ref:`xmlelem-SpabusmaAI`" ":numref:`tabid-SpabusmaAI`" ":ref:`docref-IEC10xslAI`" "AI" "analog information" "IED"

Please see sample :ref:`xmlgroup-SpabusmaAI` group and :ref:`xmlelem-SpabusmaAI` element nodes below.
There are 4 analog information objects defined with 3 :ref:`xmlelem-SpabusmaAI` element nodes.

.. code-block:: none

   <AITable>
	<AI Index="0" PollMsg="1" DataPos="1" Coeff="1.0" Deadband="0.5" Percent="0" Total="2"/>
	<AI Index="2" Request="10I1" Coeff="1.0" Deadband="0" Percent="1.4"/>
	<AI Index="3" Request="22I1" DataPos="1" Coeff="-17.0" Deadband="1.4"/>
   </AITable>

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaAI`"

.. code-block:: none

   <AI Index="0" PollMsg="1" DataPos="1" Request="10I1" Qualifier="0x00" Coeff="1.0" Deadband="0.5" Percent="0" StartOffset="6554" ZeroDeadband="3.0" Offset="-2.0" OffsetDeadband="2.0" NonZeroOffset="200.0" Total="1" Name="Voltage" />

.. include-file:: sections/Include/tip_order.rstinc "" ":ref:`xmlelem-SpabusmaAI`"

AI attributes
^^^^^^^^^^^^^

.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaAI" "Spabus Master AI attributes" ":spec: |C{0.18}|C{0.16}|C{0.1}|S{0.56}|"

.. include-file:: sections/Include/ma_Index.rstinc "" "AI"

.. include-file:: sections/Include/Spabusma_PollMsg.rstinc ""
		Value 0 means no poll message is selected, :ref:`xmlattr-SpabusmaAIRequest` attribute must be used to specify the message.
		:inlinetip:`This attribute has higher priority than` :ref:`xmlattr-SpabusmaAIRequest`\  :inlinetip:`, if both attributes are specified` :ref:`xmlattr-SpabusmaAIPollMsg` :inlinetip:`will be used.`

   * :attr:	:xmlattr:`DataPos`
     :val:	1...16
     :def:	1
     :desc:	Data position in the received message.

   * :attr:	:xmlattr:`Request`
     :val:	see description
     :def:	n/a
     :desc:	| Spabus request to poll data from outstation. Attribute has the following format [:lemonobgtext:`Channel`][:lemonobgtext:`Category`][:lemonobgtext:`Data Number`].
		| Range of [:lemonobgtext:`Channel`] values 0..999
		| [:lemonobgtext:`Category`] is one of :lemonobgtext:`I`, :lemonobgtext:`M`, :lemonobgtext:`O`, :lemonobgtext:`S`, :lemonobgtext:`V`
		| Range of [:lemonobgtext:`Data Number`] values 1..999999
		| Example :ref:`xmlattr-SpabusmaAIRequest`\ ="\ :lemonobgtext:`15I2`"
		| :inlinetip:`Attribute is optional if` :ref:`xmlattr-SpabusmaAIPollMsg` :inlinetip:`is used.`

.. include-file:: sections/Include/Qualifier.rstinc "" ":numref:`tabid-SpabusmaAIQualifier`"

.. include-file:: sections/Include/AI_Coeff.rstinc ""

.. include-file:: sections/Include/AI_Thresholds.rstinc "" ":ref:`xmlattr-SpabusmaAIDeadband`" ":ref:`xmlattr-SpabusmaAIPercent`" ":ref:`xmlelem-SpabusmaApp`.\ :ref:`xmlattr-SpabusmaAppAIDeadband`" ":ref:`xmlelem-SpabusmaApp`.\ :ref:`xmlattr-SpabusmaAppAIPercent`"

.. include-file:: sections/Include/AI_Scaling.rstinc "" ":ref:`xmlattr-SpabusmaAIStartOffset`" ":ref:`xmlattr-SpabusmaAIZeroDeadband`" ":ref:`xmlattr-SpabusmaAIOffset`" ":ref:`xmlattr-SpabusmaAIOffsetDeadband`" ":ref:`xmlattr-SpabusmaAINonZeroOffset`"

.. include-file:: sections/Include/Total.rstinc "" ":ref:`xmlattr-SpabusmaAIIndex` and :ref:`xmlattr-SpabusmaAIDataPos`" ":ref:`xmlelem-SpabusmaAI`" "254"

.. include-file:: sections/Include/Name.rstinc ""

.. include-file:: sections/Include/ma_AI_Annex.rstinc "" ":ref:`xmlattr-SpabusmaAIDeadband`" ":ref:`xmlattr-SpabusmaAIPercent`"

AI.Qualifier
^^^^^^^^^^^^

.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-SpabusmaAIQualifier" "Spabus Master AI internal qualifier" ":ref:`xmlattr-SpabusmaAIQualifier`" "AI internal qualifier"

   * :attr:	Bit 7
     :val:	0xxx.xxxx
     :desc:	AI is **enabled** and will be processed when received

   * :(attr):
     :val:	1xxx.xxxx
     :desc:	AI is **disabled** and will be discarded when received

   * :attr:	Bits 0..6
     :val:	Any
     :desc:	Bits reserved for future use

