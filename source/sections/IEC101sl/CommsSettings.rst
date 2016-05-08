.. _ref-IEC101slCommsSettings:

CommsSettings
^^^^^^^^^^^^^

Communication state change behavior and related delays can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101slCommsSettings>`"

.. code-block:: none

   <CommsSettings OfflineDelay="120" StartupGIDelay="10" />


.. _docref-IEC101slCommsSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Slave CommsSettings attributes"

   * :attr:     :xmlref:`OfflineDelay`
     :val:      1...2\ :sup:`32`\  - 1
     :def:      60 sec
     :desc:     Delay in seconds before resetting the link if there is no request from Master station. Reset remote link message is required after communication loss exceeding configured offline delay in order to restart communication.

.. include-file:: sections/Include/IEC10xsl_StartupGIDelay.rstinc

