.. _ref-IEC101slProtocolCfg:

ProtocolCfg group node
----------------------

Protocol settings of the IEC60870-5-101 controlled station (Slave) communication protocol instance are 
configured using various child element nodes under :ref:`ProtocolCfg<ref-IEC101slProtocolCfg>` group node.

.. important:: It is essential to keep element nodes in the listed order otherwise it will affect the XML file validation.

Please see sample :ref:`ProtocolCfg<ref-IEC101slProtocolCfg>` group node and the table listing all available child element nodes below.

.. code-block:: none

   <ProtocolCfg>
      <XMLSettings … />
      <LinkSettings … />
      <CommsSettings … />
      <ASDUSettings … />
      <ServiceSettings … />
      <Timeouts … />
      <TimeSettings … />
      <Periodic … />
      <BufferSizes … />
   </ProtocolCfg>

.. tip:: All element nodes are optional, default values will be used for attributes of omitted nodes.

.. _docref-IEC101slProtocolCfgNotab:

.. field-list-table:: IEC 60870-5-101 Slave ProtocolCfg child element nodes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Node
     :val,15:  Attributes
     :desc,75: Description
     
   * :attr: .. _ref-IEC101slXMLSettings:
       
            :xmlref:`XMLSettings`
     :val:  See table :numref:`docref-IEC101slXMLSettingsAttab`
     :desc: XML parse setting specification node. Refer to section :ref:`docref-IEC101slXMLSettingsAttr` for details.

   * :attr: .. _ref-IEC101slLinkSettings:
       
            :xmlref:`LinkSettings`
     :val:  See table :numref:`docref-IEC101slLinkSettingsAttab`
     :desc: Communication link layer timeout and control bit configuration node. Refer to section :ref:`docref-IEC101slLinkSettingsAttr` for details.

   * :attr: .. _ref-IEC101slCommsSettings:
       
            :xmlref:`CommsSettings`
     :val:  See table :numref:`docref-IEC101slCommsSettingsAttab`
     :desc: Communication status (e.g. online and offline) change behavior and related delay configuration node. Refer to section :ref:`docref-IEC101slCommsSettingsAttr` for details.

   * :attr: .. _ref-IEC101slASDUSettings:
       
            :xmlref:`ASDUSettings`
     :val:  See table :numref:`docref-IEC101slASDUSettingsAttab`
     :desc: Various application layer settings configuration node. Refer to section :ref:`docref-IEC101slASDUSettingsAttr` for details.

   * :attr: .. _ref-IEC101slServiceSettings:
       
            :xmlref:`ServiceSettings`
     :val:  See table :numref:`docref-IEC101slServiceSettingsAttab`
     :desc: Service settings configuration node. Refer to section :ref:`docref-IEC101slServiceSettingsAttr` for details.

   * :attr: .. _ref-IEC101slTimeouts:
       
            :xmlref:`Timeouts`
     :val:  See table :numref:`docref-IEC101slTimeoutsAttab`
     :desc: Control command expiration timeout configuration node. Refer to section :ref:`docref-IEC101slTimeoutsAttr` for details.

   * :attr: .. _ref-IEC101slTimeSettings:
       
            :xmlref:`TimeSettings`
     :val:  See table :numref:`docref-IEC101slTimeSettingsAttab`
     :desc: Unique time settings (e.g. time zone) of particular protocol instance. Refer to section :ref:`docref-IEC101slTimeSettingsAttr` for details.

   * :attr: .. _ref-IEC101slPeriodic:
       
            :xmlref:`Periodic`
     :val:  See table :numref:`docref-IEC101slPeriodicAttab`
     :desc: Periodically generated message configuration node. Refer to section :ref:`docref-IEC101slPeriodicAttr` for details.

   * :attr: .. _ref-IEC101slBufferSizes:
       
            :xmlref:`BufferSizes`
     :val:  See table :numref:`docref-IEC101slBufferSizesAttab`
     :desc: Various application layer buffer size configuration node. Refer to section :ref:`docref-IEC101slBufferSizesAttr` for details.


.. include-file:: sections/Include/IEC60870_XMLSettings.rstinc "" ".. _docref-IEC101slXMLSettingsAttr:" ":ref:`XMLSettings<ref-IEC101slXMLSettings>`" ".. _docref-IEC101slXMLSettingsAttab:" "IEC 60870-5-101 Slave XMLSettings attributes"

.. include:: IEC101sl/LinkSettings.rst
.. include:: IEC101sl/CommsSettings.rst
.. include:: IEC101sl/ASDUSettings.rst

.. include-file:: sections/Include/IEC10xsl_ServiceSettings.rstinc "" ".. _docref-IEC101slServiceSettingsAttr:" ":ref:`ServiceSettings<ref-IEC101slServiceSettings>`" ".. _docref-IEC101slServiceSettingsAttab:" "IEC 60870-5-101 Slave ServiceSettings attributes" ":numref:`docref-IEC101slServiceQualityBitsAttab`"
.. include-file:: sections/Include/EventMask.rstinc "" ".. _docref-IEC101slServiceEventMaskAttab:" ":numref:`docref-IEC101slServiceEventMaskAttab`" ":ref:`OfflineDelay<ref-IEC101maCommsSettingsOfflineDelay>`" ":ref:`PostOfflineDelay<ref-IEC101maCommsSettingsPostOfflineDelay>`"
.. include-file:: sections/Include/IEC60870_QualityBits.rstinc "" ".. _docref-IEC101slServiceQualityBitsAttab:" 

.. include-file:: sections/Include/IEC10xsl_Timeouts.rstinc "" ".. _docref-IEC101slTimeoutsAttr:" ":ref:`Timeouts<ref-IEC101slTimeouts>`" ".. _docref-IEC101slTimeoutsAttab:" "IEC 60870-5-101 Slave Timeouts attributes"
.. include-file:: sections/Include/IEC60870_SelectTimeout.rstinc

.. include-file:: sections/Include/IEC60870_TimeSettings.rstinc "" ".. _docref-IEC101slTimeSettingsAttr:" ":ref:`TimeSettings<ref-IEC101slTimeSettings>`" ".. _docref-IEC101slTimeSettingsAttab:" "IEC 60870-5-101 Slave TimeSettings attributes" ".. _ref-IEC101slTimeSettingsTimeZone:"
.. include-file:: sections/Include/IEC10xsl_Periodic.rstinc "" ".. _docref-IEC101slPeriodicAttr:" ":ref:`Periodic<ref-IEC101slPeriodic>`" ".. _docref-IEC101slPeriodicAttab:" "IEC 60870-5-101 Slave Periodic attributes"

.. include:: IEC101sl/BufferSizes.rst
