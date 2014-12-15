
LinkSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`LinkSettings<ref-IEC101maLinkSettings>` element node.

Please see sample :ref:`LinkSettings<ref-IEC101maLinkSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <LinkSettings LinkAddrSize="1" TxAllVarLength="0" LinkOnlineCounter="5"/> 

.. _ref-IEC101maLinkSettingsAttributes:

.. field-list-table:: IEC 60807-5-101 Master LinkSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.22}|C{0.23}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     .. _ref-IEC101maLinkSettingsLinkAddrSize:
            
                :xmlref:`LinkAddrSize`
     :val:      1 or 2
     :desc:     Link layer address size in bytes (default 1 byte) :inlinetip:`Please note link address size of the protocol instances sharing the same hardware node must be the same.`
   
   * :attr:     .. _ref-IEC101maLinkSettingsTxAllVarLength:
            
                :xmlref:`TxAllVarLength`
     :val:      0
     :desc:     Send **variable** and **fixed** length link layer messages as required (default value) (Variable link layer messages start with 0x68 and fixed length messages start with 0x10)
   
   * :(attr):
     :val:      1
     :desc:     Send only **variable** length link layer messages
   
   * :attr:     .. _ref-IEC101maLinkSettingsLinkOnlineCounter:
            
                :xmlref:`LinkOnlineCounter`
     :val:      0...255
     :desc:     Application layer operation delay after link becomes valid. First application layer message (e.g. GI or Time Sync) will be delayed for a configured number of outgoing messages after Reset Remote link response from outstation. Value 0 doesn't delay application layer operation, application layer starts running immediately after Reset Remote link response is received from outstation. (default 0 messages)
