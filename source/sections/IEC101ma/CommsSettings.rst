.. _xmlelem-IEC101maComm:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) reporting and related delays can be specified using attributes of :ref:`xmlelem-IEC101maComm`
element node.

Please see sample :ref:`xmlelem-IEC101maComm` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings NoRespCount="5" DegradedRetries="5" DegradedTimeout="600" ControlLockTimer="20" OfflineDelay="10" PostOfflineDelay="1000" OnlineGIDelay="10" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC101maComm" "IEC60870-5-101 Master CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ":ref:`xmlattr-IEC101maCommOfflineDelay`" ":ref:`xmlattr-IEC101maCommDegradedTimeout`" ":ref:`xmlattr-IEC101maCommDegradedRetries`" "600 sec"

.. include-file:: sections/Include/IEC10xma_ControlLockTimer.rstinc "" ":ref:`xmlattr-IEC101maCommControlLockTimer`"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ":ref:`xmlattr-IEC101maCommNoRespCount`"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ":ref:`xmlattr-IEC101maCommOfflineDelay`"

.. include-file:: sections/Include/IEC10xma_OnlineGIDelay.rstinc ""
