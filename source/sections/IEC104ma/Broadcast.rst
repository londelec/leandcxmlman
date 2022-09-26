.. _xmlelem-IEC104maBroadcast:

Broadcast
^^^^^^^^^

Broadcast common address of ASDU (CAA) usage for various commands can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC104maBroadcast`"

.. code-block:: none

   <Broadcast GI="1" TimeSync="0" Reset="0" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC104maBroadcast" "IEC60870-5-104 Master Broadcast attributes" ":spec: |C{0.12}|C{0.1}|C{0.1}|S{0.68}|"

.. include-file:: sections/Include/IEC10xma_BroadcastGI.rstinc "" "Broadcast address is 65535"

   * :attr:	:xmlattr:`TimeSync`
     :val:	0
     :def:	0
     :desc:	Send Time Synchronization [:lemonobgtext:`C_CS_NA_1`] commands with **individual** Common Addresses of ASDU (CAA)

   * :(attr):
     :val:	1
     :(def):
     :desc:	Send Time Synchronization [:lemonobgtext:`C_CS_NA_1`] commands with **broadcast** Common Address of ASDU (CAA).
		Broadcast address is 65535

.. include-file:: sections/Include/IEC10xma_BroadcastRP.rstinc "" "Broadcast address is 65535"
