.. _xmlelem-IEC104slBufferSizes:

BufferSizes
^^^^^^^^^^^

Communication buffer sizes can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC104slBufferSizes`"

.. code-block:: none

   <BufferSizes DIEVmult="1.1" AIEVmult="2.1" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC104slBufferSizes" "IEC60870-5-104 Slave BufferSizes attributes" ":spec: |C{0.1}|C{0.1}|C{0.1}|S{0.7}|"

.. include-file:: sections/Include/hidden_BufferEVsize.rstinc "internal" ":xmlattr:`DIEVsize`" "DI"

.. include-file:: sections/Include/hidden_BufferEVsize.rstinc "internal" ":xmlattr:`AIEVsize`" "AI"

.. include-file:: sections/Include/IEC10xsl_BufferEVmult.rstinc "" ":xmlattr:`DIEVmult`" "DI"

.. include-file:: sections/Include/IEC10xsl_BufferEVmult.rstinc "" ":xmlattr:`AIEVmult`" "AI"

.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc "internal"
