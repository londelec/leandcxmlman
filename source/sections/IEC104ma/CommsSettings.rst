.. _xmlelem-IEC104maComm:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) change behavior and related delays can be specified using attributes of :ref:`xmlelem-IEC104maComm` 
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC104maComm`"

.. code-block:: none

   <CommsSettings OfflineDelay="10" PostOfflineDelay="1000" OnlineGIDelay="10" Flags="0x00" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC104maComm" "IEC60870-5-104 Master CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

   * :attr:	:xmlattr:`OfflineDelay`
     :val:	0...2\ :sup:`32`\  - 1
     :def:	6 sec
     :desc:	Offline delay in seconds before station status is changed to OFFLINE.
		Offline delay timer is activated after TCP socket has been closed.
		Default 6 seconds - station status will change to OFFLINE 6 seconds after TCP socket has been closed by either host.

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ":ref:`xmlattr-IEC104maCommOfflineDelay`"

.. include-file:: sections/Include/IEC10xma_OnlineGIDelay.rstinc ""

   * :attr:	:xmlattr:`Flags`
     :val:	|flags8range|
     :def:	0x00
     :desc:	Various communication related settings.
		See :numref:`tabid-IEC104maCommFlags` for description.


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC104maCommFlags" "IEC60870-5-104 Master Communication flags" ":ref:`xmlattr-IEC104maCommFlags`" "Communication flags"

   * :attr:	:bitdef:`3`
     :val:	xxxx.0xxx
     :desc:	**Send** General Interrogation command when outstation goes online after a communication loss (station status changes to ONLINE)

   * :(attr):
     :val:	xxxx.1xxx
     :desc:	**Don't send** General Interrogation command when outstation goes online after a communication loss (station status changes to ONLINE).
		:inlinetip:`General Interrogation is always sent on system startup regardless of this setting.`

   * :attr:	Bit 4
     :val:	xxx0.xxxx
     :desc:	**Purge** unacknowledged [:lemonobgtext:`I-frames`] when new connection to outstation is established after a communication loss.

   * :(attr):
     :val:	xxx1.xxxx
     :desc:	**Resend** unacknowledged [:lemonobgtext:`I-frames`] when new connection to outstation is established after a communication loss.
		:inlineimportant:`Care must be taken when this option is enabled as it may result in previously unacknowledged Control commands being sent.
		This can happen after any length of time.`

   * :attr:	Bits 0...2;5...7
     :val:	Any
     :desc:	Bits reserved for future use
