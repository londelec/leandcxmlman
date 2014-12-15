
CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state change behavior and related delays can be specified using attributes of :ref:`CommsSettings<ref-IEC104maCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-IEC104maCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings OfflineDelay="10"
         OnlineGIDelay="10"
         GIAfterRecovery="1"
         OfflineNTDelay="1000"
         DisabledNT="1" />

.. _ref-IEC104maCommsSettingsAttributes:

.. field-list-table:: IEC 60807-5-104 Master CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
      
   * :attr:    .. _ref-IEC104maCommsSettingsOfflineDelay:
            
               :xmlref:`OfflineDelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Offline delay in seconds before outstation status is changed to OFFLINE. Offline delay timer is activated after TCP socket has been closed. Default 6 seconds -  station status will be changed to OFFLINE  6 seconds after TCP socket has been closed by either peer (default 6 seconds)
 
   * :attr:    .. _ref-IEC104maCommsSettingsOnlineGIDelay:
            
               :xmlref:`OnlineGIDelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    General interrogation command will be delayed by a configured number of seconds when outstation becomes online. Delay is designed to allow outstation to acquire data before it is being requested by General Interrogation (default value 0)
 
   * :attr:    .. _ref-IEC104maCommsSettingsGIAfterRecovery:
            
               :xmlref:`GIAfterRecovery`
     :val:     0
     :desc:    **Don't send** General Interrogation command when outstation becomes online after a communication loss. (Outstation status changes to ONLINE). :inlinetip:`General Interrogation is always sent on leandc startup regardless the setting of this node.`

   * :(attr):
     :val:     1
     :desc:    **Send** General Interrogation command when outstation becomes online after a communication loss. (Outstation status changes to ONLINE) (default value)
 
   * :attr:    .. _ref-IEC104maCommsSettingsOfflineNTDelay:
               
               :xmlref:`OfflineNTDelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    DI/AI objects will get marked with Not Topical [NT] bit for a configured number of seconds when station goes offline. After the delay DI/AI objects will be marked with Invalid [IV] bit. Objects are not marked with Not Topical [NT] bit if this delay is 0. (default 0 seconds)
 
   * :attr:    .. _ref-IEC104maCommsSettingsDisabledNT:
            
               :xmlref:`DisabledNT`
     :val:     0
     :desc:    Mark DI/AI objects with **Invalid [IV]** bit when communication disable service command is received (default value)

   * :(attr):
     :val:     1
     :desc:    Mark DI/AI objects with **Not Topical [NT]** bit when communication disable service command is received
     