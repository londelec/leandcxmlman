.. _docref-IEC103maPeriodicAttr:

Periodic attributes
^^^^^^^^^^^^^^^^^^^

Periodic intervals of sending various messages can be specified using attributes of :ref:`Periodic<ref-IEC103maPeriodic>` element node.

Please see sample :ref:`Periodic<ref-IEC103maPeriodic>` node and the table listing all available attributes below.

.. code-block:: none

   <Periodic GI="600" TimeSync="0" />

.. include-file:: sections/Include/IEC10xma_Periodic.rstinc "" ".. _docref-IEC103maPeriodicAttab:" "IEC 60870-5-103 Master Periodic attributes"

.. include-file:: sections/Include/IEC10xma_PeriodicTimeSync.rstinc "" ":inlinetip:`Time Synchronization commands are sent only at predefined intervals which means station Online/Offline status changes don't trigger additional synchronziation command.`"
