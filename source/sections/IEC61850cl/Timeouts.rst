.. _xmlelem-IEC61850clTimeouts:

Timeouts
^^^^^^^^

Command processing timeouts are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clTimeouts`"

.. code-block:: none

   <Timeouts Application="30" Command="10" Select="30" Response="5"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clTimeouts" "IEC61850 Client Timeouts attributes" ":spec: |C{0.12}|C{0.1}|C{0.1}|S{0.68}|"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc ""
.. include-file:: sections/Include/SelectTimeout.rstinc ""

   * :attr:	:xmlattr:`Response`
     :val:	|uint32range|
     :def:	5 sec
     :desc:	Response timeout in seconds.
		Connection to IED will be closed if no response to a sent message has been received within this timeout.

