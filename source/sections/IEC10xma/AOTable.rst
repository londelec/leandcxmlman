
.. _ref-IEC10xmaAOTable:
.. _ref-IEC10xmaAO:

AOTable group and AO node
-------------------------

Group node :ref:`AOTable<ref-IEC10xmaAOTable>` and child element nodes :ref:`AO<ref-IEC10xmaAO>` are used to create AO information objects to send setpoint 
command to the downstream outstation. Each created AO can be used as a destination for any AO information 
object defined in the IO table of any Slave protocol instance. Command execution procedure is as follows: Slave 
protocol instance receives a setpoint command from the upstream Master station and forwards to the 
destination AO information object. Then current communication protocol instance prepares and sends a 
command to the outstation based on AO settings configured below. Please refer to the 
section :ref:`docref-IEC10xslAOTable` for more information on how to use AO as a destination for 
command received by the Slave protocol instance.

Every outgoing control command to the downstream outstation must have information address (IOA) specified 
using :ref:`AO<ref-IEC10xmaAO>`.\ :ref:`InfAddr<ref-IEC10xmaAOInfAddr>` \ attribute.

Please see sample :ref:`AOITable<ref-IEC10xmaAOTable>` group node and :ref:`AO<ref-IEC10xmaAO>` child element nodes below. There are 5 AO information 
objects configured using 4 :ref:`AO<ref-IEC10xmaAO>` element nodes.

.. code-block:: none

   <AOTable> 
	<AO Index="0" InfAddr="1" TypeID="48"/>
	<AO Index="1" InfAddr="2" TypeID="49"/>
	<AO Index="2" InfAddr="3" Coeff="3.3"/>
	<AO Index="3" InfAddr="4" Total="2"/>
   </AOTable>
   
Please see sample :ref:`AO<ref-IEC10xmaAO>` element node below listing all available attributes.
            
.. code-block:: none
            
   <AO  Index="0"
	InfAddr="1"
	qualifier="0x00"
	Coeff="11.6"
	TypeID="50"
	Total="2"
	Name="Filtering value" />
      
.. tip:: Attributes of the :ref:`AO<ref-IEC10xmaAO>` element node can be arranged in any order, it will not affect the XML file validation.         

AO attributes
^^^^^^^^^^^^^

.. _ref-IEC10xmaAOAttributes:

.. field-list-table:: IEC 60807-5-101/104 Master AO attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description

   * :attr:    .. _ref-IEC10xmaAOIndex:
   
               :xmlref:`Index`
     :val:     0...2\ :sup:`32`\  - 8
     :desc:    Index is a unique identifier of the AO object. :inlineimportant:`Index numbering must start with 0 and indexes must be arranged in an ascending order as it prevents insertion of a new object. This requirement is essential because it affects object mapping to Slave communication protocol instances.`

   * :attr:    .. _ref-IEC10xmaAOInfAddr:
   
               :xmlref:`InfAddr`
     :val:     1...16777215
     :desc:    Information Object Address (IOA) of the AO object. This IOA will be used to send setpoint command to downstream outstation. :inlinetip:`Addresses don't have to be arranged in an ascending order.`

   * :attr:    .. _ref-IEC10xmaAOqualifier:
   
               :xmlref:`qualifier`
     :val:     See table :numref:`ref-IEC10xmaAOqualifierBits` for description
     :desc:    Internal object qualifier to enable customized data processing. See table :numref:`ref-IEC10xmaAOqualifierBits` for internal object qualifier description. (default value 0) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaAOCoeff:
   
               :xmlref:`Coeff`
     :val:     0 or ±1.18×10\ :sup:`-38`\ ...±3.4×10\ :sup:`38`\ 
     :desc:    Coefficient to multiply the setpoint object value before sending to destination outstation. (default value 1) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaAOTypeID:
   
               :xmlref:`TypeID`
     :val:     See table :numref:`ref-IEC10xmaAOTypeIDValues` for description
     :desc:    Send command with the defined ASDU Type. There is no default value, ASDU TypeID is transparent if neither this attribute nor communication protocol generic attribute (e.g. IEC101ma or IEC104ma :ref:`ASDUSettings<ref-IEC101maASDUSettings>`.\ :ref:`AOType<ref-IEC101maASDUSettingsAOType>` \) is used. :inlinetip:`Attribute is optional and doesn't have to be included in configuration.`

   * :attr:    .. _ref-IEC10xmaAOTotal:
   
               :xmlref:`Total`
     :val:     1...16777215
     :desc:    Total number of information objects. Attribute is used to create sequence of information objects with consecutive :ref:`AO<ref-IEC10xmaAO>`.\ :ref:`Index<ref-IEC10xmaAOIndex>` \ and :ref:`AO<ref-IEC10xmaAO>`.\ :ref:`InfAddr<ref-IEC10xmaAOInfAddr>` \ attribute values without a need to create individual :ref:`AO<ref-IEC10xmaAO>` nodes for each information object. (default value 1; only 1 object is created with this :ref:`AO<ref-IEC10xmaAO>` node) :inlinetip:`Attribute is optional and doesn't have to be included in configuration, default value will be used if omitted.`

   * :attr:    .. _ref-IEC10xmaAOName:
   
               :xmlref:`Name`
     :val:     Max 100 chars
     :desc:    Freely configurable name, just for reference. :inlinetip:`Name attribute is optional and doesn't have to be included in configuration.`

