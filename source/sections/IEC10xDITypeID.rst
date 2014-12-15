.. field-list-table:: IEC 60807-5-101/104 Slave DI TypeID
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.25}|C{0.25}|S{0.5}|
   :header-rows: 1

   * :attr,10: TypeID Value for IEC60870-5-101
     :val,10:  TypeID Value for IEC60870-5-104
     :desc,80: Description

   * :attr:    1
     :val:     1
     :desc:    Static DI 'Single-point Information' will be sent using ASDU type 1 [M_SP_NA_1] DI event will be sent using ASDU type 1 [M_SP_NA_1], **no time-tag**

   * :attr:    2
     :val:     N/A
     :desc:    Static DI 'Single-point Information' will be sent using ASDU type 1 [M_SP_NA_1] DI event will be sent using ASDU type 2 [M_SP_TA_1], **CP24time2A**, msec and min

   * :attr:    3
     :val:     3
     :desc:    Static DI 'Double-point Information' will be sent using ASDU type 3 [M_DP_NA_1] DI event will be sent using ASDU type 3 [M_DP_NA_1], **no time-tag**

   * :attr:    4
     :val:     N/A
     :desc:    Static DI 'Double-point Information' will be sent using ASDU type 3 [M_DP_NA_1] DI event will be sent using ASDU type 4 [M_DP_TA_1], **CP24time2A**, msec and min

   * :attr:    30
     :val:     30
     :desc:    Static DI 'Single-point Information' will be sent using ASDU type 1 [M_SP_NA_1] DI event will be sent using ASDU type 30 [M_SP_TB_1], **CP56time2A**, full time

   * :attr:    31
     :val:     31
     :desc:    Static DI 'Double-point Information' will be sent using ASDU type 3 [M_DP_NA_1] DI event will be sent using ASDU type 31 [M_DP_TB_1], **CP56time2A**, full time

   * :attr:    Other
     :val:     Other
     :desc:    Undefined, default values will be used:
               IEC 60870-5-101 default ASDU type 2 [M_SP_TA_1], **CP24time2A**, msec and min
               IEC 60870-5-104 default ASDU type 30 [M_SP_TB_1], **CP56time2A**, full time

.. tip::

   Note, all DI objects are internally stored and processed as 'Double-point status information'. If 'Single-point 
   status information' type needs to be reported to the upstream Master station, object is being converted just 
   before it is sent.
