.. _xmlelem-IEC61850clTransport:

TransportSettings
^^^^^^^^^^^^^^^^^

Settings of the Transport layer (ISO8073) can be specified using attributes of :ref:`xmlelem-IEC61850clTransport` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clTransport`"

.. code-block:: none

   <TransportSettings CallingTSEL="0001" SourceREF="15" PDUsize="2048" TS1timeout="0" Flags="0x00" LogFlags="0x00"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clTransport" "IEC61850 Client TransportSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

   * :attr:	:xmlattr:`CallingTSEL`
     :val:	Up to 8 hexadecimal characters 0...F
     :def:	0001
     :desc:	[:lemonobgtext:`Calling Transport-Selector`] field value for outgoing Connection Request [:lemonobgtext:`CR-TPDU`].

   * :attr:	:xmlattr:`SourceREF`
     :val:	1...65535
     :def:	10
     :desc:	[:lemonobgtext:`SRC-REF`] Reference selected by the transport entity initiating the Connection Request [:lemonobgtext:`CR-TPDU`] to identify the requested transport connection.

   * :attr:	:xmlattr:`PDUsize`
     :val:	2\ :sup:`7`\ ...2\ :sup:`11`
     :def:	1024
     :desc:	Proposed maximum TPDU size parameter used for outgoing Connection Request [:lemonobgtext:`CR-TPDU`].
		Only power of 2 values (e.g. 128, 256, 512) can be specified.

   * :attr:	:xmlattr:`TS1timeout`
     :val:	0...65535
     :def:	5 sec
     :desc:	Supervisory Timer 1 [:lemonobgtext:`TS1`] in seconds.
		Timer is stated when Connection Request [:lemonobgtext:`CR-TPDU`] message is sent.
		Network connection will be closed if no Connection Confirm [:lemonobgtext:`CC-TPDU`] is received from IED before the timer expires.
		Value 0 disables the timer.

.. include-file:: sections/Include/IEC61850cl_Flags.rstinc "" ":numref:`tabid-IEC61850clTransportFlags`" "Transport"

.. include-file:: sections/Include/IEC61850_LogFlags8.rstinc "" ":numref:`tabid-IEC61850clLogFlags`" "Transport"


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clTransportFlags" "Transport layer flags" ":ref:`xmlattr-IEC61850clTransportFlags`" "Transport layer flags"

   * :attr:	:bitdef:`0`
     :val:	xxxx.xxx0
     :desc:	**Ignore** destination reference [:lemonobgtext:`DST-REF`] of the received [:lemonobgtext:`CC-TPDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	**Check** destination reference [:lemonobgtext:`DST-REF`] of the received [:lemonobgtext:`CC-TPDU`].
		Communication will not be established if the received value doesn't match :ref:`xmlattr-IEC61850clTransportSourceREF`.

   * :attr:	:bitdef:`1`
     :val:	xxxx.xx0x
     :desc:	**Ignore** [:lemonobgtext:`Calling Transport-Selector`] and [:lemonobgtext:`Responding Transport-Selector`] identifiers of the received [:lemonobgtext:`CC-TPDU`]. (default value)

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	**Check** [:lemonobgtext:`Calling Transport-Selector`] and [:lemonobgtext:`Responding Transport-Selector`] identifiers of the received [:lemonobgtext:`CC-TPDU`].
		Communication will not be established if the received [:lemonobgtext:`Calling Transport-Selector`] doesn't match :ref:`xmlattr-IEC61850clTransportCallingTSEL` or
		[:lemonobgtext:`Responding Transport-Selector`] doesn't match "OSI-TSEL" defined in the SCL file.

   * :attr:	Bits 2...7
     :val:	Any
     :desc:	Bits reserved for future use

