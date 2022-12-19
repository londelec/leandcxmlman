.. _xmlelem-IEC61850clAssociation:

AssociationSettings
^^^^^^^^^^^^^^^^^^^

Settings of the Association control service layer (ISO8650) can be specified using attributes of :ref:`xmlelem-IEC61850clAssociation` element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`xmlelem-IEC61850clAssociation`"

.. code-block:: none

   <AssociationSettings CallingAPtitle="1,1,1,999" CallingAEqualifier="10" CallingAPinvokeID="4" CallingAEinvokeID="5" AARQfields="0x0000" Flags="0x00" LogFlags="0x00"/>


.. include-file:: sections/Include/table_attrs.rstinc "" "tabid-IEC61850clAssociation" "IEC61850 Client AssociationSettings attributes" ":spec: |C{0.18}|C{0.18}|C{0.1}|S{0.54}|"

   * :attr:	:xmlattr:`CallingAPtitle`
     :val:	OID 1...64 chars
     :def:	1.3.6.1.4.1.45898.10
     :desc:	[:lemonobgtext:`Calling AP Title`] field value for outgoing [:lemonobgtext:`AARQ APDU`].
		The field will be automatically included in the outgoing [:lemonobgtext:`AARQ APDU`] if this attribute is specified, but it can be excluded using :ref:`xmlattr-IEC61850clAssociationAARQfields`.
		Attribute value must be a valid Object Identifier (OID) e.g. "1.1.1.999". Either dot '.' or comma ',' can be used a separator.

   * :attr:	:xmlattr:`CallingAEqualifier`
     :val:	0...99999
     :def:	1
     :desc:	[:lemonobgtext:`Calling AE Qualifier`] field value for outgoing [:lemonobgtext:`AARQ APDU`].
		The field will be automatically included in the outgoing [:lemonobgtext:`AARQ APDU`] if this attribute is specified, but it can be excluded using :ref:`xmlattr-IEC61850clAssociationAARQfields`.

   * :attr:	:xmlattr:`CallingAPinvokeID`
     :val:	0...99999
     :def:	0
     :desc:	[:lemonobgtext:`Calling AP Invocation-identifier`] field value for outgoing [:lemonobgtext:`AARQ APDU`].
		The field will be automatically included in the outgoing [:lemonobgtext:`AARQ APDU`] if this attribute is specified, but it can be excluded using :ref:`xmlattr-IEC61850clAssociationAARQfields`.

   * :attr:	:xmlattr:`CallingAEinvokeID`
     :val:	0...99999
     :def:	0
     :desc:	[:lemonobgtext:`Calling AE Invocation-identifier`] field value for outgoing [:lemonobgtext:`AARQ APDU`].
		The field will be automatically included in the outgoing [:lemonobgtext:`AARQ APDU`] if this attribute is specified, but it can be excluded using :ref:`xmlattr-IEC61850clAssociationAARQfields`.

   * :attr:	:xmlattr:`AARQfields`
     :val:	|flags16range|
     :def:	0x0000
     :desc:	Fields that are included in the outgoing [:lemonobgtext:`AARQ APDU`].
		See :numref:`tabid-IEC61850clAssociationAARQfields` for description.

.. include-file:: sections/Include/IEC61850cl_Flags.rstinc "" ":numref:`tabid-IEC61850clAssociationFlags`" "Association"

.. include-file:: sections/Include/IEC61850_LogFlags8.rstinc "" ":numref:`tabid-IEC61850clLogFlags`" "Association"


