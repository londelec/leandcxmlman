.. _xmlelem-IEC101maLink:

LinkSettings
^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`xmlelem-IEC101maLink` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC101maLink`"

.. code-block:: none

   <LinkSettings LinkAddrSize="1" LinkOnlineCounter="5" Flags="0x00"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC101maLink" "IEC60870-5-101 Master LinkSettings attributes" ":spec: |C{0.2}|C{0.12}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/IEC60870_LinkAddrSize.rstinc ""

   * :attr:	:xmlattr:`LinkOnlineCounter`
     :val:	0...65535
     :def:	0 requests
     :desc:	Application layer operation delay after link becomes valid. First application layer message (e.g. GI or Time Sync) will be delayed for a configured number of outgoing link messages after Reset Remote link response is received from outstation.
		Value 0 disables delay - application layer starts running immediately after Reset Remote link response is received from outstation.

   * :attr:	:xmlattr:`Flags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Various settings to enable customized data processing.
		See :numref:`tabid-IEC101maLinkFlags` for description.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC101maLinkFlags" "IEC60870-5-101 Master Link flags" ":ref:`xmlattr-IEC101maLinkFlags`" "Link flags"

.. include-file:: sections/Include/IEC60870_LinkFlags.rstinc

   * :attr:	:bitdef:`4`
     :val:	xxx0.xxxx
     :desc:	**Process** received application layer messages while link online delay counter operates.
		This setting applies only if :ref:`xmlattr-IEC101maLinkLinkOnlineCounter` is used.

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	**Ignore** received application layer messages while link online delay counter operates.
		Application message processing starts only after number of link messages defined in :ref:`xmlattr-IEC101maLinkLinkOnlineCounter` have been received from outstation.

   * :attr:     Bits 1...3;5...7
     :val:      Any
     :desc:     Bits reserved for future use
