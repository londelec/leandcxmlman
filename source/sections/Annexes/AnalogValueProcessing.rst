
.. _docref-AIProcessing:

Analog value processing
=======================

This annex contains information about analog value processing, scaling options and application examples.
All analog values are converted to Short Floating-point (32bit) numbers internally before scaling takes place.
All AI scaling attributes used in this document:
:ref:`xmlattr-IEC10xmaAICoeff`, :ref:`xmlattr-IEC10xmaAIDeadband`, :ref:`xmlattr-IEC10xmaAIPercent`, :ref:`xmlattr-IEC10xmaAIStartOffset`, :ref:`xmlattr-IEC10xmaAIZeroDeadband`, :ref:`xmlattr-IEC10xmaAIOffset`, :ref:`xmlattr-IEC10xmaAIOffsetDeadband`, :ref:`xmlattr-IEC10xmaAINonZeroOffset`
are Short Floating-point numbers.
The value range is given for each of these attributes and values have to be specified either in decimal or scientific notation.
Sample values are shown in the table below.

.. field-list-table:: Analog value notations
   :class: table table-condensed table-bordered table-left table-center-all
   :name: tabid-analognotation
   :spec: |C{0.14}|C{0.14}|
   :header-rows: 1

   * :dec,10: Decimal
     :sci,10: Scientific

   * :dec:	1520.3
     :sci:	1.5203e3

   * :dec:	-11
     :sci:	-1.1e1

   * :dec:	0.00152
     :sci:	1.52e-3

   * :dec:	-0.0456
     :sci:	-4.56e-2

.. important::
   Precision of the Short Floating-point number is **7** decimal digits regardless of position of the decimal point.
   This applies to decimal and scientific notations.
   For example there are 7 decimal digits in numbers '1234567' '1234.567' '1.234567e3' which is the maximum accuracy.
   Numbers with more decimal digits will be rounded.

.. _docref-AIScaling:

Analog value scaling
--------------------

Analog value scaling attributes 
:ref:`xmlattr-IEC10xmaAICoeff`, :ref:`xmlattr-IEC10xmaAIStartOffset`, :ref:`xmlattr-IEC10xmaAIZeroDeadband`, :ref:`xmlattr-IEC10xmaAIOffset`, :ref:`xmlattr-IEC10xmaAIOffsetDeadband`, :ref:`xmlattr-IEC10xmaAINonZeroOffset`
exist in Master and Slave protocol instances and scaling processes are independent of each other.
This means analog value received from an outstation will be scaled at Master protocol instance first and then by a Slave protocol instance before sending the value out.
It is recommended to enable scaling at Master protocol instances that receive analog values from outstations, but there are no restrictions that would prevent using scaling at Slave protocol instances.
Analog value scaling sequence in shown in the flowchart below.

.. figure:: ../_images/AI_scaling_flow.*
   :name: figid-aiscaling
   :figclass: figure-left

   AI scaling sequence

.. tip::

   :ref:`xmlattr-IEC10xmaAIStartOffset` attribute automatically sets Invalid [:lemonobgtext:`IV`] quality flag when forcing analog value to zero '0'.
   This is designed to detect failure of a 4-20mA tranducer (or similar) connected to an Analog Input.
   4mA current is expecet when transducer is connected even if it is not measuring anything.
   If the current drops below 4mA Invalid [:lemonobgtext:`IV`] quality flag is used to indicate a transducer failure or disconnect.
   :ref:`xmlattr-IEC10xmaAIZeroDeadband` attribute works alongside :ref:`xmlattr-IEC10xmaAIStartOffset` in order to suppress noise around 4mA value and its use is receommended.

Scaling calculator below shows how |leandcapp| analog scaling actually works.
Enter a numeric value in the box 'Start value' and the 'Result' box will show the value after scaling has been applied.
Scaling attributes are arranged in the order they are applied as shown in the sequence flowchart above.
Calculator shows intermediate values after each attribute as well as basic math that was applied in each step.
Any changes to scaling attributes are applied instantly and the result will be updated accordingly.
The 'Copy' button on the top left corner can be used to copy scaling attributes and their entered values to clipboard.
They will be formated in XML syntax and can be pasted directly into XML file.

.. include-html:: ../_html/AIcalc.html
   :start-after: <!--start_scaling-->
   :end-before: <!--end_scaling-->
   :caption: AI scaling calculator
   :latex-tip: Interactive scaling attribute calculator can be found in the current HTML manual

