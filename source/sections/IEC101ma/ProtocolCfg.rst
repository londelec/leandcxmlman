.. _ref-IEC101maProtocolCfg:

ProtocolCfg group node
----------------------

Protocol-related settings of the IEC60870-5-101 controlling station (Master) communication protocol instance 
are configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC101maProtocolCfg>` group node. 

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC101maProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg> 
      <XMLSettings … />
      <LinkSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <ServiceSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Broadcast … />
      <Periodic … />
      <BufferSizes … />
      <Miscellaneous … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _docref-IEC101maProtocolCfgNotab:

.. field-list-table:: IEC 60870-5-101 Master ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Node
     :val,15:  Attributes
     :desc,75: Description
     
   * :attr:    .. _ref-IEC101maXMLSettings:
       
               :xmlref:`XMLSettings`
     :val:     See table :numref:`docref-IEC101maXMLSettingsAttab`
     :desc:    XML parse setting specification node. Refer to section :ref:`docref-IEC101maXMLSettingsAttr` for details.

   * :attr:    .. _ref-IEC101maLinkSettings:
       
               :xmlref:`LinkSettings`
     :val:     See table :numref:`docref-IEC101maLinkSettingsAttab`
     :desc:    Communication link layer timeout and control bit configuration node. Refer to section :ref:`docref-IEC101maLinkSettingsAttr` for details.

   * :attr:    .. _ref-IEC101maCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`docref-IEC101maCommsSettingsAttab`
     :desc:    Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to section :ref:`docref-IEC101maCommsSettingsAttr` for details.

   * :attr:    .. _ref-IEC101maASDUSettings:
       
               :xmlref:`ASDUSettings`
     :val:     See table :numref:`docref-IEC101maASDUSettingsAttab`
     :desc:    Various application layer settings configuration node. Refer to section :ref:`docref-IEC101maASDUSettingsAttr` for details.

   * :attr: .. _ref-IEC101maServiceSettings:
       
            :xmlref:`ServiceSettings`
     :val:  See table :numref:`docref-IEC101maServiceSettingsAttab`
     :desc: Service settings configuration node. Refer to section :ref:`docref-IEC101maServiceSettingsAttr` for details.

   * :attr:    .. _ref-IEC101maTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`docref-IEC101maTimeoutsAttab`
     :desc:    Control command expiration timeout configuration node. Refer to section :ref:`docref-IEC101maTimeoutsAttr` for details.

   * :attr:    .. _ref-IEC101maTimeSettings:
       
               :xmlref:`TimeSettings`
     :val:     See table :numref:`docref-IEC101maTimeSettingsAttab`
     :desc:    Unique time settings (e.g. time zone) of particular protocol instance. Refer to section :ref:`docref-IEC101maTimeSettingsAttr` for details.

   * :attr:    .. _ref-IEC101maBroadcast:
       
               :xmlref:`Broadcast`
     :val:     See table :numref:`docref-IEC101maBroadcastAttab`
     :desc:    Broadcast or individual common address of ASDU (CAA) specification node. Refer to section :ref:`docref-IEC101maBroadcastAttr` for details.

   * :attr:    .. _ref-IEC101maPeriodic:
       
               :xmlref:`Periodic`
     :val:     See table :numref:`docref-IEC101maPeriodicAttab`
     :desc:    Periodically generated message configuration node. Refer to section :ref:`docref-IEC101maPeriodicAttr` for details.

   * :attr:    .. _ref-IEC101maBufferSizes:
       
               :xmlref:`BufferSizes`
     :val:     See table :numref:`docref-IEC101maBufferSizesAttab`
     :desc:    Various application layer buffer size configuration node. Refer to section :ref:`docref-IEC101maBufferSizesAttr` for details.

   * :attr:    .. _ref-IEC101maMiscellaneous:
       
               :xmlref:`Miscellaneous`
     :val:     See table :numref:`docref-IEC101maMiscellaneousAttab`
     :desc:    Miscellaneous and project-specific setting configuration node. Refer to section :ref:`docref-IEC101maMiscellaneousAttr` for details.

.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _docref-IEC101maXMLSettingsAttr:" ":ref:`XMLSettings<ref-IEC101maXMLSettings>`" ".. _docref-IEC101maXMLSettingsAttab:" "IEC 60870-5-101 Master XMLSettings attributes"

.. include:: IEC101ma/LinkSettings.rst
.. include:: IEC101ma/CommsSettings.rst
.. include:: IEC101ma/ASDUSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _docref-IEC101maServiceSettingsAttr:" ":ref:`ServiceSettings<ref-IEC101maServiceSettings>`" ".. _docref-IEC101maServiceSettingsAttab:" "IEC 60870-5-101 Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC101maServiceEventMaskAttab:" ":numref:`docref-IEC101maServiceEventMaskAttab`" ":ref:`OfflineDelay<ref-IEC101maCommsSettingsOfflineDelay>`" ":ref:`PostOfflineDelay<ref-IEC101maCommsSettingsPostOfflineDelay>`"

.. include-file:: sections/Include/IEC10xma_Timeouts.rstinc "" ".. _docref-IEC101maTimeoutsAttr:" ":ref:`Timeouts<ref-IEC101maTimeouts>`" ".. _docref-IEC101maTimeoutsAttab:" "IEC 60870-5-101 Master Timeouts attributes"
.. include-file:: sections/Include/ma_TimeoutsAppCmd.rstinc
.. include-file:: sections/Include/IEC60870_SelectTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _docref-IEC101maTimeSettingsAttr:" ":ref:`TimeSettings<ref-IEC101maTimeSettings>`" ".. _docref-IEC101maTimeSettingsAttab:" "IEC 60870-5-101 Master TimeSettings attributes" ".. _ref-IEC101maTimeSettingsTimeZone:"

.. include:: IEC101ma/Broadcast.rst
.. include:: IEC101ma/Periodic.rst

.. include-file:: sections/Include/IEC10xma_BufferSizes.rstinc "" ".. _docref-IEC101maBufferSizesAttr:" ":ref:`BufferSizes<ref-IEC101maBufferSizes>`" ".. _docref-IEC101maBufferSizesAttab:" "IEC 60870-5-101 Master BufferSizes attributes"
.. include-file:: sections/Include/IEC60870_DOBufferSize.rstinc

.. include:: IEC101ma/Miscellaneous.rst
