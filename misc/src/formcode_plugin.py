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

class FormcodePlugin(colony.base.system.Plugin):
    """
    The main class for the Formcode plugin.
    """

    id = "pt.hive.colony.plugins.misc.formcode"
    name = "Formcode Plugin"
    short_name = "Formcode"
    description = "A plugin to serialize and unserialize formcode files"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.base.system.EAGER_LOADING_TYPE
    platforms = [
        colony.base.system.CPYTHON_ENVIRONMENT
    ]
    attributes = {
        "build_automation_file_path" : "$base{plugin_directory}/misc/formcode/resources/baf.xml"
    }
    capabilities = [
        "serializer.formcode",
        "build_automation_item"
    ]
    main_modules = [
        "misc.formcode.formcode_exceptions",
        "misc.formcode.formcode_serializer",
        "misc.formcode.formcode_system"
    ]

    formcode = None
    """ The formcode """

    def load_plugin(self):
        colony.base.system.Plugin.load_plugin(self)
        import misc.formcode.formcode_system
        self.formcode = misc.formcode.formcode_system.Formcode(self)

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

    def dumps(self, object):
        return self.formcode.dumps(object)

    def dumps_base_path(self, object, base_path):
        return self.formcode.dumps_base_path(object, base_path)

    def loads(self, formcode_string):
        return self.formcode.loads(formcode_string)

    def load_file(self, formcode_file):
        return self.formcode.load_file(formcode_file)

    def load_file_encoding(self, formcode_file, encoding):
        return self.formcode.load_file(formcode_file, encoding)

    def get_mime_type(self):
        return self.formcode.get_mime_type()