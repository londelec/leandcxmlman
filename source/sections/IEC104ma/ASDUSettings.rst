.. _ref-IEC104maASDUSettings:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`<ref-IEC104maASDUSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC104maASDUSettings>`"

.. code-block:: none

 <ASDUSettings InvalidEvent="1" IgnoreTimetags="1" SUthroughoutDST="1" AIDeadband="2" AIPercent="0.5" DOQOC="1" DOType="46" AOType="50" Flags="0x00" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" />


.. _docref-IEC104maASDUSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-104 Master ASDUSettings attributes"  ":spec: |C{0.19}|C{0.14}|C{0.12}|S{0.55}|"

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc

.. include-file:: sections/Include/ma_IgnoreTimetags.rstinc

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ".. _ref-IEC104maASDUSettingsAIDeadband:" ".. _ref-IEC104maASDUSettingsAIPercent:" ":ref:`AI<ref-IEC10xmaAI>`" ":ref:`<ref-IEC10xmaAIDeadband>`" ":ref:`<ref-IEC10xmaAIPercent>`"

.. include-file:: sections/Include/IEC10xma_ASDU_2.rstinc "" ".. _ref-IEC104maASDUSettingsDOQOC:" ".. _ref-IEC104maASDUSettingsDOType:" ".. _ref-IEC104maASDUSettingsAOType:" ".. _ref-IEC104maASDUSettingsFlags:" ":numref:`ref-IEC104maASDUFlagsBits`"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc

.. _ref-IEC104maASDUFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-104 Master ASDU flags" ":ref:`<ref-IEC104maASDUSettingsFlags>`" "ASDU flags"

.. include-file:: sections/Include/IEC10xma_ASDUflags.rstinc
