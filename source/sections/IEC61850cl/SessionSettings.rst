.. _ref-IEC61850clSessionSettings:

SessionSettings
^^^^^^^^^^^^^^^

Settings of the Session layer (ISO8327) can be specified using attributes of :ref:`<ref-IEC61850clSessionSettings>` 
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clSessionSettings>`"

.. code-block:: none

   <SessionSettings CallingSSEL="0001" Flags="0x00"/>


.. _docref-IEC61850clSessionSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client SessionSettings attributes"

   * :attr:     .. _ref-IEC61850clCallingSSEL:

                :xmlref:`CallingSSEL`
     :val:      Up to 16 hexadecimal characters 0...F
     :def:      0001
     :desc:     Calling Session Selector used for outgoing [:lectext1:`CONNECT (CN) SPDU`] message

   * :attr:     .. _ref-IEC61850clSessionFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous settings of the Session layer.
		See table :numref:`ref-IEC61850clSessionFlagsBits` for description


.. _ref-IEC61850clSessionFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Session layer flags" ":ref:`<ref-IEC61850clSessionFlags>`" "Session layer flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     **Ignore** [:lectext1:`Calling Session Selector`] and [:lectext1:`Called Session Selector`] identifiers of the received [:lectext1:`ACCEPT (AC) SPDU`] message (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     **Check** [:lectext1:`Calling Session Selector`] and [:lectext1:`Called Session Selector`] identifiers of the received [:lectext1:`ACCEPT (AC) SPDU`] message.
		Communication will not be established if the received [:lectext1:`Calling Session Selector`] doesn't match "OSI-SSEL" in the SCL file or
		[:lectext1:`Called Session Selector`] is different from [:lectext1:`CONNECT (CC) SPDU`] message value.

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     Transport connection is **released** when sending [:lectext1:`FINISH (FN) SPDU`] message (default value)

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     Transport connection is **kept** when sending [:lectext1:`FINISH (FN) SPDU`] message

   * :attr:     Bits 2...7
     :val:      Any
     :desc:     Bits reserved for future use
