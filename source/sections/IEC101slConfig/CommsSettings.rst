
CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state change behavior and related delays can be specified using attributes of :ref:`CommsSettings<ref-IEC101slCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-IEC101slCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings OfflineDelay="120" StartupGIDelay="10" />

.. _ref-IEC101slCommsSettingsAttributes:

.. field-list-table:: IEC 60807-5-101 Slave CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     :xmlref:`OfflineDelay`
     :val:      1...2\ :sup:`32`\  - 1
     :desc:     Delay in seconds before resetting the link in case there is no request from Master station. Reset remote link message is required after communication loss longer than a configured offline delay in order to restore communication (default 60 seconds)

   * :attr:     :xmlref:`StartupGIDelay`
     :val:      0...2\ :sup:`32`\  - 1
     :desc:     General interrogation commands are rejected for a configured number of seconds on system startup. Negative response will be generated if General interrogation command is received within this delay. Delay is designed to allow leandc firmware  acquire data from outstations before reporting upstream (default value 0)
     