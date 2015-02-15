.. _docref-IEC101slBufferSizesAttr:

BufferSizes attributes
^^^^^^^^^^^^^^^^^^^^^^

Various communication buffer sizes and can be specified using attributes of :ref:`BufferSizes<ref-IEC101slBufferSizes>` element node.

Please see sample :ref:`BufferSizes<ref-IEC101slBufferSizes>` node and the table listing all available attributes below.

.. code-block:: none

   <BufferSizes DIEVsize="1024" AIEVsize="1024" DIEVmult="1.1" AIEVmult="2.1" DO="1" ASDUTx="253" />

.. include-file:: sections/Include/IEC10xsl_BufferSizes.rstinc "" ".. _docref-IEC101slBufferSizesAttab:" "IEC 60870-5-101 Slave BufferSizes attributes"

.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc

   * :attr:     :xmlref:`ASDUTx`
     :val:      14...253
     :desc:     Application layer transmission buffer size in bytes. Maximal length of message transmitted over IEC 60870-5-101 communication link is 255 bytes. Considering the link layer framing, maximal size of the application layer is 253 bytes (if size of the link address is 1 byte) or 252 (if size of the link address is 2 bytes). This attribute allows to limit maximal length of a transmitted message (default value 253)


