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

import time
import struct
import threading

import colony.libs.map_util
import colony.libs.string_buffer_util

DEFAULT_HOST = "224.0.0.251"
""" The default port """

DEFAULT_PORT = 5353
""" The default port """

DEFAULT_PERSISTENT = False
""" The default persistent """

DEFAULT_SOCKET_NAME = "datagram"
""" The default socket name """

DEFAULT_SOCKET_PARAMETERS = {
    "multicast_address" : (DEFAULT_HOST, DEFAULT_PORT)
}
""" The default socket parameters """

REQUEST_TIMEOUT = 10
""" The request timeout """

RESPONSE_TIMEOUT = 10
""" The response timeout """

MESSAGE_MAXIMUM_SIZE = 512
""" The message maximum size """

MESSAGE_HEADER_SIZE = 12
""" The size of the mdns message header (in bytes) """

NORMAL_REQUEST_VALUE = 0x0100
""" The normal request value """

TYPES_MAP = {
    "A" : 0x01,
    "NS" : 0x02,
    "MD" : 0x03,
    "MF" : 0x04,
    "CNAME" : 0x05,
    "SOA" : 0x06,
    "MB" : 0x07,
    "MG" : 0x08,
    "MR" : 0x09,
    "NULL" : 0x0a,
    "WKS" : 0x0b,
    "PTR" : 0x0c,
    "HINFO" : 0x0d,
    "MINFO" : 0x0e,
    "MX" : 0x0f,
    "TXT" : 0x10,
    "RP" : 0x11,
    "AFSDB" : 0x12,
    "X25" : 0x13,
    "ISDN" : 0x14,
    "RT" : 0x15,
    "NSAP" : 0x16,
    "NSAP-PTR" : 0x17,
    "SIG" : 0x18,
    "KEY" : 0x19,
    "PX" : 0x1a,
    "GPOS" : 0x1b,
    "AAAA" : 0x1c,
    "LOC" : 0x1d,
    "NXT" : 0x1e,
    "EID" : 0x1f,
    "NIMLOC" : 0x20,
    "SRV" : 0x21,
    "ATMA" : 0x22,
    "NAPTR" : 0x23,
    "KX" : 0x24,
    "CERT" : 0x25,
    "A6" : 0x26,
    "DNAME" : 0x27,
    "SINK" : 0x28,
    "OPT" : 0x29,
    "APL" : 0x2a,
    "DS" : 0x2b,
    "SSHFP" : 0x2c,
    "IPSECKEY" : 0x2d,
    "RRSIG" : 0x2e,
    "NSEC" : 0x2f,
    "DNSKEY" : 0x30,
    "DHCID" : 0x31,
    "NSEC3" : 0x32,
    "NSEC3PARAM" : 0x33,
    "HIP" : 0x37,
    "HINFO" : 0x38,
    "RKEY" : 0x39,
    "TALINK" : 0x3a,
    "SPF" : 0x63,
    "UINFO" : 0x64,
    "UID" : 0x65,
    "GID" : 0x66,
    "UNSPEC" : 0x67,
    "TKEY" : 0xf9,
    "TSIG" : 0xfa,
    "IXFR" : 0xfb,
    "AXFR" : 0xfc,
    "MAILB" : 0xfd,
    "MAILA" : 0xfe,
    "*" : 0xff
}
""" The map associating the type string with the integer value """

