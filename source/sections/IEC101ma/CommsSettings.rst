.. _docref-IEC101maCommsSettingsAttr:

CommsSettings attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Communication state reporting and related delays can be specified using attributes of :ref:`CommsSettings<ref-IEC101maCommsSettings>` 
element node.

Please see sample :ref:`CommsSettings<ref-IEC101maCommsSettings>` node and the table listing all available attributes below.

.. code-block:: none

   <CommsSettings	NoRespCount="5"
                        DegradedRetries="5"
                        DegradedTimeout="600"
                        ControlLockTimer="20"
                        OfflineDelay="10"
                        PostOfflineDelay="1000"
                        OnlineGIDelay="10" />

.. _docref-IEC101maCommsSettingsAttab:

.. field-list-table:: IEC 60870-5-101 Master CommsSettings attributes
   :class: table table-condensed table-bordered longtable
   :spec: |C{0.20}|C{0.25}|S{0.55}|
   :header-rows: 1

   * :attr,10: Attribute
     :val,15:  Values or range
     :desc,75: Description
     
.. include-file:: sections/Include/serma_CommsSettings.rstinc "" ".. _ref-IEC101maCommsSettingsNoRespCount:" ".. _ref-IEC101maCommsSettingsDegradedRetries:" ".. _ref-IEC101maCommsSettingsDegradedTimeout:"

.. include-file:: sections/Include/IEC10xma_ControlLockTimer.rstinc "" ".. _ref-IEC101maCommsSettingsControlLockTimer:"

.. include-file:: sections/Include/serma_OfflineDelay.rstinc "" ".. _ref-IEC101maCommsSettingsOfflineDelay:"

.. include-file:: sections/Include/PostOfflineDelay.rstinc "" ".. _ref-IEC101maCommsSettingsPostOfflineDelay:" ":ref:`OfflineDelay<ref-IEC101maCommsSettingsOfflineDelay>`"

.. include-file:: sections/Include/IEC10xma_OnlineGIDelay.rstinc "" ".. _ref-IEC101maCommsSettingsOnlineGIDelay:"
