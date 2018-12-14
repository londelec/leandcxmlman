.. _ref-IEC61850clTransportSettings:

TransportSettings
^^^^^^^^^^^^^^^^^

Settings of the Transport layer (ISO8073) can be specified using attributes of :ref:`<ref-IEC61850clTransportSettings>`
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clTransportSettings>`"

.. code-block:: none

   <TransportSettings CallingTSEL="0001" SourceREF="15" Flags="0x00"/>


.. _docref-IEC61850clTransportSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client TransportSettings attributes"

   * :attr:     .. _ref-IEC61850clCallingTSEL:

                :xmlref:`CallingTSEL`
     :val:      Up to 8 hexadecimal characters 0...F
     :def:      0001
     :desc:     Identifier of the calling Transport-Selector used for outgoing Connection Request [:lectext1:`CR-TPDU`] message.

   * :attr:     :xmlref:`SourceREF`
     :val:      1...65535
     :def:      10
     :desc:     Reference selected by the transport entity initiating the Connection Request [:lectext1:`CR-TPDU`] message to identify the requested transport connection.

   * :attr:     .. _ref-IEC61850clTransportFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous settings of the Transport layer.
		See table :numref:`ref-IEC61850clTransportFlagsBits` for description.


.. _ref-IEC61850clTransportFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Transport layer flags" ":ref:`<ref-IEC61850clTransportFlags>`" "Transport layer flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     **Ignore** destination reference [:lectext1:`DST-REF`] of the received [:lectext1:`CC-TPDU`] message (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     **Check** destination reference [:lectext1:`DST-REF`] of the received [:lectext1:`CC-TPDU`] message.
		Communication will not be established if reference is incorrect.

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     **Ignore** [:lectext1:`Calling Transport Selector`] and [:lectext1:`Called Transport Selector`] identifiers of the received [:lectext1:`CC-TPDU`] message (default value)

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     **Check** [:lectext1:`Calling Transport Selector`] and [:lectext1:`Called Transport Selector`] identifiers of the received [:lectext1:`CC-TPDU`] message.
		Communication will not be established if the received [:lectext1:`Calling Transport Selector`] doesn't match "OSI-TSEL" in the SCL file or
		[:lectext1:`Called Transport Selector`] is different from [:lectext1:`CR-TPDU`] message value.

   * :attr:     Bits 2...7
     :val:      Any
     :desc:     Bits reserved for future use
