.. _docref-ModbusmaLinkSettingsAttr:

LinkSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`LinkSettings<ref-ModbusmaLinkSettings>` element node.

Please see sample :ref:`LinkSettings<ref-ModbusmaLinkSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <LinkSettings Frame="RTU" /> 

.. _docref-ModbusmaLinkSettingsAttab:

.. field-list-table:: Modbus Master LinkSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.22}|C{0.23}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     .. _ref-ModbusmaLinkSettingsFrame:
            
                :xmlref:`Frame`
     :val:      RTU*
     :desc:     Frame format of the Modbus messages. (default RTU) :inlinetip:`Please note frame format of all protocol instances sharing the hardware node must be the same.`
   

.. important:: \* Only ModbusRTU frame format is available in current release of leandc firmware, more formats to be added in the future.

