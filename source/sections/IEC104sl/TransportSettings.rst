.. _ref-IEC104slTransportSettings:

TransportSettings
^^^^^^^^^^^^^^^^^

Protocol transport interface settings such as timeout and message window sizes can be specified using attributes of :ref:`<ref-IEC104slTransportSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC104slTransportSettings>`"

.. code-block:: none

   <TransportSettings T1="15" T2="10" T3="20" Kparam="12" Wparam="8" />


.. _docref-IEC104slTransportSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC60870-5-104 Slave TransportSettings attributes" ":spec: |C{0.1}|C{0.12}|C{0.1}|S{0.68}|"

.. include-file:: sections/Include/IEC60870_Transport.rstinc
