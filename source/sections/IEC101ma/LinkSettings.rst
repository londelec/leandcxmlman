.. _ref-IEC101maLinkSettings:

LinkSettings
^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`<ref-IEC101maLinkSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101maLinkSettings>`"

.. code-block:: none

   <LinkSettings LinkAddrSize="1" LinkOnlineCounter="5" IgnoreWhileLinkcnt="1" Flags="0x00"/>


.. _docref-IEC101maLinkSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Master LinkSettings attributes" ":spec: |C{0.2}|C{0.12}|C{0.1}|S{0.58}|"

.. include-file:: sections/Include/IEC60870_LinkAddrSize.rstinc "" ".. _ref-IEC101maLinkSettingsLinkAddrSize:"

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
		Application message processing starts after number of link messages defined in :ref:`<ref-IEC101maLinkSettingsLinkOnlineCounter>` are received from outstation.

   * :attr:     .. _ref-IEC101maLinkSettingsFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Various settings to enable customized data processing.
		See table :numref:`docref-IEC101maLinkFlagsBits` for description.


.. _docref-IEC101maLinkFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-101 Master Link flags" ":ref:`<ref-IEC101maLinkSettingsFlags>`" "Link flags"

.. include-file:: sections/Include/IEC60870_LinkFlags.rstinc

   * :attr:     Bits 1...7
     :val:      Any
     :desc:     Bits reserved for future use
