
.. _docref-IEC10xslDOTable:
.. _ref-IEC10xslDOTable:
.. _ref-IEC10xslDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-IEC10xslDOTable>` and child element nodes :ref:`DO<ref-IEC10xslDO>` are used to create DO information objects to receive control 
commands from the upstream Master station. Each created DO information object needs to have a destination 
to forward the control information. The destination is created by linking DO information object to a :ref:`DO<ref-IEC10xslDO>` node of 
any Master protocol instance that is defined in leandc. (Master protocol instances are defined under 
:ref:`CommunicationCfg<ref-CommunicationCfg>` node in **leandc.xml** file)

The link is created using :ref:`DO<ref-IEC10xslDO>`.\ :ref:`Device<ref-IEC10xslDODevice>` \ and :ref:`DO<ref-IEC10xslDO>`.\ :ref:`Index<ref-IEC10xslDOIndex>` \ attributes. The first step is to select the **destination Master 
protocol instance**, use value of the :ref:`Index<ref-IEC101maIndex>` attribute of any Master protocol instance. The next step is to select 
the **destination DO object**, use value of the :ref:`DO<ref-IEC10xslDO>`.\ :ref:`Index<ref-IEC10xslDOIndex>` \ attribute of any DO object listed in the IO object table of 
any Master protocol instance. Enter the selected values of **destination Master protocol instance** in 
:ref:`DO<ref-IEC10xslDO>`.\ :ref:`Device<ref-IEC10xslDODevice>` \ attribute and **destination DO object** in :ref:`DO<ref-IEC10xslDO>`.\ :ref:`Index<ref-IEC10xslDOIndex>` \ attribute.

Information address (IOA) for receiving control command is entered in :ref:`DO<ref-IEC10xslDO>`.\ :ref:`InfAddr<ref-IEC10xslDOInfAddr>` \ attribute.

Please see sample :ref:`DOTable<ref-IEC10xslDOTable>`  group node and :ref:`DO<ref-IEC10xslDO>` child element nodes below. There are 5 DO information 
objects configured using 4 :ref:`DO<ref-IEC10xslDO>` element nodes.

.. code-block:: none

   <DOTable> 
	<DO Device="10" Index="0" InfAddr="1" Policy="0" … />
	<DO Device="10" Index="1" InfAddr="2" Policy="250" … />
	<DO Device="10" Index="-2" InfAddr="3" Policy="0" … />
	<DO Device="10" Index="2" InfAddr="4" Policy="0" Total="2" … />
   </DOTable>
   
Please see sample :ref:`DO<ref-IEC10xslDO>` element node below listing all available attributes.
            
.. code-block:: none
            
   <DO  Device="10"
	Index="2"
	InfAddr="4"
	qualifier="0x10"
	Policy="0"
	TypeID="0"
	OffIndex="33"
	Total="2"
	Name="CB command" />
      
.. tip:: Attributes of the :ref:`DO<ref-IEC10xslDO>` element node can be arranged in any order, it will not affect the XML file validation.         

DO attributes
^^^^^^^^^^^^^

.. _ref-IEC10xslDOAttributes:

.. field-list-table:: IEC 60870-5-101/104 Slave DO attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC10xslDODevice:
               
               :xmlref:`Device`
     :val:     1...254
     :desc:    Source communication protocol instance. Any Master protocol instance listed in :ref:`CommunicationCfg<ref-CommunicationCfg>` group can be used as a source. Use value of the Master protocol instance :ref:`Index<ref-IEC101maIndex>` attribute in order to link DO to it. :inlinetip:`Attribute is optional and doesn't have to be included in configuration, value of the` :ref:`IEC101sl<ref-IEC101sl>`.\ :ref:`Source<ref-IEC101slSource>` \ or :ref:`IEC104sl<ref-IEC104sl>`.\ :ref:`Source<ref-IEC104slSource>` \ :inlinetip:`attributes will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDOIndex:

               :xmlref:`Index`
     :val:     -8...2\ :sup:`32`\  - 8
     :desc:    Destination DO object. Any DO element node of the selected Master protocol instance can be used as a destination. Use value of the :ref:`DO<ref-IEC10xmaDO>`.\ :ref:`Index<ref-IEC10xmaDOIndex>` \ attribute of any DO element node listed in the IO table of the selected Master protocol instance. Apart from regular indexes, there are some Service index values available, those are designed to control the linked Master protocol instance. Service index values are summarized in the table :numref:`ref-IEC10xslDOServiceIndexValues`. :inlinetip:`Indexes don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xslDOInfAddr:
   
               :xmlref:`InfAddr`
     :val:     1...16777215
     :desc:    Information Object Address (IOA) of the DO object. This IOA will be used to receive command from upstream Master station. :inlinetip:`Addresses don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xslDOqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC10xslDOqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC10xslDOqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDOPolicy:
   
               :xmlref:`Policy`
     :val:     0...255
     :desc:    Command execution policy, see table :numref:`ref-IEC10xslPolicy` for description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDOTypeID:
   
               :xmlref:`TypeID`
     :val:     See table :numref:`ref-IEC10xslDOTypeIDValues` for description
     :desc:    Only accept command if received with this ASDU Type. Value 0 disables incoming command ASDU type checking and any command is accepted. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDOOffIndex:
   
               :xmlref:`OffIndex`
     :val:     0...2\ :sup:`32`\  - 1
     :desc:    Destination DO object for OFF command. Attribute allows to send ON and OFF commands to different destinations. Any DO element node of the selected Master protocol instance can be used as a destination. Use value of the :ref:`DO<ref-IEC10xmaDO>`.\ :ref:`Index<ref-IEC10xmaDOIndex>` \ attribute of any DO element node listed in the IO table of the selected Master protocol instance. (default value is equal to :ref:`DO<ref-IEC10xslDO>`.\ :ref:`Index<ref-IEC10xslDOIndex>` \ attribute) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, both ON and OFF commands will be sent to the same destination object if this attribute is omitted.`

   * :attr:    .. _ref-IEC10xslDOTotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`DO<ref-IEC10xslDO>`.\ :ref:`Index<ref-IEC10xslDOIndex>` \ and :ref:`DO<ref-IEC10xslDO>`.\ :ref:`InfAddr<ref-IEC10xslDOInfAddr>` \ attribute values without a need to create individual :ref:`DO<ref-IEC10xslDO>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`DO<ref-IEC10xslDO>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xslDOName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

DO.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xslDOqualifierBits:

.. field-list-table:: IEC 60870-5-101/104 Slave DO internal qualifier
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
     :desc:    DI object **will** be inverted (OFF → ON; ON → OFF)

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
     :desc:    DO is **enabled** and command will be processed when received

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    DO is **disabled** and command will be rejected when received

   * :attr:    Bits 1...4
     :val:     Any
     :desc:    Bits reserved for future use

DO.TypeID
^^^^^^^^^

.. _ref-IEC10xslDOTypeIDValues:

.. field-list-table:: IEC 60870-5-101/104 Slave DO TypeID
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:    45
     :desc:    Only 'Single command' will be accepted and processed (ASDU type 45 [C_SC_NA_1])

   * :attr:    46
     :desc:    Only 'Double command' will be accepted and processed (ASDU type 46 [C_DC_NA_1])

   * :attr:    47
     :desc:    Only 'Regulating step command' will be accepted and processed (ASDU type 47 [C_RC_NA_1])

   * :attr:    58
     :desc:    Only applicable to IEC60870-5-104 Slave protocol instance;
               Only time-tagged 'Single command' will be accepted and processed (ASDU type 58 [C_SC_TA_1])

   * :attr:    59
     :desc:    Only applicable to IEC60870-5-104 Slave protocol instance;
               Only time-tagged 'Double command' will be accepted and processed (ASDU type 59 [C_DC_TA_1])

   * :attr:    60
     :desc:    Only applicable to IEC60870-5-104 Slave protocol instance;
               Only time-tagged 'Regulating step command' will be accepted and processed (ASDU type 59 [C_RC_TA_1])

   * :attr:    Other
     :desc:    Undefined, control command received with any ASDU type will be accepted
   
.. _ref-IEC10xslDOServiceIndex:

DO Service Indexes
^^^^^^^^^^^^^^^^^^

There are some Service DO indexes available allowing to control operation of the Master protocol instance. 
These indexes have negative decimal values to easily separate them from regular indexes used for linking.

.. _ref-IEC10xslDOServiceIndexValues:

.. field-list-table:: IEC 60870-5-101/104 Slave Service DO indexes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.25}|C{0.25}|S{0.5}|
   :header-rows: 1

   * :attr,10: Index value
     :val,10:  Object value
     :desc,80: Description

   * :attr:    -2 
               (0xFFFFFFFE)
     :val:     ON or OFF
     :desc:    Only applicable to Master communication protocol instances; Send forced **Poll** (e.g. General Interrogation) to downstream outstation.
   
   * :attr:    -3 
               (0xFFFFFFFD)
     :val:     ON
     :desc:    **Enable** leandc communication to peer station. This service index can be used for any protocol instance.
   
   * :(attr):
     :val:     OFF
     :desc:    **Disable** leandc communication to peer station. his service index can be used for any protocol instance.
   
   * :attr:    -4 
               (0xFFFFFFFC)
     :val:     ON
     :desc:    Only applicable to IEC60870-5-104 Master protocol instance; **Start** communication to downstream station by sending [**STARTDT_act**] message
   
   * :(attr):
     :val:     OFF
     :desc:    Only applicable to IEC60870-5-104 Master protocol instance; **Stop** communication to downstream station by sending [**STOPDT_act**] message
   
   * :attr:    -5 
               (0xFFFFFFFB)
     :val:     ON or OFF
     :desc:    Only applicable to Master communication protocol instances; Send **Reset Process** command (ASDU type 105 [C_RP_NA_1]) to downstream outstation

   * :attr:    -1 and -6...-8
     :val:     Any
     :desc:    Service commands reserved for future use
   
