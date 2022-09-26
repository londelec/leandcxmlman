.. _xmlelem-IEC101maBroadcast:

Broadcast
^^^^^^^^^

Broadcast common address of ASDU (CAA) usage for various commands can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC101maBroadcast`"

.. code-block:: none

   <Broadcast GI="1" TimeSync="0" Reset="0"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC101maBroadcast" "IEC60870-5-101 Master Broadcast attributes" ":spec: |C{0.12}|C{0.1}|C{0.1}|S{0.68}|"

.. include-file:: sections/Include/IEC10xma_BroadcastGI.rstinc "" "Broadcast address is 255 (if :ref:`xmlattr-IEC101maAsduCAASize` is 1 byte) or 65535 (if :ref:`xmlattr-IEC101maAsduCAASize` is 2 bytes)"

.. include-file:: sections/Include/IEC10xma_BroadcastCS.rstinc "" "Broadcast address is 255 (if :ref:`xmlattr-IEC101maLinkLinkAddrSize` is 1 byte) or 65535 (if :ref:`xmlattr-IEC101maLinkLinkAddrSize` is 2 bytes)"

.. include-file:: sections/Include/IEC10xma_BroadcastRP.rstinc "" "Broadcast address is 255 (if :ref:`xmlattr-IEC101maAsduCAASize` is 1 byte) or 65535 (if :ref:`xmlattr-IEC101maAsduCAASize` is 2 bytes)"
