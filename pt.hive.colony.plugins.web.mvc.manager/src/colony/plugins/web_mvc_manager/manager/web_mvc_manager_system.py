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

import types

import web_mvc_manager_exceptions

WEB_MVC_MANAGER_RESOURCES_PATH = "web_mvc_manager/manager/resources"
""" The web mvc manager resources path """

EXTRAS_PATH = WEB_MVC_MANAGER_RESOURCES_PATH + "/extras"
""" The extras path """

AJAX_ENCODER_NAME = "ajx"
""" The ajax encoder name """

class WebMvcManager:
    """
    The web mvc manager class.
    """

    web_mvc_manager_plugin = None
    """ The web mvc manager plugin """

    menu_items_map = {}
    """ The menu items map """

    side_panel_items_map = {}
    """ The side panel items map """

    extra_patterns_list = []
    """ The list containing the extra patterns """

    extra_patterns_map = {}
    """ The map containing the extra patterns mapping """

    def __init__(self, web_mvc_manager_plugin):
        """
        Constructor of the class.

        @type web_mvc_manager_plugin: WebMvcManagerPlugin
        @param web_mvc_manager_plugin: The web mvc manager plugin.
        """

        self.web_mvc_manager_plugin = web_mvc_manager_plugin

        self.menu_items_map = {}
        self.side_panel_items_map = {}
        self.extra_patterns_list = []
        self.extra_patterns_map = {}

    def load_components(self):
        """
        Loads the main components controller, etc.
        This load should occur only after the dependencies are loaded.
        """

        # retrieves the web mvc utils plugin
        web_mvc_utils_plugin = self.web_mvc_manager_plugin.web_mvc_utils_plugin

        # creates the controllers for the web mvc manager controller modules
        web_mvc_utils_plugin.create_controllers("web_mvc_manager.manager.web_mvc_manager_controllers", self, self.web_mvc_manager_plugin, "web_mvc_manager")
        web_mvc_utils_plugin.create_controllers("web_mvc_manager.manager.web_mvc_manager_communication", self, self.web_mvc_manager_plugin, "web_mvc_manager")
        web_mvc_utils_plugin.create_controllers("web_mvc_manager.manager.web_mvc_manager_helpers", self, self.web_mvc_manager_plugin, "web_mvc_manager")

    def get_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as patterns,
        to the web mvc service. The tuple should relate the route with the handler
        method/function.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as patterns,
        to the web mvc service.
        """

        base_patterns_tuple = (
            (r"^web_mvc_manager/?$", self.web_mvc_manager_main_controller.handle_web_mvc_manager_index, "get"),
            (r"^web_mvc_manager/index$", self.web_mvc_manager_main_controller.handle_web_mvc_manager_index, "get"),
            (r"^web_mvc_manager/side_panel/configuration$", self.web_mvc_manager_side_panel_controller.handle_configuration, "get"),
            (r"^web_mvc_manager/side_panel/update$", self.web_mvc_manager_side_panel_controller.handle_update, "get"),
            (r"^web_mvc_manager/header$", self.web_mvc_manager_header_controller.handle_header, "get"),
            (r"^web_mvc_manager/packages$", self.web_mvc_manager_package_controller.handle_create_json, "post", "json"),
            (r"^web_mvc_manager/bundles$", self.web_mvc_manager_bundle_controller.handle_create_json, "post", "json"),
        )

        # extends the base patterns tuple with the extra patterns tuple retrieving the result
        # patterns tuple
        result_patterns_tuple = base_patterns_tuple + tuple(self.extra_patterns_list)

        # returns the result patterns tuple
        return result_patterns_tuple

    def get_communication_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as communication patterns,
        to the web mvc service. The tuple should relate the route with a tuple
        containing the data handler, the connection changed handler and the name
        of the connection.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as communication patterns,
        to the web mvc service.
        """

        return (
            (r"^web_mvc_manager/communication$", (self.web_mvc_manager_communication_controller.handle_data, self.web_mvc_manager_communication_controller.handle_connection_changed, "web_mvc_manager/communication")),
        )

    def get_resource_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as resource patterns,
        to the web mvc service. The tuple should relate the route with the base
        file system path to be used.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as resource patterns,
        to the web mvc service.
        """

        # retrieves the plugin manager
        plugin_manager = self.web_mvc_manager_plugin.manager

        # retrieves the web mvc resources base plugin
        web_mvc_resources_base_plugin = self.web_mvc_manager_plugin.web_mvc_resources_base_plugin

        # retrieves the web mvc resources ui plugin
        web_mvc_resources_ui_plugin = self.web_mvc_manager_plugin.web_mvc_resources_ui_plugin

        # retrieves the web mvc manager plugin path
        web_mvc_manager_plugin_path = plugin_manager.get_plugin_path_by_id(self.web_mvc_manager_plugin.id)

        # retrieves the web mvc resources base plugin resources path
        web_mvc_resources_base_plugin_resources_path = web_mvc_resources_base_plugin.get_resources_path()

        # retrieves the web mvc resources ui plugin resources path
        web_mvc_resources_ui_plugin_resources_path = web_mvc_resources_ui_plugin.get_resources_path()

        return (
            (r"^web_mvc_manager/resources/.+$", (web_mvc_manager_plugin_path + "/" + EXTRAS_PATH, "web_mvc_manager/resources")),
            (r"^web_mvc_manager/resources_base/.+$", (web_mvc_resources_base_plugin_resources_path, "web_mvc_manager/resources_base")),
            (r"^web_mvc_manager/resources_ui/.+$", (web_mvc_resources_ui_plugin_resources_path, "web_mvc_manager/resources_ui"))
        )

    def load_web_mvc_manager_page_item_bundle_plugin(self, web_mvc_manager_page_item_bundle_plugin):
        # generates the patterns unload event
        self.web_mvc_manager_plugin.generate_event("web.mvc.patterns_unload", [self.web_mvc_manager_plugin])

        # retrieves the page item bundle from the web mvc manager page item bundle plugin
        page_item_bundle = web_mvc_manager_page_item_bundle_plugin.get_page_item_bundle({})

        # iterate over all the page items in the
        # page item bundle
        for page_item in page_item_bundle:
            # unpacks the page item i
            page_item_menu, page_item_side_panel, page_item_base_address, page_item_pattern = self.__unpack_page_item(page_item)

            # in case there is a menu defined for the page item
            # and the base address is also defined
            if page_item_menu and page_item_base_address:
                # adds the menu item for the menu and base address
                self._add_menu_item(page_item_menu, page_item_base_address)

            # in case there is a side panel defined for the page item
            # and the base address is also defined
            if page_item_side_panel and page_item_base_address:
                # adds the side panel item for the side panel and base address
                self._add_side_panel_item(page_item_side_panel, page_item_base_address)

            # unpacks the page item pattern
            page_item_action = page_item_pattern[1]

            # converts the page item action to allow composite validation of mvc manager
            page_item_action_composite = self.web_mvc_manager_main_controller.generate_handle_handle_web_mvc_manager_page_item(page_item_action)

            # converts the page item patter to list
            page_item_pattern_list = list(page_item_pattern)

            # sets the new page item action
            page_item_pattern_list[1] = page_item_action_composite

            # converts the page item patter back t tuple
            _page_item_pattern = tuple(page_item_pattern_list)

            # adds the page item pattern to the extra patterns list
            self.extra_patterns_list.append(_page_item_pattern)

            # sets the "new" page item pattern in the extra patterns map
            self.extra_patterns_map[page_item_pattern] = _page_item_pattern

        # generates the patterns load event (to update the patterns)
        self.web_mvc_manager_plugin.generate_event("web.mvc.patterns_load", [self.web_mvc_manager_plugin])

        # reloads the ui in the client side
        self._reload_ui()

    def unload_web_mvc_manager_page_item_bundle_plugin(self, web_mvc_manager_page_item_bundle_plugin):
        # generates the patterns unload event
        self.web_mvc_manager_plugin.generate_event("web.mvc.patterns_unload", [self.web_mvc_manager_plugin])

        # retrieves the page item bundle from the web mvc manager page item bundle plugin
        page_item_bundle = web_mvc_manager_page_item_bundle_plugin.get_page_item_bundle({})

        # iterate over all the page items in the
        # page item bundle
        for page_item in page_item_bundle:
            # unpacks the page item
            page_item_menu, page_item_side_panel, page_item_base_address, page_item_pattern = self.__unpack_page_item(page_item)

            # in case there is a menu defined for the page item
            # and the base address is also defined
            if page_item_menu and page_item_base_address:
                # removes the menu item for the menu and base address
                self._remove_menu_item(page_item_menu, page_item_base_address)

            # in case there is a side panel defined for the page item
            # and the base address is also defined
            if page_item_side_panel and page_item_base_address:
                # removes the side panel item for the side panel and base address
                self._remove_side_panel_item(page_item_side_panel, page_item_base_address)

            # retrieves the "new" page item pattern from the extra patterns map
            _page_item_pattern = self.extra_patterns_map[page_item_pattern]

            # removes the page item pattern from the extra patterns list
            self.extra_patterns_list.remove(_page_item_pattern)

            # removes the page item pattern from the extra patterns map
            del self.extra_patterns_map[page_item_pattern]

        # generates the patterns load event (to update the patterns)
        self.web_mvc_manager_plugin.generate_event("web.mvc.patterns_load", [self.web_mvc_manager_plugin])

        # reloads the ui in the client side
        self._reload_ui()

    def load_web_mvc_panel_item_plugin(self, web_mvc_panel_item_plugin):
        """
        Loads the given web mvc panel item plugin.

        @type web_mvc_panel_item_plugin: Plugin
        @param web_mvc_panel_item_plugin: The web mvc panel item plugin to be loaded.
        """

        # reloads the ui in the client side
        self._reload_ui()

    def unload_web_mvc_panel_item_plugin(self, web_mvc_panel_item_plugin):
        """
        Unloads the given web mvc panel item plugin.

        @type web_mvc_panel_item_plugin: Plugin
        @param web_mvc_panel_item_plugin: The web mvc panel item plugin to be unloaded.
        """

        # reloads the ui in the client side
        self._reload_ui()

    def process_web_mvc_side_panel_reload_event(self, event_name, validation):
        # reloads the ui in the client side
        self._reload_ui()

    def require_permissions(self, controller, rest_request, permissions_list = [], base_path = None):
        """
        Requires the permissions in the given permissions list to be set.

        @type controller: Controller
        @param controller: The controller being validated.
        @type rest_request: RestRequest
        @param rest_request: The rest request to be updated.
        @type permissions_list: List
        @param permissions_list: The list of permission to be validated.
        @type base_path: String
        @param base_path: The base path to be used as prefix in the url.
        @rtype: List
        @return: The list of reasons for permission validation failure.
        """

        # casts the permissions list
        permissions_list = self.__cast_list(permissions_list)

        # creates the reasons list
        reasons_list = []

        # returns the reasons list
        return reasons_list

    def escape_permissions_failed(self, controller, rest_request, reasons_list = [], base_path = None):
        """
        Handler for permission validation failures.
        Displays a message or redirects depending on the encoder name.

        @type controller: Controller
        @param controller: The controller which handled the request.
        @type rest_request: RestRequest
        @param rest_request: The rest request object.
        @type reasons_list: List
        @param reasons_list: A list with the reasons for validation failure.
        @type base_path: String.
        @param base_path: The base path for the request. Defaults to None.
        """

        # in case the encoder name is ajax
        if rest_request.encoder_name == AJAX_ENCODER_NAME:
            # sets the contents
            controller.set_contents(rest_request, "not enough permissions - access denied")
        else:
            # in case the base path is not defined
            if not base_path:
                # retrieves the base path from the rest request
                base_path = controller.get_base_path(rest_request)

            # redirects to the signin page
            controller.redirect(rest_request, base_path + "signin")

        # returns true
        return True

    def _reload_ui(self):
        # retrieves the serialized message
        serialized_message = self.web_mvc_manager_communication_helper_controller._get_serialized_message("web_mvc_manager/header/reload", "")

        # generates the communication event
        self.web_mvc_manager_plugin.generate_event("web.mvc.communication", ["web_mvc_manager/communication", serialized_message])

        # retrieves the serialized message
        serialized_message = self.web_mvc_manager_communication_helper_controller._get_serialized_message("web_mvc_manager/side_panel/reload", "")

        # generates the communication event
        self.web_mvc_manager_plugin.generate_event("web.mvc.communication", ["web_mvc_manager/communication", serialized_message])

    def _add_menu_item(self, menu_item, base_address):
        base_item, _rest_items = menu_item.split("/", 1)

        _rest_items, target_item = menu_item.rsplit("/", 1)

        if not base_item in self.menu_items_map:
            self.menu_items_map[base_item] = []

        base_item_list = self.menu_items_map[base_item]

        # creates the target item map
        target_item_map = {
            "target" : target_item,
            "address" : base_address
        }

        # adds the target item map to the base item list
        base_item_list.append(target_item_map)

    def _remove_menu_item(self, menu_item, base_address):
        base_item, _rest_items = menu_item.split("/", 1)

        _rest_items, target_item = menu_item.rsplit("/", 1)

        if not base_item in self.menu_items_map:
            self.menu_items_map[base_item] = []

        base_item_list = self.menu_items_map[base_item]

        # creates the target item map
        target_item_map = {
            "target" : target_item,
            "address" : base_address
        }

        # in case the target item map
        # exists in the base item list
        if target_item_map in base_item_list:
            # removes the target item map from the base item list
            base_item_list.remove(target_item_map)

        # in case the base item list is empty
        if not base_item_list:
            # removes the base item from the menu items map
            del self.menu_items_map[base_item]

    def _add_side_panel_item(self, side_panel_item, base_address):
        # splits the side panel item
        side_panel_item_splitted = side_panel_item.split("/")

        # retrieves the side panel item splitted length
        side_panel_item_splitted_length = len(side_panel_item_splitted)

        # in case the side panel item splitted length is not two
        if not side_panel_item_splitted_length == 2:
            # raises a run time exception
            raise web_mvc_manager_exceptions.RuntimeException("invalid side panel item length")

        # upacks the side panel item splitted, retrieving
        # the base item and the target item
        base_item, target_item = side_panel_item_splitted

        # in case the base item does not exists in the menu items map
        if not base_item in self.menu_items_map:
            # creates a list for the current base item in the side panel
            # items map
            self.side_panel_items_map[base_item] = []

        # retrieves the base item list
        base_item_list = self.side_panel_items_map[base_item]

        # creates the target item tuple
        target_item_tuple = (
            target_item,
            base_address
        )

        # adds the target item tuple to the base item list
        base_item_list.append(target_item_tuple)

    def _remove_side_panel_item(self, side_panel_item, base_address):
        # splits the side panel item
        side_panel_item_splitted = side_panel_item.split("/")

        # retrieves the side panel item splitted length
        side_panel_item_splitted_length = len(side_panel_item_splitted)

        # in case the side panel item splitted length is not two
        if not side_panel_item_splitted_length == 2:
            # raises a run time exception
            raise web_mvc_manager_exceptions.RuntimeException("invalid side panel item length")

        # upacks the side panel item splitted, retrieving
        # the base item and the target item
        base_item, target_item = side_panel_item_splitted

        # in case the base item does not exists in the menu items map
        if not base_item in self.menu_items_map:
            # creates a list for the current base item in the side panel
            # items map
            self.side_panel_items_map[base_item] = []

        # retrieves the base item list
        base_item_list = self.side_panel_items_map[base_item]

        # creates the target item tuple
        target_item_tuple = (
            target_item,
            base_address
        )

        # in case the target item tuple
        # exists in the base item list
        if target_item_tuple in base_item_list:
            # removes the target item tuple from the base item list
            base_item_list.remove(target_item_tuple)

    def __unpack_page_item(self, page_item):
        # retrieves the page item type
        page_item_type = type(page_item)

        # in case the page item is a map
        if page_item_type == types.DictType:
            # retrieves the page item menu
            page_item_menu = page_item.get("menu", None)

            # retrieves the page item side panel
            page_item_side_panel = page_item.get("side_panel", None)

            # retrieves the base address item side panel
            page_item_base_address = page_item.get("base_address", None)

            # retrieves the page item pattern
            page_item_pattern = page_item.get("pattern", None)
        # otherwise it must be a tuple
        else:
            # sets the unused value to none
            page_item_menu = None
            page_item_side_panel = None
            page_item_base_address = None

            # sets the page item pattern as the page item
            page_item_pattern = page_item

        # creates the page item tuple
        page_item_tuple = (
            page_item_menu,
            page_item_side_panel,
            page_item_base_address,
            page_item_pattern
        )

        # returns the page item tuple
        return page_item_tuple

    def __cast_list(self, value):
        """
        Casts the given value to a list,
        converting it if required.

        @type value: Object
        @param value: The value to be "casted".
        @rtype: List
        @return: The casted list value.
        """

        # in case the value is invalid
        if value == None:
            # returns the value
            return value

        # creates the list value from the value
        list_value = type(value) == types.ListType and value or (value,)

        # returns the list value
        return list_value
