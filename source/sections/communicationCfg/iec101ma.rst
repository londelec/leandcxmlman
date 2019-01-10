
.. _ref-IEC101ma:

IEC101ma
^^^^^^^^

General settings of the IEC60870-5-101 controlling station (Master) communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101ma>`"

.. code-block:: none

   <IEC101ma Index="10" HWIndex="2" XMLpath="IEC101ma_test.xml" LinkAddr="5" ASDUAddr="5" CommsFlags="0x80" Name="Radio Comms"/>


.. _ref-IEC101maAttributes:

.. field-list-table:: IEC101ma node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.14}|C{0.12}|S{0.74}|
   
   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:     .. _ref-IEC101maIndex:

                :xmlref:`Index`
     :val:      1...254
     :desc:     Index is a unique identifier of the communication protocol instance.
		It is used to reference protocol instance from other configuration files e.g. IO object tables
		(please see :ref:`DI<ref-IEC10xslDI>`.\ :ref:`<ref-IEC10xslDIDevice>`\; :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAIDevice>`\; :ref:`DO<ref-IEC10xslDO>`.\ :ref:`<ref-IEC10xslDODevice>`\; :ref:`AO<ref-IEC10xslAO>`.\ :ref:`<ref-IEC10xslAODevice>` \ attributes of the Slave protocol instance)
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     :xmlref:`HWIndex`
     :val:      1...254
     :desc:     Hardware Index is used to link the communication protocol instance to a hardware node.
		Use value of the :ref:`<ref-UART>`.\ :ref:`<ref-UARTIndex>`\; :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIndex>`\; :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTIndex>` \ or :ref:`<ref-UDP>`.\ :ref:`<ref-UDPIndex>` \ attribute as a hardware index in order to link the protocol instance.
		:inlinetip:`Multiple` :ref:`<ref-IEC101ma>` :inlinetip:`communication protocol instances can share the same hardware node.`

.. include-file:: sections/Include/Comms_XMLpath.rstinc "" ".. _ref-IEC101maXMLpath:"

   * :attr:    .. _ref-IEC101maLinkAddr:

                :xmlref:`LinkAddr`
     :val:      1...254 or 1...65534
     :desc:     Link layer address of the communication protocol instance.
		Address of the connected IEC60870-5-101 Slave station must be the same.
		Size of the link layer address may be 1 or 2 bytes as set by the :ref:`<ref-IEC101maLinkSettings>`.\ :ref:`<ref-IEC101maLinkSettingsLinkAddrSize>` \ attribute.
		Please note value 255 (if link layer address size is 1 byte) or 65535 (if link layer address size is 2 bytes) is Broadcast address and can't be used.

   * :attr:     :xmlref:`ASDUAddr`
     :val:      1...254 or 1...65534
     :desc:     Common address of ASDU (CAA).
		Connected IEC60870-5-101 Slave station may have 1 or more ASDUs.
		Multiple :ref:`<ref-IEC101ma>` nodes must be created in case peer station has multiple ASDUs, one for each ASDU.
		All of these :ref:`<ref-IEC101ma>` nodes will have the same :ref:`<ref-IEC101maLinkAddr>` and unique :xmlref:`ASDUAddr`.
		Size of the common ASDU address may be 1 or 2 bytes as set by the :ref:`<ref-IEC101maASDUSettings>`.\ :ref:`<ref-IEC101maASDUSettingsCAASize>` \ attribute.
		Please note value 255 (if ASDU address size is 1 byte) or 65535 (if ASDU address size is 2 bytes) is Broadcast address and can't be used.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`<ref-IEC101maLinkAddr>` :inlinetip:`will be used if omitted.`

.. include-file:: sections/Include/Comms_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