TYPES_REVERSE_MAP = {
    0x01 : "A",
    0x02 : "NS",
    0x03 : "MD",
    0x04 : "MF",
    0x05 : "CNAME",
    0x06 : "SOA",
    0x07 : "MB",
    0x08 : "MG",
    0x09 : "MR",
    0x0a : "NULL",
    0x0b : "WKS",
    0x0c : "PTR",
    0x0d : "HINFO",
    0x0e : "MINFO",
    0x0f : "MX",
    0x10 : "TXT",
    0x11 : "RP",
    0x12 : "AFSDB",
    0x13 : "X25",
    0x14 : "ISDN",
    0x15 : "RT",
    0x16 : "NSAP",
    0x17 : "NSAP-PTR",
    0x18 : "SIG",
    0x19 : "KEY",
    0x1a : "PX",
    0x1b : "GPOS",
    0x1c : "AAAA",
    0x1d : "LOC",
    0x1e : "NXT",
    0x1f : "EID",
    0x20 : "NIMLOC",
    0x21 : "SRV",
    0x22 : "ATMA",
    0x23 : "NAPTR",
    0x24 : "KX",
    0x25 : "CERT",
    0x26 : "A6",
    0x27 : "DNAME",
    0x28 : "SINK",
    0x29 : "OPT",
    0x2a : "APL",
    0x2b : "DS",
    0x2c : "SSHFP",
    0x2d : "IPSECKEY",
    0x2e : "RRSIG",
    0x2f : "NSEC",
    0x30 : "DNSKEY",
    0x31 : "DHCID",
    0x32 : "NSEC3",
    0x33 : "NSEC3PARAM",
    0x37 : "HIP",
    0x38 : "HINFO",
    0x39 : "RKEY",
    0x3a : "TALINK",
    0x63 : "SPF",
    0x64 : "UINFO",
    0x65 : "UID",
    0x66 : "GID",
    0x67 : "UNSPEC",
    0xf9 : "TKEY",
    0xfa : "TSIG",
    0xfb : "IXFR",
    0xfc : "AXFR",
    0xfd : "MAILB",
    0xfe : "MAILA",
    0xff : "*"
}
""" The map associating the type integer with the string value """

CLASSES_MAP = {
    "IN" : 0x01,
    "CS" : 0x02,
    "CH" : 0x03,
    "HS" : 0x04
}
""" The map associating the class string with the integer value """

CLASSES_REVERSE_MAP = {
    0x01 : "IN",
    0x02 : "CS",
    0x03 : "CH",
    0x04 : "HS"
}
""" The map associating the class integer with the string value """

class MainClientMdns:
    """
    The main client mdns class.
    """

    main_client_mdns_plugin = None
    """ The main client mdns plugin """

    def __init__(self, main_client_mdns_plugin):
        """
        Constructor of the class.

        @type main_client_mdns_plugin: MainClientMdnsPlugin
        @param main_client_mdns_plugin: The main client mdns plugin.
        """

        self.main_client_mdns_plugin = main_client_mdns_plugin

    def create_client(self, parameters):
        """
        Creates a client object for the given parameters.

        @type parameters: Dictionary
        @param parameters: The parameters to be used in creating
        the client object.
        @rtype: MdnsClient
        @return: The created client object.
        """

        # creates the mdns client
        mdns_client = MdnsClient(self)

        # returns the mdns client
        return mdns_client

    def create_request(self, parameters):
        pass

