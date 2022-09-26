.. _xmlelem-IEC61850clPresentation:

PresentationSettings
^^^^^^^^^^^^^^^^^^^^

Settings of the Presentation layer (ISO8823) can be specified using attributes of :ref:`xmlelem-IEC61850clPresentation` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clPresentation`"

.. code-block:: none

   <PresentationSettings CallingPSEL="0001" Flags="0x00" LogFlags="0x00"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clPresentation" "IEC61850 Client PresentationSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

   * :attr:	:xmlattr:`CallingPSEL`
     :val:	Up to 16 hexadecimal characters 0...F
     :def:	0001
     :desc:	[:lemonobgtext:`Calling-presentation-selector`] field value for outgoing [:lemonobgtext:`CP-PPDU`].

.. include-file:: sections/Include/IEC61850cl_Flags.rstinc "" ":numref:`tabid-IEC61850clPresentationFlags`" "Presentation"

.. include-file:: sections/Include/IEC61850_LogFlags.rstinc "" ":numref:`tabid-IEC61850clLogFlags`" "Presentation"


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clPresentationFlags" "Presentation layer flags" ":ref:`xmlattr-IEC61850clPresentationFlags`" "Presentation layer flags"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	**Ignore** [:lemonobgtext:`Responding-presentation-selector`] of the received [:lemonobgtext:`CPA-PPDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	**Check** [:lemonobgtext:`Responding-presentation-selector`] of the received [:lemonobgtext:`CPA-PPDU`].
		Communication will not be established if the received value doesn't match "OSI-PSEL" defined in the SCL file.

   * :attr:	Bits 1...7
     :val:	Any
     :desc:	Bits reserved for future use

