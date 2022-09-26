.. _xmlelem-IEC104maAsdu:

ASDUSettings
^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`xmlelem-IEC104maAsdu` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC104maAsdu`"

.. code-block:: none

 <ASDUSettings InvalidEvent="1" IgnoreTimetags="1" SUthroughoutDST="1" AIDeadband="2" AIPercent="0.5" DOQOC="1" DOType="46" AOType="50" Flags="0x00" DIEventStartup="1" AIEventStartup="1" ForwardGI="1" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC104maAsdu" "IEC60870-5-104 Master ASDUSettings attributes"  ":spec: |C{0.19}|C{0.14}|C{0.12}|S{0.55}|"

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc ""

.. include-file:: sections/Include/ma_IgnoreTimetags.rstinc "" ":ref:`xmlelem-IEC10xmaDI`.\ :ref:`xmlattr-IEC10xmaDIqualifier` \ or :ref:`xmlelem-IEC10xmaAI`.\ :ref:`xmlattr-IEC10xmaAIqualifier` \ attribute can be used to disable timetag processing for each DI/AI."
.. include-file:: sections/Include/ma_IgnoreTimetags2.rstinc ""

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc ""

.. include-file:: sections/Include/AI_ThresholdsCmn.rstinc "" ":ref:`xmlelem-IEC10xmaAI`" ":ref:`xmlattr-IEC10xmaAIDeadband`" ":ref:`xmlattr-IEC10xmaAIPercent`"

.. include-file:: sections/Include/IEC10xma_ASDU_2.rstinc "" ":numref:`tabid-IEC104maAsduFlags`"

.. include-file:: sections/Include/IEC60870_ASDU_EventStartup.rstinc ""

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc ""


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC104maAsduFlags" "IEC60870-5-104 Master ASDU flags" ":ref:`xmlattr-IEC104maAsduFlags`" "ASDU flags"

.. include-file:: sections/Include/IEC10xma_ASDUflags.rstinc
