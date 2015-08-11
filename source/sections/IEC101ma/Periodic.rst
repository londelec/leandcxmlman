.. _docref-IEC101maPeriodicAttr:

Periodic attributes
^^^^^^^^^^^^^^^^^^^

Periodic intervals of sending various messages can be specified using attributes of :ref:`Periodic<ref-IEC101maPeriodic>` element node.

Please see sample :ref:`Periodic<ref-IEC101maPeriodic>` node and the table listing all available attributes below.

.. code-block:: none

   <Periodic GI="600" Group1="300" Group16="400" TimeSync="600" />

.. include-file:: sections/Include/IEC10xma_Periodic.rstinc "" ".. _docref-IEC101maPeriodicAttab:" "IEC 60870-5-101 Master Periodic attributes"

.. include-file:: sections/Include/IEC10xma_PeriodicICGroups.rstinc ""

.. include-file:: sections/Include/IEC10xma_PeriodicTimeSync.rstinc "" ":inlinetip:`Time Synchronization commands are sent only at predefined intervals which means station Online/Offline status changes don't trigger additional synchronziation command.`"
