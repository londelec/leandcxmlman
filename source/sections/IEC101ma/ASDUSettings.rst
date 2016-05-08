.. _ref-IEC101maASDUSettings:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`<ref-IEC101maASDUSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101maASDUSettings>`"

.. code-block:: none

 <ASDUSettings COTSize="1" CAASize="1" IOASize="2" InvalidEvent="1" IgnoreTimetags="1" SUthroughoutDST="1" AIDeadband="2" AIPercent="0.5" DOQOC="1" DOType="46" AOType="50" Flags="0x00" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" TimetagFBrange="180"/>


.. _docref-IEC101maASDUSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Master ASDUSettings attributes"

.. include-file:: sections/Include/IEC60870_ASDUsizes.rstinc "" ".. _ref-IEC101maASDUSettingsCOTSize:" ".. _ref-IEC101maASDUSettingsCAASize:" ".. _ref-IEC101maASDUSettingsIOASize:"

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc

.. include-file:: sections/Include/ma_IgnoreTimetags.rstinc

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ".. _ref-IEC101maASDUSettingsAIDeadband:" ".. _ref-IEC101maASDUSettingsAIPercent:" ":ref:`AI<ref-IEC10xmaAI>`" ":ref:`<ref-IEC10xmaAIDeadband>`" ":ref:`<ref-IEC10xmaAIPercent>`"

.. include-file:: sections/Include/IEC10xma_ASDU_2.rstinc "" ".. _ref-IEC101maASDUSettingsDOQOC:" ".. _ref-IEC101maASDUSettingsDOType:" ".. _ref-IEC101maASDUSettingsAOType:" ".. _ref-IEC101maASDUSettingsFlags:" ":numref:`ref-IEC101maASDUFlagsBits`"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc

   * :attr:     .. _ref-IEC101maASDUSettingsTimetagFBrange:

                :xmlref:`TimetagFBrange`
     :val:      0...600
     :def:      240 sec
     :desc:     Recevied time-tag hour forward-backward adjustment range.
		If the short time-tag [CP24Time2a] of the event received from outstation is closer to full hour (0 mins 0 secs) than the specified range in seconds, the hour value of the resulting timestamp will be automatically adjusted if event is received late. 
		This functionality ensures correct hour value is attached to the short time-tags [CP24Time2a] as they carry only minutes and milliseconds. 
		Hour, day, month and year values are attached from leandc's internal time.
		If the time value of the received time-tag is just before a full hour (e.g. min:msec = 59:58000) and there is a delay in a communication channel,
		event might get received only after internal hour has already changed (e.g. hh:min:msec = 13:00:10000).
		This will lead to incorrect hour (e.g. hh = 13) being applied to the resulting timestamp although it is most likely the event was generated (e.g. hh:min:msec = 12:59:58000)
		:xmlref:`TimetagFBrange` attribute ensures if the time of the received time-tag falls within a forward-backward adjustment range and
		internal hour has already changed, the hour being applied to the resulting timestamp is automatically decremented.
		Similar functionality applies if the time of the received time-tag appears to be in the future, but the internal hour hasn't changed yet.
		In this case hour being applied to the resulting timestamp is automatically incremented.

.. _ref-IEC101maASDUFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-101 Master ASDU flags" ":ref:`<ref-IEC101maASDUSettingsFlags>`" "ASDU flags"

.. include-file:: sections/Include/IEC10xma_ASDUflags.rstinc
