
.. _ref-IEC104slProtocolCfg:

ProtocolCfg group node
----------------------

Protocol-related settings of the IEC60870-5-104 controlled station (Slave) communication protocol instance are 
configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC104slProtocolCfg>` group node. 

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC104slProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg>
      <XMLSettings … />
      <TransportSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <ServiceSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Periodic … />
      <BufferSizes … />
      <Miscellaneous … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _docref-IEC104slProtocolCfgNotab:

.. field-list-table:: IEC 60870-5-104 Slave ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Node
     :val,15:  Attributes
     :desc,75: Description
     
   * :attr:    .. _ref-IEC104slXMLSettings:
       
               :xmlref:`XMLSettings`
     :val:     See table :numref:`docref-IEC104slXMLSettingsAttab`
     :desc:    XML parse setting specification node. Refer to section :ref:`docref-IEC104slXMLSettingsAttr` for details.

   * :attr:    .. _ref-IEC104slTransportSettings:
       
               :xmlref:`TransportSettings`
     :val:     See table :numref:`docref-IEC104slTransportSettingsAttab`
     :desc:    Communication transport interface timeout and message window size configuration node. Refer to section :ref:`docref-IEC104slTransportSettingsAttr` for details.

   * :attr:    .. _ref-IEC104slCommsSettings:
       
               :xmlref:`CommsSettings`
     :val:     See table :numref:`docref-IEC104slCommsSettingsAttab`
     :desc:    Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to section :ref:`docref-IEC104slCommsSettingsAttr` for details.

   * :attr:    .. _ref-IEC104slASDUSettings:
       
               :xmlref:`ASDUSettings`
     :val:     See table :numref:`docref-IEC104slASDUSettingsAttab`
     :desc:    Various application layer settings configuration node. Refer to section :ref:`docref-IEC104slASDUSettingsAttr` for details.

   * :attr: .. _ref-IEC104slServiceSettings:
       
            :xmlref:`ServiceSettings`
     :val:  See table :numref:`docref-IEC104slServiceSettingsAttab`
     :desc: Service settings configuration node. Refer to section :ref:`docref-IEC104slServiceSettingsAttr` for details.

   * :attr:    .. _ref-IEC104slTimeouts:
       
               :xmlref:`Timeouts`
     :val:     See table :numref:`docref-IEC104slTimeoutsAttab`
     :desc:    Control command expiration timeout configuration node. Refer to section :ref:`docref-IEC104slTimeoutsAttr` for details.

   * :attr:    .. _ref-IEC104slTimeSettings:
       
               :xmlref:`TimeSettings`
     :val:     See table :numref:`docref-IEC104slTimeSettingsAttab`
     :desc:    Unique time settings (e.g. time zone) of particular protocol instance. Refer to section :ref:`docref-IEC104slTimeSettingsAttr` for details.

   * :attr:    .. _ref-IEC104slPeriodic:
       
               :xmlref:`Periodic`
     :val:     See table :numref:`docref-IEC104slPeriodicAttab`
     :desc:    Periodically generated message configuration node. Refer to section :ref:`docref-IEC104slPeriodicAttr` for details.

   * :attr:    .. _ref-IEC104slBufferSizes:
       
               :xmlref:`BufferSizes`
     :val:     See table :numref:`docref-IEC104slBufferSizesAttab`
     :desc:    Various application layer buffer size configuration node. Refer to section :ref:`docref-IEC104slBufferSizesAttr` for details.

   * :attr:    .. _ref-IEC104slMiscellaneous:
       
               :xmlref:`Miscellaneous`
     :val:     See table :numref:`docref-IEC104slMiscellaneousAttab`
     :desc:    Miscellaneous and project-specific setting configuration node. Refer to section :ref:`docref-IEC104slMiscellaneousAttr` for details.


.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _docref-IEC104slXMLSettingsAttr:" ":ref:`XMLSettings<ref-IEC104slXMLSettings>`" ".. _docref-IEC104slXMLSettingsAttab:" "IEC 60870-5-104 Slave XMLSettings attributes"

.. include:: IEC104sl/TransportSettings.rst
.. include:: IEC104sl/CommsSettings.rst
.. include:: IEC104sl/ASDUSettings.rst

.. include-file:: sections/Include/IEC10xsl_ServiceSettings.rstinc "" ".. _docref-IEC104slServiceSettingsAttr:" ":ref:`ServiceSettings<ref-IEC104slServiceSettings>`" ".. _docref-IEC104slServiceSettingsAttab:" "IEC 60870-5-104 Slave ServiceSettings attributes" ":numref:`docref-IEC104slServiceQualityBitsAttab`"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC104slServiceEventMaskAttab:" ":numref:`docref-IEC104slServiceEventMaskAttab`" ":ref:`OfflineDelay<ref-IEC101maCommsSettingsOfflineDelay>`" ":ref:`PostOfflineDelay<ref-IEC101maCommsSettingsPostOfflineDelay>`"
.. include-file:: sections/Include/IEC60870_QualityBits.rstinc "" ".. _docref-IEC104slServiceQualityBitsAttab:" 

.. include-file:: sections/Include/IEC10xsl_Timeouts.rstinc "" ".. _docref-IEC104slTimeoutsAttr:" ":ref:`Timeouts<ref-IEC104slTimeouts>`" ".. _docref-IEC104slTimeoutsAttab:" "IEC 60870-5-104 Slave Timeouts attributes"
.. include-file:: sections/Include/IEC60870_SelectTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _docref-IEC104slTimeSettingsAttr:" ":ref:`TimeSettings<ref-IEC104slTimeSettings>`" ".. _docref-IEC104slTimeSettingsAttab:" "IEC 60870-5-104 Slave TimeSettings attributes" ".. _ref-IEC104slTimeSettingsTimeZone:"
.. include-file:: sections/Include/IEC10xsl_Periodic.rstinc "" ".. _docref-IEC104slPeriodicAttr:" ":ref:`Periodic<ref-IEC104slPeriodic>`" ".. _docref-IEC104slPeriodicAttab:" "IEC 60870-5-104 Slave Periodic attributes"

.. include:: IEC104sl/BufferSizes.rst
.. include:: IEC104sl/Miscellaneous.rst
