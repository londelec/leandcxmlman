.. _ref-IEC104maProtocolCfg:

ProtocolCfg group node
----------------------

Protocol-related settings of the IEC60870-5-104 controlling station (Master) communication protocol instance 
are configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC104maProtocolCfg>` group node. 

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC104maProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg> 
      <XMLSettings … />
      <TransportSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <ServiceSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Broadcast … />
      <Periodic … />
      <BufferSizes … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _docref-IEC104maProtocolCfgNotab:

.. field-list-table:: IEC 60870-5-104 Master ProtocolCfg element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Node
     :val,15:  Attributes
     :desc,75: Description
     
   * :attr:    .. _ref-IEC104maXMLSettings:
       
               :xmlref:`XMLSettings`
     :val:     See table :numref:`docref-IEC104maXMLSettingsAttab`
     :desc:    XML parse setting specification node. Refer to section :ref:`docref-IEC104maXMLSettingsAttr` for details.

   * :attr:    .. _ref-IEC104maTransportSettings:
       
               :xmlref:`TransportSettings`
     :val:     See table :numref:`docref-IEC104maTransportSettingsAttab`
     :desc:    Communication transport interface timeout and message window size configuration node. Refer to section :ref:`docref-IEC104maTransportSettingsAttr` for details.

   * :attr:    .. _ref-IEC104maCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`docref-IEC104maCommsSettingsAttab`
     :desc:    Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to section :ref:`docref-IEC104maCommsSettingsAttr` for details.

   * :attr:    .. _ref-IEC104maASDUSettings:
       
               :xmlref:`ASDUSettings`
     :val:     See table :numref:`docref-IEC104maASDUSettingsAttab`
     :desc:    Various application layer settings configuration node. Refer to section :ref:`docref-IEC104maASDUSettingsAttr` for details.

   * :attr: .. _ref-IEC104maServiceSettings:

            :xmlref:`ServiceSettings`
     :val:  See table :numref:`docref-IEC104maServiceSettingsAttab`
     :desc: Service settings configuration node. Refer to section :ref:`docref-IEC104maServiceSettingsAttr` for details.

   * :attr:    .. _ref-IEC104maTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`docref-IEC104maTimeoutsAttab`
     :desc:    Control command expiration timeout configuration node. Refer to section :ref:`docref-IEC104maTimeoutsAttr` for details.

   * :attr:    .. _ref-IEC104maTimeSettings:
       
               :xmlref:`TimeSettings`
     :val:     See table :numref:`docref-IEC104maTimeSettingsAttab`
     :desc:    Unique time settings (e.g. time zone) of particular protocol instance. Refer to section :ref:`docref-IEC104maTimeSettingsAttr` for details.

   * :attr:    .. _ref-IEC104maBroadcast:
       
               :xmlref:`Broadcast`
     :val:     See table :numref:`docref-IEC104maBroadcastAttab`
     :desc:    Broadcast or individual common address of ASDU (CAA) specification node. Refer to section :ref:`docref-IEC104maBroadcastAttr` for details.

   * :attr:    .. _ref-IEC104maPeriodic:
       
               :xmlref:`Periodic`
     :val:     See table :numref:`docref-IEC104maPeriodicAttab`
     :desc:    Periodically generated message configuration node. Refer to section :ref:`docref-IEC104maPeriodicAttr` for details.

   * :attr:    .. _ref-IEC104maBufferSizes:
       
               :xmlref:`BufferSizes`
     :val:     See table :numref:`docref-IEC104maBufferSizesAttab`
     :desc:    Various application layer buffer size configuration node. Refer to section :ref:`docref-IEC104maBufferSizesAttr` for details.

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _docref-IEC104maXMLSettingsAttr:" ":ref:`XMLSettings<ref-IEC104maXMLSettings>`" ".. _docref-IEC104maXMLSettingsAttab:" "IEC 60870-5-104 Master XMLSettings attributes"

.. include:: IEC104ma/TransportSettings.rst
.. include:: IEC104ma/CommsSettings.rst
.. include:: IEC104ma/ASDUSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _docref-IEC104maServiceSettingsAttr:" ":ref:`ServiceSettings<ref-IEC104maServiceSettings>`" ".. _docref-IEC104maServiceSettingsAttab:" "IEC 60870-5-104 Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC104maServiceEventMaskAttab:" ":numref:`docref-IEC104maServiceEventMaskAttab`" ":ref:`OfflineDelay<ref-IEC104maCommsSettingsOfflineDelay>`" ":ref:`PostOfflineDelay<ref-IEC104maCommsSettingsPostOfflineDelay>`"

.. include-file:: sections/Include/IEC10xma_Timeouts.rstinc "" ".. _docref-IEC104maTimeoutsAttr:" ":ref:`Timeouts<ref-IEC104maTimeouts>`" ".. _docref-IEC104maTimeoutsAttab:" "IEC 60870-5-104 Master Timeouts attributes"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc
.. include-file:: sections/Include/IEC60870_SelectTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _docref-IEC104maTimeSettingsAttr:" ":ref:`TimeSettings<ref-IEC104maTimeSettings>`" ".. _docref-IEC104maTimeSettingsAttab:" "IEC 60870-5-104 Master TimeSettings attributes" ".. _ref-IEC104maTimeSettingsTimeZone:"

.. include:: IEC104ma/Broadcast.rst
.. include:: IEC104ma/Periodic.rst

.. include-file:: sections/Include/IEC10xma_BufferSizes.rstinc "" ".. _docref-IEC104maBufferSizesAttr:" ":ref:`BufferSizes<ref-IEC104maBufferSizes>`" ".. _docref-IEC104maBufferSizesAttab:" "IEC 60870-5-104 Master BufferSizes attributes"
.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc

