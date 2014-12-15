
ASDUSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^

Application layer settings can be specified using attributes of :ref:`ASDUSettings<ref-IEC101maASDUSettings>` element node.

Please see sample :ref:`ASDUSettings<ref-IEC101maASDUSettings>` node and the table listing all available attributes below.

.. code-block:: none

 <ASDUSettings  COTSize="1"
		CAASize="1"
		IOASize="2"
		InvalidEvent="1"
		IgnoreTimetags="1"
		SUthroughoutDST="1"
		AIDeadband="2"
		AIPercent="0.5"
		DOQOC="1"
		DOType="46"
		AOType="50"
		DIEventStartup="1"
		AIEventStartup="1" />

.. _ref-IEC101maASDUSettingsAttributes:

.. field-list-table:: IEC 60807-5-101 Master ASDUSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
   * :attr:    .. _ref-IEC101maASDUSettingsCOTSize:
            
               :xmlref:`COTSize`
     :val:     1 or 2
     :desc:    Cause Of Transmission size in bytes including Originator address (default 1 byte, if originator address is not used)

   * :attr:    .. _ref-IEC101maASDUSettingsCAASize:
   
               :xmlref:`CAASize`
     :val:     1 or 2
     :desc:    Common address of ASDU size in bytes (default 1 byte)

   * :attr:    .. _ref-IEC101maASDUSettingsIOASize:
            
               :xmlref:`IOASize`
     :val:     1; 2 or 3
     :desc:    Information Object Address size in bytes (default 2 bytes)

.. include-file:: sections/Include/IEC10xma_ASDU_IVSU.rstinc

.. include-file:: sections/Include/AIcommon_Thresholds.rstinc "" ".. _ref-IEC101maASDUSettingsAIDeadband:" ".. _ref-IEC101maASDUSettingsAIPercent:" ":ref:`AI<ref-IEC10xmaAI>`" ":ref:`Deadband<ref-IEC10xmaAIDeadband>`" ":ref:`Percent<ref-IEC10xmaAIPercent>`"

   * :attr:    .. _ref-IEC101maASDUSettingsDOQOC:
            
               :xmlref:`DOQOC`
     :val:     See table :numref:`ref-IEC10xmaDOQOCValues` for description
     :desc:    Qualifier Of Command (QOC) is used to set additional information (e.g. [no additional definition];  [short-pulse duration]) when command is being sent to the DO object which doesn't have :ref:`DO<ref-IEC10xmaDO>`.\ :ref:`QOC<ref-IEC10xmaDOQOC>` \ attribute specified in its element node. Refer to table :numref:`ref-IEC10xmaDOQOCValues` for :xmlref:`QOC` values. (default value 0 [no additional definition])

   * :attr:    .. _ref-IEC101maASDUSettingsDOType:
            
               :xmlref:`DOType`
     :val:     See table :numref:`ref-IEC10xmaDOTypeIDValues` for description
     :desc:    DO ASDU type is used when command is being sent to the DO object which doesn't have :ref:`DO<ref-IEC10xmaDO>`.\ :ref:`TypeID<ref-IEC10xmaDOTypeID>` \ attribute specified in its element node. Refer to table :numref:`ref-IEC10xmaDOTypeIDValues` for :xmlref:`TypeID` values. (there is no default value, ASDU TypeID is transparent if neither this element nor :ref:`DO<ref-IEC10xmaDO>`.\ :ref:`TypeID<ref-IEC10xmaDOTypeID>` \ attribute is used)

   * :attr:    .. _ref-IEC101maASDUSettingsAOType:
            
               :xmlref:`AOType`
     :val:     See table :numref:`ref-IEC10xmaAOTypeIDValues` for description
     :desc:    AO ASDU type is used when command is being sent to the AO object which doesn't have :ref:`AO<ref-IEC10xmaAO>`.\ :ref:`TypeID<ref-IEC10xmaAOTypeID>` \ attribute specified in its element node. Refer to table :numref:`ref-IEC10xmaAOTypeIDValues` for :xmlref:`TypeID` values. (there is no default value, ASDU TypeID is transparent if neither this element nor :ref:`AO<ref-IEC10xmaAO>`.\ :ref:`TypeID<ref-IEC10xmaAOTypeID>` \ attribute is used)

.. include-file:: sections/Include/IEC10xma_ASDU_EventStartup.rstinc

