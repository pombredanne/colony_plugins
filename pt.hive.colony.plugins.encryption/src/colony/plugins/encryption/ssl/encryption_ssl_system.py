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

__revision__ = "$LastChangedRevision: 428 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-11-20 18:42:55 +0000 (Qui, 20 Nov 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import base64

BASE_64_ENCODED_MAXIMUM_SIZE = 64
""" The base 64 encoded maximum size """

class EncryptionSsl:
    """
    The encryption ssl class.
    """

    encryption_ssl_plugin = None
    """ The encryption ssl plugin """

    def __init__(self, encryption_ssl_plugin):
        """
        Constructor of the class.

        @type encryption_ras_plugin: EncryptionSslPlugin
        @param encryption_ras_plugin: The encryption ssl plugin.
        """

        self.encryption_ssl_plugin = encryption_ssl_plugin

    def create_structure(self, parameters):
        # retrieves the encryption rsa plugin
        encryption_rsa_plugin = self.encryption_ssl_plugin.encryption_rsa_plugin

        # retrieves the encryption pkcs 1 plugin
        encryption_pkcs_1_plugin = self.encryption_ssl_plugin.encryption_pkcs_1_plugin

        # creates the ssl structure
        ssl_structure = SslStructure(encryption_rsa_plugin, encryption_pkcs_1_plugin)

        # returns the ssl structure
        return ssl_structure

class SslStructure:
    """
    Class representing the ssl,
    cryptographic protocol structure.
    """

    encryption_rsa_plugin = None
    """ The encryption rsa plugin """

    encryption_pkcs_1_plugin = None
    """ The encryption pkcs 1 plugin """

    def __init__(self, encryption_rsa_plugin, encryption_pkcs_1_plugin):
        """
        Constructor of the class.

        @type encryption_rsa_plugin: EncryptionRsaPlugin
        @param encryption_rsa_plugin: The encryption rsa plugin.
        @type encryption_pkcs_1_plugin: EncryptionPkcs1Plugin
        @param encryption_pkcs_1_plugin: The encryption pkkc 1 plugin.
        """

        self.encryption_rsa_plugin = encryption_rsa_plugin
        self.encryption_pkcs_1_plugin = encryption_pkcs_1_plugin

    def sign_base_64(self, private_key_path, hash_algorithm_name, base_string_value):
        # signs the base string value using the hash algorithm
        # with the given name and retrieving the signature
        signature = self.sign(private_key_path, hash_algorithm_name, base_string_value)

        # encodes the signature into base 64
        signature_base_64 = base64.b64encode(signature)

        # splits the signature base 64 value
        signature_base_64 = self._split_base_64(signature_base_64)

        # returns the signature base 64
        return signature_base_64

    def verify_base_64(self, public_key_path, signature_base_64, base_string_value):
        # joins the base 64 value back
        signature_base_64 = self._join_base_64(signature_base_64)

        # decodes the signature base 64
        signature = base64.b64decode(signature_base_64)

        # verifies the signature against the base string value,
        # and returns the return value
        return_value = self.verify(public_key_path, signature, base_string_value)

        # returns the return value
        return return_value

    def sign(self, private_key_path, hash_algorithm_name, base_string_value):
        # creates the rsa structure
        rsa_structure = self.encryption_rsa_plugin.create_structure({})

        # creates the pkcs 1 structure
        pkcs_1_structure = self.encryption_pkcs_1_plugin.create_structure({})

        # loads the private key, retrieving the keys tuple and the version value
        keys, _version = pkcs_1_structure.load_read_private_key_pem(private_key_path)

        # sets the keys in the rsa structure
        rsa_structure.set_keys(keys)

        # signs the base string value using the given hash algorithm name
        signature_verified = pkcs_1_structure.sign(keys, hash_algorithm_name, base_string_value)

        # signs the signature verified retrieving the signature
        signature = rsa_structure.sign(signature_verified)

        # returns the signature
        return signature

    def verify(self, public_key_path, signature, base_string_value):
        # creates the rsa structure
        rsa_structure = self.encryption_rsa_plugin.create_structure({})

        # creates the pkcs 1 structure
        pkcs_1_structure = self.encryption_pkcs_1_plugin.create_structure({})

        # loads the public key, retrieving the keys tuple
        keys = pkcs_1_structure.load_read_public_key_pem(public_key_path)

        # sets the keys in the rsa structure
        rsa_structure.set_keys(keys)

        # verifies the signature (using the public key) and
        # retrieves the signature verified
        signature_verified = rsa_structure.verify(signature)

        # verifies the and tests the signature, retrieving the return value
        return_value = pkcs_1_structure.verify(signature_verified, base_string_value)

        # returns the return value
        return return_value

    def _split_base_64(self, string_value):
        # retrieves the string value length
        string_value_length = len(string_value)

        # starts the base index
        base_index = 0

        # creates the list
        string_value_list = []

        # iterates continuously
        while True:
            # in case the base index is greater or equal
            # to the private key der encoded length
            if base_index >= string_value_length:
                # breaks the loop
                break

            # calculates the end index from the base index
            end_index = base_index + BASE_64_ENCODED_MAXIMUM_SIZE

            # retrieves the string value token
            string_value_token = string_value[base_index:end_index]

            # creates the string value from the string value token
            # and a newline character
            string_value_line = string_value_token + "\n"

            # adds the string value line to the string value list
            string_value_list.append(string_value_line)

            # sets the base index as the end index
            base_index = end_index

        # joins the string value list retrieving the
        # string value splitted
        string_value_splitted = "".join(string_value_list)

        # returns the string value splitted
        return string_value_splitted

    def _join_base_64(self, string_value):
        # removes the newline characters to obtain
        # the plain base 64 value
        string_value_joined = string_value.replace("\n", "")

        # returns the string value joined
        return string_value_joined