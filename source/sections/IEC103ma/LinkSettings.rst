.. _ref-IEC103maLinkSettings:

LinkSettings
^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`<ref-IEC103maLinkSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC103maLinkSettings>`"

.. code-block:: none

   <LinkSettings Flags="0x00"/>


.. _docref-IEC103maLinkSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-103 Master LinkSettings attributes"

   * :attr:     .. _ref-IEC103maLinkSettingsFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Various settings to enable customized data processing.
		See table :numref:`ref-IEC103maLinkFlagsBits` for description.

.. _ref-IEC103maLinkFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "IEC60870-5-103 Master Link flags" ":ref:`<ref-IEC103maLinkSettingsFlags>`" "Link flags"

   * :attr:     Bit 4
     :val:      xxx0.xxxx
     :desc:     Use **'Request status of link'** message to check if station is online.
		('Request status of link' message has function code 0x49)

   * :(attr):
     :val:      xxx1.xxxx
     :desc:     Use **'Reset FCB'** message to check if station is online.
		('Reset FCB' message has function code 0x47. This message is defined only in IEC60870-5-103 standard)

   * :attr:     Bits 0...3;5...7
     :val:      Any
     :desc:     Bits reserved for future use
