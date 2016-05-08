
.. _ref-IEC101sl:

IEC101sl
^^^^^^^^

General settings of the IEC60870-5-101 controlled station (Slave) communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101sl>`"

.. code-block:: none

   <IEC101sl Index="5" HWIndex="1" XMLpath="IEC101sl_test.xml" LinkAddr="5" ASDUAddr="5" Source="6" CommsFlags="0x80" Name="Serial SCADA"/>


.. _ref-IEC101slAttributes:

.. field-list-table:: IEC101sl node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.20}|C{0.25}|S{0.55}|

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:     :xmlref:`Index`
     :val:      1...254
     :desc:     Index is a unique identifier of the communication protocol instance. 
		It is used to reference protocol instance from other configuration files e.g. logfile configuration XML file.
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     :xmlref:`HWIndex`
     :val:      1...254
     :desc:     Hardware Index is used to link the communication protocol instance to a hardware node.
		Use value of the :ref:`<ref-UART>`.\ :ref:`<ref-UARTIndex>`\; :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIndex>`\; :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTIndex>` \ or :ref:`<ref-UDP>`.\ :ref:`<ref-UDPIndex>` \ attribute as a hardware index in order to link the protocol instance.
		:inlinetip:`Multiple` :ref:`<ref-IEC101sl>` :inlinetip:`communication protocol instances can share the same hardware node.`

.. include-file:: sections/Include/Comms_XMLpath.rstinc "" ".. _ref-IEC101slXMLpath:"

   * :attr:    .. _ref-IEC101slLinkAddr:

                :xmlref:`LinkAddr`
     :val:      1...254 or 1...65534
     :desc:     Link layer address of the communication protocol instance.
		Address of the connected IEC60870-5-101 Master station must be the same.
		Size of the link layer address may be 1 or 2 bytes as set by the :ref:`<ref-IEC101slLinkSettings>`.\ :ref:`<ref-IEC101slLinkSettingsLinkAddrSize>` \ attribute.
		Please note value 255 (if link layer address size is 1 byte) or 65535 (if link layer address size is 2 bytes) is Broadcast address and can't be used.

   * :attr:     :xmlref:`ASDUAddr`
     :val:      1...254 or 1...65534
     :desc:     Common address of ASDU (CAA).
		It is possible to create more than 1 ASDU for our IEC60870-5-101 Slave station.
		Multiple :ref:`<ref-IEC101sl>` nodes must be created in this case, one for each ASDU.
		All of these :ref:`<ref-IEC101sl>` nodes will have the same :ref:`<ref-IEC101slLinkAddr>` and unique :xmlref:`ASDUAddr`.
		Size of the common ASDU address may be 1 or 2 bytes as set by the :ref:`<ref-IEC101slASDUSettings>`.\ :ref:`<ref-IEC101slASDUSettingsCAASize>` \ attribute.
		Please note value 255 (if ASDU address size is 1 byte) or 65535 (if ASDU address size is 2 bytes) is Broadcast address and can't be used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`<ref-IEC101slLinkAddr>` :inlinetip:`will be used if omitted.`

.. include-file:: sections/Include/IEC10xsl_Source.rstinc "" ".. _ref-IEC101slSource:"

.. include-file:: sections/Include/Comms_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

