.. _ref-IEC101slBufferSizes:

BufferSizes
^^^^^^^^^^^

Communication and event buffer sizes can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101slBufferSizes>`"

.. code-block:: none

   <BufferSizes DIEVmult="1.1" AIEVmult="2.1" ASDUTx="253" />

.. _docref-IEC101slBufferSizesAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-101 Slave BufferSizes attributes"

.. include-file:: sections/Include/hidden_BufferEVsize.rstinc "internal" ".. _ref-IEC101slBufferDIevsize:" ":xmlref:`DIEVsize`" "DI"

.. include-file:: sections/Include/hidden_BufferEVsize.rstinc "internal" ".. _ref-IEC101slBufferAIevsize:" ":xmlref:`AIEVsize`" "AI"

.. include-file:: sections/Include/IEC10xsl_BufferEVmult.rstinc "" ".. _ref-IEC101slBufferDImult:" ":xmlref:`DIEVmult`" "DI"

.. include-file:: sections/Include/IEC10xsl_BufferEVmult.rstinc "" ".. _ref-IEC101slBufferAImult:" ":xmlref:`AIEVmult`" "AI"

.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc "internal"

   * :attr:     :xmlref:`ASDUTx`
     :val:      14...253
     :def:      253 bytes
     :desc:     Application layer transmission buffer size in bytes.
		Maximal length of message transmitted over IEC60870-5-101 communication link is 255 bytes.
		Including the link layer framing, maximal size of the application layer is 253 bytes (if :ref:`<ref-IEC101slLinkSettingsLinkAddrSize>` is 1 byte) or 252 (if :ref:`<ref-IEC101slLinkSettingsLinkAddrSize>` is 2 bytes).
		This attribute is used to limit maximal length of a transmitted message.


