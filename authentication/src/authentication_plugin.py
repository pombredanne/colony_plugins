#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Framework
# Copyright (c) 2008-2012 Hive Solutions Lda.
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

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony.base.system
import colony.base.decorators

class AuthenticationPlugin(colony.base.system.Plugin):
    """
    The main class for the Authentication plugin.
    """

    id = "pt.hive.colony.plugins.authentication"
    name = "Authentication"
    description = "Plugin that provides the authentication front-end mechanisms"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    platforms = [
        colony.base.system.CPYTHON_ENVIRONMENT,
        colony.base.system.JYTHON_ENVIRONMENT
    ]
    capabilities = [
        "authentication"
    ]
    capabilities_allowed = [
        "authentication_handler"
    ]
    main_modules = [
        "authentication.authentication.system"
    ]

    authentication = None
    """ The authentication """

    authentication_handler_plugins = []
    """ The authentication handler plugins """

    def load_plugin(self):
        colony.base.system.Plugin.load_plugin(self)
        import authentication.authentication.system
        self.authentication = authentication.authentication.system.Authentication(self)

    @colony.base.decorators.load_allowed
    def load_allowed(self, plugin, capability):
        colony.base.system.Plugin.load_allowed(self, plugin, capability)

    @colony.base.decorators.unload_allowed
    def unload_allowed(self, plugin, capability):
        colony.base.system.Plugin.unload_allowed(self, plugin, capability)

    def authenticate_user(self, username, password, authentication_handler, arguments):
        return self.authentication.authenticate_user(username, password, authentication_handler, arguments)

    def process_authentication_string(self, authentication_string):
        return self.authentication.process_authentication_string(authentication_string)

    @colony.base.decorators.load_allowed_capability("authentication_handler")
    def authentication_handler_load_allowed(self, plugin, capability):
        self.authentication_handler_plugins.append(plugin)

    @colony.base.decorators.unload_allowed_capability("authentication_handler")
    def authentication_handler_unload_allowed(self, plugin, capability):
        self.authentication_handler_plugins.remove(plugin)
