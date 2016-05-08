
.. _ref-IEC104ma:

IEC104ma
^^^^^^^^

General settings of the IEC60870-5-104 controlling station (Master) communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC104ma>`"

.. code-block:: none

   <IEC104ma Index="20" HWIndex="2" XMLpath="IEC104ma_test.xml" ASDUAddr="5" StationID="2" CommsFlags="0x10" Name="RTU"/>


.. _ref-IEC104maAttributes:

.. field-list-table:: IEC104ma node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.20}|C{0.25}|S{0.55}|

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:     :xmlref:`Index`
     :val:      1...254
     :desc:     Index is a unique identifier of the communication protocol instance.
		It is used to reference protocol instance from other configuration files e.g. IO object tables
		(please see :ref:`DI<ref-IEC10xslDI>`.\ :ref:`<ref-IEC10xslDIDevice>`\; :ref:`AI<ref-IEC10xslAI>`.\ :ref:`<ref-IEC10xslAIDevice>`\; :ref:`DO<ref-IEC10xslDO>`.\ :ref:`<ref-IEC10xslDODevice>`\; :ref:`AO<ref-IEC10xslAO>`.\ :ref:`<ref-IEC10xslAODevice>` \ attributes of the Slave protocol instance)
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     :xmlref:`HWIndex`
     :val:      1...254
     :desc:     Hardware Index is used to link the communication protocol instance to a hardware node.
		Use value of the :ref:`<ref-TCPCLIENT>`.\ :ref:`<ref-TCPCLIENTIndex>` \ attribute as a hardware index in order to link the protocol instance.
		:inlinetip:`Multiple` :ref:`<ref-IEC104ma>` :inlinetip:`communication protocol instances can share the same hardware node.`

.. include-file:: sections/Include/Comms_XMLpath.rstinc "" ".. _ref-IEC104maXMLpath:"

   * :attr:    .. _ref-IEC104maASDUAddr:

		:xmlref:`ASDUAddr`
     :val:      1...65534
     :desc:     Common address of ASDU (CAA). Please note value 65535 is Broadcast address and can't be used.

   * :attr:     :xmlref:`StationID`
     :val:      1...254
     :desc:     Station identifier.
		Connected IEC60870-5-104 Slave station may have 1 or more ASDUs.
		Multiple :ref:`<ref-IEC104ma>` nodes must be created in case peer station has multiple ASDUs, one for each ASDU.
		All of these :ref:`<ref-IEC104ma>` nodes will have the same :xmlref:`StationID` and unique :ref:`<ref-IEC104maASDUAddr>`.
		Station identifier is unique per hardware node so it is possible to have multiple stations with the same :xmlref:`StationID` as long as they are linked to different hardware nodes.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, our IEC60870-5-104 Master station will have only one ASDU if attribute omitted.`

.. include-file:: sections/Include/Comms_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

