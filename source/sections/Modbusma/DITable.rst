
.. _ref-ModbusmaDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-ModbusmaDI>` and child element nodes :ref:`DI<ref-ModbusmaDI>` are used to create DI information objects to receive status 
information from downstream outstation. Each created DI information object can be used as source of 
information for any DI information object defined in IO table of the Slave protocol instances. If used as a source, 
status information received from an outstation will be forwarded to DI information object of the Slave protocol 
instance and then to the upstream Master station. Please refer to
section :ref:`docref-IEC10xslDITable` for more information on how to use DI information object as a source.

.. tip:: \ :ref:`DITable<ref-ModbusmaDI>` group and :ref:`DI<ref-ModbusmaDI>` element nodes are optional if hardcoded Modbus device :ref:`Type<ref-ModbusmaHardcodedType>` is used. DI information objects will be automatically initialized for these devices.

Please see sample :ref:`DITable<ref-ModbusmaDI>` group node and :ref:`DI<ref-ModbusmaDI>` child element nodes below. There are 5 DI information 
objects configured using 4 :ref:`DI<ref-ModbusmaDI>` element nodes.

.. code-block:: none

   <DITable>
	<DI Index="0" qualifier="0x00"/>
	<DI Index="1" qualifier="0x10"/>
	<DI Index="2" qualifier="0x10"/>
	<DI Index="3" qualifier="0x00" Total="2"/>
   </DITable>
   
Please see sample :ref:`DI<ref-ModbusmaDI>` element node below listing all available attributes.
            
.. code-block:: none
            
   <DI  Index="0"
	qualifier="0"
	Total="2"
	Name="Transducer mode" />
      
.. tip:: Attributes of the :ref:`DI<ref-ModbusmaDI>` element node can be arranged in any order, it will not affect XML file validation.

DI attributes
^^^^^^^^^^^^^

.. _ref-ModbusmaDIAttributes:

.. field-list-table:: Modbus Master DI attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-ModbusmaDIIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the DI object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-ModbusmaDIqualifier:
   
               :xmlref:`qualifier`
     :val:     0...255
     :desc:    Internal object qualifier to enable customized data processing. (default value 0) :inlinetip:`Attribute is not implemented currently and reserved for future use.`

   * :attr:    .. _ref-ModbusmaDITotal:
   
               :xmlref:`Total`
     :val:     1...255
     :desc:    Sequence of identical DI objects. Attribute is used to create sequence of information objects with consecutive :ref:`Index<ref-ModbusmaDIIndex>` attributes. This eliminates the need to create individual :ref:`DI<ref-ModbusmaDI>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`DI<ref-ModbusmaDI>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-ModbusmaDIName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

