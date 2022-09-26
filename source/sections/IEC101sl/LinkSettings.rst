.. _xmlelem-IEC101slLink:

LinkSettings
^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`xmlelem-IEC101slLink` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC101slLink`"

.. code-block:: none

   <LinkSettings LinkAddrSize="1" ClassIgnore="0" Flags="0x00"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC101slLink" "IEC60870-5-101 Slave LinkSettings attributes" ":spec: |C{0.21}|C{0.12}|C{0.1}|S{0.57}|"

.. include-file:: sections/Include/IEC60870_LinkAddrSize.rstinc ""

   * :attr:	:xmlattr:`ClassIgnore`
     :val:	0
     :def:	0
     :desc:	Class of the received message is **being used** to determine either Class 1 or Class 2 data should be sent.

   * :(attr):
     :val:	1
     :(def):
     :desc:	Class of the received message is **ignored**, Class 1 and Class 2 data is sent regardless of the requested Class.
		:inlinetip:`Please note this functionality is deviation from communication standard and should be avoided.`

   * :attr:	:xmlattr:`Flags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Various settings to enable customized data processing.
		See :numref:`tabid-IEC101slLinkFlags` for description.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC101slLinkFlags" "IEC60870-5-101 Slave Link flags" ":ref:`xmlattr-IEC101slLinkFlags`" "Link flags"

.. include-file:: sections/Include/IEC60870_LinkFlags.rstinc

   * :attr:	:bitdef:`1`
     :val:	xxxx.xx0x
     :desc:	**Don't use** single character ACK and NACK responses (0xE5 and 0xA2).

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	**Use** single character ACK and NACK responses (0xE5 and 0xA2).

   * :attr:	:bitdef:`2`
     :val:	xxxx.x0xx
     :desc:	[:lemonobgtext:`FCB`] bit (link control field) **must be zero** in 'Status of Link' request received from Master station.
		We will not reply to the 'Status of Link' request if [:lemonobgtext:`FCB`] bit is set. 

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	[:lemonobgtext:`FCB`] bit (link control field) **is ignored** in 'Status of Link' request received from Master station.

   * :attr:	:bitdef:`3`
     :val:	xxxx.0xxx
     :desc:	[:lemonobgtext:`ACD`] bit (link control field) in response messages is set **only if Class 1 data is available**.

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	[:lemonobgtext:`ACD`] bit (link control field) in response messages is **always** set.

   * :attr:	:bitdef:`4`
     :val:	xxx0.xxxx
     :desc:	[:lemonobgtext:`ACD`] bit (link control field) value of the 'Status of Link' response is **0** [:lemonobgtext:`no access demand`]

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	[:lemonobgtext:`ACD`] bit (link control field) value of the 'Status of Link' response is **1** [:lemonobgtext:`access demand`]

   * :attr:	Bits 5...7
     :val:	Any
     :desc:	Bits reserved for future use
