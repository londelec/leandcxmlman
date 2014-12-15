
ASDUSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`ASDUSettings<ref-IEC104slASDUSettings>` element node.

Please see sample :ref:`ASDUSettings<ref-IEC104slASDUSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <ASDUSettings  InvalidEvent="1"
         SUthroughoutDST="1"
         DIEventType="31"
         AIEventType="36"
         TranspTypes="1" />

.. _ref-IEC104slASDUSettingsAttributes:

.. field-list-table:: IEC 60807-5-104 Slave ASDUSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description

   * :attr:     :xmlref:`InvalidEvent`
     :val:      0
     :desc:     Events with set Invalid [IV] bit **will not be** generated

   * :(attr):
     :val:      1
     :desc:     Events with set Invalid [IV] bit **will be** generated (default value)
   
   * :attr:     :xmlref:`SUthroughoutDST`
     :val:      0
     :desc:     Summer Time [SU] bit in any outgoing message timestamp will be set to indicate **last hour of the summer time** before clock adjustment at the end of DST (clock change one hour back) (default value)

   * :(attr):
     :val:      1
     :desc:     Summer Time [SU] bit in any outgoing message timestamp **will always be set** if  date and time of the timestamp is Summer time. :inlinetip:`Please note this functionality is deviation from communication standard and option should be avoided.`
   
   * :attr:     :xmlref:`DIEventType`
     :val:      See table :numref:`ref-IEC10xslDITypeIDValues`
     :desc:     Use this ASDU type to send DI events which don't have :ref:`DI<ref-IEC10xslDI>`.\ :ref:`TypeID<ref-IEC10xslDITypeID>` \ attribute specified in their element node. This setting also affects ASDU type of the static data (e.g. Single or Double status information) being reported to General interrogation request. (default value 30 – 'Single-point Information', DI event will be sent using ASDU type 30 [M_SP_TB_1], **CP56time2A**, full time)

   * :attr:     :xmlref:`AIEventType`
     :val:      See table :numref:`ref-IEC10xslAITypeIDValues`
     :desc:     Use this ASDU type to send AI events which don't have :ref:`AI<ref-IEC10xslAI>`.\ :ref:`TypeID<ref-IEC10xslAITypeID>` \ attribute specified in their element node. This setting also affects ASDU type of the static data (e.g. Normalized, Scaled, Short floating point) being reported to General interrogation request. (default value 36 – 'Short floating point', AI event will be sent using ASDU type 36 [M_ME_TF_1], **CP56time2A**, full time)

   * :attr:     :xmlref:`TranspTypes`
     :val:      0
     :desc:     ASDU type to be used for each DI/AI object reporting upstream will be determined by XML configuration settings. (default value)

   * :(attr):
     :val:      1
     :desc:     ASDU type to be used for each DI/AI object reporting upstream will be made transparent whenever possible. Normally ASDU type of each individual object received from downstream outstation will be used to report this object upstream, providing both particular communication protocol instances are compatible. Otherwise default ASDU type will be used. :inlinetip:`Please note object will be excluded from General Interrogation responses before it is received from downstream outstation, as its type is not yet known.`

   * :attr:     :xmlref:`CommandLatency`
     :val:      0...2\ :sup:`32`\  - 1
     :desc:     Maximal difference in seconds between timestamp of the received time-tagged control command and internal time. Incoming control command timestamp is being validated and command gets discarded if it has been substantially delayed in the communication channel while being received. Value 0 disables timestamp validation and any incoming control command will be accepted (default value 0)

     