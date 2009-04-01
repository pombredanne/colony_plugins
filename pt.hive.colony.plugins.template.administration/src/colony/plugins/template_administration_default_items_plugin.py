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

__revision__ = "$LastChangedRevision: 723 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-12-15 21:09:57 +0000 (Seg, 15 Dez 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony.plugins.plugin_system
import colony.plugins.decorators

class TemplateAdministrationDefaultItemsPlugin(colony.plugins.plugin_system.Plugin):
    """
    The main class for the Template Administration Default Items plugin.
    """

    id = "pt.hive.colony.plugins.template.administration.default_items"
    name = "Template Administration Default Items Plugin"
    short_name = "Template Administration Default Items"
    description = "Template Administration Default Items Plugin"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.plugins.plugin_system.EAGER_LOADING_TYPE
    platforms = [colony.plugins.plugin_system.CPYTHON_ENVIRONMENT]
    capabilities = ["template_administration_extension.bundle"]
    capabilities_allowed = []
    dependencies = []
    events_handled = []
    events_registrable = []

    template_administration_default_items = None

    def load_plugin(self):
        colony.plugins.plugin_system.Plugin.load_plugin(self)
        global template_administration
        import template_administration.default_items.template_administration_default_items_system
        self.template_administration_default_items = template_administration.default_items.template_administration_default_items_system.TemplateAdministrationDefaultItems(self)

    def end_load_plugin(self):
        colony.plugins.plugin_system.Plugin.end_load_plugin(self)

    def unload_plugin(self):
        colony.plugins.plugin_system.Plugin.unload_plugin(self)

    def end_unload_plugin(self):
        colony.plugins.plugin_system.Plugin.end_unload_plugin(self)

    def load_allowed(self, plugin, capability):
        colony.plugins.plugin_system.Plugin.load_allowed(self, plugin, capability)

    def unload_allowed(self, plugin, capability):
        colony.plugins.plugin_system.Plugin.unload_allowed(self, plugin, capability)

    def dependency_injected(self, plugin):
        colony.plugins.plugin_system.Plugin.dependency_injected(self, plugin)

    def get_extension_name(self):
        return self.template_administration_default_items.get_extension_name()

    def get_base_resources_path(self):
        return self.template_administration_default_items.get_base_resources_path()

    def get_css_files(self):
        return self.template_administration_default_items.get_css_files()

    def get_js_files(self):
        return self.template_administration_default_items.get_js_files()

    def get_menu_items(self):
        return self.template_administration_default_items.get_menu_items()

    def get_content_items(self):
        return self.template_administration_default_items.get_content_items()
