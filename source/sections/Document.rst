.. include:: global.roles

Document
========

Abbreviations used in this document are listed in the following table.

.. field-list-table:: Abbreviations
   :class: table table-condensed table-bordered longtable
   :name: tabid-Abbreviations
   :spec: |C{0.2}|S{0.6}|
   :header-rows: 1

   * :abbr,10,center:	Abbreviation
     :desc,90:		Description
   * :abbr:	ADC
     :desc:	Analog Digital Converter
   * :abbr:	AI
     :desc:	Analog Input
   * :abbr:	AO
     :desc:	Analog Output
   * :abbr:	APCI
     :desc:	Application Protocol Control Interface
   * :abbr:	APDU
     :desc:	Application Protocol Data Unit
   * :abbr:	ASDU
     :desc:	Application Service Data Unit
   * :abbr:	CAA
     :desc:	Common Address of ASDU
   * :abbr:	CID
     :desc:	Configured IED Description
   * :abbr:	COT
     :desc:	Cause Of Transmission
   * :abbr:	CPU
     :desc:	Central Processing Unit
   * :abbr:	DI
     :desc:	Digital Input
   * :abbr:	DO
     :desc:	Digital Output
   * :abbr:	DPI
     :desc:	Double Point Information
   * :abbr:	DST
     :desc:	Daylight Saving Time
   * :abbr:	GPIO
     :desc:	General Purpose Input Output
   * :abbr:	HMI
     :desc:	Human Machine Interface
   * :abbr:	IANA
     :desc:	Internet Assigned Numbers Authority
   * :abbr:	ICD
     :desc:	IED Capabilities Description
   * :abbr:	IED
     :desc:	Intelligent Electronic Device
   * :abbr:	IO
     :desc:	Input/Output
   * :abbr:	IP
     :desc:	Internet Protocol
   * :abbr:	IOA
     :desc:	Information Object Address
   * :abbr:	LD
     :desc:	Logical Device (for IEC61850)
   * :abbr:	LN
     :desc:	Logical Node (for IEC61850)
   * :abbr:	LRU
     :desc:	Logical Remote Unit
   * :abbr:	PC
     :desc:	Personal Computer
   * :abbr:	PID
     :desc:	Running Process Identifier
   * :abbr:	PLC
     :desc:	Programmable Logic Controller
   * :abbr:	OS
     :desc:	|opsystem|
   * :abbr:	SCADA
     :desc:	Supervisory Control And Data Acqusition system
   * :abbr:	SCD
     :desc:	Substation Configuration Description
   * :abbr:	SCL
     :desc:	System Configuration description Language
   * :abbr:	SPI
     :desc:	Single Point Information
   * :abbr:	SSH
     :desc:	Secure SHell
   * :abbr:	TCP
     :desc:	Transmission Control Protocol
   * :abbr:	UDP
     :desc:	User Datagram Protocol
   * :abbr:	XML
     :desc:	eXtensible Markup Language

Text styles used in this manual:

:xmlstyle:`Dark blue used for XML elements and attributes`

:leubold:`Links to tables and manual sections are bold underlined`

:bitref:`Links to bits of bit-encoded attributes are italic underlined`

:inlinetip:`Notes in green for additional information on how to use attribute/setting`

:inlineimportant:`Important information on how to use attribute/setting in red`

:lemonobgtext:`Highlighted text refers to keywords found in communication standards`

.. tip:: Generic tips in a green box

.. important:: Important notes in a red box

.. note:: Various notes

Introduction
------------

This document contains information on how to set up |leandcapp|.
Configuration of |leandcapp| consists of several XML files and contents of these files are described in this document.

| |leandcapp| is distributed as a compiled binary file that can be executed on a 32bit or 64bit |linuxos|.
| Application installer contains separate binary files for the following CPU architectures:
| > Intel x86
| > ARM926EJ-S

Application can be used on any hardware with these processors.
List of hardwares that application have been tested on is summarized in the table below.

.. field-list-table:: Supported hardware
   :class: table table-condensed table-bordered longtable table-left
   :name: tabid-SupportedHW
   :spec: |S{0.3}|C{0.2}|C{0.2}|
   :header-rows: 1

   * :hw,30:		Model
     :cpu,20,center:	Processor
     :arch,20,center:	CPU Architecture
   * :hw:	Londelec LEIODC-X32
     :cpu:	Freescale i.MX287
     :arch:	ARM926EJ-S (32bit)
   * :hw:	Advantech ARK-2120F
     :cpu:	Intel Atom D2550
     :arch:	x64 (64bit)
   * :hw:	Advantech ARK-3360F
     :cpu:	Intel Atom N450
     :arch:	x64 (64bit)
   * :hw:	Advantech UNO-1172AH
     :cpu:	Intel Atom D510
     :arch:	x64 (64bit)
   * :hw:	Advantech UNO-1372G-J
     :cpu:	Intel Celeron J1900
     :arch:	x64 (64bit)
   * :hw:	Advantech UNO-2484G
     :cpu:	Intel Core i3-6100U
     :arch:	x64 (64bit)
   * :hw:	Advantech ARK-3202F
     :cpu:	Intel Atom N270
     :arch:	x86 (32bit)
   * :hw:	Advantech UNO-1150G
     :cpu:	AMD Geode LX800
     :arch:	x86 (32bit)

