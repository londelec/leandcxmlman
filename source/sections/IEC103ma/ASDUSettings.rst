.. _ref-IEC103maASDUSettings:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`<ref-IEC103maASDUSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC103maASDUSettings>`"

.. code-block:: none

 <ASDUSettings InvalidEvent="1" IgnoreTimetags="1" SUthroughoutDST="1" AIDeadband="2" AIPercent="0.5" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" />


.. _docref-IEC103maASDUSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-103 Master ASDUSettings attributes"

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc

.. include-file:: sections/Include/ma_IgnoreTimetags.rstinc

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ".. _ref-IEC103maASDUSettingsAIDeadband:" ".. _ref-IEC103maASDUSettingsAIPercent:" ":ref:`AI<ref-IEC103maAI>`" ":ref:`<ref-IEC103maAIDeadband>`" ":ref:`<ref-IEC103maAIPercent>`"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc
