
.. _xmlelem-gp104ma:

IEC104ma
^^^^^^^^

General settings of the IEC60870-5-104 controlling station (Master) communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gp104ma`"

.. code-block:: none

   <IEC104ma Index="20" HWIndex="2" XMLpath="IEC104ma_test.xml" ASDUAddr="5" StationID="2" CommsFlags="0x10" Name="RTU"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gp104ma" "IEC104ma"

.. include-file:: sections/Include/gp_ma_Index.rstinc "" 

.. include-file:: sections/Include/gp_HWIndex.rstinc "" ":ref:`xmlelem-tcpclient`.\ :ref:`xmlattr-TCPCLIENTIndex`"
		:inlinetip:`Multiple` :ref:`xmlelem-gp104ma` :inlinetip:`instances can share the same hardware node.`

.. include-file:: sections/Include/gp_XMLpath.rstinc ""

   * :attr:	:xmlattr:`ASDUAddr`
     :val:	1...65534
     :desc:	Common address of ASDU (CAA). Please note value 65535 is Broadcast address and can't be used.

   * :attr:	:xmlattr:`StationID`
     :val:	1...254
     :desc:	Station identifier.
		Connected IEC60870-5-104 Slave station may have 1 or more ASDUs.
		Multiple :ref:`xmlelem-gp104ma` nodes must be created in case peer station has multiple ASDUs, one for each ASDU.
		All of these :ref:`xmlelem-gp104ma` nodes will have the same :ref:`xmlattr-gp104maStationID` and unique :ref:`xmlattr-gp104maASDUAddr`.
		Station identifier is unique per hardware node so it is possible to have multiple stations with the same :ref:`xmlattr-gp104maStationID` as long as they are linked to different hardware nodes.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, our IEC60870-5-104 Master station will have only one ASDU if attribute omitted.`

.. include-file:: sections/Include/gp_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. include-file:: sections/Include/gp_section.rstinc "" ":ref:`xmlattr-gp104maXMLpath`" ":ref:`docref-IEC104ma`"
