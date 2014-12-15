
CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state reporting and related delays can be specified using attributes of :ref:`CommsSettings<ref-IEC103maCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-IEC103maCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings    NoRespCount="5"
         DegradedRetries="5"
         DegradedTimeout="600"
         ControlLockTimer="20"
         OfflineDelay="10"
         OnlineGIDelay="10" 
         OfflineNTDelay="1000" 
         DisabledNT="1" />

.. _ref-IEC103maCommsSettingsAttributes:

.. field-list-table:: IEC 60807-5-103 Master CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    .. _ref-IEC103maCommsSettingsNoRespCount:
            
               :xmlref:`NoRespCount`
     :val:     1...255
     :desc:    Outstation no-response counter. Station status will be changed to OFFLINE and Invalid [IV] bit of all DI/AI information objects will be set if outstation fails to reply to a configured number of subsequent requests. Outstation status will be changed to OFFLINE immediately unless additional :ref:`OfflineDelay<ref-IEC103maCommsSettingsOfflineDelay>` is specified. (default 5 retries; leandc will retry outgoing message for 5 times before changing outstation status to OFFLINE) (default 5 retries)

   * :attr:    .. _ref-IEC103maCommsSettingsDegradedRetries:
            
               :xmlref:`DegradedRetries`
     :val:     0...255
     :desc:    Outgoing message retries before activating :ref:`DegradedTimeout<ref-IEC103maCommsSettingsDegradedTimeout>`. Outstation will be temporarily excluded from polling if it fails to reply to a configured number of requests. Value 0 disables degraded timeout functionality (default 5 retries)

   * :attr:    .. _ref-IEC103maCommsSettingsDegradedTimeout:
            
               :xmlref:`DegradedTimeout`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Degraded timeout in seconds. Outstation is excluded from polling for a configured number of seconds if it has failed to reply to a number of requests configured in :ref:`DegradedRetries<ref-IEC103maCommsSettingsDegradedRetries>` node. Value 0 disables degraded timeout functionality (default 600 seconds)

   * :attr:    .. _ref-IEC103maCommsSettingsControlLockTimer:
            
               :xmlref:`ControlLockTimer`
     :val:     0...120
     :desc:    Control command lock timer is used to poll only one outstation for a configured number of seconds after sending a control command. All other outstations sharing the same hardware channel are temporary excluded from polling while :xmlref:`ControlLockTimer` operates. This feature allows to speed up reception of a control command feedback. :xmlref:`ControlLockTimer` can be used only if more than one outstation uses the same hardware channel. Value 0 disables control lock timer feature. (default 30 seconds)
 
   * :attr:    .. _ref-IEC103maCommsSettingsOfflineDelay:
            
               :xmlref:`OfflineDelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Offline delay in seconds before outstation status is changed to OFFLINE. Offline delay timer is activated only after outstation has failed to reply to a number of requests configured in :ref:`NoRespCount<ref-IEC103maCommsSettingsNoRespCount>` node. (example, if this delay is 10, status will be changed to OFFLINE when outstation has failed to reply to a number of requests configured in :ref:`NoRespCount<ref-IEC103maCommsSettingsNoRespCount>` plus 10 second delay (default 0 seconds)
 
   * :attr:    .. _ref-IEC103maCommsSettingsOnlineGIDelay:
            
               :xmlref:`OnlineGIDelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    General interrogation command will be delayed by a configured number of seconds when outstation becomes online. Delay is designed to allow outstation to acquire data after reset/power-on and before leandc issues General Interrogation (default value 0)
 
   * :attr:    .. _ref-IEC103maCommsSettingsOfflineNTDelay:
            
               :xmlref:`OfflineNTDelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    DI/AI objects will be marked with Not Topical [NT] bit for a configured number of seconds when station goes offline. DI/AI objects will be marked with Invalid [IV] bit after this delay expires. Objects are never marked with Not Topical [NT] bit if this delay is 0. (default 0 seconds)
 
   * :attr:    .. _ref-IEC103maCommsSettingsDisabledNT:
            
               :xmlref:`DisabledNT`
     :val:     0
     :desc:    Mark DI/AI objects with **Invalid [IV]** bit when communication disable service command is received (default value)

   * :(attr):
     :val:     1
     :desc:    Mark DI/AI objects with **Not Topical [NT]** bit when communication disable service command is received
     
