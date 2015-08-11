.. _docref-IEC104maPeriodicAttr:

Periodic attributes
^^^^^^^^^^^^^^^^^^^

Periodic intervals of sending various messages can be specified using attributes of :ref:`Periodic<ref-IEC104maPeriodic>` element node.

Please see sample :ref:`Periodic<ref-IEC104maPeriodic>` node and the table listing all available attributes below.

.. code-block:: none

   <Periodic GI="600" Group1="300" Group16="400" TimeSync="600" />

.. include-file:: sections/Include/IEC10xma_Periodic.rstinc "" ".. _docref-IEC104maPeriodicAttab:" "IEC 60870-5-104 Master Periodic attributes"

.. include-file:: sections/Include/IEC10xma_PeriodicICGroups.rstinc ""

.. include-file:: sections/Include/IEC10xma_PeriodicTimeSync.rstinc "" ":inlinetip:`Additional Time Synchronization command will be sent automatically every time station goes Online regardless if predefined interval has expired.`"
