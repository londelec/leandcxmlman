.. _xmlelem-IEC61850clSession:

SessionSettings
^^^^^^^^^^^^^^^

Settings of the Session layer (ISO8327) can be specified using attributes of :ref:`xmlelem-IEC61850clSession` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clSession`"

.. code-block:: none

   <SessionSettings CallingSSEL="0001" TIMtimeout="2" Flags="0x00" LogFlags="0x00"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clSession" "IEC61850 Client SessionSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

   * :attr:	:xmlattr:`CallingSSEL`
     :val:	Up to 16 hexadecimal characters 0...F
     :def:	0001
     :desc:	[:lemonobgtext:`Calling Session Selector`] field value for outgoing [:lemonobgtext:`CONNECT (CN) SPDU`].

   * :attr:	:xmlattr:`TIMtimeout`
     :val:	1...65535
     :def:	5 sec
     :desc:	| Disconnection and abort timer [:lemonobgtext:`TIM`] in seconds. Timer is stated when sending [:lemonobgtext:`ABORT (AB) SPDU`].
		| Network connection will be closed if timer expires before either:
		| > No [:lemonobgtext:`T-DISCONNECT`] is received from Transport layer in case if Transport connection is **released** (:ref:`bitref-IEC61850clSessionFlagsBit2`\ |bitfalse|) or
		| > No [:lemonobgtext:`ABORT ACCEPT (AA) SPDU`] is received from IED in case if Transport connection is **kept** (:ref:`bitref-IEC61850clSessionFlagsBit2`\ |bittrue|).

.. include-file:: sections/Include/IEC61850cl_Flags.rstinc "" ":numref:`tabid-IEC61850clSessionFlags`" "Session"

.. include-file:: sections/Include/IEC61850_LogFlags.rstinc "" ":numref:`tabid-IEC61850clLogFlags`" "Session"


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clSessionFlags" "Session layer flags" ":ref:`xmlattr-IEC61850clSessionFlags`" "Session layer flags"

   * :attr:	:bitdef:`0`
     :val:	xxxx.xxx0
     :desc:	**Ignore** [:lemonobgtext:`Calling Session Selector`] and [:lemonobgtext:`Called Session Selector`] identifiers of the received [:lemonobgtext:`ACCEPT (AC) SPDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	**Check** [:lemonobgtext:`Calling Session Selector`] and [:lemonobgtext:`Called Session Selector`] identifiers of the received [:lemonobgtext:`ACCEPT (AC) SPDU`].
		Communication will not be established if the received [:lemonobgtext:`Calling Session Selector`] doesn't match "OSI-SSEL" defined in the SCL file or
		[:lemonobgtext:`Called Session Selector`] doesn't match :ref:`xmlattr-IEC61850clSessionCallingSSEL`.

   * :attr:	:bitdef:`1`
     :val:	xxxx.xx0x
     :desc:	Transport connection is **released** when sending [:lemonobgtext:`FINISH (FN) SPDU`]. (default value)

   * :(attr):
     :val:	xxxx.xx1x
     :desc:	Transport connection is **kept** when sending [:lemonobgtext:`FINISH (FN) SPDU`].

   * :attr:	:bitdef:`2`
     :val:	xxxx.x0xx
     :desc:	Transport connection is **released** when sending [:lemonobgtext:`ABORT (AB) SPDU`]. (default value)

   * :(attr):
     :val:	xxxx.x1xx
     :desc:	Transport connection is **kept** when sending [:lemonobgtext:`ABORT (AB) SPDU`].

   * :attr:	Bits 3...7
     :val:	Any
     :desc:	Bits reserved for future use

