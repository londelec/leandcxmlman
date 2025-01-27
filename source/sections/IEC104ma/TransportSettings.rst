.. _xmlelem-IEC104maTransport:

TransportSettings
^^^^^^^^^^^^^^^^^

Protocol transport interface settings such as timeouts and message window sizes can be specified using attributes of :ref:`xmlelem-IEC104maTransport` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC104maTransport`"

.. code-block:: none

   <TransportSettings T0="30" T1="15" T2="10" T3="20" Kparam="12" Wparam="8" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC104maTransport" "IEC60870-5-104 Master TransportSettings attributes" ":spec: |C{0.1}|C{0.12}|C{0.1}|S{0.68}|"

   * :attr:	:xmlattr:`T0`
     :val:	1...65535
     :def:	30 sec
     :desc:	Timeout of connection establishment as per IEC60870-5-104 standard.
		It is a delay in seconds for how long TCP socket should wait acknowledge from a peer station after sending connection establishment request (e.g. TCP SYN)

.. include-file:: sections/Include/IEC60870_Transport.rstinc
