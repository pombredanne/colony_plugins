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

__revision__ = "$LastChangedRevision: 421 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-11-20 15:16:53 +0000 (Qui, 20 Nov 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import web_mvc_manager_page_item_repository_controllers

REPOSITORY_LIST_PAGE_ITEM_ATTRIBUTES = {"menu" : "update/repositories",
                                        "side_panel" : "lists/repositories",
                                        "base_address" : "web_mvc_manager/repositories",
                                        "pattern" : (r"^web_mvc_manager/repositories$", 1)}
""" The repository list page item attributes """

REPOSITORY_SHOW_PAGE_ITEM_ATTRIBUTES = {"pattern" : (r"^web_mvc_manager/repositories/[0-9]+$", 2)}
""" The repository show page item attributes """

REPOSITORY_PARTIAL_LIST_PAGE_ITEM_ATTRIBUTES = {"pattern" : (r"^web_mvc_manager/repositories/partial$", 3)}
""" The repository partial list page item attributes """

REPOSITORY_INSTALL_PLUGIN_PAGE_ITEM_ATTRIBUTES = {"pattern" : (r"^web_mvc_manager/repositories/install_plugin$", 4)}
""" The repository install plugin page item attributes """

REPOSITORY_PLUGINS_PARTIAL_ITEM_ATTRIBUTES = {"pattern" : (r"^web_mvc_manager/repositories/[0-9]+/plugins_partial$", 5)}
""" The repository plugins partial page item attributes """

REPOSITORY_PACKAGES_PARTIAL_ITEM_ATTRIBUTES = {"pattern" : (r"^web_mvc_manager/repositories/[0-9]+/packages_partial$", 5)}
""" The repository packages partial page item attributes """

class WebMvcManagerPageItemRepository:
    """
    The web mvc manager page item repository class.
    """

    web_mvc_manager_page_item_repository_plugin = None
    """ The web mvc manager page item repository plugin """

    def __init__(self, web_mvc_manager_page_item_repository_plugin):
        """
        Constructor of the class.

        @type web_mvc_manager_page_item_repository_plugin: WebMvcManagerPageItemRepositoryPlugin
        @param web_mvc_manager_page_item_repository_plugin: The web mvc manager page item repository plugin.
        """

        self.web_mvc_manager_page_item_repository_plugin = web_mvc_manager_page_item_repository_plugin

    def load_components(self):
        """
        Loads the main components controller, etc.
        This load should occur only after the dependencies are loaded.
        """

        # retrieves the web mvc utils plugin
        web_mvc_utils_plugin = self.web_mvc_manager_page_item_repository_plugin.web_mvc_utils_plugin

        # creates the web mvc panel item monitor main controller
        self.web_mvc_panel_item_monitor_main_controller = web_mvc_utils_plugin.create_controller(web_mvc_manager_page_item_repository_controllers.WebMvcManagerPageItemRepositoryController, [self.web_mvc_manager_page_item_repository_plugin, self], {})

    def get_page_item_bundle(self):
        """
        Retrieves a bundle containing a combination
        """

        return {}
