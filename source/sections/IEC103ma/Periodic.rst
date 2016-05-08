.. _ref-IEC103maPeriodic:

Periodic
^^^^^^^^

Periodic intervals to send various messages are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC103maPeriodic>`"

.. code-block:: none

   <Periodic GI="600" TimeSync="0" />

.. include-file:: sections/Include/ma_Periodic.rstinc "" ".. _docref-IEC103maPeriodicAttab:" "IEC60870-5-103 Master Periodic attributes"

.. include-file:: sections/Include/IEC10xma_PeriodicTimeSync.rstinc "" ":inlinetip:`Time Synchronization commands are sent only at predefined intervals which means station Online/Offline status changes don't trigger additional synchronziation command.`"
