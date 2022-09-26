.. _xmlelem-SpabusmaTime:

TimeSettings
^^^^^^^^^^^^

Time settings of the communication protocol instance are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-SpabusmaTime`"

.. code-block:: none

   <TimeSettings TimeZone="UTC" Flags="0x00"/>


.. include-file:: sections/Include/TimeZone.rstinc "" "tabid-SpabusmaTimeSettings" "Spabus Master TimeSettings attributes"

   * :attr:	:xmlattr:`Flags`
     :val:	0...255 or 0x00...0xFF
     :def:	0x00
     :desc:	Miscellaneous time synchronization settings.
		See :numref:`tabid-SpabusmaTimeFlags` for description.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-SpabusmaTimeFlags" "Time Synchronization flags" ":ref:`xmlattr-SpabusmaTimeFlags`" "Time synchronization flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     **Include** leading zeros to Year, Month, Day, Hour and Minute values of Date :lemonobgtext:`WD` synchronization message (default value).
		Sample outgoing date string :lemonobgtext:`WD:12-03-02 12.05`

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     **Omit** leading zeros from Year, Month, Day, Hour and Minute values of Date :lemonobgtext:`WD` synchronization message.
		Sample outgoing date string :lemonobgtext:`WD:12-3-2 12.5`

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     **Include** leading zeros to Second and Millisecond values of Time :lemonobgtext:`WT` and Date :lemonobgtext:`WD` messages (default value).
		Sample outgoing time string :lemonobgtext:`WT:03.034`

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     **Omit** leading zeros from Second and Millisecond values of Time :lemonobgtext:`WT` and Date :lemonobgtext:`WD` messages.
		Sample outgoing time string :lemonobgtext:`WT:3.34`

   * :attr:     Bits 2...7
     :val:      Any
     :desc:     Bits reserved for future use
