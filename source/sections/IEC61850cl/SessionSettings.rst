.. _ref-IEC61850clSessionSettings:

SessionSettings
^^^^^^^^^^^^^^^

Settings of the Session layer (ISO8327) can be specified using attributes of :ref:`<ref-IEC61850clSessionSettings>` 
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clSessionSettings>`"

.. code-block:: none

   <SessionSettings CallingSSEL="1" Flags="0x00"/>


.. _docref-IEC61850clSessionSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client SessionSettings attributes"

   * :attr:     :xmlref:`CallingSSEL`
     :val:      1...65535
     :def:      1
     :desc:     Calling Session Selector used for outgoing [CONNECT (CN) SPDU] message

   * :attr:     .. _ref-IEC61850clSessionFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous settings of the Session layer. See table :numref:`docref-IEC61850clSessionFlagsBits` for description


.. _docref-IEC61850clSessionFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Session layer flags" ":ref:`<ref-IEC61850clSessionFlags>`" "Session layer flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     Transport connection is **released** when sending [FINISH (FN) SPDU] message (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     Transport connection is **kept** when sending [FINISH (FN) SPDU] message

   * :attr:     Bits 1...7
     :val:      Any
     :desc:     Bits reserved for future use
