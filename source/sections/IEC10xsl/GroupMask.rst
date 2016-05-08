
DI/AI.GroupMask
---------------

.. _ref-IEC10xslGroupMask:

.. field-list-table:: IEC60870-5-101/104 Slave DI/AI GroupMask
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.24}|C{0.24}|S{0.52}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Values
     :desc,80: Description

   * :attr:     :xmlref:`GroupMask` [xxxx.xxxx.xxxx.xxxx]
     :val:      0x0000...0xFFFF
     :desc:     Group Mask is 16 bit encoded variable. Decimal 0...65535 and hex 0x0000...0xFFFF values supported

   * :attr:     Bit 0
     :val:      xxxx.xxxx.xxxx.xxx0
     :desc:     DI/AI object is **excluded** from Group **1** Interrogation

   * :(attr):
     :val:      xxxx.xxxx.xxxx.xxx1
     :desc:     DI/AI object is **included** in Group **1** Interrogation

   * :attr:     Bit 1
     :val:      xxxx.xxxx.xxxx.xx0x
     :desc:     DI/AI object is **excluded** from Group **2** Interrogation

   * :(attr):
     :val:      xxxx.xxxx.xxxx.xx1x
     :desc:     DI/AI object is **included** in Group **2** Interrogation

   * :attr:     Bit 2
     :val:      xxxx.xxxx.xxxx.x0xx
     :desc:     DI/AI object is **excluded** from Group **3** Interrogation

   * :(attr):
     :val:      xxxx.xxxx.xxxx.x1xx
     :desc:     DI/AI object is **included** in Group **3** Interrogation

   * :attr:     Bit 3
     :val:      xxxx.xxxx.xxxx.0xxx
     :desc:     DI/AI object is **excluded** from Group **4** Interrogation

   * :(attr):
     :val:      xxxx.xxxx.xxxx.1xxx
     :desc:     DI/AI object is **included** in Group **4** Interrogation

   * :attr:     Bit 4
     :val:      xxxx.xxxx.xxx0.xxxx
     :desc:     DI/AI object is **excluded** from Group **5** Interrogation

   * :(attr):
     :val:      xxxx.xxxx.xxx1.xxxx
     :desc:     DI/AI object is **included** in Group **5** Interrogation

   * :attr:     Bit 5
     :val:      xxxx.xxxx.xx0x.xxxx
     :desc:     DI/AI object is **excluded** from Group **6** Interrogation

   * :(attr):
     :val:      xxxx.xxxx.xx1x.xxxx
     :desc:     DI/AI object is **included** in Group **6** Interrogation

   * :attr:     Bit 6
     :val:      xxxx.xxxx.x0xx.xxxx
     :desc:     DI/AI object is **excluded** from Group **7** Interrogation

   * :(attr):
     :val:      xxxx.xxxx.x1xx.xxxx
     :desc:     DI/AI object is **included** in Group **7** Interrogation

   * :attr:     Bit 7
     :val:      xxxx.xxxx.0xxx.xxxx
     :desc:     DI/AI object is **excluded** from Group **8** Interrogation

   * :(attr):
     :val:      xxxx.xxxx.1xxx.xxxx
     :desc:     DI/AI object is **included** in Group **8** Interrogation

   * :attr:     Bit 8
     :val:      xxxx.xxx0.xxxx.xxxx
     :desc:     DI/AI object is **excluded** from Group **9** Interrogation

   * :(attr):
     :val:      xxxx.xxx1.xxxx.xxxx
     :desc:     DI/AI object is **included** in Group **9** Interrogation

   * :attr:     Bit 9
     :val:      xxxx.xx0x.xxxx.xxxx
     :desc:     DI/AI object is **excluded** from Group **10** Interrogation

   * :(attr):
     :val:      xxxx.xx1x.xxxx.xxxx
     :desc:     DI/AI object is **included** in Group **10** Interrogation

   * :attr:     Bit 10
     :val:      xxxx.x0xx.xxxx.xxxx
     :desc:     DI/AI object is **excluded** from Group **11** Interrogation

   * :(attr):
     :val:      xxxx.x1xx.xxxx.xxxx
     :desc:     DI/AI object is **included** in Group **11** Interrogation

   * :attr:     Bit 11
     :val:      xxxx.0xxx.xxxx.xxxx
     :desc:     DI/AI object is **excluded** from Group **12** Interrogation

   * :(attr):
     :val:      xxxx.1xxx.xxxx.xxxx
     :desc:     DI/AI object is **included** in Group **12** Interrogation

   * :attr:     Bit 12
     :val:      xxx0.xxxx.xxxx.xxxx
     :desc:     DI/AI object is **excluded** from Group **13** Interrogation

   * :(attr):
     :val:      xxx1.xxxx.xxxx.xxxx
     :desc:     DI/AI object is **included** in Group **13** Interrogation

   * :attr:     Bit 13
     :val:      xx0x.xxxx.xxxx.xxxx
     :desc:     DI/AI object is **excluded** from Group **14** Interrogation

   * :(attr):
     :val:      xx1x.xxxx.xxxx.xxxx
     :desc:     DI/AI object is **included** in Group **14** Interrogation

   * :attr:     Bit 14
     :val:      x0xx.xxxx.xxxx.xxxx
     :desc:     DI/AI object is **excluded** from Group **15** Interrogation

   * :(attr):
     :val:      x1xx.xxxx.xxxx.xxxx
     :desc:     DI/AI object is **included** in Group **15** Interrogation

   * :attr:     Bit 15
     :val:      0xxx.xxxx.xxxx.xxxx
     :desc:     DI/AI object is **excluded** from Group **16** Interrogation

   * :(attr):
     :val:      1xxx.xxxx.xxxx.xxxx
     :desc:     DI/AI object is **included** in Group **16** Interrogation

.. tip::

   Value 0x0001 will include DI/AI object in Group1 Interrogation; value 0x0003 will include DI/AI object in Group1 
   and Group2 Interrogation, etc.
