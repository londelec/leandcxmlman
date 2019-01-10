.. _ref-ModbusmaLinkSettings:

LinkSettings
^^^^^^^^^^^^

Link layer settings can be specified using attributes of :ref:`<ref-ModbusmaLinkSettings>` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-ModbusmaLinkSettings>`"

.. code-block:: none

   <LinkSettings Frame="RTU" />


.. _docref-ModbusmaLinkSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "Modbus Master LinkSettings attributes" ":spec: |C{0.12}|C{0.12}|C{0.1}|S{0.66}|"

   * :attr:     .. _ref-ModbusmaLinkSettingsFrame:

                :xmlref:`Frame`
     :val:      RTU*
     :def:      RTU
     :desc:     Frame format of the Modbus messages.
		:inlinetip:`Please note frame format of all protocol instances sharing the hardware node must be the same.`


.. important:: \* Only Modbus® RTU frame format is available in the current release of leandc firmware, more formats to be added in the future.

