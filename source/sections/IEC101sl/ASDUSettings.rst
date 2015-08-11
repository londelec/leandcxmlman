.. _docref-IEC101slASDUSettingsAttr:

ASDUSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`ASDUSettings<ref-IEC101slASDUSettings>` element node.

Please see sample :ref:`ASDUSettings<ref-IEC101slASDUSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <ASDUSettings COTSize="1" CAASize="1" IOASize="2" InvalidEvent="1" SUthroughoutDST="1" DIEventType="2" AIEventType="14" DOType="46" AOType="50" DIInterDelay="8000" DIIndetDelay="3500" DIEventStartup="1" AIEventStartup="1" TimeSync="1" TranspTypes="1" ForwardGI="1" />

.. _docref-IEC101slASDUSettingsAttab:

.. field-list-table:: IEC 60870-5-101 Slave ASDUSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10:  Attribute
     :val,15:   Values or range
     :desc,75:  Description
     
   * :attr:     :xmlref:`COTSize`
     :val:      1 or 2
     :desc:     Cause Of Transmission size in bytes including Originator address (default 1 byte, if originator address is not used)

   * :attr:     .. _ref-IEC101slASDUSettingsCAASize:
   
                :xmlref:`CAASize`
     :val:      1 or 2
     :desc:     Common Address of ASDU size in bytes (default 1 byte)

   * :attr:     :xmlref:`IOASize`
     :val:      1; 2 or 3
     :desc:     Information Object Address size in bytes (default 2 bytes)

.. include-file:: sections/Include/IEC60870_InvalidEvent.rstinc

.. include-file:: sections/Include/IEC60870_SUthroughoutDST.rstinc
  
   * :attr:     :xmlref:`DIEventType`
     :val:      See table :numref:`ref-IEC10xslDITypeIDValues`
     :desc:     Use this ASDU type to send DI events which don't have :ref:`DI<ref-IEC10xslDI>`.\ :ref:`TypeID<ref-IEC10xslDITypeID>` \ attribute specified in their element node. This setting also affects ASDU type of the static data (e.g. Single or Double status information) reported to a General Interrogation request. (default value 2 – 'Single-point Information', DI event will be sent using ASDU type 2 [M_SP_TA_1], **CP24time2A**, msec and min)

   * :attr:     :xmlref:`AIEventType`
     :val:      See table :numref:`ref-IEC10xslAITypeIDValues`
     :desc:     Use this ASDU type to send AI events which don't have :ref:`AI<ref-IEC10xslAI>`.\ :ref:`TypeID<ref-IEC10xslAITypeID>` \ attribute specified in their element node. This setting also affects ASDU type of the static data (e.g. Normalized, Scaled, Short floating point) reported to a General Interrogation request. (default value 14 – 'Short floating point', AI event will be sent using ASDU type 14 [M_ME_TC_1], **CP24time2A**, msec and min)

.. include-file:: sections/Include/IEC10xsl_ASDU.rstinc "" ".. _ref-IEC101slASDUSettingsTranspTypes:"

.. include-file:: sections/Include/IEC60870_ForwardGI.rstinc

