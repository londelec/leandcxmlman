.. _docref-IEC104maTransportSettingsAttr:

TransportSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Protocol transport interface settings can be specified using attributes of :ref:`TransportSettings<ref-IEC104maTransportSettings>` element node.

Please see sample :ref:`TransportSettings<ref-IEC104maTransportSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <TransportSettings T0="30" T1="15" T2="10" T3="20" Kparam="12" Wparam="8" /> 

.. _docref-IEC104maTransportSettingsAttab:

.. field-list-table:: IEC 60870-5-104 Master TransportSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     :xmlref:`T0`
     :val:      1...65535
     :desc:     Timeout of connection establishment as per IEC 60870-5-104 standard. It is a delay in seconds for how long TCP socket should wait acknowledge from a peer station after sending connection establishment request (e.g. TCP SYN) (default 30 seconds)

.. include-file:: sections/Include/IEC60870_Transport.rstinc