class MdnsClient:
    """
    The mdns client class, representing
    a client connection in the mdns protocol.
    """

    main_client_mdns = None
    """ The main client mdns object """

    current_transaction_id = 0x0000
    """ The current transaction id """

    client_connection = None
    """ The current client connection """

    _mdns_client = None
    """ The mdns client object used to provide connections """

    _mdns_client_lock = None
    """ Lock to control the fetching of the queries """

    def __init__(self, main_client_mdns):
        """
        Constructor of the class.

        @type main_client_mdns: MainClientMdns
        @param main_client_mdns: The main client mdns object.
        """

        self.main_client_mdns = main_client_mdns

        self._mdns_client_lock = threading.RLock()

    def open(self, parameters):
        # generates the parameters
        client_parameters = self._generate_client_parameters(parameters)

        # creates the mdns client, generating the internal structures
        self._mdns_client = self.main_client_mdns.main_client_mdns_plugin.main_client_utils_plugin.generate_client(client_parameters)

        # starts the mdns client
        self._mdns_client.start_client()

    def close(self, parameters):
        # stops the mdns client
        self._mdns_client.stop_client()

    def resolve_queries(self, queries, parameters = {}, persistent = DEFAULT_PERSISTENT, socket_name = DEFAULT_SOCKET_NAME, socket_parameters = DEFAULT_SOCKET_PARAMETERS):
        # defines the connection parameters
        connection_parameters = (
            DEFAULT_HOST,
            DEFAULT_PORT,
            persistent,
            socket_name,
            socket_parameters
        )

        # retrieves the callback parameters
        callback_function = parameters.get("callback_function", None)
        callback_timeout = parameters.get("callback_timeout", RESPONSE_TIMEOUT)

        # retrieves the corresponding (mdns) client connection
        self.client_connection = self._mdns_client.get_client_connection(connection_parameters)

        # acquires the mdns client lock
        self._mdns_client_lock.acquire()

        try:
            # sends the request for the given queries and
            # parameters, and retrieves the request
            request = self.send_request(queries, parameters)

            # in case the callback function is defined
            if callback_function:
                # retrieves the response using the callback approach
                response = self.retrieve_response_callback(request, callback_function, callback_timeout)
            # otherwise it's a normal synchronous call
            else:
                # retrieves the response
                response = self.retrieve_response(request)
        finally:
            # releases the mdns client lock
            self._mdns_client_lock.release()

        # returns the response
        return response

    def send_request(self, queries, parameters):
        """
        Sends the request for the given parameters.

        @type queries: List
        @param queries: The list of queries to be sent.
        @type parameters: Dictionary
        @param parameters: The parameters to the request.
        @rtype: MdnsRequest
        @return: The sent request for the given parameters.
        """

        # generates and retrieves a new transaction id
        transaction_id = self._get_transaction_id()

        # creates the mdns request with the the transaction id,
        # the queries and the parameters
        request = MdnsRequest(transaction_id, queries, parameters)

        # retrieves the result value from the request
        result_value = request.get_result()

        # sends the result value
        self.client_connection.send(result_value)

        # returns the request
        return request

    def retrieve_response(self, request, response_timeout = None):
        """
        Retrieves the response from the sent request.

        @type request: MdnsRequest
        @param request: The request that originated the response.
        @type response_timeout: int
        @param response_timeout: The timeout for the response retrieval.
        @rtype: MdnsResponse
        @return: The response from the sent request.
        """

        # creates a response object
        response = MdnsResponse(request)

        # receives the data
        data = self.client_connection.receive(response_timeout, MESSAGE_MAXIMUM_SIZE)

        # processes the data
        response.process_data(data)

        # returns the response
        return response

    def retrieve_response_callback(self, request, callback_function, callback_timeout):
        """
        Retrieves the responses from the sent request.
        This approach uses a timeout and the responses are fed
        to the given callback function.

        @type request: MdnsRequest
        @param request: The request that originated the responses.
        @type callback_function: Function
        @param callback_function: The callback function to be used.
        @type callback_timeout: int
        @param callback_timeout: The timeout for the callback.
        """

        # the request queries
        request_queries = request.queries

        # iterates continuously
        while True:
            # in case the callback timeout is invalid
            if callback_timeout <= 0:
                break

            # retrieves the start time
            start_time = time.time()

            try:
                # retrieves the response
                response = self.retrieve_response(request, callback_timeout)

                # validates the response against the (original request) queries
                valid_query = self._validate_response(request_queries, response)

                # in case there is a valid query calls the callback function
                valid_query and callback_function(valid_query, response)
            except:
                # passes the exception (no need to handle it)
                pass

            # retrieves the end time and calculates the
            # delta time using the start time
            end_time = time.time()
            delta_time = end_time - start_time

            # subtracts the delta time from the callback timeout
            callback_timeout -= delta_time

    def _get_transaction_id(self):
        """
        Retrieves the transaction id, incrementing the
        current transaction id counter.

        @rtype: int
        @return: The newly generated transaction id.
        """

        # returns the current transaction id
        return self.current_transaction_id

    def _generate_client_parameters(self, parameters):
        """
        Retrieves the client parameters map from the base parameters
        map.

        @type parameters: Dictionary
        @param parameters: The base parameters map to be used to build
        the final client parameters map.
        @rtype: Dictionary
        @return: The client service parameters map.
        """

        # creates the default parameters
        default_parameters = {
            "client_plugin" : self.main_client_mdns.main_client_mdns_plugin,
            "request_timeout" : REQUEST_TIMEOUT,
            "response_timeout" : RESPONSE_TIMEOUT
        }

        # creates the parameters map, from the default parameters
        parameters = colony.libs.map_util.map_extend(parameters, default_parameters, False)

        # returns the parameters
        return parameters

    def _validate_response(self, queries, response):
        """
        Validates the given response checking if any of the
        queries included in the set represents the original
        query for the given response.

        @type queries: List
        @param queries: The list of queries to be used in the
        validation of the response.
        @type response: MdnsResponse
        @param response: The response to be validated.
        @rtype: Tuple
        @return: The original query tuple for the given response.
        """

        # in case no response is defined
        if not response:
            # returns immediately (in error)
            return None

        # retrieves the response answers
        response_answers = response.answers

        # iterates over all the response answers
        for response_answer in response_answers:
            # retrieves the query aprt of the response answer
            response_answer_query = response_answer[:3]

            # in case the response answer query does not
            # exist in the list of queries
            if not response_answer_query in queries:
                # continues the loop
                continue

            # returns the response answer query
            return response_answer_query

