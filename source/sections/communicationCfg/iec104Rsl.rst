
.. _xmlelem-gp104Rsl:

IEC104Rsl
^^^^^^^^^

There is an option to use multiple redundant connections for communication between |leandcapp| and controlling
(Master) stations ensuring a failure of a single communication channel will not disrupt the exchange of data.
This option is currently available for IEC60870-5-104 controlled station (Slave) instances and can be enabled by creating a so-called redundancy group.
Redundancy group is a set of communication protocol instances working together and allowing several controlling stations (Masters)
to receive the same data over single/multiple communication channels.
Only one controlling station (Master) within a redundancy group is in a 'Started connection' state which means only this station is sending/receiving data.
Other controlling stations (Masters) are in a 'Stopped connection' state, they only monitor availability of the communication channel, but do not send/receive data.

In order to explain how to set up a redundancy group 2 terms 'Main' (:ref:`xmlelem-gp104sl`) and 'Redundant' (:ref:`xmlelem-gp104Rsl`) communication protocol
instance are used throughout this manual.
There is no functional difference between 'Main' and 'Redundant' communication protocol instance as far as the communication standard is concerned.
These terms are only used to differentiate communication instances in |leandcapp| configuration.

IEC60870-5-104 controlled station (Slave) redundancy group is enabled as follows:
any :ref:`xmlelem-gp104sl` communication protocol instance can be chosen as 'Main' and redundancy is automatically enabled if one or more
:ref:`xmlelem-gp104Rsl` instances are linked to the 'Main' instance.
It is possible to link up to 15 'Redundant' instances to the same 'Main' instance, thus creating a redundancy group of 16.
This would allow up to 16 controlling (Master) stations to connect to |leandcapp|.

No IO object tables are required for 'Redundant' communication protocol instance, because it is always linked to a 'Main' instance which has IO object tables.
An identical set of IO objects is shared by all instances within a redundancy group.
.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-gp104Rsl`"

.. code-block:: none

   <IEC104Rsl Index="13" HWIndex="3" RedundantToIndex="12" FilterID="0" CommsFlags="0x80" Name="SCADA"/>


.. include-file:: sections/Include/table_gp.rstinc "" "tabid-gp104Rsl" "IEC104Rsl"

.. include-file:: sections/Include/gp_sl_Index.rstinc "" 

.. include-file:: sections/Include/gp_HWIndex.rstinc "" ":ref:`xmlelem-tcpserver`.\ :ref:`xmlattr-TCPSERVERIndex`"
		:inlinetip:`Multiple` :ref:`xmlelem-gp104Rsl` :inlinetip:`instances can share the same hardware node.`

   * :attr:	:xmlattr:`RedundantToIndex`
     :val:	|gpindexrange|
     :desc:	Link 'Redundant' instance to 'Main' instance.
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

