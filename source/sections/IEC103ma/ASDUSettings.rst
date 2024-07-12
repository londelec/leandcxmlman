.. _xmlelem-IEC103maAsdu:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`xmlelem-IEC103maAsdu` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC103maAsdu`"

.. code-block:: none

 <ASDUSettings InvalidEvent="1" IgnoreTimetags="1" SUthroughoutDST="1" AIDeadband="2" AIPercent="0.5" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" Flags="0x00" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC103maAsdu" "IEC60870-5-103 Master ASDUSettings attributes" ":spec: |C{0.19}|C{0.14}|C{0.1}|S{0.57}|"

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc ""

.. include-file:: sections/Include/ma_IgnoreTimetags.rstinc "" ""
.. include-file:: sections/Include/ma_IgnoreTimetags2.rstinc ""

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc ""

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ":ref:`xmlelem-IEC103maAI`" ":ref:`xmlattr-IEC103maAIDeadband`" ":ref:`xmlattr-IEC103maAIPercent`"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc ""

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc ""

   * :attr:	:xmlattr:`Flags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Various settings to enable customized data processing.
		See :numref:`tabid-IEC103maAsduFlags` for description.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC103maAsduFlags" "IEC60870-5-103 Master ASDU flags" ":ref:`xmlattr-IEC103maAsduFlags`" "ASDU flags"

   * :attr:	Bit 4
     :val:	xxx0.xxxx
     :desc:	**Check** Test bit of the received Cause Of Transmission [:lemonobgtext:`COT`].
		DI/AI messages received with set test bit in the [:lemonobgtext:`COT`] will be discarded.

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	**Ignore** Test bit of the received Cause Of Transmission [:lemonobgtext:`COT`].
		DI/AI messages received with set test bit in the [:lemonobgtext:`COT`] will be processed as if no test bit was set.

   * :attr:	:bitdef:`5`
     :val:	xx0x.xxxx
     :desc:	**Don't generate** DI position change event when positive command confirmation is received from outstation.
		DI event is generated only when received from oustation with Causes Of Transmission [:lemonobgtext:`COT`]=1,9,11,12.

   * :(attr):
     :val:	xx1x.xxxx
     :desc:	**Generate** DI position change event when positive command confirmation is received from outstation.
		DI event is generated when command response with Cause Of Transmission [:lemonobgtext:`COT`]=20 is received.

   * :attr:	Bits 0...3;6...7
     :val:	Any
     :desc:	Bits reserved for future use
