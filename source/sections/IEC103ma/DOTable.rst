
.. _ref-IEC103maDOTable:
.. _ref-IEC103maDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-IEC103maDOTable>` and child element nodes :ref:`DO<ref-IEC103maDO>` are used to create DO information objects to send control 
command to the downstream outstation. Each created DO information object can be used as a destination for 
any DO information object defined in IO table of the Slave protocol instances. If used as a destination, 
procedure is as follows: Slave protocol instance receives control command from the upstream Master station 
and forwards to destination DO information object. Then current communication protocol instance prepares and 
sends command to the outstation based on DO information object settings. Please refer to the 
section :ref:`DOTable<ref-IEC10xslDOTable>` for more information on how to use DO information object as a destination.

In order to send control command to the downstream outstation function type (FUN) and information number 
(INF) need to be entered in :ref:`DO<ref-IEC103maDO>`.\ :ref:`FUN<ref-IEC103maDOFUN>` \ and :ref:`DO<ref-IEC103maDO>`.\ :ref:`INF<ref-IEC103maDOINF>` \ attributes.

Please see sample :ref:`DOTable<ref-IEC103maDOTable>` group node and :ref:`DO<ref-IEC103maDO>` child element nodes below. There are 5 DO information 
objects configured using 4 :ref:`DO<ref-IEC103maDO>` element nodes.

.. code-block:: none

   <DOTable>
	<DO Index="0" FUN="1" INF="1" qualifier="0x00"/>
	<DO Index="1" FUN="1" INF="2" qualifier="0x10"/>
	<DO Index="2" FUN="240" INF="55" qualifier="0x10"/>
	<DO Index="3" FUN="240" INF="56" qualifier="0x00" Total="2"/>
   </DOTable>
   
Please see sample :ref:`DO<ref-IEC103maDO>` element node below listing all available attributes.
            
.. code-block:: none
            
   <DO  Index="0"
	FUN="1"
	INF="1"
	qualifier="0x00"
	Total="2"
      
.. tip:: Attributes of the :ref:`DO<ref-IEC103maDO>` element node can be arranged in any order, it will not affect the XML file validation.         

DO attributes
^^^^^^^^^^^^^

.. _ref-IEC103maDOAttributes:

.. field-list-table:: IEC 60870-5-103 Master DO attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC103maDOIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the DO object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-IEC103maDOFUN:
   
               :xmlref:`FUN`
     :val:     0...255
     :desc:    Function Type (FUN) of the DI object. This FUN will be used to send command to downstream outstation. :inlinetip:`Function types don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC103maDOINF:
   
               :xmlref:`INF`
     :val:     0...255
     :desc:    Information Number (INF) of the DI object. This INF will be used to send command to downstream outstation. :inlinetip:`Information numbers don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC103maDOqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC103maDOqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC103maDOqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC103maDOTotal:
   
               :xmlref:`Total`
     :val:     1...255
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`DO<ref-IEC103maDO>`.\ :ref:`Index<ref-IEC103maDOIndex>` \ and :ref:`DO<ref-IEC103maDO>`.\ :ref:`INF<ref-IEC103maDOINF>` \ attribute values without a need to create individual :ref:`DO<ref-IEC103maDO>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`DO<ref-IEC103maDO>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC103maDOName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

DO.qualifier
^^^^^^^^^^^^

.. _ref-IEC103maDOqualifierBits:

.. field-list-table:: IEC 60870-5-103 Master DO internal qualifier
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Values
     :desc,80: Description

   * :attr:    qualifier [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    DO internal qualifier has 8 data bits

   * :attr:    Bit 0
     :val:     xxxx.xxx0
     :desc:    DO object **will not** be inverted

   * :(attr):
     :val:     xxxx.xxx1
     :desc:    DO object **will** be inverted (OFF → ON; ON → OFF)

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    DO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    DO is **disabled**, command will not be sent to outstation

   * :attr:    Bits 1...6
     :val:     Any
     :desc:    Bits reserved for future use
   
