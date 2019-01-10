.. _ref-IEC61850clTransportSettings:

TransportSettings
^^^^^^^^^^^^^^^^^

Settings of the Transport layer (ISO8073) can be specified using attributes of :ref:`<ref-IEC61850clTransportSettings>`
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clTransportSettings>`"

.. code-block:: none

   <TransportSettings CallingTSEL="0001" SourceREF="15" Flags="0x00"/>


.. _docref-IEC61850clTransportSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client TransportSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

   * :attr:     .. _ref-IEC61850clCallingTSEL:

                :xmlref:`CallingTSEL`
     :val:      Up to 8 hexadecimal characters 0...F
     :def:      0001
     :desc:     Identifier of the calling Transport-Selector used for outgoing Connection Request [:lemonobgtext:`CR-TPDU`] message.

   * :attr:     :xmlref:`SourceREF`
     :val:      1...65535
     :def:      10
     :desc:     Reference selected by the transport entity initiating the Connection Request [:lemonobgtext:`CR-TPDU`] message to identify the requested transport connection.

   * :attr:     .. _ref-IEC61850clTransportFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous settings of the Transport layer.
		See table :numref:`docref-IEC61850clTransportFlagsBits` for description.


.. _docref-IEC61850clTransportFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Transport layer flags" ":ref:`<ref-IEC61850clTransportFlags>`" "Transport layer flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     **Ignore** destination reference [:lemonobgtext:`DST-REF`] of the received [:lemonobgtext:`CC-TPDU`] message (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     **Check** destination reference [:lemonobgtext:`DST-REF`] of the received [:lemonobgtext:`CC-TPDU`] message.
		Communication will not be established if reference is incorrect.

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     **Ignore** [:lemonobgtext:`Calling Transport Selector`] and [:lemonobgtext:`Called Transport Selector`] identifiers of the received [:lemonobgtext:`CC-TPDU`] message (default value)

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     **Check** [:lemonobgtext:`Calling Transport Selector`] and [:lemonobgtext:`Called Transport Selector`] identifiers of the received [:lemonobgtext:`CC-TPDU`] message.
		Communication will not be established if the received [:lemonobgtext:`Calling Transport Selector`] doesn't match "OSI-TSEL" in the SCL file or
		[:lemonobgtext:`Called Transport Selector`] is different from [:lemonobgtext:`CR-TPDU`] message value.

   * :attr:     Bits 2...7
     :val:      Any
     :desc:     Bits reserved for future use
