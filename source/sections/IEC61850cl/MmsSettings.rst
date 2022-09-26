.. _xmlelem-IEC61850clMms:

MMSSettings
^^^^^^^^^^^

Settings of the Manufacturing Message Specification (ISO9506) can be specified using attributes of :ref:`xmlelem-IEC61850clMms` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clMms`"

.. code-block:: none

   <MMSSettings ASN="3" PDUsize="2048" LogFlags="0x00"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clMms" "IEC61850 Client MMSSettings attributes" ":spec: |C{0.14}|C{0.18}|C{0.1}|S{0.58}|"

   * :attr:	:xmlattr:`ASN`
     :val:	1,3,5
     :def:	1
     :desc:	MMS version number as part of [:lemonobgtext:`Application-context-name`] field of the [:lemonobgtext:`AARQ APDU`].

   * :attr:	:xmlattr:`PDUsize`
     :val:	1024...65535
     :def:	32768
     :desc:	Protocol Data Unit (PDU) size in bytes.
		Value will be used for [:lemonobgtext:`Local Detail Calling`] field of the [:lemonobgtext:`Initiate-RequestPDU`].

.. include-file:: sections/Include/IEC61850_LogFlags.rstinc "" ":numref:`tabid-IEC61850clLogFlags`" "MMS"
