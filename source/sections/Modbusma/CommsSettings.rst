
.. _ref-ModbusmaCommsSettingsAttributes:

CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state reporting and related delays can be specified using attributes of :ref:`CommsSettings<ref-ModbusmaCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-ModbusmaCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings NoRespCount="5"
		  DegradedRetries="5"
		  DegradedTimeout="600"
		  OfflineDelay="10" />

.. _ref-ModbusmaCommsSettingsAttributesTab:

.. field-list-table:: Modbus Master CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    .. _ref-ModbusmaCommsSettingsNoRespCount:
            
               :xmlref:`NoRespCount`
     :val:     1...255
     :desc:    Outstation no-response counter. Station status will be changed to OFFLINE and Invalid [IV] bit of all DI/AI information objects will be set if outstation fails to reply to a configured number of subsequent requests. Outstation status will be changed to OFFLINE immediately unless additional :ref:`OfflineDelay<ref-ModbusmaCommsSettingsOfflineDelay>` is specified. (default 5 retries; leandc will retry outgoing message for 5 times before changing outstation status to OFFLINE) (default 5 retries)

   * :attr:    .. _ref-ModbusmaCommsSettingsDegradedRetries:
            
               :xmlref:`DegradedRetries`
     :val:     0...255
     :desc:    Outgoing message retries before activating :ref:`DegradedTimeout<ref-ModbusmaCommsSettingsDegradedTimeout>`. Outstation will be temporarily excluded from polling if it fails to reply to a configured number of requests. Value 0 disables degraded timeout functionality (default 5 retries)

   * :attr:    .. _ref-ModbusmaCommsSettingsDegradedTimeout:
            
               :xmlref:`DegradedTimeout`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Degraded timeout in seconds. Outstation is excluded from polling for a configured number of seconds if it has failed to reply to a number of requests configured in :ref:`DegradedRetries<ref-ModbusmaCommsSettingsDegradedRetries>` attribute. Value 0 disables degraded timeout functionality (default 600 seconds)

   * :attr:    .. _ref-ModbusmaCommsSettingsOfflineDelay:
            
               :xmlref:`OfflineDelay`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Delay in seconds before outstation status is changed to OFFLINE. Offline delay timer is activated only after outstation has failed to reply to a number of requests configured in :ref:`NoRespCount<ref-ModbusmaCommsSettingsNoRespCount>` attribute. (example, if this delay is 10, status will be changed to OFFLINE when outstation has failed to reply to a number of requests configured in :ref:`NoRespCount<ref-ModbusmaCommsSettingsNoRespCount>` plus 10 second delay (default 0 seconds)
 
 

