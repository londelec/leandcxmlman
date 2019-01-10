.. _ref-IEC61850clSessionSettings:

SessionSettings
^^^^^^^^^^^^^^^

Settings of the Session layer (ISO8327) can be specified using attributes of :ref:`<ref-IEC61850clSessionSettings>` 
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clSessionSettings>`"

.. code-block:: none

   <SessionSettings CallingSSEL="0001" Flags="0x00"/>


.. _docref-IEC61850clSessionSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client SessionSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

   * :attr:     .. _ref-IEC61850clCallingSSEL:

                :xmlref:`CallingSSEL`
     :val:      Up to 16 hexadecimal characters 0...F
     :def:      0001
     :desc:     Calling Session Selector used for outgoing [:lemonobgtext:`CONNECT (CN) SPDU`] message

   * :attr:     .. _ref-IEC61850clSessionFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous settings of the Session layer.
		See table :numref:`docref-IEC61850clSessionFlagsBits` for description


.. _docref-IEC61850clSessionFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Session layer flags" ":ref:`<ref-IEC61850clSessionFlags>`" "Session layer flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     **Ignore** [:lemonobgtext:`Calling Session Selector`] and [:lemonobgtext:`Called Session Selector`] identifiers of the received [:lemonobgtext:`ACCEPT (AC) SPDU`] message (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     **Check** [:lemonobgtext:`Calling Session Selector`] and [:lemonobgtext:`Called Session Selector`] identifiers of the received [:lemonobgtext:`ACCEPT (AC) SPDU`] message.
		Communication will not be established if the received [:lemonobgtext:`Calling Session Selector`] doesn't match "OSI-SSEL" in the SCL file or
		[:lemonobgtext:`Called Session Selector`] is different from [:lemonobgtext:`CONNECT (CC) SPDU`] message value.

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     Transport connection is **released** when sending [:lemonobgtext:`FINISH (FN) SPDU`] message (default value)

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     Transport connection is **kept** when sending [:lemonobgtext:`FINISH (FN) SPDU`] message

   * :attr:     Bits 2...7
     :val:      Any
     :desc:     Bits reserved for future use
