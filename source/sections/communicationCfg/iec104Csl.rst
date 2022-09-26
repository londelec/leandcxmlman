
.. _xmlelem-gp104Csl:

IEC104Csl
^^^^^^^^^

There is an option to clone IEC60870-5-104 stations which have multiple ASDUs, 
i.e. multiple :ref:`xmlelem-gp104sl` nodes with the same :ref:`xmlattr-gp104slStationID` attributes and unique :ref:`xmlattr-gp104slASDUAddr` attributes.
Cloned IEC60870-5-104 station will have identical number of ASDUs and can be linked to different hardware node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gp104Csl`"

.. code-block:: none

   <IEC104Csl Index="13" HWIndex="3" CloneFromIndex="12" StationID="5" FilterID="0" CommsFlags="0x80" Name="SCADA"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gp104Csl" "IEC104Csl"

   * :attr:	:xmlattr:`Index`
     :val:	|gpindexrange|
     :desc:	Base index of the first cloned node.
		If the source IEC60870-5-104 Slave station has multiple ASDUs, all of those will be cloned and indexes will be initialized sequentially.
		:inlineimportant:`Remember to leave a gap for the sequence of indexes to be created automatically after base index value specified. Number of index values created will be the number ASDUs source IEC60870-5-104 Slave station has.`

   * :attr:	:xmlattr:`HWIndex`
     :val:	|hwindexrange|
     :desc:	Hardware Index is used to link cloned communication protocol instance(s) to a hardware node.
		Use value of the :ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex` \ attribute as a hardware index in order to link the cloned protocol instance(s).
		:inlinetip:`Multiple` :ref:`xmlelem-gp104Csl` :inlinetip:`instances can share the same hardware node.`

   * :attr:	:xmlattr:`CloneFromIndex`
     :val:	|gpindexrange|
     :desc:	Source :ref:`xmlelem-gp104sl` node to be cloned.
		Use value of the :ref:`xmlelem-gp104sl`.\ :ref:`xmlattr-gp104slIndex` \ attribute.

   * :attr:	:xmlattr:`StationID`
     :val:	1...254
     :desc:	Station identifier.
		It is possible to create more than 1 ASDU for our IEC60870-5-104 Slave station.
		Multiple :ref:`xmlelem-gp104sl` nodes must be created in this case, one for each ASDU.
		All of those :ref:`xmlelem-gp104sl` nodes will have the same :ref:`xmlattr-gp104slStationID` and unique :ref:`xmlattr-gp104slASDUAddr`.
		If the IEC60870-5-104 Slave station with multiple ASDUs is being cloned, new identifier can be specified in this attribute.
		Station identifier is unique per hardware node so it is possible to have multiple stations with the same :ref:`xmlattr-gp104CslStationID` as long as they are linked to different hardware nodes.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, cloned station will create its own unique station identifier if attribute omitted.`

.. include-file:: sections/Include/gp_FilterID.rstinc ""

.. include-file:: sections/Include/gp_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

