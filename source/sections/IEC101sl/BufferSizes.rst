.. _xmlelem-IEC101slBufferSizes:

BufferSizes
^^^^^^^^^^^

Communication and event buffer sizes can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC101slBufferSizes`"

.. code-block:: none

   <BufferSizes DIEVmult="1.1" AIEVmult="2.1" ASDUTx="253" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC101slBufferSizes" "IEC60870-5-101 Slave BufferSizes attributes" ":spec: |C{0.1}|C{0.1}|C{0.1}|S{0.7}|"

.. include-file:: sections/Include/hidden_BufferEVsize.rstinc "internal" ":xmlattr:`DIEVsize`" "DI"

.. include-file:: sections/Include/hidden_BufferEVsize.rstinc "internal" ":xmlattr:`AIEVsize`" "AI"

.. include-file:: sections/Include/IEC10xsl_BufferEVmult.rstinc "" ":xmlattr:`DIEVmult`" "DI"

.. include-file:: sections/Include/IEC10xsl_BufferEVmult.rstinc "" ":xmlattr:`AIEVmult`" "AI"

.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc "internal"

   * :attr:	:xmlattr:`ASDUTx`
     :val:	14...253
     :def:	253 bytes
     :desc:	Application layer transmission buffer size in bytes.
		Maximal length of message transmitted over IEC60870-5-101 communication link is 255 bytes.
		Including the link layer framing, maximal size of the application layer is 253 bytes (if :ref:`xmlattr-IEC101slLinkLinkAddrSize` is 1 byte) or 252 (if :ref:`xmlattr-IEC101slLinkLinkAddrSize` is 2 bytes).
		This attribute is used to limit maximal length of a transmitted message.


