.. _ref-IEC61850clAssociationSettings:

AssociationSettings
^^^^^^^^^^^^^^^^^^^

Settings of the Association control service layer (ISO8650) can be specified using attributes of :ref:`<ref-IEC61850clAssociationSettings>` 
element node.

.. include-file:: sections/Include/sample_node.rstinc "" ":ref:`<ref-IEC61850clAssociationSettings>`"

.. code-block:: none

   <AssociationSettings CallingAPtitle=",1,1,999" CallingAEqualifier="10" AARQfields="0x00" MMSversion="1" Flags="0x00"/>


.. _docref-IEC61850clAssociationSettingsAttab:

.. include-file:: sections/Include/table_attrs.rstinc "" "IEC61850 Client AssociationSettings attributes" ":spec: |C{0.18}|C{0.18}|C{0.1}|S{0.54}|"

   * :attr:     :xmlref:`CallingAPtitle`
     :val:      1...64 chars
     :def:      1,1,1,999
     :desc:     [:lemonobgtext:`Calling AP Title`] used for outgoing [:lemonobgtext:`AARQ APDU`] message

   * :attr:     :xmlref:`CallingAEqualifier`
     :val:      1...255
     :def:      12
     :desc:     [:lemonobgtext:`Calling AE Qualifier`] used for outgoing [:lemonobgtext:`AARQ APDU`] message

   * :attr:     .. _ref-IEC61850clAARQfields:

                :xmlref:`AARQfields`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Enabled fields of the outgoing [:lemonobgtext:`AARQ APDU`] message.
		See table :numref:`docref-IEC61850clAARQfieldsBits` for description

   * :attr:     :xmlref:`MMSversion`
     :val:      1; 2 or 3
     :def:      1
     :desc:     MMS version number as part of Application Context Name of outgoing [:lemonobgtext:`AARQ APDU`] message

   * :attr:     .. _ref-IEC61850clAssociationFlags:

                :xmlref:`Flags`
     :val:      0...255 or 0x00...0xFF
     :def:      0x00
     :desc:     Miscellaneous Association Control Service settings.
		See table :numref:`docref-IEC61850clAssocFlagsBits` for description.


.. _docref-IEC61850clAARQfieldsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Enabled AARQfields" ":ref:`<ref-IEC61850clAARQfields>`" "AARQfields"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     [:lemonobgtext:`Calling AP Title`] field of outgoing [:lemonobgtext:`AARQ APDU`] message is **disabled** (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     [:lemonobgtext:`Calling AP Title`] field of outgoing [:lemonobgtext:`AARQ APDU`] message is **enabled**

   * :attr:     Bit 1
     :val:      xxxx.xx0x
     :desc:     [:lemonobgtext:`Calling AE Qualifier`] field of outgoing [:lemonobgtext:`AARQ APDU`] message is **disabled** (default value)

   * :(attr):
     :val:      xxxx.xx1x
     :desc:     [:lemonobgtext:`Calling AE Qualifier`] field of outgoing [:lemonobgtext:`AARQ APDU`] message is **enabled**

   * :attr:     Bit 6
     :val:      x0xx.xxxx
     :desc:     [:lemonobgtext:`direct-reference`] (ISO8825-1) in [:lemonobgtext:`Association-information`] field of outgoing [:lemonobgtext:`AARQ APDU`] message is **disabled** (default value)

   * :(attr):
     :val:      x1xx.xxxx
     :desc:     [:lemonobgtext:`direct-reference`] (ISO8825-1) in [:lemonobgtext:`Association-information`] field of outgoing [:lemonobgtext:`AARQ APDU`] message is **enabled**

   * :attr:     Bits 2...5;7
     :val:      Any
     :desc:     Bits reserved for future use

.. _docref-IEC61850clAssocFlagsBits:

.. include-file:: sections/Include/table_flags.rstinc "" "Specific Association Control Service flags" ":ref:`<ref-IEC61850clAssociationFlags>`" "Specific Association Control Service flags"

   * :attr:     Bit 0
     :val:      xxxx.xxx0
     :desc:     **Ignore** [:lemonobgtext:`Responding AP Title`] and [:lemonobgtext:`Responding AE Qualifier`] of the received [:lemonobgtext:`AARE APDU`] message. (default value)

   * :(attr):
     :val:      xxxx.xxx1
     :desc:     **Check** [:lemonobgtext:`Responding AP Title`] and [:lemonobgtext:`Responding AE Qualifier`] of the received [:lemonobgtext:`AARE APDU`] message.
		Communication will not be established if the received values don't match "OSI-AP-Title" and "OSI-AE-Qualifier" in the SCL file.

   * :attr:     Bits 1...7
     :val:      Any
     :desc:     Bits reserved for future use
