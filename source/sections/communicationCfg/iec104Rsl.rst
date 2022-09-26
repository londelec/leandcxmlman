
.. _xmlelem-gp104Rsl:

IEC104Rsl
^^^^^^^^^

There is an option to use multiple redundant connections for communication between leandc and controlling 
(Master) stations ensuring a failure of a single communication channel will not disrupt the exchange of data. 
This option is currently available for leandc IEC60870-5-104 controlled station (Slave) mode and can be 
enabled by creating a redundancy group. Redundancy group is a number of leandc communication protocol
instances which are working together allowing several controlling stations (Masters) to receive the same data 
over single/multiple communication channels. Only one controlling station (Master) within a redundancy group is 
in a 'Started state' which means it is exchanging the application data with leandc. Other controlling stations 
(Masters) are in a 'Stopped state', they only monitor availability of the communication channel and do not 
exchange the application data.

In order to explain how to configure a redundancy group in leandc there are two terms 'Main' (:ref:`xmlelem-gp104sl` node) 
and 'Redundant' (:ref:`xmlelem-gp104Rsl` node) communication protocol instance used throughout this manual. There is no 
functional difference between 'Main' and 'Redundant' communication protocol instance as far as communication 
standard is concerned, these are only used to reference different types of nodes in leandc configuration.

IEC60870-5-104 controlled station (Slave) redundancy group in leandc is enabled as follows: any :ref:`xmlelem-gp104sl` 
node can be chosen as 'Main' communication protocol instance and redundancy is automatically enabled if one 
or more :ref:`xmlelem-gp104Rsl` nodes are linked to the 'Main' communication protocol instance. It is possible to link up to 15 
'Redundant' communication protocol instances to the same 'Main' communication protocol instance, thus 
creating a redundancy group of 16. This allows for up to 16 controlling (Master) stations to connect to leandc.

No IO object XML configuration is required for 'Redundant' communication protocol instance, because it is 
always linked to 'Main' communication protocol instance, which has an IO object table and the application data 
will be shared by all instances within a redundancy group. 
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gp104Rsl`"

.. code-block:: none

   <IEC104Rsl Index="13" HWIndex="3" RedundantToIndex="12" FilterID="0" CommsFlags="0x80" Name="SCADA"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gp104Rsl" "IEC104Rsl"

.. include-file:: sections/Include/gp_sl_Index.rstinc "" 

.. include-file:: sections/Include/gp_HWIndex.rstinc "" ":ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex`"
		:inlinetip:`Multiple` :ref:`xmlelem-gp104Rsl` :inlinetip:`instances can share the same hardware node.`

   * :attr:	:xmlattr:`RedundantToIndex`
     :val:	|gpindexrange|
     :desc:	Link 'Redundant' protocol instance to 'Main' instance.
		Use value of the :ref:`xmlelem-gp104sl`.\ :ref:`xmlattr-gp104slIndex` attribute.

.. include-file:: sections/Include/gp_FilterID.rstinc ""

.. include-file:: sections/Include/gp_CommsFlags.rstinc ""

.. include-file:: sections/Include/Name_wodef.rstinc ""

Example redundancy group of 4 instances shown below.
This will enable up to 4 controlling (Master) stations to connect.

.. code-block:: none

   <CommunicationCfg> 
            <IEC104sl Index="12" HWIndex="3" XMLpath="IEC104ma_test.xml" Name="SCADA1"/>
            <IEC104Rsl Index="13" HWIndex="3" RedundantToIndex="12" Name="SCADA2"/>
            <IEC104Rsl Index="14" HWIndex="3" RedundantToIndex="12" Name="SCADA3"/>
            <IEC104Rsl Index="15" HWIndex="3" RedundantToIndex="12" Name="SCADA4"/>
   </CommunicationCfg>

