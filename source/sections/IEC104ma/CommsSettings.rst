.. _ref-IEC104maCommsSettings:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) change behavior and related delays can be specified using attributes of :ref:`<ref-IEC104maCommsSettings>` 
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC104maCommsSettings>`"

.. code-block:: none

   <CommsSettings OfflineDelay="10" PostOfflineDelay="1000" OnlineGIDelay="10" GIAfterRecovery="1" />


.. _docref-IEC104maCommsSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-104 Master CommsSettings attributes"

   * :attr:     .. _ref-IEC104maCommsSettingsOfflineDelay:

                :xmlref:`OfflineDelay`
     :val:      0...2\ :sup:`32`\  - 1
     :def:      6 sec
     :desc:     Offline delay in seconds before station status is changed to OFFLINE.
		Offline delay timer is activated after TCP socket has been closed.
		Default 6 seconds - station status will change to OFFLINE 6 seconds after TCP socket has been closed by either host.

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ".. _ref-IEC104maCommsSettingsPostOfflineDelay:" ":ref:`OfflineDelay<ref-IEC104maCommsSettingsOfflineDelay>`"

.. include-file:: sections/Include/IEC10xma_OnlineGIDelay.rstinc "" ".. _ref-IEC104maCommsSettingsOnlineGIDelay:"

   * :attr:     .. _ref-IEC104maCommsSettingsGIAfterRecovery:

                :xmlref:`GIAfterRecovery`
     :val:      0
     :def:      1
     :desc:     **Don't send** General Interrogation command when outstation comes online after a communication loss (station status changes to ONLINE).
		:inlinetip:`General Interrogation is always sent on leandc startup regardless this setting.`

   * :(attr):
     :val:      1
     :(def):
     :desc:     **Send** General Interrogation command when outstation comes online after a communication loss (station status changes to ONLINE)
