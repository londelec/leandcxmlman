
.. _ref-IEC104sl:

IEC104sl
^^^^^^^^

General settings of the IEC60870-5-104 controlled station (Slave) communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC104sl>`"

.. code-block:: none

   <IEC104sl Index="12" HWIndex="4" XMLpath="IEC104sl_test.xml" ASDUAddr="5" StationID="2" FilterID="0" Source="6" CommsFlags="0x80" Name="SCADA"/>


.. _ref-IEC104slAttributes:

.. field-list-table:: IEC104sl node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.14}|C{0.12}|S{0.74}|

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:     .. _ref-IEC104slIndex:

                :xmlref:`Index`
     :val:      1...254
     :desc:     Index is a unique identifier of the communication protocol instance.
		It is used to reference protocol instance from other configuration files e.g. logfile configuration XML file.
		:inlinetip:`Indexes don't have to be in a sequential order.`

   * :attr:     :xmlref:`HWIndex`
     :val:      1...254
     :desc:     Hardware Index is used to link the communication protocol instance to a hardware node.
		Use value of the :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIndex>` \ attribute as a hardware index in order to link the protocol instance.
		:inlinetip:`Multiple` :ref:`<ref-IEC104sl>` :inlinetip:`communication protocol instances can share the same hardware node.`

.. include-file:: sections/Include/Comms_XMLpath.rstinc "" ".. _ref-IEC104slXMLpath:"

   * :attr:    .. _ref-IEC104slASDUAddr:

		:xmlref:`ASDUAddr`
     :val:      1...65534
     :desc:     Common address of ASDU (CAA).
		Please note value 65535 is Broadcast address and can't be used.

   * :attr:     .. _ref-IEC104slStationID:

                :xmlref:`StationID`
     :val:      1...254
     :desc:     Station identifier.
		It is possible to create more than 1 ASDU for our IEC60870-5-104 Slave station.
		Multiple :ref:`<ref-IEC104sl>` nodes must be created in this case, one for each ASDU.
		All of these :ref:`<ref-IEC104sl>` nodes will have the same :xmlref:`StationID` and unique :ref:`<ref-IEC104slASDUAddr>`.
		Station identifier is unique per hardware node so it is possible to have multiple stations with the same :xmlref:`StationID` as long as they are linked to different hardware nodes.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, our IEC60870-5-104 Slave station will have only one ASDU if attribute omitted.`

.. include-file:: sections/Include/Comms_FilterID.rstinc "" ".. _ref-IEC104slFilterID:"

.. include-file:: sections/Include/IEC10xsl_Source.rstinc "" ".. _ref-IEC104slSource:"

.. include-file:: sections/Include/Comms_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

