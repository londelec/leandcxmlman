.. _xmlelem-IEC104slTransport:

TransportSettings
^^^^^^^^^^^^^^^^^

Protocol transport interface settings such as timeout and message window sizes can be specified using attributes of :ref:`xmlelem-IEC104slTransport` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC104slTransport`"

.. code-block:: none

   <TransportSettings T1="15" T2="10" T3="20" Kparam="12" Wparam="8" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC104slTransport" "IEC60870-5-104 Slave TransportSettings attributes" ":spec: |C{0.1}|C{0.12}|C{0.1}|S{0.68}|"

.. include-file:: sections/Include/IEC60870_Transport.rstinc