class MdnsRequest:
    """
    The mdns request class.
    """

    transaction_id = None
    """ The transaction id, identifying a unique mdns request """

    queries = []
    """ The list of queries """

    parameters = {}
    """ The parameters to the mdns request """

    flags = NORMAL_REQUEST_VALUE
    """ The flags byte """

    def __init__(self, transaction_id, queries, parameters):
        """
        Constructor of the class.

        @type transaction_id: int
        @param transaction_id: The transaction id.
        @type queries: List
        @param queries: The queries list.
        @type parameters: Dictionary
        @param parameters: The request parameters.
        """

        self.transaction_id = transaction_id
        self.queries = queries
        self.parameters = parameters

    def get_result(self):
        """
        Retrieves the result string (serialized) value of
        the request.

        @rtype: String
        @return: The result string (serialized) value of
        the request.
        """

        # validates the current request
        self.validate()

        # retrieves the result stream
        result = colony.libs.string_buffer_util.StringBuffer()

        # retrieves the number of queries
        number_queries = len(self.queries)

        # generates the query header
        query_header = struct.pack("!HHHHHH", self.transaction_id, self.flags, number_queries, 0, 0, 0)

        # writes the query header to the result stream
        result.write(query_header)

        # iterates over all the queries
        for query in self.queries:
            # serializes the query
            query_serialized = self._serialize_query(query)

            # writes the serialized query to the result stream
            result.write(query_serialized)

        # retrieves the value from the result buffer
        result_value = result.get_value()

        # returns the result value
        return result_value

    def validate(self):
        """
        Validates the current request, raising exception
        in case validation fails.
        """

        pass

    def _serialize_query(self, query):
        """
        Serializes the given query into the mdns binary format.

        @type query: Tuple
        @param query: A tuple with the query information.
        @rtype: String
        @return: The string containing the resource record.
        """

        # unpacks the query tuple, retrieving the name,
        # type and class
        query_name, query_type, query_class = query

        # converts the query type to integer
        query_type_integer = TYPES_MAP[query_type]

        # converts the query class to integer
        query_class_integer = CLASSES_MAP[query_class]

        # creates the string buffer to hold the stream
        string_buffer = colony.libs.string_buffer_util.StringBuffer()

        # splits the query name to retrieve the query name items
        query_name_items = query_name.split(".")

        # iterates over all the query name items
        for query_name_item in query_name_items:
            # retrieves the query name item length
            query_name_item_length = len(query_name_item)

            # retrieves the query name item length in binary value
            query_name_item_length_character = chr(query_name_item_length)

            # writes the size of the query name item (in binary value) and
            # the query name itself
            string_buffer.write(query_name_item_length_character)
            string_buffer.write(query_name_item)

        # writes the end of string in the string buffer
        string_buffer.write("\0")

        # creates the query data from the query type and class
        query_data = struct.pack("!HH", query_type_integer, query_class_integer)

        # writes the query data to the string buffer
        string_buffer.write(query_data)

        # retrieves the serialized query value from the string buffer
        query_serialized = string_buffer.get_value()

        # returns the serialized query
        return query_serialized

