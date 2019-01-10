.. _ref-IEC101maBroadcast:

Broadcast
^^^^^^^^^

Broadcast common address of ASDU (CAA) usage for various commands can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101maBroadcast>`"

.. code-block:: none

   <Broadcast GI="1" TimeSync="0" Reset="0"/>


.. _docref-IEC101maBroadcastAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Master Broadcast attributes" ":spec: |C{0.12}|C{0.1}|C{0.1}|S{0.68}|"

.. include-file:: sections/Include/IEC10xma_BroadcastGI.rstinc "" ".. _ref-IEC101maBroadcastGI:" "Broadcast address is 255 (if :ref:`<ref-IEC101maASDUSettingsCAASize>` is 1 byte) or 65535 (if :ref:`<ref-IEC101maASDUSettingsCAASize>` is 2 bytes)"

.. include-file:: sections/Include/IEC10xma_BroadcastCS.rstinc "" ".. _ref-IEC101maBroadcastTimeSync:" "Broadcast address is 255 (if :ref:`<ref-IEC101maLinkSettingsLinkAddrSize>` is 1 byte) or 65535 (if :ref:`<ref-IEC101maLinkSettingsLinkAddrSize>` is 2 bytes)"

.. include-file:: sections/Include/IEC10xma_BroadcastRP.rstinc "" ".. _ref-IEC101maBroadcastReset:" "Broadcast address is 255 (if :ref:`<ref-IEC101maASDUSettingsCAASize>` is 1 byte) or 65535 (if :ref:`<ref-IEC101maASDUSettingsCAASize>` is 2 bytes)"
