.. _ref-IEC103maProtocolCfg:

ProtocolCfg group node
----------------------

Protocol-related settings of the IEC60870-5-103 controlling station (Master) communication protocol instance 
are configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC103maProtocolCfg>` group node. 

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC103maProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg> 
      <CommsSettings … />
      <ASDUSettings … />
      <ServiceSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Broadcast … />
      <Periodic … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _docref-IEC103maProtocolCfgNotab:

.. field-list-table:: IEC 60870-5-103 Master ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Node
     :val,15:  Attributes
     :desc,75: Description

   * :attr:    .. _ref-IEC103maCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`docref-IEC103maCommsSettingsAttab`
     :desc:    Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to section :ref:`docref-IEC103maCommsSettingsAttr` for details.

   * :attr:    .. _ref-IEC103maASDUSettings:
       
               :xmlref:`ASDUSettings`
     :val:     See table :numref:`docref-IEC103maASDUSettingsAttab`
     :desc:    Various application layer settings configuration node. Refer to section :ref:`docref-IEC103maASDUSettingsAttr` for details.

   * :attr: .. _ref-IEC103maServiceSettings:
       
            :xmlref:`ServiceSettings`
     :val:  See table :numref:`docref-IEC103maServiceSettingsAttab`
     :desc: Service settings configuration node. Refer to section :ref:`docref-IEC103maServiceSettingsAttr` for details.

   * :attr:    .. _ref-IEC103maTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`docref-IEC103maTimeoutsAttab`
     :desc:    Control command expiration timeout configuration node. Refer to section :ref:`docref-IEC103maTimeoutsAttr` for details.

   * :attr:    .. _ref-IEC103maTimeSettings:
       
               :xmlref:`TimeSettings`
     :val:     See table :numref:`docref-IEC103maTimeSettingsAttab`
     :desc:    Unique time settings (e.g. time zone) of particular protocol instance. Refer to section :ref:`docref-IEC103maTimeSettingsAttr` for details.

   * :attr:    .. _ref-IEC103maBroadcast:
       
               :xmlref:`Broadcast`
     :val:     See table :numref:`docref-IEC103maBroadcastAttab`
     :desc:    Broadcast or individual common address of ASDU (CAA) specification node. Refer to section :ref:`docref-IEC103maBroadcastAttr` for details.

   * :attr:    .. _ref-IEC103maPeriodic:
       
               :xmlref:`Periodic`
     :val:     See table :numref:`docref-IEC103maPeriodicAttab`
     :desc:    Periodic command generation interval specification node. Refer to section :ref:`docref-IEC103maPeriodicAttr` for details.

.. include:: IEC103ma/CommsSettings.rst
.. include:: IEC103ma/ASDUSettings.rst

.. include-file:: sections/Include/ma_ServiceSettings.rstinc "" ".. _docref-IEC103maServiceSettingsAttr:" ":ref:`ServiceSettings<ref-IEC103maServiceSettings>`" ".. _docref-IEC103maServiceSettingsAttab:" "IEC 60870-5-103 Master ServiceSettings attributes"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC103maServiceEventMaskAttab:" ":numref:`docref-IEC103maServiceEventMaskAttab`" ":ref:`OfflineDelay<ref-IEC103maCommsSettingsOfflineDelay>`" ":ref:`PostOfflineDelay<ref-IEC103maCommsSettingsPostOfflineDelay>`"

.. include:: IEC103ma/Timeouts.rst
.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _docref-IEC103maTimeSettingsAttr:" ":ref:`TimeSettings<ref-IEC103maTimeSettings>`" ".. _docref-IEC103maTimeSettingsAttab:" "IEC 60870-5-103 Master TimeSettings attributes" ".. _ref-IEC103maTimeSettingsTimeZone:"

.. include:: IEC103ma/Broadcast.rst
.. include:: IEC103ma/Periodic.rst
