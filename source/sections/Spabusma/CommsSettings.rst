.. _xmlelem-SpabusmaComm:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) change behavior and related delays can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaComm`"

.. code-block:: none

   <CommsSettings NoRespCount="5" DegradedRetries="5" DegradedTimeout="600" ControlLockTimer="30" OfflineDelay="10" PostOfflineDelay="1000" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-SpabusmaComm" "Spabus Master CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ":ref:`xmlattr-SpabusmaCommOfflineDelay`" ":ref:`xmlattr-SpabusmaCommDegradedTimeout`" ":ref:`xmlattr-SpabusmaCommDegradedRetries`" "300 sec"

.. include-file:: sections/Include/IEC10xma_ControlLockTimer.rstinc "" ":ref:`xmlattr-SpabusmaCommControlLockTimer`"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ":ref:`xmlattr-SpabusmaCommNoRespCount`"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ":ref:`xmlattr-SpabusmaCommOfflineDelay`"
