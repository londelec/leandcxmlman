.. _docref-IEC103maASDUSettingsAttr:

ASDUSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`ASDUSettings<ref-IEC103maASDUSettings>` element node.

Please see sample :ref:`ASDUSettings<ref-IEC103maASDUSettings>` node and the table listing all available attributes below.

.. code-block:: none

 <ASDUSettings InvalidEvent="1" IgnoreTimetags="1" SUthroughoutDST="1" AIDeadband="2" AIPercent="0.5" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" />

.. _docref-IEC103maASDUSettingsAttab:

.. field-list-table:: IEC 60870-5-103 Master ASDUSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc

.. include-file:: sections/Include/IEC10xma_IgnoreTimetags.rstinc

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ".. _ref-IEC103maASDUSettingsAIDeadband:" ".. _ref-IEC103maASDUSettingsAIPercent:" ":ref:`AI<ref-IEC103maAI>`" ":ref:`Deadband<ref-IEC103maAIDeadband>`" ":ref:`Percent<ref-IEC103maAIPercent>`"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc
