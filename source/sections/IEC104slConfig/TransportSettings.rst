
TransportSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Protocol transport interface settings can be specified using attributes of  :ref:`TransportSettings<ref-IEC104slTransportSettings>` element node.

Please see sample :ref:`TransportSettings<ref-IEC104slTransportSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <TransportSettings T1="15" T2="10" T3="20" Kparam="12" Wparam="8" /> 

.. _ref-IEC104slTransportSettingsAttributes:

.. field-list-table:: IEC 60807-5-104 Slave XMLSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     :xmlref:`T1`
     :val:      1...65535
     :desc:     Timeout of send or test APDUs as per IEC 60870-5-104 standard. It is a delay in seconds for how long communication protocol instance waits a reply to a sent APDU [I-frame] or test message [TESTFR_act]. If no reply is received from peer station within a configured timeout, communication protocol instance initiates active close of the TCP socket (default 15 seconds)

   * :attr:     :xmlref:`T2`
     :val:      1...65535
     :desc:     Timeout for acknowledges in case of no data messages as per IEC 60870-5-104 standard. (requirement: T2timer < T1timer) It is a delay in seconds before communication protocol instance sends an acknowledge [S-frame] in case there are any unacknowledged messages from the peer station. (default 10 seconds)

   * :attr:     :xmlref:`T3`
     :val:      1...65535
     :desc:     Timeout for sending test messages in case of a long idle state from IEC 60870-5-104 standard. It is a maximal idle time in seconds before a test message [TESTFR_act] is sent to a peer station by the communication protocol instance. If this timeout is selected greater than T3 timeout configured in the peer station, it is most likely the test message will be sent by the peer station first (default 20 seconds)

   * :attr:     :xmlref:`Kparam`
     :val:      1...30
     :desc:     Maximum difference receive sequence number to send state variable as per IEC 60870-5-104 standard. Maximal number of outgoing APDU messages [I-frames] communication protocol instance will send to a peer station before it waits for an acknowledge [S-frame] (default 12 APDU messages)

   * :attr:     :xmlref:`Wparam`
     :val:      1...29
     :desc:     Latest acknowledge after receiving w number I format APDUs as per IEC 60870-5-104 standard. Number of incoming APDU messages [I-frames] received from a peer station before communication protocol instance sends an acknowledge [S-frame] (default 8 APDU messages)
     