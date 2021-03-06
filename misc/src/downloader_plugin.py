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

class DownloaderPlugin(colony.base.system.Plugin):
    """
    The main class for the Downloader plugin.
    """

    id = "pt.hive.colony.plugins.misc.downloader"
    name = "Downloader"
    description = "Downloader Plugin"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    platforms = [
        colony.base.system.CPYTHON_ENVIRONMENT
    ]
    capabilities = [
        "download",
        "_console_command_extension"
    ]
    dependencies = [
        colony.base.system.PluginDependency("pt.hive.colony.plugins.client.http", "1.x.x")
    ]
    main_modules = [
        "misc.downloader.console",
        "misc.downloader.exceptions",
        "misc.downloader.system"
    ]

    downloader = None
    """ The downloader """

    console_downloader = None
    """ The console downloader """

    client_http_plugin = None
    """ The client http plugin """

    def load_plugin(self):
        colony.base.system.Plugin.load_plugin(self)
        import misc.downloader.system
        import misc.downloader.console
        self.downloader = misc.downloader.system.Downloader(self)
        self.console_downloader = misc.downloader.console.ConsoleDownloader(self)

    @colony.base.decorators.inject_dependencies
    def dependency_injected(self, plugin):
        colony.base.system.Plugin.dependency_injected(self, plugin)

    def download_package(self, address, target_directory):
        return self.downloader.download_package(address, target_directory)

    def download_package_handlers(self, address, target_directory, handlers_map):
        return self.downloader.download_package(address, target_directory, handlers_map)

    def get_download_package_stream(self, address):
        return self.downloader.get_download_package_stream(address)

    def get_download_package_stream_handlers(self, address, handlers_map):
        return self.downloader.get_download_package_stream(address, handlers_map)

    def get_console_extension_name(self):
        return self.console_downloader.get_console_extension_name()

    def get_commands_map(self):
        return self.console_downloader.get_commands_map()

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.client.http")
    def set_client_http_plugin(self, client_http_plugin):
        self.client_http_plugin = client_http_plugin
