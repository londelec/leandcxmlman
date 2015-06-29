.. _docref-IEC104maASDUSettingsAttr:

ASDUSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`ASDUSettings<ref-IEC104maASDUSettings>` element node.

Please see sample :ref:`ASDUSettings<ref-IEC104maASDUSettings>` node and the table listing all available attributes below.

.. code-block:: none

 <ASDUSettings InvalidEvent="1" IgnoreTimetags="1" SUthroughoutDST="1" AIDeadband="2" AIPercent="0.5" DOQOC="1" DOType="46" AOType="50" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" />

.. _docref-IEC104maASDUSettingsAttab:

.. field-list-table:: IEC 60870-5-104 Master ASDUSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc

.. include-file:: sections/Include/IEC10xma_IgnoreTimetags.rstinc

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ".. _ref-IEC104maASDUSettingsAIDeadband:" ".. _ref-IEC104maASDUSettingsAIPercent:" ":ref:`AI<ref-IEC10xmaAI>`" ":ref:`Deadband<ref-IEC10xmaAIDeadband>`" ":ref:`Percent<ref-IEC10xmaAIPercent>`"

.. include-file:: sections/Include/IEC10xma_ASDU_2.rstinc "" ".. _ref-IEC104maASDUSettingsDOQOC:" ".. _ref-IEC104maASDUSettingsDOType:" ".. _ref-IEC104maASDUSettingsAOType:"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc

