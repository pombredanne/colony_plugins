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

__revision__ = "$LastChangedRevision: 2688 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2009-04-16 12:24:34 +0100 (qui, 16 Abr 2009) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony.base.plugin_system

class JsonPlugin(colony.base.plugin_system.Plugin):
    """
    The main class for the Json plugin.
    """

    id = "pt.hive.colony.plugins.misc.json"
    name = "Json Plugin"
    short_name = "Json"
    description = "A plugin to serialize and unserialize json files"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.base.plugin_system.EAGER_LOADING_TYPE
    platforms = [colony.base.plugin_system.CPYTHON_ENVIRONMENT,
                 colony.base.plugin_system.JYTHON_ENVIRONMENT]
    attributes = {"build_automation_file_path" : "$base{plugin_directory}/misc/json/resources/baf.xml"}
    capabilities = ["serializer.json", "build_automation_item"]
    capabilities_allowed = []
    dependencies = []
    events_handled = []
    events_registrable = []
    main_modules = ["misc.json.json_exceptions",
                    "misc.json.json_serializer",
                    "misc.json.json_system"]

    json_system = None

    def load_plugin(self):
        colony.base.plugin_system.Plugin.load_plugin(self)
        global misc
        import misc.json.json_system
        self.json_system = misc.json.json_system.Json(self)

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

    def dependency_injected(self, plugin):
        colony.base.plugin_system.Plugin.dependency_injected(self, plugin)

    def dumps(self, object):
        return self.json_system.dumps(object)

    def dumps_pretty(self, object):
        return self.json_system.dumps_pretty(object)

    def dumps_buffer(self, object):
        return self.json_system.dumps_buffer(object)

    def loads(self, json_string):
        return self.json_system.loads(json_string)

    def load_file(self, json_file):
        return self.json_system.load_file(json_file)

    def load_file_encoding(self, json_file, encoding):
        return self.json_system.load_file(json_file, encoding)
