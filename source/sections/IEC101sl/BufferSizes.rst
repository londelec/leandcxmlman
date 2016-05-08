.. _ref-IEC101slBufferSizes:

BufferSizes
^^^^^^^^^^^

Communication and event buffer sizes can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC101slBufferSizes>`"

.. code-block:: none

   <BufferSizes DIEVsize="1024" AIEVsize="1024" DIEVmult="1.1" AIEVmult="2.1" DO="1" ASDUTx="253" />


.. include-file:: sections/Include/IEC10xsl_BufferSizes.rstinc "" ".. _docref-IEC101slBufferSizesAttab:" "IEC60870-5-101 Slave BufferSizes attributes"

.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc

   * :attr:     :xmlref:`ASDUTx`
     :val:      14...253
     :def:      253 bytes
     :desc:     Application layer transmission buffer size in bytes.
		Maximal length of message transmitted over IEC60870-5-101 communication link is 255 bytes.
		Including the link layer framing, maximal size of the application layer is 253 bytes (if :ref:`<ref-IEC101slLinkSettingsLinkAddrSize>` is 1 byte) or 252 (if :ref:`<ref-IEC101slLinkSettingsLinkAddrSize>` is 2 bytes).
		This attribute is used to limit maximal length of a transmitted message.


