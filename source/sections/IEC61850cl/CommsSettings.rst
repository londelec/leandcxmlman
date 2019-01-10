.. _ref-IEC61850clCommsSettings:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) change behavior and related delays can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clCommsSettings>`"

.. code-block:: none

   <CommsSettings OfflineDelay="10" PostOfflineDelay="1000" />

.. _docref-IEC61850clCommsSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

   * :attr:     .. _ref-IEC61850clCommsSettingsOfflineDelay:

                :xmlref:`OfflineDelay`
     :val:      0...2\ :sup:`32`\  - 1
     :def:      6 sec
     :desc:     Offline delay in seconds before station status is changed to OFFLINE.
		Offline delay timer is activated after TCP socket has been closed.
		Default 6 seconds - station status will change to OFFLINE 6 seconds after TCP socket has been closed by either host.

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ".. _ref-IEC61850clCommsSettingsPostOfflineDelay:" ":ref:`<ref-IEC61850clCommsSettingsOfflineDelay>`"