AO.qualifier
^^^^^^^^^^^^

.. _ref-IEC10xmaAOqualifierBits:

.. field-list-table:: IEC 60807-5-101/104 Master AO internal qualifier
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Bits
     :val,10:  Values
     :desc,80: Description

   * :attr:    qualifier [xxxx.xxxx]
     :val:     0...0xFF
     :desc:    AO internal qualifier has 8 data bits

   * :attr:    Bit 6
     :val:     x0xx.xxxx
     :desc:    **Direct-Execute** setpoint command will be sent

   * :(attr):
     :val:     x1xx.xxxx
     :desc:    **Select and Execute** setpoint commands will be sent

   * :attr:    Bit 7
     :val:     0xxx.xxxx
     :desc:    AO is **enabled**, command will be sent to outstation

   * :(attr):
     :val:     1xxx.xxxx
     :desc:    AO is **disabled**, command will not be sent to outstation

   * :attr:    Bits 0...5
     :val:     Any
     :desc:    Bits reserved for future use

AO.TypeID
^^^^^^^^^

.. _ref-IEC10xmaAOTypeIDValues:

.. field-list-table:: IEC 60807-5-101/104 Master AO TypeID
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,10: TypeID Value
     :desc,90: Description

   * :attr:    48
     :desc:    'Normalized setpoint command' will be sent (ASDU type 48 [C_SE_NA_1])

   * :attr:    49
     :desc:    'Scaled setpoint command' will be sent (ASDU type 49 [C_SE_NB_1])

   * :attr:    50
     :desc:    'Short floating point setpoint command' will be sent (ASDU type 50 [C_SE_NC_1])
     
   * :attr:    61
     :desc:    Only applicable to IEC60870-5-104 Master protocol instance;
               Time-tagged 'Normalized setpoint command' will be sent (ASDU type 61 [C_SE_TA_1])

   * :attr:    62
     :desc:    Only applicable to IEC60870-5-104 Master protocol instance;
               Time-tagged 'Scaled setpoint command' will be sent (ASDU type 62 [C_SE_TB_1])

   * :attr:    63
     :desc:    Only applicable to IEC60870-5-104 Master protocol instance;
               Time-tagged 'Short floating point setpoint command' will be sent (ASDU type 63 [C_SE_TC_1])

   * :attr:    Other
     :desc:    Transparent, ASDU TypeID of the outgoing command will be the same as received from upstream Master station
   
