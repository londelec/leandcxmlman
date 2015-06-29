
.. _ref-ModbusmaDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-ModbusmaDO>` and child element nodes :ref:`DO<ref-ModbusmaDO>` are used to create DO information objects to send control 
commands to downstream outstation. Each created DO information object can be used as a destination for 
any DO information object defined in IO table of the Slave protocol instances. If used as a destination, 
procedure is as follows: Slave protocol instance receives control command from the upstream Master station 
and forwards to this destination DO information object. Then current communication protocol instance prepares and 
sends command to the outstation based on the DO information object settings. Please refer to the 
section :ref:`docref-IEC10xslDOTable` for more information on how to use DO information object as a destination.

.. tip:: \ :ref:`DOTable<ref-ModbusmaDO>` group and :ref:`DO<ref-ModbusmaDO>` element nodes are optional if hardcoded Modbus device :ref:`Type<ref-ModbusmaHardcodedType>` is used. DO information objects will be automatically initialized for these devices.

Please see sample :ref:`DOTable<ref-ModbusmaDO>` group node and :ref:`DO<ref-ModbusmaDO>` child element nodes below. There are 5 DO information 
objects configured using 4 :ref:`DO<ref-ModbusmaDO>` element nodes.

.. code-block:: none

   <DOTable>
	<DO Index="0" Qualifier="0x00"/>
	<DO Index="1" Qualifier="0x10"/>
	<DO Index="2" Qualifier="0x10"/>
	<DO Index="3" Qualifier="0x00" Total="2"/>
   </DOTable>

Please see sample :ref:`DO<ref-ModbusmaDO>` element node below listing all available attributes.

.. code-block:: none

   <DO Index="0" Qualifier="0x00" PulseDuration="500" Total="2" Name="Transducer mode" />

.. tip:: Attributes of the :ref:`DO<ref-ModbusmaDO>` element node can be arranged in any order, it will not affect XML file validation.         

DO attributes
^^^^^^^^^^^^^

.. _ref-ModbusmaDOAttributes:

.. field-list-table:: Modbus Master DO attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-ModbusmaDOIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the DO object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-ModbusmaDOQualifier:
   
               :xmlref:`Qualifier`
     :val:     0...255
     :desc:    Internal object Qualifier to enable customized data processing. (default value 0) :inlinetip:`Attribute is not implemented currently and reserved for future use.`

   * :attr:    .. _ref-ModbusmaDOPulseDuration:
   
               :xmlref:`PulseDuration`
     :val:     1...65535
     :desc:    Digital output pulse duration in milliseconds. Digital output will be activated when command is sent and automatically released after configured number of milliseconds. (default value 1500)

   * :attr:    .. _ref-ModbusmaDOTotal:
   
               :xmlref:`Total`
     :val:     1...255
     :desc:    Sequence of identical DO objects. Attribute is used to create sequence of information objects with consecutive :ref:`Index<ref-ModbusmaDOIndex>` attributes. This eliminates the need to create individual :ref:`DO<ref-ModbusmaDO>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`DO<ref-ModbusmaDO>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-ModbusmaDOName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

