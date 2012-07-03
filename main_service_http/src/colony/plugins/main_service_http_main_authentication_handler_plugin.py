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

__revision__ = "$LastChangedRevision: 684 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-12-08 15:16:55 +0000 (Seg, 08 Dez 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony.base.plugin_system
import colony.base.decorators

class MainServiceHttpMainAuthenticationHandlerPlugin(colony.base.plugin_system.Plugin):
    """
    The main class for the http Service Main Main Authentication Handler plugin.
    """

    id = "pt.hive.colony.plugins.main.service.http.main_authentication_handler"
    name = "Http Service Main Main Authentication Handler Plugin"
    short_name = "Http Service Main Main Authentication Handler"
    description = "The plugin that offers the http service authentication main handler"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.base.plugin_system.EAGER_LOADING_TYPE
    platforms = [
        colony.base.plugin_system.CPYTHON_ENVIRONMENT,
        colony.base.plugin_system.JYTHON_ENVIRONMENT
    ]
    attributes = {
        "build_automation_file_path" : "$base{plugin_directory}/main_service_http_main_authentication_handler/main_authentication_handler/resources/baf.xml"
    }
    capabilities = [
        "http_service_authentication_handler", "build_automation_item"
    ]
    dependencies = [
        colony.base.plugin_system.PluginDependency("pt.hive.colony.plugins.main.authentication", "1.x.x")
    ]
    main_modules = [
        "main_service_http_main_authentication_handler.main_authentication_handler.main_service_http_main_authentication_handler_exceptions",
        "main_service_http_main_authentication_handler.main_authentication_handler.main_service_http_main_authentication_handler_system"
    ]

    main_service_http_main_authentication_handler = None
    """ The main service http main authentication handler """

    main_authentication_plugin = None
    """ The main authentication plugin """

    def load_plugin(self):
        colony.base.plugin_system.Plugin.load_plugin(self)
        import main_service_http_main_authentication_handler.main_authentication_handler.main_service_http_main_authentication_handler_system
        self.main_service_http_main_authentication_handler =  main_service_http_main_authentication_handler.main_authentication_handler.main_service_http_main_authentication_handler_system.MainServiceHttpMainAuthenticationHandler(self)

    def end_load_plugin(self):
        colony.base.plugin_system.Plugin.end_load_plugin(self)

    def unload_plugin(self):
        colony.base.plugin_system.Plugin.unload_plugin(self)

    def end_unload_plugin(self):
        colony.base.plugin_system.Plugin.end_unload_plugin(self)

    def load_allowed(self, plugin, capability):
        colony.base.plugin_system.Plugin.load_allowed(self, plugin, capability)

    def unload_allowed(self, plugin, capability):
        colony.base.plugin_system.Plugin.unload_allowed(self, plugin, capability)

    @colony.base.decorators.inject_dependencies
    def dependency_injected(self, plugin):
        colony.base.plugin_system.Plugin.dependency_injected(self, plugin)

    def get_handler_name(self):
        """
        Retrieves the handler name.

        @rtype: String
        @return: The handler name.
        """

        return self.main_service_http_main_authentication_handler.get_handler_name()

    def handle_authentication(self, username, password, properties):
        """
        Handles the given http authentication.

        @type username: String
        @param username: The username to be used in the authentication.
        @type password: String
        @param password: The password to be used in the authentication.
        @type properties: Dictionary
        @param properties: The properties used in the authentication process.
        @rtype: Dictionary
        @return: The authentication result.
        """

        return self.main_service_http_main_authentication_handler.handle_authentication(username, password, properties)

    def get_main_authentication_plugin(self):
        return self.main_authentication_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.main.authentication")
    def set_main_authentication_plugin(self, main_authentication_plugin):
        self.main_authentication_plugin = main_authentication_plugin