Range calculator shown below enables to calculate :ref:`xmlattr-IEC10xmaAIOffset` and :ref:`xmlattr-IEC10xmaAICoeff` attribute values based on ranges of analog values before and after scaling.
The range of values before scaling takes place (e.g. range of values expected to be received from outstation) have to be entered into 'Input Range' boxes
and the range of resulting values (e.g. expected from |leandcapp|) have to be entered into 'Output Range' boxes.
'Calculate' button will update :ref:`xmlattr-IEC10xmaAIOffset` and :ref:`xmlattr-IEC10xmaAICoeff` attributes of the scaling calculator above.
Updated attributes will be highlighted yellow.

.. include-html:: ../_html/AIcalc.html
   :start-after: <!--start_rangecalc-->
   :end-before: <!--end_rangecalc-->
   :caption: AI range calculator
   :latex-tip: Interactive scaling range calculator can be found in the current HTML manual

Application example shown below can be used to calculate :ref:`xmlattr-IEC10xmaAIStartOffset`, :ref:`xmlattr-IEC10xmaAIOffset`, :ref:`xmlattr-IEC10xmaAINonZeroOffset` and :ref:`xmlattr-IEC10xmaAICoeff` attributes by selecting various devices as a source of an analog value.
LEANDC box performs scaling based on attributes of the scaling calculator above.
'Analog Input Module' checkbox simulates the Analog Input Module connected to LEANDC.
Its input range in milliamps and output integer range (based on ADC bit count) can be selected.
Changing analog value at Analog Module Input will update value at Module output and LEANDC output (after scaling).  
The 'Calculate' button must be pressed when devices are enabled/disabled or input/output ranges changed in order to update :ref:`xmlattr-IEC10xmaAIStartOffset`, :ref:`xmlattr-IEC10xmaAIOffset`, :ref:`xmlattr-IEC10xmaAINonZeroOffset` and :ref:`xmlattr-IEC10xmaAICoeff` attributes of the scaling calculator above.
Updated attributes will be highlighted yellow.
Measuring transducer and Voltage/Current transformer can be enabled/disabled with drop-down box and checkbox respectively.
Please note the transducer can be enabled only if Analog Input Module is already enabled and Voltage/Current transformer can be enabled if both transducer and Analog Input Module are enabled.
The input/output ranges can be selected from pre-defined values listed in drop-down boxes of each device and custom values can be entered manually.

.. include-html:: ../_html/AIcalc.html
   :start-after: <!--start_applsample1-->
   :end-before: <!--end_applsample1-->
   :caption: AI application example
   :latex-tip: Interactive application example can be found in the current HTML manual

.. _docref-ReceivedAIProcessing:

Received AI processing
----------------------

Flowchart below shows AI value processing when IEC60870-5-101/103/104 Master protocol instance receives
AI object from outstation. This processing takes place after AI scaling has been completed, refer to previous
annexes for additional information on AI scaling.

.. figure:: ../_images/AI_processing_2.*
   :align: center

   Received AI processing flowchart

The figure below shows how a real time value received from outstation will be processed if :ref:`xmlelem-IEC10xmaAI`.\ :ref:`xmlattr-IEC10xmaAIDeadband` \
attribute is enabled. Internal database will be updated and AI event will get generated every time a real time
value exceeds 'static deadband'. Thresholds of the 'static deadband' are calculated based on previous value
stored in the database. Attribute :ref:`xmlelem-IEC10xmaAI`.\ :ref:`xmlattr-IEC10xmaAIDeadband` \ = 2 is used as an example.

.. figure:: ../_images/AI_processing_3.*
   :align: center

   :ref:`xmlattr-IEC10xmaAIDeadband` processing sample

The figure below shows how a real time value received from outstation will be processed if :ref:`xmlelem-IEC10xmaAI`.\ :ref:`xmlattr-IEC10xmaAIPercent` \ attribute
is enabled. Internal database will be updated and AI event will get generated every time a real time value
exceeds 'dynamic deadband'. Thresholds of the 'dynamic deadband' are calculated based on previous value
stored in the database. Attribute :ref:`xmlelem-IEC10xmaAI`.\ :ref:`xmlattr-IEC10xmaAIPercent` \ = 20 is used as an example.

.. figure:: ../_images/AI_processing_4.*
   :align: center

   :ref:`xmlattr-IEC10xmaAIPercent` processing sample

