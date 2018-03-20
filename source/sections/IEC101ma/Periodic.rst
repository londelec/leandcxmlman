.. _ref-IEC101maPeriodic:

Periodic
^^^^^^^^

Periodic intervals to send various messages are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101maPeriodic>`"

.. code-block:: none

   <Periodic GI="600" Group1="300" Group2="0" Group3="0" Group4="0" Group5="0" Group6="0" Group7="0" Group8="0" Group9="0" Group10="0" Group11="0" Group12="0" Group13="0" Group14="0" Group15="0" Group16="0" TimeSync="600" />

.. include-file:: sections/Include/ma_Periodic.rstinc "" ".. _docref-IEC101maPeriodicAttab:" "IEC60870-5-101 Master Periodic attributes"

.. include-file:: sections/Include/IEC10xma_PeriodicICGroups.rstinc ""

.. include-file:: sections/Include/ma_PeriodicTimeSync.rstinc "" ":inlinetip:`Time Synchronization commands are only sent at predefined intervals. This means station Online/Offline status change doesn't trigger time synchronziation command.`"
