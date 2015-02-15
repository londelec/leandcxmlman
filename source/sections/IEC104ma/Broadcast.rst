.. _docref-IEC104maBroadcastAttr:

Broadcast attributes
^^^^^^^^^^^^^^^^^^^^

Broadcast common address of ASDU (CAA) usage for various commands can be specified using attributes of 
:ref:`Broadcast<ref-IEC104maBroadcast>` element node.

Please see sample :ref:`Broadcast<ref-IEC104maBroadcast>` node and the table listing all available attributes below.

.. code-block:: none

   <Broadcast GI="1" Reset="0" />

.. _docref-IEC104maBroadcastAttab:

.. field-list-table:: IEC 60870-5-104 Master Broadcast attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
.. include-file:: sections/Include/IEC10xma_BroadcastGI.rstinc "" ".. _ref-IEC104maBroadcastGI:" "Broadcast address is 65535"

.. include-file:: sections/Include/IEC10xma_BroadcastRP.rstinc "" ".. _ref-IEC101maBroadcastReset:" "Broadcast address is 65535"
