
.. _docref-IEC10xslAOTable:
.. _ref-IEC10xslAOTable:
.. _ref-IEC10xslAO:

AOTable group and AO node
-------------------------

Group node :ref:`AOTable<ref-IEC10xslAOTable>` and child element nodes :ref:`AO<ref-IEC10xslAO>` are used to create AO information objects to receive setpoint 
commands from the upstream Master station. Each created AO information object needs to have a destination 
to forward the setpoint information. The destination is created by linking AO information object to a :ref:`AO<ref-IEC10xslAO>` node of 
any Master protocol instance that is defined in leandc. (Master protocol instances are defined under 
:ref:`CommunicationCfg<ref-CommunicationCfg>` node in **leandc.xml** file)

The link is created using :ref:`AO<ref-IEC10xslAO>`.\ :ref:`Device<ref-IEC10xslAODevice>` \ and :ref:`AO<ref-IEC10xslAO>`.\ :ref:`Index<ref-IEC10xslAOIndex>` \ attributes. The first step is to select the **destination Master 
protocol instance**, use value of the :ref:`Index<ref-IEC101maIndex>` attribute of any Master protocol instance. The next step is to select 
the **destination AO object**, use value of the :ref:`AO<ref-IEC10xmaAO>`.\ :ref:`Index<ref-IEC10xmaAOIndex>` \ attribute of any AO object listed in the IO object table of 
any Master protocol instance. Enter the selected values of **destination Master protocol instance** in 
:ref:`AO<ref-IEC10xslAO>`.\ :ref:`Device<ref-IEC10xslAODevice>` \ attribute and destination AO object in :ref:`AO<ref-IEC10xslAO>`.\ :ref:`Index<ref-IEC10xslAOIndex>` \ attribute.

Information address (IOA) for receiving setpoint command is entered in :ref:`AO<ref-IEC10xslAO>`.\ :ref:`InfAddr<ref-IEC10xslAOInfAddr>` \ attribute.

Please see sample :ref:`AOTable<ref-IEC10xslAOTable>` group node and :ref:`AO<ref-IEC10xslAO>` child element nodes below. There are 5 AO information 
objects configured using 4 :ref:`AO<ref-IEC10xslAO>` element nodes.

.. code-block:: none

   <AOTable> 
	<AO Device="10" Index="0" InfAddr="1" Policy="0" … />
	<AO Device="10" Index="1" InfAddr="2" Policy="250" … />
	<AO Device="10" Index="-2" InfAddr="3" Policy="0" … />
	<AO Device="10" Index="2" InfAddr="4" Policy="0" Total="2" … />
   </AOTable>
   
Please see sample :ref:`AO<ref-IEC10xslAO>` element node below listing all available attributes.
            
.. code-block:: none
            
   <AO  Device="10"
	Index="2"
	InfAddr="4"
	qualifier="0x80"
	Coeff="15.3"
	Policy="0"
	TypeID="0"
	Total="2"
	Name="Filtering value" />
      
.. tip:: Attributes of the :ref:`AO<ref-IEC10xslAO>` element node can be arranged in any order, it will not affect the XML file validation.         

AO attributes
^^^^^^^^^^^^^

.. _ref-IEC10xslAOAttributes:

