
CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state change behavior and related delays can be specified using attributes of :ref:`CommsSettings<ref-IEC104slCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-IEC104slCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings OfflineDelay="10" StartupGIDelay="10" /> 

.. _ref-IEC104slCommsSettingsAttributes:

.. field-list-table:: IEC 60807-5-104 Slave CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     :xmlref:`OfflineDelay`
     :val:      1...2\ :sup:`32`\  - 1
     :desc:     Offline delay in seconds before outstation status is changed to OFFLINE. Offline delay timer is activated after TCP socket has been closed. Default 0 seconds -  outstation status will be changed to OFFLINE  immediately after TCP socket has been closed by either peer (default 0 seconds)

   * :attr:     :xmlref:`StartupGIDelay`
     :val:      0...2\ :sup:`32`\  - 1
     :desc:     General interrogation commands are rejected for a configured number of seconds on system startup. Negative response will be generated if General interrogation command is received within this delay. Delay is designed to allow leandc firmware  acquire data from outstations before reporting upstream (default value 0)
     