.. _xmlelem-IEC104slComm:

CommsSettings
^^^^^^^^^^^^^

Communication state (e.g. online and offline) change behavior and related delays can be specified in this node.

Please see sample :ref:`xmlelem-IEC104slComm` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings OfflineDelay="10" StartupGIDelay="10" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC104slComm" "IEC60870-5-104 Slave CommsSettings attributes" ":spec: |C{0.16}|C{0.12}|C{0.1}|S{0.62}|"

   * :attr:	:xmlattr:`OfflineDelay`
     :val:	0...2\ :sup:`32`\  - 1
     :def:	0 sec
     :desc:	Offline delay in seconds before status of this protocol instance is changed to OFFLINE.
		Offline delay timer is activated after TCP socket has been closed. Default 0 seconds - station status will change to OFFLINE immediately after TCP socket has been closed by a remote host.

.. include-file:: sections/Include/IEC10xsl_StartupGIDelay.rstinc ""
