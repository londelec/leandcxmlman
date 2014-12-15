
.. _ref-ModbusmaHardcodedAttributes:

Hardcoded attributes
^^^^^^^^^^^^^^^^^^^^^^^

Hardcoded device type can be specified using attributes of :ref:`Hardcoded<ref-ModbusmaHardcoded>` element node.

Please see sample :ref:`Hardcoded<ref-ModbusmaHardcoded>` node and the table listing all available attributes below.

.. code-block:: none

   <Hardcoded Type="BCDI16" /> 

.. _ref-ModbusmaHardcodedAttributesTab:

.. field-list-table:: Modbus Master Hardcoded attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.22}|C{0.23}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     .. _ref-ModbusmaHardcodedType:
            
                :xmlref:`Type`
     :val:      See table :numref:`ref-ModbusmaHardcodedTypeValues`
     :desc:     Predefined type of the Modbus device. Messages and communication sequences are hardcoded for devices of these types.
   


Hardcoded types
^^^^^^^^^^^^^^^

.. _ref-ModbusmaHardcodedTypeValues:

.. field-list-table:: Modbus Master Hardcoded Device Types
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: Type
     :desc,90: Description

   * :attr:    BCDI16
     :desc:    Brainchild Digital Input (16) module DI16. Number of information objects automatically created for this device: DI=16, AI=0, DO=0

   * :attr:    BCAIIS16
     :desc:    Brainchild isolated Analog Input (8) module AIIS8. Number of information objects automatically created for this device: DI=0, AI=8, DO=0

   * :attr:    LEDOM16
     :desc:    Londelec Digital Output (16) module DOM16. Number of information objects automatically created for this device: DI=0, AI=0, DO=16

   * :attr:    Other
     :desc:    Undefined, none of hardcoded device types will be used
   
