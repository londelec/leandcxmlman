.. _xmlelem-IEC103maComm:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) change behavior and related delays can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC103maComm`"

.. code-block:: none

   <CommsSettings NoRespCount="5" DegradedRetries="5" DegradedTimeout="600" ControlLockTimer="20" OfflineDelay="10" PostOfflineDelay="1000" OnlineGIDelay="10" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC103maComm" "IEC60870-5-103 Master CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ":ref:`xmlattr-IEC103maCommOfflineDelay`" ":ref:`xmlattr-IEC103maCommDegradedTimeout`" ":ref:`xmlattr-IEC103maCommDegradedRetries`" "600 sec"

.. include-file:: sections/Include/IEC10xma_ControlLockTimer.rstinc "" ":ref:`xmlattr-IEC103maCommControlLockTimer`"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ":ref:`xmlattr-IEC103maCommNoRespCount`"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ":ref:`xmlattr-IEC103maCommOfflineDelay`"

.. include-file:: sections/Include/IEC10xma_OnlineGIDelay.rstinc ""
