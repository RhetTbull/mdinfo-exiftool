
mdinfo-exiftool
===============

Plugin for `mdinfo <https://github.com/RhetTbull/mdinfo>`_ that provides a template interface to `exiftool <https://exiftool.org/>`_.

Synopsis
--------

.. code-block:: bash

   $ mdinfo -p "{exiftool:XMP:Title}" -p "{exiftool:Keywords}" *.jpeg
   flowers.jpeg: Zinia flowers in a field
   pears.jpeg: Pears on a tree fruit pears

Installation
------------

Requires `mdinfo <https://github.com/RhetTbull/mdinfo>`_ to be installed.

.. code-block:: bash

   pip install mdinfo
   pip install mdinfo-exiftool

Template Help
-------------


.. raw:: html

   <!-- [[[cog
   import cog
   from mdinfo_exiftool import get_markdown_help 
   cog.out(
       "\n{}\n".format(get_markdown_help())
   )
   ]]] -->



**Photo and video files (and other files supported by exiftool)**
| Field | Description                                                                 |
| - | --------------------------------------------------------------------------- |
| {exiftool} | Format: '{exiftool:GROUP:TAGNAME}'; use exiftool (https://exiftool.org) to extract metadata, in form GROUP:TAGNAME or TAGNAME, from image. E.g. '{exiftool:Make}' to get camera make, or {exiftool:IPTC:Keywords} to extract keywords. See https://exiftool.org/TagNames/ for list of valid tag names.  Group name is optional (e.g. EXIF, IPTC, etc) but if specified, should be the same as used in ``exiftool -G``\ , e.g. '{exiftool:EXIF:Make}'. exiftool must be installed in the path to use this template field (https://exiftool.org/). |

The ``{exiftool}`` template uses the third-party exiftool app (https://exiftool.org) to extract metadata from photo and video files.

It must be used with one or more subfields which are exiftool tags, for example: ``{exiftool:EXIF:Make}`` for camera make,
or ``{exiftool:IPTC:Keywords}`` for keywords. The exiftool Group name (e.g. ``IPTC``\ ) is optional.

There are two derived subfields: ``created`` and ``modified`` which represent the created date or the modified date, respectively.
These subfields are datetime values and you can access the various attributes of the datetime by using an
attribute name following a period, e.g. ``{exiftool:created.year}`` for the 4-digit year.

The following attributes are supported:

.. list-table::
   :header-rows: 1

   * - Attribute
     - Description
   * - date
     - ISO date, e.g. 2020-03-22
   * - year
     - 4-digit year, e.g. 2021
   * - yy
     - 2-digit year, e.g. 21
   * - month
     - Month name as locale's full name, e.g. December
   * - mon
     - Month as locale's abbreviated name, e.g. Dec
   * - mm
     - 2-digit month, e.g. 12
   * - dd
     - 2-digit day of the month, e.g. 22
   * - dow
     - Day of the week as locale's full name, e.g. Tuesday
   * - doy
     - Julian day of year starting from 001
   * - hour
     - 2-digit hour, e.g. 10
   * - min
     - 2-digit minute, e.g. 15
   * - sec
     - 2-digit second, e.g. 30
   * - strftime
     - Apply strftime template to date/time. Should be used in form {created.strftime,TEMPLATE} where TEMPLATE is a valid strftime template, e.g. {created.strftime,%Y-%U} would result in year-week number of year: '2020-23'. If used with no template will return null value. See https://strftime.org/ for help on strftime templates.



.. raw:: html

   <!-- [[[end]]] -->

