
.. _ref-IEC10xmaDOTable:
.. _ref-IEC10xmaDO:

DOTable group and DO node
-------------------------

Group node :ref:`DOTable<ref-IEC10xmaDOTable>` and child element nodes :ref:`DO<ref-IEC10xmaDO>` are used to create DO information objects to send control 
command to the downstream outstation. Each created DO can be used as a destination for any DO information 
object defined in the IO table of any Slave protocol instance. Command execution procedure is as follows: Slave 
protocol instance receives a control command from the upstream Master station and forwards to the destination 
DO information object. Then current communication protocol instance prepares and sends a command to the 
outstation based on DO settings configured below. Please refer to the 
section :ref:`docref-IEC10xslDOTable` for more information on how to use DO as a destination for 
command received by the Slave protocol instance.

Every outgoing control command to the downstream outstation must have information address (IOA) specified 
using :ref:`DI<ref-IEC10xmaDO>`.\ :ref:`InfAddr<ref-IEC10xmaDOInfAddr>` \ attribute.

Please see sample :ref:`DOTable<ref-IEC10xmaDOTable>` group node and :ref:`DO<ref-IEC10xmaDO>` child element nodes below. There are 5 DO information 
objects configured using 4 :ref:`DO<ref-IEC10xmaDO>` element nodes.

.. code-block:: none

   <DOTable> 
	<DO Index="0" InfAddr="1" qualifier="0x00" TypeID="45"/>
	<DO Index="1" InfAddr="2" qualifier="0x10" TypeID="46"/>
	<DO Index="2" InfAddr="3" qualifier="0x10" QOC="3"/>
	<DO Index="3" InfAddr="4" qualifier="0x00" Total="2"/>
   </DOTable>
   
Please see sample :ref:`DO<ref-IEC10xmaDO>` element node below listing all available attributes.
            
.. code-block:: none
            
   <DO  Index="0"
	InfAddr="1"
        qualifier="0x00"
        QOC="0"
        TypeID="46"
        Total="2"
        Name="CB command" />
      
.. tip:: Attributes of the :ref:`DO<ref-IEC10xmaDO>` element node can be arranged in any order, it will not affect the XML file validation.         

DO attributes
^^^^^^^^^^^^^

.. _ref-IEC10xmaDOAttributes:

.. field-list-table:: IEC 60870-5-101/104 Master DO attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC10xmaDOIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the DO object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-IEC10xmaDOInfAddr:
   
               :xmlref:`InfAddr`
     :val:     1...16777215
     :desc:    Information Object Address (IOA) of the DO object. This IOA will be used to send control command to downstream outstation. :inlinetip:`Addresses don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xmaDOqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC10xmaDOqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC10xmaDOqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaDOQOC:
   
               :xmlref:`QOC`
     :val:     See table :numref:`ref-IEC10xmaDOQOCValues` for description
     :desc:    Qualifier Of Command (QOC) is used to define specify short/long pulse information for the outgoing command. See table :numref:`ref-IEC10xmaDOQOCValues` values. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaDOTypeID:
   
               :xmlref:`TypeID`
     :val:     See table :numref:`ref-IEC10xmaDOTypeIDValues` for description
     :desc:    Send command with the defined ASDU Type. There is no default value, ASDU TypeID is transparent if neither this attribute nor communication protocol generic attribute (e.g. IEC101ma or IEC104ma :ref:`ASDUSettings<ref-IEC101maASDUSettings>`.\ :ref:`DOType<ref-IEC101maASDUSettingsDOType>` \) is used. :inlinetip:`Attribute is optional and doesn't have to be included in configuration.`

   * :attr:    .. _ref-IEC10xmaDOTotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`DO<ref-IEC10xmaDO>`.\ :ref:`Index<ref-IEC10xmaDOIndex>` \ and :ref:`DO<ref-IEC10xmaDO>`.\ :ref:`InfAddr<ref-IEC10xmaDOInfAddr>` \ attribute values without a need to create individual :ref:`DO<ref-IEC10xmaDO>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`DO<ref-IEC10xmaDO>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaDOName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

DO.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xmaDOqualifierBits:

.. field-list-table:: IEC 60870-5-101/104 Master DO internal qualifier
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

   * :attr:    Bit 6
     :val:     x0xx.xxxx
     :desc:    **Direct Execute** control command will be sent

   * :(attr):
     :val:     x1xx.xxxx
     :desc:    **Select and Execute** control commands will be sent

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    DO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    DO is **disabled**, command will not be sent to outstation

   * :attr:    Bits 1...5
     :val:     Any
     :desc:    Bits reserved for future use

DO.TypeID
^^^^^^^^^

.. _ref-IEC10xmaDOTypeIDValues:

.. field-list-table:: IEC 60870-5-101/104 Master DO TypeID
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:    45
     :desc:    'Single command' will be sent (ASDU type 45 [C_SC_NA_1])

   * :attr:    46
     :desc:    'Double command' will be sent (ASDU type 46 [C_DC_NA_1])

   * :attr:    47
     :desc:    'Regulating step command' will be sent (ASDU type 47 [C_RC_NA_1])

   * :attr:    58
     :desc:    Only applicable to IEC60870-5-104 Master protocol instance;
               Time-tagged 'Single command' will be sent (ASDU type 58 [C_SC_TA_1])

   * :attr:    59
     :desc:    Only applicable to IEC60870-5-104 Master protocol instance;
               Time-tagged 'Double command' will be sent (ASDU type 59 [C_DC_TA_1])

   * :attr:    60
     :desc:    Only applicable to IEC60870-5-104 Master protocol instance;
               Time-tagged 'Regulating step command' will be sent (ASDU type 60 [C_RC_TA_1])

   * :attr:    Other
     :desc:    Transparent, ASDU TypeID of the outgoing command will be the same as received from upstream Master station
   
DO.QOC
^^^^^^

.. _ref-IEC10xmaDOQOCValues:

.. field-list-table:: IEC 60870-5-101/104 Master QOC
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: QOC Values
     :desc,90: Description

   * :attr:    0
     :desc:    Command will be sent with [no additional definition]

   * :attr:    1
     :desc:    Command will be sent with [short-pulse duration]

   * :attr:    2
     :desc:    Command will be sent with [long-pulse duration]

   * :attr:    3
     :desc:    Command will be sent with [persistent output]

   * :attr:    128
     :desc:    Command will be sent with the same information as received from upstream Master station. This is a transparent mode.

   * :attr:    4...31
     :desc:    Reserved for [compatible range] and [private range] as per IEC 60870-5-101 standard

   * :attr:    Other
     :desc:    Undefined, don't use
   
