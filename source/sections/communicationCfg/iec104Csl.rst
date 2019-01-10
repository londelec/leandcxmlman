
.. _ref-IEC104Csl:

IEC104Csl
^^^^^^^^^

There is an option to clone IEC60870-5-104 stations which have multiple ASDUs, 
i.e. multiple :ref:`<ref-IEC104sl>` nodes with the same :ref:`<ref-IEC104slStationID>` attributes and unique :ref:`<ref-IEC104slASDUAddr>` attributes.
Cloned IEC60870-5-104 station will have identical number of ASDUs and can be linked to different hardware node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC104Csl>`"

.. code-block:: none

   <IEC104Csl Index="13" HWIndex="3" CloneFromIndex="12" StationID="5" FilterID="0" CommsFlags="0x80" Name="SCADA"/>


.. _ref-IEC104CslAttributes:

.. field-list-table:: IEC104Csl node
   :class: table table-condensed table-bordered longtable
   :header-rows: 1
   :spec: |C{0.18}|C{0.12}|S{0.7}|

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:     :xmlref:`Index`
     :val:      1...254
     :desc:     Base index of the first cloned node.
		If the source IEC60870-5-104 Slave station has multiple ASDUs, all of those will be cloned and indexes will be initialized sequentially.
		:inlineimportant:`Remember to leave a gap for the sequence of indexes to be created automatically after base index value specified. Number of index values created will be the number ASDUs source IEC60870-5-104 Slave station has.`

   * :attr:     :xmlref:`HWIndex`
     :val:      1...254
     :desc:     Hardware Index is used to link cloned communication protocol instance(s) to a hardware node.
		Use value of the :ref:`<ref-TCPSERVER>`.\ :ref:`<ref-TCPSERVERIndex>` \ attribute as a hardware index in order to link the cloned protocol instance(s).
		:inlinetip:`Multiple` :ref:`<ref-IEC104Csl>` :inlinetip:`communication protocol instances can share the same hardware node.`

   * :attr:     :xmlref:`CloneFromIndex`
     :val:      1...254
     :desc:     Source :ref:`<ref-IEC104sl>` node to be cloned.
		Use value of the :ref:`<ref-IEC104sl>`.\ :ref:`<ref-IEC104slIndex>` \ attribute.

   * :attr:     :xmlref:`StationID`
     :val:      1...254
     :desc:     Station identifier.
		It is possible to create more than 1 ASDU for our IEC60870-5-104 Slave station.
		Multiple :ref:`<ref-IEC104sl>` nodes must be created in this case, one for each ASDU.
		All of those :ref:`<ref-IEC104sl>` nodes will have the same :ref:`<ref-IEC104slStationID>` and unique :ref:`<ref-IEC104slASDUAddr>`.
		If the IEC60870-5-104 Slave station with multiple ASDUs is being cloned, new identifier can be specified in this attribute.
		Station identifier is unique per hardware node so it is possible to have multiple stations with the same :xmlref:`StationID` as long as they are linked to different hardware nodes.
		:inlinetip:`Attribute is optional and doesn't have to be included in configuration, cloned station will create its own unique station identifier if attribute omitted.`

.. include-file:: sections/Include/Comms_FilterID.rstinc "" ".. _ref-IEC104CslFilterID:"

.. include-file:: sections/Include/Comms_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

