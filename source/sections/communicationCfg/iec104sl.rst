
.. _xmlelem-gp104sl:

IEC104sl
^^^^^^^^

General settings of the IEC60870-5-104 controlled station (Slave) communication protocol instance.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gp104sl`"

.. code-block:: none

   <IEC104sl Index="12" HWIndex="4" XMLpath="IEC104sl_test.xml" ASDUAddr="5" StationID="2" FilterID="0" Source="6" CommsFlags="0x80" Name="SCADA"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gp104sl" "IEC104sl"

.. include-file:: sections/Include/gp_sl_Index.rstinc "" 

.. include-file:: sections/Include/gp_HWIndex.rstinc "" ":ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex`"
		:inlinetip:`Multiple` :ref:`xmlelem-gp104sl` :inlinetip:`instances can share the same hardware node.`

.. include-file:: sections/Include/gp_XMLpath.rstinc ""

   * :attr:	:xmlattr:`ASDUAddr`
     :val:	1...65534
     :desc:	Common address of ASDU (CAA).
		Please note value 65535 is Broadcast address and can't be used.

   * :attr:	:xmlattr:`StationID`
     :val:	1...254
     :desc:	Station identifier.
		It is possible to create more than 1 ASDU for our IEC60870-5-104 Slave station.
		Multiple :ref:`xmlelem-gp104sl` nodes must be created in this case, one for each ASDU.
		All of these :ref:`xmlelem-gp104sl` nodes will have the same :ref:`xmlattr-gp104slStationID` and unique :ref:`xmlattr-gp104slASDUAddr`.
		Station identifier is unique per hardware node so it is possible to have multiple stations with the same :ref:`xmlattr-gp104slStationID` as long as they are linked to different hardware nodes.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, our IEC60870-5-104 Slave station will have only one ASDU if attribute omitted.`

.. include-file:: sections/Include/gp_FilterID.rstinc ""

.. include-file:: sections/Include/IEC10xsl_Source.rstinc ""

.. include-file:: sections/Include/gp_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

.. include-file:: sections/Include/gp_section.rstinc "" ":ref:`xmlattr-gp104slXMLpath`" ":ref:`docref-IEC104sl`"
