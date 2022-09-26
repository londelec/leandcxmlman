.. _xmlelem-IEC103maLink:

LinkSettings
^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`xmlelem-IEC103maLink` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC103maLink`"

.. code-block:: none

   <LinkSettings Flags="0x00"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC103maLink" "IEC60870-5-103 Master LinkSettings attributes" ":spec: |C{0.12}|C{0.12}|C{0.1}|S{0.66}|"

   * :attr:	:xmlattr:`Flags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Various settings to enable customized data processing.
		See :numref:`tabid-IEC103maLinkFlags` for description.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC103maLinkFlags" "IEC60870-5-103 Master Link flags" ":ref:`xmlattr-IEC103maLinkFlags`" "Link flags"

.. include-file:: sections/Include/IEC60870_LinkFlags.rstinc

   * :attr:	:bitdef:`2`
     :val:	xxxx.x0xx
     :desc:	Use **'Reset of remote link'** message to check if station is online.
		[:lemonobgtext:`Reset of remote link`] message has function code 0x40.

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Use **'Reset FCB'** message to check if station is online.
		[:lemonobgtext:`Reset FCB`] message has function code 0x47. This message is defined only in IEC60870-5-103.

   * :attr:	Bits 1;3...7
     :val:	Any
     :desc:	Bits reserved for future use
