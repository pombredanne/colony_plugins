#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Framework
# Copyright (C) 2008 Hive Solutions Lda.
#
# This file is part of Hive Colony Framework.
#
# Hive Colony Framework is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Colony Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Colony Framework. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision: 5720 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2009-10-21 17:36:22 +0100 (qua, 21 Out 2009) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import types

import colony.libs.list_util
import colony.libs.object_util
import colony.libs.string_buffer_util

import csv_exceptions

DEFAULT_ENCODING = "Cp1252"
""" The default encoding for csv files """

NEWLINE_CHARACTER = "\n"
""" The newline character """

SEPARATOR_CHARACTER = ";"
""" The separator character """

LIST_TYPES = (types.ListType, types.TupleType)
""" A tuple with the various list types """

def dumps(object):
    # creates a new string buffer
    string_buffer = colony.libs.string_buffer_util.StringBuffer()

    # "chunks" the object into the string buffer
    _chunk(object, string_buffer)

    # retrieves the string value from the
    # string buffer
    string_value = string_buffer.get_value()

    # returns the string value
    return string_value

def _chunk(object, string_buffer):
    # retrieves the object type
    object_type = type(object)

    # in case the object type is an instance
    # or a map (dictionary)
    if object_type in (types.InstanceType, types.DictionaryType):
        # converts the object into a list
        object = [object]
    # in case the object type is neither an
    # instance nor a list
    elif not object_type in LIST_TYPES:
        # raises the csv encoder exception
        csv_exceptions.CsvEncodeException("invalid object type")

    # retrieves the (header) attribute names in order to
    # create the header value
    attribute_names = _attribute_names(object)
    header_value = SEPARATOR_CHARACTER.join(attribute_names) + NEWLINE_CHARACTER

    # writes the header value to the string buffer
    string_buffer.write(header_value)

    # iterates over all the object (items)
    # in the object list for serialization
    for object_item in object:
        # retrieves the various object items attribute values
        # (from the previously calculated attribute names)
        attribute_values = colony.libs.object_util.object_attribute_values(object_item, attribute_names)

        # retrieves the attribute values length
        attribute_values_length = len(attribute_values)

        # starts the index value
        index = 0

        # iterates over all the attribute values
        # to write them to the string buffer
        for attribute_value in attribute_values:
            # retrieves the attribute value type
            attribute_value_type = type(attribute_value)

            # encodes the attribute value using the default encoding
            attribute_value_encoded = attribute_value_type == types.UnicodeType and attribute_value.encode(DEFAULT_ENCODING) or (attribute_value and str(attribute_value))

            # writes the encoded attribute value (in case
            # the value is valid)
            attribute_value_encoded and string_buffer.write(attribute_value_encoded)

            # in case the current index represents
            # the last attribute
            if index == attribute_values_length - 1:
                # continue the loop skipping the separator
                # character writing
                continue

            # writes the separator character
            string_buffer.write(SEPARATOR_CHARACTER)

            # increments the index
            index += 1

        # writes the new line in the string buffer
        string_buffer.write(NEWLINE_CHARACTER)

def _attribute_names(object):
    # retrieves the first element (for initial
    # set reference)
    object_item = object[0]

    # creates the first and initial set of attribute names
    # from the first object item
    attribute_names = colony.libs.object_util.object_attribute_names(object_item)

    # iterates over all the other object items in the set
    # in order to intersect the attributes name list with the
    # previous
    for object_item in object:
        # retrieves the object attribute names for the current
        # object item value
        object_attribute_names = colony.libs.object_util.object_attribute_names(object_item)

        # intersects the attribute names list with the object attribute names
        # list to calculate the current attribute names
        attribute_names = colony.libs.list_util.list_intersect(attribute_names, object_attribute_names)

    # returns the attribute names
    return attribute_names

def loads(data):
    # strips the data from extra lines
    # (avoids possible problems)
    data = data.strip()

    # splits the data around the new line character
    chunks = [value.strip() for value in data.split(NEWLINE_CHARACTER)]

    # "dechunks" the data (retrieving the object list)
    object = _dechunk(chunks)

    # returns the object (list)
    return object

def _dechunk(chunks):
    # creates the object list
    object_list = []

    # retrieves the header value
    header_value = chunks[0]

    # retrieves the various header names
    header_names = [value.strip() for value in header_value.split(SEPARATOR_CHARACTER)]

    # retrieves the "various" content values
    content_values = chunks[1:]

    # iterates over all the content
    # in the content values
    for content in content_values:
        # creates a new (csv) object (map)
        object = {}

        # retrieves the various object attributes
        object_attributes = [value.strip() for value in content.split(SEPARATOR_CHARACTER)]

        # starts the index value
        index = 0

        # iterates over all the object attributes
        # to set them in the object
        for attribute in object_attributes:
            # retrieves the (current) attribute name
            # from the header names
            attribute_name = header_names[index]

            # set the attribute in the object
            object[attribute_name] = attribute

            # increments the index value
            index += 1

        # adds the object to the object list
        object_list.append(object)

    # returns the object list
    return object_list