.. include-file:: sections/Include/table_flags16.rstinc "" "tabid-IEC61850clAssociationAARQfields" "Fields of the AARQ APDU" ":ref:`xmlattr-IEC61850clAssociationAARQfields`" "AARQ fields"

   * :attr:	Bit 0
     :val:	xxxx.xxxx xxxx.xxx0
     :desc:	**Exclude** [:lemonobgtext:`Protocol Version`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.xxx1
     :desc:	**Include** [:lemonobgtext:`Protocol Version`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bit 1
     :val:	xxxx.xxxx xxxx.xx0x
     :desc:	**Exclude** [:lemonobgtext:`Called AP Title`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.xx1x
     :desc:	**Include** [:lemonobgtext:`Called AP Title`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bit 2
     :val:	xxxx.xxxx xxxx.x0xx
     :desc:	**Exclude** [:lemonobgtext:`Called AE Qualifier`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.x1xx
     :desc:	**Include** [:lemonobgtext:`Called AE Qualifier`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bit 3
     :val:	xxxx.xxxx xxxx.0xxx
     :desc:	**Exclude** [:lemonobgtext:`Called AP Invocation-identifier`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxxx xxxx.1xxx
     :desc:	**Include** [:lemonobgtext:`Called AP Invocation-identifier`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bit 4
     :val:	xxxx.xxxx xxx0.xxxx
     :desc:	**Exclude** [:lemonobgtext:`Called AE Invocation-identifier`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxxx xxx1.xxxx
     :desc:	**Include** [:lemonobgtext:`Called AE Invocation-identifier`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bit 5
     :val:	xxxx.xxxx xx0x.xxxx
     :desc:	**Exclude** [:lemonobgtext:`Calling AP Title`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxxx xx1x.xxxx
     :desc:	**Include** [:lemonobgtext:`Calling AP Title`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bit 6
     :val:	xxxx.xxxx x0xx.xxxx
     :desc:	**Exclude** [:lemonobgtext:`Calling AE Qualifier`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxxx x1xx.xxxx
     :desc:	**Include** [:lemonobgtext:`Calling AE Qualifier`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bit 7
     :val:	xxxx.xxxx 0xxx.xxxx
     :desc:	**Exclude** [:lemonobgtext:`Calling AP Invocation-identifier`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxxx 1xxx.xxxx
     :desc:	**Include** [:lemonobgtext:`Calling AP Invocation-identifier`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bit 8
     :val:	xxxx.xxx0 xxxx.xxxx
     :desc:	**Exclude** [:lemonobgtext:`Calling AE Invocation-identifier`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxx1 xxxx.xxxx
     :desc:	**Include** [:lemonobgtext:`Calling AE Invocation-identifier`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bit 15
     :val:	0xxx.xxxx xxxx.xxxx
     :desc:	**Exclude** [:lemonobgtext:`direct-reference`] (ISO8825-1) in [:lemonobgtext:`Association-information`] field from [:lemonobgtext:`AARQ APDU`]. (default value)

   * :(attr):
     :val:	1xxx.xxxx xxxx.xxxx
     :desc:	**Include** [:lemonobgtext:`direct-reference`] (ISO8825-1) in [:lemonobgtext:`Association-information`] field in [:lemonobgtext:`AARQ APDU`].

   * :attr:	Bits 9...14
     :val:	Any
     :desc:	Bits reserved for future use


.. include-file:: sections/Include/table_flags8.rstinc "" "tabid-IEC61850clAssociationFlags" "Specific Association Control Service flags" ":ref:`xmlattr-IEC61850clAssociationFlags`" "Specific Association Control Service flags"

   * :attr:	Bit 0
     :val:	xxxx.xxx0
     :desc:	**Ignore** [:lemonobgtext:`Responding AP Title`] and [:lemonobgtext:`Responding AE Qualifier`] of the received [:lemonobgtext:`AARE APDU`]. (default value)

   * :(attr):
     :val:	xxxx.xxx1
     :desc:	**Check** [:lemonobgtext:`Responding AP Title`] and [:lemonobgtext:`Responding AE Qualifier`] of the received [:lemonobgtext:`AARE APDU`].
		Communication will not be established if the received values don't match "OSI-AP-Title" and "OSI-AE-Qualifier" defined in the SCL file.

   * :attr:	Bits 1...7
     :val:	Any
     :desc:	Bits reserved for future use

