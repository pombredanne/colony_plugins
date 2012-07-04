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

class YamlResourceParserPlugin(colony.base.system.Plugin):
    """
    The main class for the Yaml Resource Parser plugin.
    """

    id = "pt.hive.colony.plugins.resources.yaml_resource_parser"
    name = "Yaml Resource Parser Plugin"
    short_name = "Yaml Resource Parser"
    description = "A plugin to parse yaml resources"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.base.system.EAGER_LOADING_TYPE
    platforms = [
        colony.base.system.CPYTHON_ENVIRONMENT
    ]
    attributes = {
        "build_automation_file_path" : "$base{plugin_directory}/resources/yaml_resource_parser/resources/baf.xml"
    }
    capabilities = [
        "resource_parser",
        "build_automation_item"
    ]
    main_modules = [
        "resources.yaml_resource_parser.yaml_resource_parser_system"
    ]

    yaml_resource_parser = None
    """ The yaml resource parser """

    def load_plugin(self):
        colony.base.system.Plugin.load_plugin(self)
        import resources.yaml_resource_parser.yaml_resource_parser_system
        self.yaml_resource_parser = resources.yaml_resource_parser.yaml_resource_parser_system.YamlResourceParser(self)

    def end_load_plugin(self):
        colony.base.system.Plugin.end_load_plugin(self)

    def unload_plugin(self):
        colony.base.system.Plugin.unload_plugin(self)

    def end_unload_plugin(self):
        colony.base.system.Plugin.end_unload_plugin(self)

    def load_allowed(self, plugin, capability):
        colony.base.system.Plugin.load_allowed(self, plugin, capability)

    def unload_allowed(self, plugin, capability):
        colony.base.system.Plugin.unload_allowed(self, plugin, capability)

    def dependency_injected(self, plugin):
        colony.base.system.Plugin.dependency_injected(self, plugin)

    def get_resource_parser_name(self):
        return self.yaml_resource_parser.get_resource_parser_name()

    def parse_resource(self, resource):
        return self.yaml_resource_parser.parse_resource(resource)