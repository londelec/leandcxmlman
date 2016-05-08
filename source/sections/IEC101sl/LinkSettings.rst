.. _ref-IEC101slLinkSettings:

LinkSettings
^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`<ref-IEC101slLinkSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101slLinkSettings>`"

.. code-block:: none

   <LinkSettings LinkAddrSize="1" ACDLinkStatusResp="0" ACDAlways="0" FCBMaskLinkReq="0" TxAllVarLength="0" SingleCharACK="1" ClassIgnore="0" />


.. _docref-IEC101slLinkSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Slave LinkSettings attributess"

.. include-file:: sections/Include/IEC60870_LinkAddrSize.rstinc "" ".. _ref-IEC101slLinkSettingsLinkAddrSize:"

   * :attr:     :xmlref:`ACDLinkStatusResp`
     :val:      0
     :def:      0
     :desc:     [ACD] bit (link control field) value of the 'status of link' response message (**no access demand**)

   * :(attr):
     :val:      1
     :(def):
     :desc:     [ACD] bit (link control field) value of the 'status of link' response message (**access demand**)

   * :attr:     :xmlref:`ACDAlways`
     :val:      0
     :def:      0
     :desc:     [ACD] bit (link control field) in response messages gets set **only if Class 1 data is available**

   * :(attr):
     :val:      1
     :(def):
     :desc:     [ACD] bit (link control field) in response messages is **always** set

   * :attr:     :xmlref:`FCBMaskLinkReq`
     :val:      0
     :def:      0
     :desc:     [FCB] bit (link control field) **must be zero** in 'status of link' request received from Master station. Leandc will not reply to the 'status of link' request if [FCB] bit is set. 

   * :(attr):
     :val:      1
     :(def):
     :desc:     [FCB] bit (link control field) **is ignored** in 'status of link' request received from Master station

   * :attr:     :xmlref:`TxAllVarLength`
     :val:      0
     :def:      0
     :desc:     Send **variable** and **fixed** length link layer messages as required. (Variable link layer messages start with 0x68 and fixed length messages start with 0x10)

   * :(attr):
     :val:      1
     :(def):
     :desc:     Send only **variable** length link layer messages

   * :attr:     :xmlref:`SingleCharACK`
     :val:      0
     :def:      0
     :desc:     **Don't use** single character (0xE5 and 0xA2) ACK and NACK responses

   * :(attr):
     :val:      1
     :(def):
     :desc:     **Use** single character (0xE5 and 0xA2) ACK and NACK responses

   * :attr:     :xmlref:`ClassIgnore`
     :val:      0
     :def:      0
     :desc:     Class of the received message is **being used** to determine either Class 1 or Class 2 data should be sent.

   * :(attr):
     :val:      1
     :(def):
     :desc:     Class of the received message is **ignored**, Class 1 and Class 2 data is sent regadless of the requested Class. :inlinetip:`Please note this functionality is deviation from communication standard and option should be avoided.`
