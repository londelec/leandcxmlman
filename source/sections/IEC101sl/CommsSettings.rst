.. _docref-IEC101slCommsSettingsAttr:

CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state change behavior and related delays can be specified using attributes of :ref:`CommsSettings<ref-IEC101slCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-IEC101slCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings OfflineDelay="120" StartupGIDelay="10" />

.. _docref-IEC101slCommsSettingsAttab:

.. field-list-table:: IEC 60870-5-101 Slave CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     :xmlref:`OfflineDelay`
     :val:      1...2\ :sup:`32`\  - 1
     :desc:     Delay in seconds before resetting the link if there is no request from Master station. Reset remote link message is required after communication loss exceeding configured offline delay in order to restart communication (default 60 seconds)

.. include-file:: sections/Include/IEC10xsl_StartupGIDelay.rstinc

