.. _docref-IEC104maCommsSettingsAttr:

CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state change behavior and related delays can be specified using attributes of :ref:`CommsSettings<ref-IEC104maCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-IEC104maCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings	OfflineDelay="10"
                        PostOfflineDelay="1000"
                        OnlineGIDelay="10"
                        GIAfterRecovery="1" />

.. _docref-IEC104maCommsSettingsAttab:

.. field-list-table:: IEC 60870-5-104 Master CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
      
   * :attr:    .. _ref-IEC104maCommsSettingsOfflineDelay:
            
               :xmlref:`OfflineDelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Offline delay in seconds before station status is changed to OFFLINE. Offline delay timer is activated after TCP socket has been closed. Default 6 seconds - station status will change to OFFLINE 6 seconds after TCP socket has been closed by either host (default 6 seconds)
 
.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ".. _ref-IEC104maCommsSettingsPostOfflineDelay:" ":ref:`OfflineDelay<ref-IEC104maCommsSettingsOfflineDelay>`"

.. include-file:: sections/Include/IEC10xma_OnlineGIDelay.rstinc "" ".. _ref-IEC104maCommsSettingsOnlineGIDelay:"
 
   * :attr:    .. _ref-IEC104maCommsSettingsGIAfterRecovery:
            
               :xmlref:`GIAfterRecovery`
     :val:     0
     :desc:    **Don't send** General Interrogation command when outstation comes online after a communication loss (station status changes to ONLINE). :inlinetip:`General Interrogation is always sent on leandc startup regardless this setting.`

   * :(attr):
     :val:     1
     :desc:    **Send** General Interrogation command when outstation comes online after a communication loss (station status changes to ONLINE) (default value)
