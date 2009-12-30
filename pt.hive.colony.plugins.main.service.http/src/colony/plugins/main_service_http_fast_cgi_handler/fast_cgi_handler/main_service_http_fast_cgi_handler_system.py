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

import main_service_http_fast_cgi_handler_exceptions

HANDLER_NAME = "fast_cgi"
""" The handler name """

class MainServiceHttpFastCgiHandler:
    """
    The main service http fast cgi handler class.
    """

    main_service_http_fast_cgi_handler_plugin = None
    """ The main service http fast cgi handler plugin """

    def __init__(self, main_service_http_fast_cgi_handler_plugin):
        """
        Constructor of the class.

        @type main_service_http_fast_cgi_handler_plugin: MainServiceHttpFastCgiHandlerPlugin
        @param main_service_http_fast_cgi_handler_plugin: The main service http fast cgi handler plugin.
        """

        self.main_service_http_fast_cgi_handler_plugin = main_service_http_fast_cgi_handler_plugin

    def get_handler_name(self):
        """
        Retrieves the handler name.

        @rtype: String
        @return: The handler name.
        """

        return HANDLER_NAME

    def handle_request(self, request):
        # raises the request not handled exception
        raise main_service_http_fast_cgi_handler_exceptions.RequestNotHandled("no fast cgi handler could handle the request")
