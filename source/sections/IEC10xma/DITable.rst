
.. _ref-IEC10xmaDITable:
.. _ref-IEC10xmaDI:

DITable group and DI node
-------------------------

Group node :ref:`DITable<ref-IEC10xmaDITable>` and child element nodes :ref:`DI<ref-IEC10xmaDI>` are used to create DI information objects to receive status 
information from the downstream outstation. Each created DI information object can be used as source of 
information for any DI information object defined in IO table of the Slave protocol instances. If used as a source,
status information received from an outstation will be forwarded to DI information object of the Slave protocol 
instance and then to the upstream Master station. Please refer to the 
section :ref:`docref-IEC10xslDITable` for more information on how to use DI information object as a source.

In order to receive status information from downstream outstation information object address (IOA) needs to be 
entered in :ref:`DI<ref-IEC10xmaDI>`.\ :ref:`InfAddr<ref-IEC10xmaDIInfAddr>` \ attribute. Status information is processed when received with any of the following ASDU 
types:
1 [M_SP_NA_1]; 2 [M_SP_TA_1]; 3 [M_DP_NA_1]; 
4 [M_DP_TA_1]; 30 [M_SP_TB_1]; 31 [M_DP_TB_1]

Please see sample :ref:`DITable<ref-IEC10xmaDITable>` group node and :ref:`DI<ref-IEC10xmaDI>` child element nodes below. There are 5 DI information objects 
configured using 4 :ref:`DI<ref-IEC10xmaDI>` element nodes.

.. code-block:: none

   <DITable> 
	<DI Index="0" InfAddr="1" qualifier="0x00" />
	<DI Index="1" InfAddr="2" qualifier="0x10" />
	<DI Index="2" InfAddr="3" qualifier="0x10" TypeID="31"/>
	<DI Index="3" InfAddr="4" qualifier="0x00" Total="2"/>
   </DITable>
   
Please see sample :ref:`DI<ref-IEC10xmaDI>` element node below listing all available attributes.
            
.. code-block:: none
            
   <DI  Index="0"
	InfAddr="1"
	qualifier="0"
	TypeID="31"
	Total="2"
        Name="CB position" />
      
.. tip:: Attributes of the :ref:`DI<ref-IEC10xmaDI>` element node can be arranged in any order, it will not affect the XML file validation.         

DI attributes
^^^^^^^^^^^^^

.. _ref-IEC10xmaDIAttributes:

.. field-list-table:: IEC 60870-5-101/104 Master DI attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC10xmaDIIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the DI object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-IEC10xmaDIInfAddr:
   
               :xmlref:`InfAddr`
     :val:     1...16777215
     :desc:    Information Object Address (IOA) of the DI object. This IOA will be used to receive object from downstream outstation. :inlinetip:`Addresses don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xmaDIqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC10xmaDIqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC10xmaDIqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaDITypeID:
   
               :xmlref:`TypeID`
     :val:     See table :numref:`ref-IEC10xmaDITypeIDValues` for description
     :desc:    Use this ASDU type to send a DI object upstream, if transparent ASDU function is enabled in Slave protocol instance using :ref:`ASDUSettings<ref-IEC101slASDUSettings>`.\ :ref:`TranspTypes<ref-IEC101slASDUSettingsTranspTypes>` \ attribute. This ASDU type will be used to report object regardless of the received ASDU type. (There is no default value, attribute must not be specified if not used). :inlinetip:`Attribute is optional and doesn't have to be included in configuration.`

   * :attr:    .. _ref-IEC10xmaDITotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`DI<ref-IEC10xmaDI>`.\ :ref:`Index<ref-IEC10xmaDIIndex>` \ and :ref:`DI<ref-IEC10xmaDI>`.\ :ref:`InfAddr<ref-IEC10xmaDIInfAddr>` \ attribute values without a need to create individual :ref:`DI<ref-IEC10xmaDI>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`DI<ref-IEC10xmaDI>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaDIName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

DI.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xmaDIqualifierBits:

.. field-list-table:: IEC 60870-5-101/104 Master DI internal qualifier
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Values
     :desc,80: Description

   * :attr:    qualifier [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    DI internal qualifier has 8 data bits

   * :attr:    Bit 0
     :val:     xxxx.xxx0
     :desc:    DI object **will not** be inverted (ON = 1; OFF = 0 for [M_SP_NA_1] type and ON = 2; OFF = 1; INTER = 0; INVALID = 3 for [M_DP_NA_1] type)

   * :(attr):
     :val:     xxxx.xxx1
     :desc:    DI object **will** be inverted (ON = 0; OFF = 1 for [M_SP_NA_1] type and ON = 1; OFF = 2; INTER = 0; INVALID = 3 for [M_DP_NA_1] type)

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
     :desc:    DI event is generated **every time** it is received from outstation. Invalid [IV] flag is automatically cleared from these DI objects when outstation becomes online ensuring they are are always valid. :inlinetip:`This option is only used for backward compatibility.`

   * :attr:    Bit 3
     :val:     xxxx.0xxx
     :desc:    **Use original** timetag when event is received from outstation

   * :(attr):
     :val:     xxxx.1xxx
     :desc:    **Substitute timetag** with local time when event is received from outstation

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    DI is **enabled** and will be processed when received

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    DI is **disabled** and will be discarded when received

   * :attr:    Bits 4;6
     :val:     Any
     :desc:    Bits reserved for future use

DI.TypeID
^^^^^^^^^

.. _ref-IEC10xmaDITypeIDValues:

.. include:: IEC10xDITypeID.rst
