.. _docref-IEC104slCommsSettingsAttr:

CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state change behavior and related delays can be specified using attributes of :ref:`CommsSettings<ref-IEC104slCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-IEC104slCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings OfflineDelay="10" StartupGIDelay="10" /> 

.. _docref-IEC104slCommsSettingsAttab:

.. field-list-table:: IEC 60870-5-104 Slave CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     :xmlref:`OfflineDelay`
     :val:      1...2\ :sup:`32`\  - 1
     :desc:     Offline delay in seconds before status of this protocol instance is changed to OFFLINE. Offline delay timer is activated after TCP socket has been closed. Default 0 seconds - station status will be changed to OFFLINE immediately after TCP socket has been closed by a remote host (default 0 seconds)

.. include-file:: sections/Include/IEC10xsl_StartupGIDelay.rstinc
