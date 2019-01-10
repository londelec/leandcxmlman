.. _ref-IEC61850clPresentationSettings:

PresentationSettings
^^^^^^^^^^^^^^^^^^^^

Settings of the Presentation layer (ISO8823) can be specified using attributes of :ref:`<ref-IEC61850clPresentationSettings>` 
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clPresentationSettings>`"

.. code-block:: none

   <PresentationSettings CallingPSEL="0001" Flags="0x00"/>


.. _docref-IEC61850clPresentationSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client PresentationSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

   * :attr:     .. _ref-IEC61850clCallingPSEL:

                :xmlref:`CallingPSEL`
     :val:      Up to 16 hexadecimal characters 0...F
     :def:      0001
     :desc:     Calling Presentation Selector used for outgoing [:lemonobgtext:`CP-PPDU`] message

   * :attr:     .. _ref-IEC61850clPresentationFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous settings of the Presentation layer.
		See table :numref:`docref-IEC61850clPresentationFlagsBits` for description.


.. _docref-IEC61850clPresentationFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Presentation layer flags" ":ref:`<ref-IEC61850clPresentationFlags>`" "Presentation layer flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     **Ignore** [:lemonobgtext:`Responding presentation selector`] of the received [:lemonobgtext:`CPA-PPDU`] message (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     **Check** [:lemonobgtext:`Responding presentation selector`] of the received [:lemonobgtext:`CPA-PPDU`] message.
		Communication will not be established if the received value doesn't match "OSI-PSEL" in the SCL file.

   * :attr:     Bits 1...7
     :val:      Any
     :desc:     Bits reserved for future use
