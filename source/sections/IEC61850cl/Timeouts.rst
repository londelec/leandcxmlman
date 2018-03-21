.. _ref-IEC61850clTimeouts:

Timeouts
^^^^^^^^

Command processing timeouts are specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clTimeouts>`"

.. code-block:: none

   <Timeouts Application="30" Command="10" Select="30" Response="5"/>


.. _docref-IEC61850clTimeoutsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client Timeouts attributes"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc
.. include-file:: sections/Include/SelectTimeout.rstinc

   * :attr:     :xmlref:`Response`
     :val:      1...2\ :sup:`32`\  - 1
     :def:      5 sec
     :desc:     Response timeout in seconds.
		Connection to IED will be closed if no response to a sent message has been received within this timeout.

