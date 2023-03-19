
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

``{exiftool}``

Format: ``{exiftool:GROUP:TAGNAME}``; use exiftool (https://exiftool.org) to extract metadata, in form GROUP:TAGNAME or TAGNAME, from image. E.g. ``{exiftool:Make}`` to get camera make, or ``{exiftool:IPTC:Keywords}`` to extract keywords. See https://exiftool.org/TagNames/ for list of valid tag names.  Group name is optional (e.g. EXIF, IPTC, etc) but if specified, should be the same as used in ``exiftool -G``\ , e.g. ``{exiftool:EXIF:Make}``. exiftool must be installed in the path to use this template field (https://exiftool.org/).

The ``{exiftool}`` template uses the third-party exiftool app (https://exiftool.org) to extract metadata from photo and video files.

It must be used with one or more subfields which are exiftool tags, for example: ``{exiftool:EXIF:Make}`` for camera make,
or ``{exiftool:IPTC:Keywords}`` for keywords. The exiftool Group name (e.g. ``IPTC``\ ) is optional.

There are two derived subfields: ``created`` and ``modified`` which represent the created date or the modified date, respectively.
These subfields are datetime values and you can access the various attributes of the datetime by using an
attribute name following a period, e.g. ``{exiftool:created.year}`` for the 4-digit year.  This follows the conventions of mdinfo date/time fields.
