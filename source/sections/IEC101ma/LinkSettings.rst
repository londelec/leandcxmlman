.. _ref-IEC101maLinkSettings:

LinkSettings
^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`<ref-IEC101maLinkSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101maLinkSettings>`"

.. code-block:: none

   <LinkSettings LinkAddrSize="1" TxAllVarLength="0" LinkOnlineCounter="5" IgnoreWhileLinkcnt="1"/>


.. _docref-IEC101maLinkSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Master LinkSettings attributes"

.. include-file:: sections/Include/IEC60870_LinkAddrSize.rstinc "" ".. _ref-IEC101maLinkSettingsLinkAddrSize:"

   * :attr:     .. _ref-IEC101maLinkSettingsTxAllVarLength:

                :xmlref:`TxAllVarLength`
     :val:      0
     :def:      0
     :desc:     Send **variable** and **fixed** length link layer messages as required. (First character of variable link layer messages is - 0x68 and fixed length messages - 0x10)

   * :(attr):
     :val:      1
     :(def):
     :desc:     Send only **variable** length link layer messages

   * :attr:     .. _ref-IEC101maLinkSettingsLinkOnlineCounter:

                :xmlref:`LinkOnlineCounter`
     :val:      0...65535
     :def:      0 requests
     :desc:     Application layer operation delay after link becomes valid. First application layer message (e.g. GI or Time Sync) will be delayed for a configured number of outgoing link messages after Reset Remote link response is received from outstation. Value 0 disables delay - application layer starts running immediately after Reset Remote link response is received from outstation.

   * :attr:     .. _ref-IEC101maLinkSettingsIgnoreWhileLinkcnt:

                :xmlref:`IgnoreWhileLinkcnt`
     :val:      0
     :def:      0
     :desc:     **Process** received application layer messages while link online delay counter operates

   * :(attr):
     :val:      1
     :(def):
     :desc:     **Ignore** received application layer messages while link online delay counter operates.
		Application message processing starts after number of link messages defined in :ref:`<ref-IEC101maLinkSettingsLinkOnlineCounter>` are received from oustation.