.. field-list-table:: IEC 60870-5-101/104 Slave AO attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC10xslAODevice:
               
               :xmlref:`Device`
     :val:     1...254
     :desc:    Source communication protocol instance. Any Master protocol instance listed in :ref:`CommunicationCfg<ref-CommunicationCfg>` group can be used as a source. Use value of the Master protocol instance :ref:`Index<ref-IEC101maIndex>` attribute in order to link AO to it. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`IEC101sl<ref-IEC101sl>`.\ :ref:`Source<ref-IEC101slSource>` \ or :ref:`IEC104sl<ref-IEC104sl>`.\ :ref:`Source<ref-IEC104slSource>` \ :inlinetip:`attributes will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAOIndex:
   
               :xmlref:`Index`
     :val:     -8...2\ :sup:`32`\  - 1
     :desc:    Destination AO object. Any AO element node of the selected Master protocol instance can be used as a destination. Use value of the :ref:`AO<ref-IEC10xmaAO>`.\ :ref:`Index<ref-IEC10xmaAOIndex>` \ attribute of any AO element node listed in the IO table of the selected Master protocol instance. :inlinetip:`Indexes don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xslAOInfAddr:
   
               :xmlref:`InfAddr`
     :val:     1...16777215
     :desc:    Information Object Address (IOA) of the AO object. This IOA will be used to receive command from upstream Master station. :inlinetip:`Addresses don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xslAOqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC10xslAOqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC10xslAOqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAOCoeff:
   
               :xmlref:`Coeff`
     :val:     0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Coefficient to multiply the setpoint object value before forwarding to linked protocol instance. (default value 1) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAOPolicy:
   
               :xmlref:`Policy`
     :val:     0...255
     :desc:    Command execution policy, see table :numref:`ref-IEC10xslPolicy` for description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAOTypeID:
   
               :xmlref:`TypeID`
     :val:     See table :numref:`ref-IEC10xslAOTypeIDValues` for description
     :desc:    Only accept command if received with this ASDU Type. Value 0 disables incoming command ASDU type checking and any command is accepted. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAOTotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`AO<ref-IEC10xslAO>`.\ :ref:`Index<ref-IEC10xslAOIndex>` \ and :ref:`AO<ref-IEC10xslAO>`.\ :ref:`InfAddr<ref-IEC10xslAOInfAddr>` \ attribute values without a need to create individual :ref:`AO<ref-IEC10xslAO>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`AO<ref-IEC10xslAO>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslAOName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

AO.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xslAOqualifierBits:

.. field-list-table:: IEC 60870-5-101/104 Slave AO internal qualifier
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Values
     :desc,80: Description

   * :attr:    qualifier [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    AO internal qualifier has 8 data bits

   * :attr:    Bits 6;5
     :val:     x00x.xxxx
     :desc:    Only **Direct-Execute** commands are accepted

   * :(attr):
     :val:     x01x.xxxx
     :desc:    **Direct-Execute** and **Select-before-Execute** commands are accepted

   * :(attr):
     :val:     x10x.xxxx
     :desc:    **Only Select-Before-Execute** commands are accepted

   * :(attr):
     :val:     x11x.xxxx
     :desc:    Reserved for future use

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    AO is **enabled** and command will be processed when received

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    AO is **disabled** and command will be rejected when received

   * :attr:    Bits 0...4
     :val:     Any
     :desc:    Bits reserved for future use

AO.TypeID
^^^^^^^^^

.. _ref-IEC10xslAOTypeIDValues:

.. field-list-table:: IEC 60870-5-101/104 Slave AO TypeID
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:    48
     :desc:    Only 'Normalized setpoint command' will be accepted and processed (ASDU type 48 [C_SE_NA_1])

   * :attr:    49
     :desc:    Only 'Scaled setpoint command' will be accepted and processed (ASDU type 49 [C_SE_NB_1])

   * :attr:    50
     :desc:    Only 'Short floating point setpoint command' will be accepted and processed (ASDU type 50 [C_SE_NC_1])

   * :attr:    61
     :desc:    Only applicable to IEC60870-5-104 Slave protocol instance;
               Only time-tagged 'Normalized setpoint command' will be accepted and processed (ASDU type 61 [C_SE_TA_1])

   * :attr:    62
     :desc:    Only applicable to IEC60870-5-104 Slave protocol instance;
               Only time-tagged 'Scaled setpoint command' will be accepted and processed (ASDU type 62 [C_SE_TB_1])

   * :attr:    63
     :desc:    Only applicable to IEC60870-5-104 Slave protocol instance;
               Only time-tagged 'Short floating point setpoint command' will be accepted and processed (ASDU type 63 [C_SE_TC_1])

   * :attr:    Other
     :desc:    Undefined, setpoint command received with any ASDU type will be accepted
   
