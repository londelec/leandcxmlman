.. _xmlelem-ModbusmaHardcoded:

Hardcoded
^^^^^^^^^

Hardcoded device type can be specified in this node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-ModbusmaHardcoded`"

.. code-block:: none

   <Hardcoded Type="BCDI16" />


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-ModbusmaHardcoded" "Modbus Master Hardcoded attributes" ":spec: |C{0.1}|C{0.12}|C{0.1}|S{0.68}|"

   * :attr:	:xmlattr:`Type`
     :val:	See :numref:`tabid-ModbusmaHardcodedType`
     :def:	n/a
     :desc:	Predefined type of a Modbus device.
		Messages and communication sequences are hardcoded for these devices.
		:inlineimportant:`Attribute is case sensitive, observe case of the device type when specifying.`


.. field-list-table:: Modbus Master Hardcoded Device Types
   :class: table table-condensed table-bordered longtable
   :name: tabid-ModbusmaHardcodedType
   :spec: |C{0.20}|S{0.80}|
   :header-rows: 1

   * :attr,20,center:	:ref:`xmlattr-ModbusmaHardcodedType`
     :desc,80:		Description

   * :attr:	BCDI16
     :desc:	Brainchild Digital Input (16) module DI16. Data points are automatically created for this device as follows: DI=16, AI=0, DO=0, AO=0

   * :attr:	BCAIIS8
     :desc:	Brainchild isolated Analog Input (8) module AIIS8. Data points are automatically created for this device as follows: DI=0, AI=8, DO=0, AO=0

   * :attr:	LEDOM16
     :desc:	Londelec Digital Output (16) module DOM16. Data points are automatically created for this device as follows: DI=0, AI=0, DO=16, AO=0

   * :attr:	LEIODC-C32-3100
     :desc:	Londelec LEIODC-C32-3100 unit. Data points are automatically created for this device as follows: DI=12, AI=0, DO=4, AO=0

   * :attr:	LEIODC-X32-3100
     :desc:	Londelec LEIODC-X32-3100 unit. Data points are automatically created for this device as follows: DI=12, AI=0, DO=4, AO=0

   * :attr:	LEIODC-P32-3100
     :desc:	Londelec LEIODC-X32-3100 unit. Data points are automatically created for this device as follows: DI=12, AI=0, DO=4, AO=0

   * :attr:	LEIODC-X10-3100
     :desc:	Londelec LEIODC-X10-3100 unit. Data points are automatically created for this device as follows: DI=12, AI=0, DO=4, AO=0

   * :attr:	LEIODC-X32-4000
     :desc:	Londelec LEIODC-X32-4000 unit. Data points are automatically created for this device as follows: DI=16, AI=0, DO=0, AO=0

   * :attr:	LEIODC-P32-4000
     :desc:	Londelec LEIODC-X32-4000 unit. Data points are automatically created for this device as follows: DI=16, AI=0, DO=0, AO=0

   * :attr:	LEIODC-X10-4000
     :desc:	Londelec LEIODC-X10-4000 unit. Data points are automatically created for this device as follows: DI=16, AI=0, DO=0, AO=0

   * :attr:	LEIODC-X32-0400
     :desc:	Londelec LEIODC-X32-0400 unit. Data points are automatically created for this device as follows: DI=0, AI=0, DO=16, AO=0

   * :attr:	LEIODC-P32-0400
     :desc:	Londelec LEIODC-X32-0400 unit. Data points are automatically created for this device as follows: DI=0, AI=0, DO=16, AO=0

   * :attr:	LEIODC-X10-0400
     :desc:	Londelec LEIODC-X10-0400 unit. Data points are automatically created for this device as follows: DI=0, AI=0, DO=16, AO=0

   * :attr:	LEIODC-X32-2200
     :desc:	Londelec LEIODC-X32-2200 unit. Data points are automatically created for this device as follows: DI=8, AI=0, DO=8, AO=0

   * :attr:	LEIODC-P32-2200
     :desc:	Londelec LEIODC-X32-2200 unit. Data points are automatically created for this device as follows: DI=8, AI=0, DO=8, AO=0

   * :attr:	LEIODC-X10-2200
     :desc:	Londelec LEIODC-X10-2200 unit. Data points are automatically created for this device as follows: DI=8, AI=0, DO=8, AO=0

   * :attr:	THT2
     :desc:	| Papouch THT2 thermometer. Data points are automatically created for this device as follows: DI=0, AI=3, DO=0, AO=0. AI indexes as follows:
		| 0 => Temperature;
		| 1 => Humidity;
		| 2 => Dew point;

   * :attr:	Other
     :desc:	Undefined, none of hardcoded device types will be used
