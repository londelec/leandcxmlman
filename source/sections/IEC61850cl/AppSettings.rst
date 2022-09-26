.. _xmlelem-IEC61850clApp:

AppSettings
^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`xmlelem-IEC61850clApp` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clApp`"

.. code-block:: none

 <AppSettings IgnoreTimetags="1" AIDeadband="2" AIPercent="0.5" DIEventStartup="1" AIEventStartup="1" ForwardGI="1"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clApp" "IEC61850 Client AppSettings attributes" ":spec: |C{0.18}|C{0.16}|C{0.1}|S{0.56}|"

.. include-file:: sections/Include/ma_IgnoreTimetags.rstinc "" ":ref:`xmlelem-IEC61850clDI`.\ :ref:`xmlattr-IEC61850clDIQualifier` \ or :ref:`xmlelem-IEC61850clAI`.\ :ref:`xmlattr-IEC61850clAIQualifier` \ attribute can be used to disable timetag processing for each DI/AI."
.. include-file:: sections/Include/ma_IgnoreTimetags2.rstinc

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ":ref:`xmlelem-IEC61850clAI`" ":ref:`xmlattr-IEC61850clAIDeadband`" ":ref:`xmlattr-IEC61850clAIPercent`"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc ""

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc ""


