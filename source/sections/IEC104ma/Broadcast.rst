.. _ref-IEC104maBroadcast:

Broadcast
^^^^^^^^^

Broadcast common address of ASDU (CAA) usage for various commands can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC104maBroadcast>`"

.. code-block:: none

   <Broadcast GI="1" TimeSync="0" Reset="0" />


.. _docref-IEC104maBroadcastAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-104 Master Broadcast attributes"

.. include-file:: sections/Include/IEC10xma_BroadcastGI.rstinc "" ".. _ref-IEC104maBroadcastGI:" "Broadcast address is 65535"

   * :attr:     .. _ref-IEC104maBroadcastTimeSync:

                :xmlref:`TimeSync`
     :val:      0
     :def:      0
     :desc:     Send Time Synchronization [C_CS_NA_1] commands with **individual** Common Addresses of ASDU (CAA)

   * :(attr):
     :val:      1
     :(def):
     :desc:     Send Time Synchronization [C_CS_NA_1] commands with **broadcast** Common Address of ASDU (CAA). Broadcast address is 65535

.. include-file:: sections/Include/IEC10xma_BroadcastRP.rstinc "" ".. _ref-IEC104maBroadcastReset:" "Broadcast address is 65535"