class MdnsResponse:
    """
    The mdns response class.
    """

    request = None
    """ The request that originated the response """

    transaction_id = None
    """ The transaction id, identifying a unique mdns request """

    queries = []
    """ The list of queries """

    answers = []
    """ The list of answers """

    authority_resource_records = []
    """ The list of authority resource records """

    additional_resource_records = []
    """ The list of additional resource records """

    parameters = {}
    """ The parameters to the mdns request """

    flags = None
    """ The flags byte """

    def __init__(self, request):
        """
        Constructor of the class.

        @type request: MdnsRequest
        @param request: The request.
        """

        self.request = request

        self.queries = []
        self.answers = []
        self.authority_resource_records = []
        self.additional_resource_records = []
        self.parameters = {}

    def process_data(self, data):
        # retrieves the message header from the data
        message_header = struct.unpack_from("!HHHHHH", data)

        # unpacks the message header retrieving the transaction id, the flags, the number of queries
        # the number of authority resource records and the number of additional resource records
        transaction_id, flags, queries, answers, authority_resource_records, additional_resource_records = message_header

        # sets the transaction id and the flags
        self.transaction_id = transaction_id
        self.flags = flags

        # sets the current index as the
        # message header size (offset)
        current_index = MESSAGE_HEADER_SIZE

        # iterates over the number of queries
        for _index in range(queries):
            # retrieves the query and the current index
            query, current_index = self._get_query(data, current_index)

            # adds the query to the list of queries
            self.queries.append(query)

        # iterates over the number of answers
        for _index in range(answers):
            # retrieves the answer and the current index
            answer, current_index = self._get_answer(data, current_index)

            # adds the answer to the list of answers
            self.answers.append(answer)

        # iterates over the number of authority resource records
        for _index in range(authority_resource_records):
            # retrieves the authority resource record and the current index
            authority_resource_record, current_index = self._get_answer(data, current_index)

            # adds the authority resource record to the list of authority resource records
            self.authority_resource_records.append(authority_resource_record)

        # iterates over the number of additional resource records
        for _index in range(additional_resource_records):
            # retrieves the additional resource record and the current index
            additional_resource_record, current_index = self._get_answer(data, current_index)

            # adds the additional resource record to the list of additional resource records
            self.additional_resource_records.append(additional_resource_record)

    def _get_query(self, data, current_index):
        # retrieves the name for the data and current index
        name_list, current_index = self._get_name(data, current_index)

        # creates the query name by joining the name list
        query_name = ".".join(name_list)

        # retrieves the query type and the query class integer values
        query_type_integer, query_class_integer = struct.unpack_from("!HH", data, current_index)

        # increments the current index with four bytes
        current_index += 4

        # retrieves the query type (string value)
        query_type = TYPES_REVERSE_MAP[query_type_integer]

        # retrieves the query class (string value)
        query_class = CLASSES_REVERSE_MAP[query_class_integer]

        # creates the query tuple with the name, type and class of the query
        query = (
            query_name,
            query_type,
            query_class
        )

        return (
            query,
            current_index
        )

    def _get_answer(self, data, current_index):
        # retrieves the name for the data and current index
        answer_name, current_index = self._get_name_joined(data, current_index)

        # retrieves the answer type, answer class, time to live
        # and data length integer values
        answer_type_integer, answer_class_integer, answer_time_to_live, answer_data_length = struct.unpack_from("!HHIH", data, current_index)

        # filters the answer class integer value
        answer_class_integer = answer_class_integer & 0x7fff

        # filters the answer class integer to retrieve the answer cache flush
        answer_cache_flush = (answer_class_integer & 0x8000) >> 15

        # increments the current index with ten bytes
        current_index += 10

        # processes the answer data from the answer type, answer length and answer cache flush
        answer_data = self._process_answer_data(data, current_index, answer_type_integer, answer_data_length, answer_cache_flush)

        # increments the current index with the answer data length
        current_index += answer_data_length

        # retrieves the answer type (string value)
        answer_type = TYPES_REVERSE_MAP[answer_type_integer]

        # retrieves the answer class (string value)
        answer_class = CLASSES_REVERSE_MAP[answer_class_integer]

        # creates the answer tuple with the name, type, class,
        # time to live and data of the answer
        answer = (
            answer_name,
            answer_type,
            answer_class,
            answer_time_to_live,
            answer_data
        )

        return (
            answer,
            current_index
        )

    def _process_answer_data(self, data, current_index, answer_type_integer, answer_data_length, answer_cache_flush):
        """
        Processes the answer data according to the mdns protocol
        specification.
        The answer data is processed converting it into the most
        appropriate python representation.

        @type data: String
        @param data: The data buffer to be used.
        @type current_index: int
        @param current_index: The index to be used as base index.
        @type answer_type_integer: int
        @param answer_type_integer: The answer type in integer mode.
        @type answer_data_length: int
        @param answer_data_length: The length of the answer data.
        @type answer_cache_flush: int
        @param answer_cache_flush: If the answer data should be flushed.
        @rtype: Object
        @return: The "processed" answer data.
        """

        # in case the answer is of type a
        if answer_type_integer in (0x01,):
            # processes the ipv4 address value
            raw_answer_data_bytes = struct.unpack_from("!" + str(answer_data_length) + "B", data, current_index)
            raw_answer_data_string = [str(value) for value in raw_answer_data_bytes]
            answer_data = ".".join(raw_answer_data_string)
        # in case the answer is of type ns, cname, ptr or txt
        elif answer_type_integer in (0x02, 0x05, 0x0c, 0x10):
            # retrieves the answer data as a joined name
            answer_data, _current_index = self._get_name_joined(data, current_index)
        # in case the answer is of type srv
        elif answer_type_integer in (0x21,):
            # retrieves the priority the weight and the port
            priority, weight, port = struct.unpack_from("!HHH", data, current_index)

            # retrieves the answer data name as a joined name
            answer_data_name, _current_index = self._get_name_joined(data, current_index + 6)

            # sets the answer data tuple
            answer_data = (
                priority,
                weight,
                port,
                answer_data_name
            )
        # in case the answer is of type mx
        elif answer_type_integer in (0x0f,):
            # retrieves the answer data preference
            answer_data_preference, = struct.unpack_from("!H", data, current_index)

            # retrieves the answer data name as a joined name
            answer_data_name, _current_index = self._get_name_joined(data, current_index + 2)

            # sets the answer data tuple
            answer_data = (
                answer_data_preference,
                answer_data_name
            )
        # in case the answer is of type aaaa
        elif answer_type_integer in (0x1c,):
            # processes the ipv6 address value
            raw_answer_data_shorts = struct.unpack_from("!" + str(answer_data_length / 2) + "H", data, current_index)
            raw_answer_data_string = ["%x" % value for value in raw_answer_data_shorts if value > 0]
            answer_data = ":".join(raw_answer_data_string)
        # otherwise it's a generic value
        else:
            # sets the answer data as the raw answer data
            answer_data = data[current_index:current_index + answer_data_length]

        # returns the answer data
        return answer_data

    def _get_name_joined(self, data, current_index):
        """
        Retrieves the name "encoded" according to the mdns
        specification in the given index.
        This method joins the resulting list in a string
        separated with dots.

        @type data: String
        @param data: The data buffer to be used.
        @type current_index: int
        @param current_index: The index to be used as base index.
        @rtype: Tuple
        @return: The "decoded" name (joined in with dots) in the given index
        and the current index encoded in a tuple.
        """

        # retrieves the name list and the "new" current index
        name_list, current_index = self._get_name(data, current_index)

        # joins the name with dots
        name_joined = ".".join(name_list)

        return (
            name_joined,
            current_index
        )

    def _get_name(self, data, current_index):
        """
        Retrieves the name "encoded" according to the mdns
        specification in the given index.

        @type data: String
        @param data: The data buffer to be used.
        @type current_index: int
        @param current_index: The index to be used as base index.
        @rtype: Tuple
        @return: The "decoded" name (in list) in the given index
        and the current index encoded in a tuple.
        """

        # creates the name items list
        name_items = []

        # iterates while the current data item is
        # not end of string
        while not data[current_index] == "\0":
            # retrieves the length of the partial name name
            partial_name_length, = struct.unpack_from("!B", data, current_index)

            # checks if the name already exists (according to the message compression)
            existing_resource = partial_name_length & 0xc0 == 0xc0

            # in case the resource exists (message compression reference)
            if existing_resource:
                # sets the partial name length as the
                # first offset byte
                first_offset_byte = partial_name_length

                # unpacks the second offset byte from the data
                second_offset_byte, = struct.unpack_from("!B", data, current_index + 1)

                # calculates the offset index
                offset_index = ((first_offset_byte & 0x3f) << 8) + second_offset_byte

                # updates the current index with the two bytes
                current_index += 2

                # returns the previous (cached) name items list
                extra_name_items, _current_index = self._get_name(data, offset_index)

                # extends the current name items with the previous (cached) name items
                name_items.extend(extra_name_items)

                return (
                    name_items,
                    current_index
                )
            # otherwise it's raw data
            else:
                # retrieves the partial name from the data
                partial_name = data[current_index + 1:current_index + partial_name_length + 1]

                # adds the partial name to the name items list
                name_items.append(partial_name)

                # updates the current index with the partial name length plus one
                current_index += partial_name_length + 1

        # increments the current index with the
        # end string byte
        current_index += 1

        # returns the name items list
        return (
            name_items,
            current_index
        )