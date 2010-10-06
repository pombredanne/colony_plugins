#!/usr/bin/python
# -*- coding: Cp1252 -*-

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

__author__ = "Jo�o Magalh�es <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision: 3219 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2009-05-26 11:52:00 +0100 (ter, 26 Mai 2009) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import binascii

def encode_long(long_value):
    """
    Encode a long to a two's complement little-endian binary string.
    Note that 0L is a special case, returning an empty string, to save a
    byte.

    @type long_value: int
    @param long_value: The long value to be encoded.
    @rtype: String
    @return: The encoded two's complement little-endian binary string.
    """

    # in case the long value is zero
    if long_value == 0:
        # returns empty string
        return ""
    # in case the long value is larger
    # than zero
    elif long_value > 0:
        # converts the long value to the hexadecimal string value
        long_value_hexadecial = hex(long_value)

        # assets that the hexadecimal starts with the hexadecimal
        # initialization value
        assert long_value_hexadecial.startswith("0x")

        # calculates the number of "junk" characters
        number_junk_characters = 2 + long_value_hexadecial.endswith("L")

        nibbles = len(long_value_hexadecial) - number_junk_characters

        if nibbles & 1:
            # need an even # of nibbles for unhexlify
            long_value_hexadecial = "0x0" + long_value_hexadecial[2:]
        elif int(long_value_hexadecial[2], 16) >= 8:
            # looks negative so need a byte of sign bits
            long_value_hexadecial = "0x00" + long_value_hexadecial[2:]
    else:
        # Build the 256's-complement:  (1L << nbytes) + x.  The trick is
        # to find the number of bytes in linear time (although that should
        # really be a constant-time task)
        long_value_hexadecial = hex(-long_value)
        assert long_value_hexadecial.startswith("0x")
        njunkchars = 2 + long_value_hexadecial.endswith('L')
        nibbles = len(long_value_hexadecial) - njunkchars
        if nibbles & 1:
            # extends to a full byte.
            nibbles += 1
        nbits = nibbles * 4
        long_value += 1L << nbits
        assert long_value > 0
        long_value_hexadecial = hex(long_value)
        njunkchars = 2 + long_value_hexadecial.endswith('L')
        newnibbles = len(long_value_hexadecial) - njunkchars
        if newnibbles < nibbles:
            long_value_hexadecial = "0x" + "0" * (nibbles - newnibbles) + long_value_hexadecial[2:]
        if int(long_value_hexadecial[2], 16) < 8:
            # "looks positive", so need a byte of sign bits
            long_value_hexadecial = "0xff" + long_value_hexadecial[2:]

    # in case the long value hexadeciaml ends with the long
    # indication value
    if long_value_hexadecial.endswith("L"):
        # removes the last character to avoid the extra long indication
        long_value_hexadecial = long_value_hexadecial[2:-1]
    # otherwise
    else:
        # sets the normal value without the "0x" initialization
        long_value_hexadecial = long_value_hexadecial[2:]

    assert len(long_value_hexadecial) & 1 == 0, (long_value, long_value_hexadecial)

    binary = binascii.unhexlify(long_value_hexadecial)

    # reverses the binary value
    reversed_binary = binary[::-1]

    # returns the reversed binary value
    return reversed_binary

def decode_long(data):
    """
    Decode a long from a two's complement little-endian binary string.

    @type data: String
    @param data: The data to be used in the decoding.
    @rtype: int
    @return: The decoded data.
    """

    # retrieves the data length
    data_length = len(data)

    # in case the data length is zero
    if data_length == 0:
        # return zero
        return 0L

    # converts the (inverted) data to hexadecimal string
    long_value_hexadecial = binascii.hexlify(data[::-1])

    # converts the long value hexadecimal to integer
    # using base 16
    long_value = long(long_value_hexadecial, 16)

    # in case the last digit is 0x80 (negative)
    if data[-1] >= '\x80':
        # puts the negative indication as the last digit
        long_value -= 1L << (data_length * 8)

    # returns the long value
    return long_value
