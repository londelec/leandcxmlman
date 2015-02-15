.. _docref-IEC101maBroadcastAttr:

Broadcast attributes
^^^^^^^^^^^^^^^^^^^^

Broadcast common address of ASDU (CAA) usage for various commands can be specified using attributes of 
:ref:`Broadcast<ref-IEC101maBroadcast>` element node.

Please see sample :ref:`Broadcast<ref-IEC101maBroadcast>` node and the table listing all available attributes below.

.. code-block:: none

   <Broadcast GI="1" TimeSync="0" Reset="0"/>

.. _docref-IEC101maBroadcastAttab:

.. field-list-table:: IEC 60870-5-101 Master Broadcast attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

.. include-file:: sections/Include/IEC10xma_BroadcastGI.rstinc "" ".. _ref-IEC101maBroadcastGI:" "Broadcast address is 255 (if size of the CAA is 1 byte) or 65535 (if size of the CAA is 2 bytes)"

.. include-file:: sections/Include/IEC10xma_BroadcastCS.rstinc "" ".. _ref-IEC101maBroadcastTimeSync:" "Broadcast address is 255 (if size of address is 1 byte) or 65535 (if size of address is 2 bytes)"

.. include-file:: sections/Include/IEC10xma_BroadcastRP.rstinc "" ".. _ref-IEC101maBroadcastReset:" "Broadcast address is 255 (if size of the CAA is 1 byte) or 65535 (if size of the CAA is 2 bytes)"
     
