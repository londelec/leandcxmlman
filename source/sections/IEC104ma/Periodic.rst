.. _xmlelem-IEC104maPeriodic:

Periodic
^^^^^^^^

Periodic intervals to send various messages are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC104maPeriodic`"

.. code-block:: none

   <Periodic GI="600" Group1="300" Group2="0" Group3="0" Group4="0" Group5="0" Group6="0" Group7="0" Group8="0" Group9="0" Group10="0" Group11="0" Group12="0" Group13="0" Group14="0" Group15="0" Group16="0" TimeSync="600" />

.. include-file:: sections/Include/ma_Periodic.rstinc "" "tabid-IEC104maPeriodic" "IEC60870-5-104 Master Periodic attributes"

.. include-file:: sections/Include/IEC10xma_PeriodicICGroups.rstinc ""

.. include-file:: sections/Include/ma_PeriodicTimeSync.rstinc "" ":inlinetip:`Time Synchronization command will be sent every time station goes Online regardless if predefined interval has expired.`"
