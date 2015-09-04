.. _docref-IEC101slLinkSettingsAttr:

LinkSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`LinkSettings<ref-IEC101slLinkSettings>` element node.

Please see sample :ref:`LinkSettings<ref-IEC101slLinkSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <LinkSettings	LinkAddrSize="1"
                        ACDLinkStatusResp="0"
                        ACDAlways="0"
                        FCBMaskLinkReq="0"
                        TxAllVarLength="0" 
                        SingleCharACK="1" 
                        ClassIgnore="0" />

.. _docref-IEC101slLinkSettingsAttab:

.. field-list-table:: IEC 60870-5-101 Slave LinkSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.22}|C{0.23}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     .. _ref-IEC101slLinkSettingsLinkAddrSize:
            
                :xmlref:`LinkAddrSize`
     :val:      1 or 2
     :desc:     Link layer address size in bytes (default 1 byte) :inlinetip:`Please note link address size of all protocol instances sharing the same hardware node must be the same.`

   * :attr:     :xmlref:`ACDLinkStatusResp`
     :val:      0
     :desc:     ACD bit (of the link control field) value for 'status of link' response message (**no access demand**) (default value)

   * :(attr):
     :val:      1
     :desc:     ACD bit (of the link control field) value for 'status of link' response message (**access demand**)

   * :attr:     :xmlref:`ACDAlways`
     :val:      0
     :desc:     ACD bit (of the link control field) in response messages is set **only if Class 1 data is available** (default value)

   * :(attr):
     :val:      1
     :desc:     ACD bit (of the link control field) in response messages is **always** set

   * :attr:     :xmlref:`FCBMaskLinkReq`
     :val:      0
     :desc:     FCB bit (of the link control field) **must be zero** in 'status of link' request received from Master station (default value)

   * :(attr):
     :val:      1
     :desc:     FCB bit (of the link control field) **is ignored** in 'status of link' request received from Master station

   * :attr:     :xmlref:`TxAllVarLength`
     :val:      0
     :desc:     Send **variable** and **fixed** length link layer messages as required (default value) (Variable link layer messages start with 0x68 and fixed length messages start with 0x10)

   * :(attr):
     :val:      1
     :desc:     Send only **variable** length link layer messages

   * :attr:     :xmlref:`SingleCharACK`
     :val:      0
     :desc:     **Don't use** single character (0xE5 and 0xA2) ACK and NACK responses (default value)

   * :(attr):
     :val:      1
     :desc:     **Use** single character (0xE5 and 0xA2) ACK and NACK responses

   * :attr:     :xmlref:`ClassIgnore`
     :val:      0
     :desc:     Class of the received message is **being used** to determine either Class 1 or Class 2 data should be sent (default value)

   * :(attr):
     :val:      1
     :desc:     Class of the received message is **ignored**, Class 1 and Class 2 data is sent regadless of the requested Class. :inlinetip:`Please note this functionality is deviation from communication standard and option should be avoided.`
