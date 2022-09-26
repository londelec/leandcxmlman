.. _xmlelem-IEC101slComm:

CommsSettings
^^^^^^^^^^^^^

Communication state change behavior and related delays can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC101slComm`"

.. code-block:: none

   <CommsSettings OfflineDelay="120" StartupGIDelay="10" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC101slComm" "IEC60870-5-101 Slave CommsSettings attributes" ":spec: |C{0.18}|C{0.1}|C{0.1}|S{0.62}|"

   * :attr:	:xmlattr:`OfflineDelay`
     :val:	1...2\ :sup:`32`\  - 1
     :def:	60 sec
     :desc:	Delay in seconds before resetting the link if there is no request from Master station.
		Reset remote link message is required after communication loss exceeding configured offline delay in order to restart communication.

.. include-file:: sections/Include/IEC10xsl_StartupGIDelay.rstinc ""

