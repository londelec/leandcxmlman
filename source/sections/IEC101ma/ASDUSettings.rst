.. _xmlelem-IEC101maAsdu:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`xmlelem-IEC101maAsdu` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC101maAsdu`"

.. code-block:: none

 <ASDUSettings COTSize="1" CAASize="1" IOASize="2" InvalidEvent="1" IgnoreTimetags="1" SUthroughoutDST="1" AIDeadband="2" AIPercent="0.5" DOQOC="1" DOType="46" AOType="50" Flags="0x00" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" TimetagFBrange="180"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC101maAsdu" "IEC60870-5-101 Master ASDUSettings attributes" ":spec: |C{0.19}|C{0.14}|C{0.12}|S{0.55}|"

.. include-file:: sections/Include/IEC60870_ASDUsizes.rstinc ""

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc ""

.. include-file:: sections/Include/ma_IgnoreTimetags.rstinc "" ":ref:`xmlelem-IEC10xmaDI`.\ :ref:`xmlattr-IEC10xmaDIqualifier` \ or :ref:`xmlelem-IEC10xmaAI`.\ :ref:`xmlattr-IEC10xmaAIqualifier` \ attribute can be used to disable timetag processing for each DI/AI."
.. include-file:: sections/Include/ma_IgnoreTimetags2.rstinc ""

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc ""

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ":ref:`xmlelem-IEC10xmaAI`" ":ref:`xmlattr-IEC10xmaAIDeadband`" ":ref:`xmlattr-IEC10xmaAIPercent`"

.. include-file:: sections/Include/IEC10xma_ASDU_2.rstinc "" ":numref:`tabid-IEC101maAsduFlags`"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc ""

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc ""

   * :attr:	:xmlattr:`TimetagFBrange`
     :val:	0...600
     :def:	240 sec
     :desc:	Received time-tag hour forward-backward adjustment range.
		If the short time-tag [:lemonobgtext:`CP24Time2a`] of the event received from outstation is closer to full hour (0 mins 0 secs) than the specified range in seconds, the hour value of the resulting timestamp will be automatically adjusted.
		This functionality ensures correct hour value is attached to the short time-tag [:lemonobgtext:`CP24Time2a`], as it carries only minutes and milliseconds, if event arrived late.
		Hour, day, month and year values are taken from internal system time.
		If the time value of the event time-tag is just before a full hour (e.g. min:msec = 59:58000) and there is a delay in communication channel,
		there is a chance the event is received only after internal hour has already changed (e.g. hh:min:sec.msec = 13:00:01.000).
		This will lead to incorrect hour (hour = 13) being applied to the resulting timestamp, although it is most likely the event was generated before the hour change (e.g. generated at hh:min:sec.msec = 12:59:58.000).
		:ref:`xmlattr-IEC101maAsduTimetagFBrange` attribute ensures the hour of the resulting timestamp is automatically decremented if the time of the received time-tag falls within a forward-backward adjustment range and internal hour has recently changed.
		Similar functionality applies if the time of the received time-tag appears to be in the future, but the internal hour hasn't changed yet.
		In this case hour of the resulting timestamp is automatically incremented.
		Default value 240 will adjust received event time-tags min:msec = 56:00000...03:59999 if they arrive when internal time is hh:min:sec.msec = 12:56:00.000...13:03:59.999


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC101maAsduFlags" "IEC60870-5-101 Master ASDU flags" ":ref:`xmlattr-IEC101maAsduFlags`" "ASDU flags"

.. include-file:: sections/Include/IEC10xma_ASDUflags.rstinc
