
ASDUSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`ASDUSettings<ref-IEC103maASDUSettings>` element node.

Please see sample :ref:`ASDUSettings<ref-IEC103maASDUSettings>` node and the table listing all available attributes below.

.. code-block:: none

 <ASDUSettings  InvalidEvent="1"
		IgnoreTimetags="1"
		SUthroughoutDST="1"
		AIDeadband="2"
		AIPercent="0.5"
		DIEventStartup="1"
		AIEventStartup="1" />

.. _ref-IEC103maASDUSettingsAttributes:

.. field-list-table:: IEC 60807-5-103 Master ASDUSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
.. include-file:: sections/Include/IEC10xma_ASDU_IVSU.rstinc

.. include-file:: sections/Include/AIcommon_Thresholds.rstinc "" ".. _ref-IEC103maASDUSettingsAIDeadband:" ".. _ref-IEC103maASDUSettingsAIPercent:" ":ref:`AI<ref-IEC103maAI>`" ":ref:`Deadband<ref-IEC103maAIDeadband>`" ":ref:`Percent<ref-IEC103maAIPercent>`"

.. include-file:: sections/Include/IEC10xma_ASDU_EventStartup.rstinc

