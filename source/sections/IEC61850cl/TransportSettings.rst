.. _ref-IEC61850clTransportSettings:

TransportSettings
^^^^^^^^^^^^^^^^^

Settings of the Transport layer (ISO8073) can be specified using attributes of :ref:`<ref-IEC61850clTransportSettings>`
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clTransportSettings>`"

.. code-block:: none

   <TransportSettings CallingTSEL="1" SourceREF="15" Flags="0x00"/>


.. _docref-IEC61850clTransportSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client TransportSettings attributes"

   * :attr:     :xmlref:`CallingTSEL`
     :val:      1...65535
     :def:      1
     :desc:     Identifier of the calling Transport-Selector used for outgoing Connection Request [CR-TPDU] message.

   * :attr:     :xmlref:`SourceREF`
     :val:      1...65535
     :def:      10
     :desc:     Reference selected by the transport entity initiating the Connection Request [CR-TPDU] message to identify the requested transport connection.

   * :attr:     .. _ref-IEC61850clTransportFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous settings of the Transport layer. See table :numref:`docref-IEC61850clTransportFlagsBits` for description.


.. _docref-IEC61850clTransportFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Transport layer flags" ":ref:`<ref-IEC61850clTransportFlags>`" "Transport layer flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     Calling and called Transport-Selector identifiers of the received Connection Confirm [CC-TPDU] message will be **ignored** (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     Calling and called Transport-Selector identifiers of the received Connection Confirm [CC-TPDU] message will be **checked**.
		Connection will be aborted if identifiers are incorrect.

   * :attr:     Bits 1...7
     :val:      Any
     :desc:     Bits reserved for future use
