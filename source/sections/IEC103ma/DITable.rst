
.. _ref-IEC103maDITable:
.. _ref-IEC103maDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-IEC103maDITable>` and child element nodes :ref:`DI<ref-IEC103maDI>` are used to create DI information objects to receive status 
information from the downstream outstation. Each created DI information object can be used as source of 
information for any DI information object defined in IO table of the Slave protocol instances. If used as a source, 
status information received from an outstation will be forwarded to DI information object of the Slave protocol 
instance and then to the upstream Master station. Please refer to the 
section :ref:`docref-IEC10xslDITable` for more information on how to use DI information object as a source.

In order to receive status information from the downstream outstation function type (FUN) and information 
number (INF) need to be entered in :ref:`DI<ref-IEC103maDI>`.\ :ref:`FUN<ref-IEC103maDIFUN>` \ and :ref:`DI<ref-IEC103maDI>`.\ :ref:`INF<ref-IEC103maDIINF>` \ attributes.

Please see sample :ref:`DITable<ref-IEC103maDITable>` group node and :ref:`DI<ref-IEC103maDI>` child element nodes below. There are 5 DI information 
objects configured using 4 :ref:`DI<ref-IEC103maDI>` element nodes.

.. code-block:: none

   <DITable>
	<DI Index="0" FUN="1" INF="1" Qualifier="0x00"/>
	<DI Index="1" FUN="1" INF="2" Qualifier="0x10"/>
	<DI Index="2" FUN="240" INF="55" Qualifier="0x10"/>
	<DI Index="3" FUN="240" INF="56" Qualifier="0x00" Total="2"/>
   </DITable>

Please see sample :ref:`DI<ref-IEC103maDI>` element node below listing all available attributes.

.. code-block:: none

   <DI Index="0" FUN="1" INF="1" Qualifier="0" Total="2" Name="CB position" />

.. tip:: Attributes of the :ref:`DI<ref-IEC103maDI>` element node can be arranged in any order, it will not affect the XML file validation.         

DI attributes
^^^^^^^^^^^^^

.. _ref-IEC103maDIAttributes:

.. field-list-table:: IEC 60870-5-103 Master DI attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC103maDIIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the DI object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-IEC103maDIFUN:
   
               :xmlref:`FUN`
     :val:     0...255
     :desc:    Function Type (FUN) of the DI object. This FUN will be used to receive object from downstream outstation. :inlinetip:`Function types don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC103maDIINF:
   
               :xmlref:`INF`
     :val:     0...255
     :desc:    Information Number (INF) of the DI object. This INF will be used to receive object from downstream outstation. :inlinetip:`Information numbers don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC103maDIQualifier:
   
               :xmlref:`Qualifier`
     :val:     See table :numref:`ref-IEC103maDIQualifierBits` for description
     :desc:    Internal object Qualifier to enable customized data processing. See table :numref:`ref-IEC103maDIQualifierBits` for internal object Qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC103maDITotal:
   
               :xmlref:`Total`
     :val:     1...255
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`DI<ref-IEC103maDI>`.\ :ref:`Index<ref-IEC103maDIIndex>` \ and :ref:`DI<ref-IEC103maDI>`.\ :ref:`INF<ref-IEC103maDIINF>` \ attribute values without a need to create individual :ref:`DI<ref-IEC103maDI>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`DI<ref-IEC103maDI>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC103maDIName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

DI.Qualifier
^^^^^^^^^^^^

.. _ref-IEC103maDIQualifierBits:

.. field-list-table:: IEC 60870-5-103 Master DI internal Qualifier
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Values
     :desc,80: Description

   * :attr:    Qualifier [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    DI internal Qualifier has 8 data bits

   * :attr:    Bit 0
     :val:     xxxx.xxx0
     :desc:    DI object **will not** be inverted (ON = 2; OFF = 1; INTER = 0; INVALID = 3)

   * :(attr):
     :val:     xxxx.xxx1
     :desc:    DI object **will** be inverted (ON = 1; OFF = 2; INTER = 0; INVALID = 3)

   * :attr:    Bit 1
     :val:     xxxx.xx0x
     :desc:    Additional 'Zero' DI event generation **disabled**

   * :(attr):
     :val:     xxxx.xx1x
     :desc:    Additional 'Zero' DI event generation **enabled**. An OFF event will be internally generated following every sent DI ON event. Static DI object will be set to OFF value, static value is used when Slave protocol instance responds to an Interrogation.

   * :attr:    Bit 2
     :val:     xxxx.x0xx
     :desc:    DI event is generated **only** when object state is changed

   * :(attr):
     :val:     xxxx.x1xx
     :desc:    DI event is generated **every time** object is received from outstation. Invalid [IV] flag is automatically cleared from these DI objects when outstation goes online which ensures they are always valid. :inlinetip:`This option is only used for backward compatibility.`

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    DI is **enabled** and will be processed when received

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    DI is **disabled** and will be discarded when received

   * :attr:    Bits 3;6
     :val:     Any
     :desc:    Bits reserved for future use
