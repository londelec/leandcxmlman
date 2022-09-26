.. _xmlelem-IEC103maPeriodic:

Periodic
^^^^^^^^

Periodic intervals to send various messages are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC103maPeriodic`"

.. code-block:: none

   <Periodic GI="600" TimeSync="0" />

.. include-file:: sections/Include/ma_Periodic.rstinc "" "tabid-IEC103maPeriodic" "IEC60870-5-103 Master Periodic attributes"

.. include-file:: sections/Include/ma_PeriodicTimeSync.rstinc "" ":inlinetip:`Time Synchronization commands are only sent at predefined intervals. This means station Online/Offline status change doesn't trigger time synchronization command.`"
