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

import os
import time
import copy
import base64

import colony.libs.importer_util

WEB_MVC_UTILS_VALUE = "web_mvc_utils"
""" The web mvc utils value """

DEFAULT_ENCODING = "utf-8"
""" The default encoding value """

WEB_MVC_MANAGER_RESOURCES_PATH = "web_mvc_manager/manager/resources"
""" The web mvc manager resources path """

COLONY_BUNDLE_FILE_EXTENSION = "cbx"
""" The colony bundle file extension """

COLONY_PLUGIN_FILE_EXTENSION = "cpx"
""" The colony plugin file extension """

LOAD_VALUE = "load"
""" The load value """

UNLOAD_VALUE = "unload"
""" The unload value """

LOADED_VALUE = "loaded"
""" The loaded value """

UNLOADED_VALUE = "unloaded"
""" The unloaded value """

PROVIDING_VALUE = "providing"
""" The providing value """

ALLOWING_VALUE = "allowing"
""" The allowing value """

UPGRADE_VALUE = "upgrade"
""" The upgrade value """

COLONY_PACKING_VALUE = "colony_packing"
""" The colony packing value """

SERIALIZER_VALUE = "serializer"
""" The serializer value """

NORMAL_ENCODER_NAME = None
""" The normal encoder name """

PATTERN_NAMES_VALUE = "pattern_names"
""" The pattern names value """

EXCEPTION_VALUE = "exception"
""" The exception value """

MESSAGE_VALUE = "message"
""" The message value """

EXCEPTION_HANDLER_VALUE = "exception_handler"
""" The exception handler value """

# imports the web mvc utils
web_mvc_utils = colony.libs.importer_util.__importer__(WEB_MVC_UTILS_VALUE)

class MainController:
    """
    The web mvc manager main controller.
    """

    web_mvc_manager_plugin = None
    """ The web mvc manager plugin """

    web_mvc_manager = None
    """ The web mvc manager """

    def __init__(self, web_mvc_manager_plugin, web_mvc_manager):
        """
        Constructor of the class.

        @type web_mvc_manager_plugin: WebMvcManagerPlugin
        @param web_mvc_manager_plugin: The web mvc manager plugin.
        @type web_mvc_manager: WebMvcManager
        @param web_mvc_manager: The web mvc manager.
        """

        self.web_mvc_manager_plugin = web_mvc_manager_plugin
        self.web_mvc_manager = web_mvc_manager

    def start(self):
        """
        Method called upon structure initialization.
        """

        # sets the relative resources path
        self.set_relative_resources_path(WEB_MVC_MANAGER_RESOURCES_PATH)

    def validate(self, rest_request, parameters, validation_parameters):
        # returns the result of the require permission call
        return self.web_mvc_manager.require_permissions(self, rest_request, validation_parameters)

    @web_mvc_utils.serialize_exceptions("all")
    def handle_web_mvc_manager_index(self, rest_request, parameters = {}):
        """
        Handles the given web mvc manager index rest request.

        @type rest_request: RestRequest
        @param rest_request: The web mvc manager index rest request
        to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the exception handler
        exception_handler = self.web_mvc_manager.web_mvc_manager_exception_controller

        # sets the exception handler in the parameters
        parameters[EXCEPTION_HANDLER_VALUE] = exception_handler

        # retrieves the template file
        template_file = self.retrieve_template_file("general.html.tpl")

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    def generate_handle_handle_web_mvc_manager_page_item(self, original_handler):
        """
        Generates a composite handler from the original page item handler.

        @type original_handler: Method
        @param original_handler: The original page item handler.
        @rtype: Method
        @return: The generated handler method.
        """

        def handle_web_mvc_manager_page_item(rest_request, parameters = {}):
            # retrieves the web mvc manager search helper controller
            web_mvc_manager_search_helper_controller = self.web_mvc_manager.web_mvc_manager_search_helper_controller

            # retrieves the web mvc manager communication helper controller
            web_mvc_manager_communication_helper_controller = self.web_mvc_manager.web_mvc_manager_communication_helper_controller

            # in case the encoder name is normal
            if rest_request.encoder_name == NORMAL_ENCODER_NAME:
                # retrieves the template file
                template_file = self.retrieve_template_file("general.html.tpl")

                # assigns the configuration (side panel) variables to the template
                self.web_mvc_manager.web_mvc_manager_side_panel_controller._assign_configuration_variables(template_file)

                # assigns the header variables to the template
                self.web_mvc_manager.web_mvc_manager_header_controller._assign_header_variables(template_file)
            else:
                # sets the template file to invalid
                template_file = None

            # defines the default parameters
            default_parameters = {
                "template_file" : template_file,
                "search_helper" : web_mvc_manager_search_helper_controller,
                "communication_helper" : web_mvc_manager_communication_helper_controller
            }

            # extends the parameters map with the template file reference
            handler_parameters = colony.libs.map_util.map_extend(parameters, default_parameters)

            # sends the request to the original handler and returns the result
            return original_handler(rest_request, handler_parameters)

        return handle_web_mvc_manager_page_item

class SidePanelController:
    """
    The web mvc manager side panel controller.
    """

    web_mvc_manager_plugin = None
    """ The web mvc manager plugin """

    web_mvc_manager = None
    """ The web mvc manager """

    def __init__(self, web_mvc_manager_plugin, web_mvc_manager):
        """
        Constructor of the class.

        @type web_mvc_manager_plugin: WebMvcManagerPlugin
        @param web_mvc_manager_plugin: The web mvc manager plugin.
        @type web_mvc_manager: WebMvcManager
        @param web_mvc_manager: The web mvc manager.
        """

        self.web_mvc_manager_plugin = web_mvc_manager_plugin
        self.web_mvc_manager = web_mvc_manager

    def start(self):
        """
        Method called upon structure initialization.
        """

        # sets the relative resources path
        self.set_relative_resources_path(WEB_MVC_MANAGER_RESOURCES_PATH, extra_templates_path = "side_panel")

    def handle_update(self, rest_request, parameters = {}):
        """
        Handles the given update rest request.

        @type rest_request: RestRequest
        @param rest_request: The take the bill update rest request
        to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the template file
        template_file = self.retrieve_template_file("side_panel_update.html.tpl")

        # assigns the update variables
        self._assign_update_variables(template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    def handle_configuration(self, rest_request, parameters = {}):
        """
        Handles the given configuration rest request.

        @type rest_request: RestRequest
        @param rest_request: The take the bill configuration rest request
        to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the template file
        template_file = self.retrieve_template_file("side_panel_configuration.html.tpl")

        # assigns the configuration variables
        self._assign_configuration_variables(template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    def _assign_update_variables(self, template_file):
        self.__assign_panel_item_variables(template_file)

    def _assign_configuration_variables(self, template_file):
        self.__assign_panel_item_variables(template_file)

    def __assign_panel_item_variables(self, template_file):
        # retrieves the web mvc panel item plugins
        web_mvc_panel_item_plugins = self.web_mvc_manager_plugin.web_mvc_panel_item_plugins

        # starts the panel items list
        panel_items_list = []

        # iterates over all the web mvc panel item plugins
        for web_mvc_panel_item_plugin in web_mvc_panel_item_plugins:
            panel_item = web_mvc_panel_item_plugin.get_panel_item({})
            panel_items_list.append(panel_item)

        # assigns the panel items to the template
        template_file.assign("panel_items", panel_items_list)

class HeaderController:
    """
    The web mvc manager header controller.
    """

    web_mvc_manager_plugin = None
    """ The web mvc manager plugin """

    web_mvc_manager = None
    """ The web mvc manager """

    def __init__(self, web_mvc_manager_plugin, web_mvc_manager):
        """
        Constructor of the class.

        @type web_mvc_manager_plugin: WebMvcManagerPlugin
        @param web_mvc_manager_plugin: The web mvc manager plugin.
        @type web_mvc_manager: WebMvcManager
        @param web_mvc_manager: The web mvc manager.
        """

        self.web_mvc_manager_plugin = web_mvc_manager_plugin
        self.web_mvc_manager = web_mvc_manager

    def start(self):
        """
        Method called upon structure initialization.
        """

        # sets the relative resources path
        self.set_relative_resources_path(WEB_MVC_MANAGER_RESOURCES_PATH)

    def handle_header(self, rest_request, parameters = {}):
        """
        Handles the given header rest request.

        @type rest_request: RestRequest
        @param rest_request: The take the bill header rest request
        to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the template file
        template_file = self.retrieve_template_file("header.html.tpl")

        # assigns the header variables
        self._assign_header_variables(template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    def _assign_header_variables(self, template_file):
        # assigns the menu items to the template
        template_file.assign("menu_items", self.web_mvc_manager.menu_items_map)

class PackageController:
    """
    The web mvc manager package controller.
    """

    web_mvc_manager_plugin = None
    """ The web mvc manager plugin """

    web_mvc_manager = None
    """ The web mvc manager """

    def __init__(self, web_mvc_manager_plugin, web_mvc_manager):
        """
        Constructor of the class.

        @type web_mvc_manager_plugin: WebMvcManagerPlugin
        @param web_mvc_manager_plugin: The web mvc manager plugin.
        @type web_mvc_manager: WebMvcManager
        @param web_mvc_manager: The web mvc manager.
        """

        self.web_mvc_manager_plugin = web_mvc_manager_plugin
        self.web_mvc_manager = web_mvc_manager

    def validate(self, rest_request, parameters, validation_parameters):
        # returns the result of the require permission call
        return self.web_mvc_manager.require_permissions(self, rest_request, validation_parameters)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("packages.create")
    def handle_create_serialized(self, rest_request, parameters = {}):
        # deploys the package
        self._deploy_package(rest_request)

    def handle_create_json(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # handles the request with the general
        # handle create serialized method
        self.handle_create_serialized(rest_request, parameters)

    def _deploy_package(self, rest_request, package_type = COLONY_PLUGIN_FILE_EXTENSION):
        # retrieves the plugin manager
        plugin_manager = self.web_mvc_manager_plugin.manager

        # retrieves the system installer plugin
        system_installer_plugin = self.web_mvc_manager_plugin.system_installer_plugin

        # retrieves the web mvc manager plugin id
        web_mvc_manager_plugin_id = self.web_mvc_manager_plugin.id

        # retrieves a temporary plugin path
        temporary_plugin_path = plugin_manager.get_temporary_plugin_path_by_id(web_mvc_manager_plugin_id)

        # creates the temporary plugin path directories
        not os.path.exists(temporary_plugin_path) and os.makedirs(temporary_plugin_path)

        # retrieves the current time
        current_time = time.time()

        # generates a unique file name base on the
        # current time
        unique_file_name = str(current_time) + "." + package_type

        # creates the unique file path joining the temporary plugin path
        # and the unique file name
        unique_file_path = os.path.join(temporary_plugin_path, unique_file_name)

        # retrieves the request contents
        contents = rest_request.request.read()

        # decodes the contents from base64
        contents_decoded = base64.b64decode(contents)

        # opens the temporary (unique) cpx file
        temp_file = open(unique_file_path, "wb")

        try:
            try:
                # writes the contents (decoded) to the file
                temp_file.write(contents_decoded)
            finally:
                # closes the temporary file
                temp_file.close()

            # installation options
            installation_properties = {
                UPGRADE_VALUE : True
            }

            # installs the package
            system_installer_plugin.install_package(unique_file_path, installation_properties, COLONY_PACKING_VALUE)
        finally:
            # removes the temporary file (with the unique file path)
            os.remove(unique_file_path)

class BundleController:
    """
    The web mvc manager bundle controller.
    """

    web_mvc_manager_plugin = None
    """ The web mvc manager plugin """

    web_mvc_manager = None
    """ The web mvc manager """

    def __init__(self, web_mvc_manager_plugin, web_mvc_manager):
        """
        Constructor of the class.

        @type web_mvc_manager_plugin: WebMvcManagerPlugin
        @param web_mvc_manager_plugin: The web mvc manager plugin.
        @type web_mvc_manager: WebMvcManager
        @param web_mvc_manager: The web mvc manager.
        """

        self.web_mvc_manager_plugin = web_mvc_manager_plugin
        self.web_mvc_manager = web_mvc_manager

    def validate(self, rest_request, parameters, validation_parameters):
        # returns the result of the require permission call
        return self.web_mvc_manager.require_permissions(self, rest_request, validation_parameters)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("bundles.create")
    def handle_create_serialized(self, rest_request, parameters = {}):
        # retrieves the package controller
        web_mvc_manager_package_controller = self.web_mvc_manager.web_mvc_manager_package_controller

        # deploys the package
        web_mvc_manager_package_controller._deploy_package(rest_request, COLONY_BUNDLE_FILE_EXTENSION)

    def handle_create_json(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # handles the request with the general
        # handle create serialized method
        self.handle_create_serialized(rest_request, parameters)

class PluginController:
    """
    The web mvc manager plugin controller.
    """

    web_mvc_manager_plugin = None
    """ The web mvc manager plugin """

    web_mvc_manager = None
    """ The web mvc manager """

    def __init__(self, web_mvc_manager_plugin, web_mvc_manager):
        """
        Constructor of the class.

        @type web_mvc_manager_plugin: WebMvcManagerPlugin
        @param web_mvc_manager_plugin: The web mvc manager plugin.
        @type web_mvc_manager: WebMvcManager
        @param web_mvc_manager: The web mvc manager.
        """

        self.web_mvc_manager_plugin = web_mvc_manager_plugin
        self.web_mvc_manager = web_mvc_manager

    def start(self):
        """
        Method called upon structure initialization.
        """

        # sets the relative resources path
        self.set_relative_resources_path(WEB_MVC_MANAGER_RESOURCES_PATH, extra_templates_path = "plugin")

    def validate(self, rest_request, parameters, validation_parameters):
        # returns the result of the require permission call
        return self.web_mvc_manager.require_permissions(self, rest_request, validation_parameters)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("plugins.list")
    def handle_list(self, rest_request, parameters = {}):
        # retrieves the exception handler
        exception_handler = self.web_mvc_manager.web_mvc_manager_exception_controller

        # sets the exception handler in the parameters
        parameters[EXCEPTION_HANDLER_VALUE] = exception_handler

        # retrieves the template file
        template_file = self.retrieve_template_file("../general.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "page_include", "plugin/plugin_list_contents.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "side_panel_include", "side_panel/side_panel_configuration.html.tpl")

        # assigns the configuration (side panel) variables to the template
        self.web_mvc_manager.web_mvc_manager_side_panel_controller._assign_configuration_variables(template_file)

        # assigns the header variables to the template
        self.web_mvc_manager.web_mvc_manager_header_controller._assign_header_variables(template_file)

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("plugins.list")
    def handle_list_ajx(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # retrieves the template file
        template_file = self.retrieve_template_file("plugin_list_contents.html.tpl")

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("plugins.list")
    def handle_partial_list_ajx(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # retrieves the web mvc manager search helper controller
        web_mvc_manager_search_helper_controller = self.web_mvc_manager.web_mvc_manager_search_helper_controller

        # retrieves the form data by processing the form
        form_data_map = self.process_form_data(rest_request, DEFAULT_ENCODING)

        # retrieves the form data attributes
        search_query = form_data_map["search_query"]

        # retrieves the start record
        start_record = form_data_map["start_record"]

        # retrieves the number records
        number_records = form_data_map["number_records"]

        # converts the start record to integer
        start_record = int(start_record)

        # converts the number records to integer
        number_records = int(number_records)

        # retrieves the filtered plugins
        filtered_plugins = self._get_filtered_plugins(rest_request, search_query)

        # retrieves the partial filtered plugins and meta data
        partial_filtered_plugins, start_record, number_records, total_number_records = web_mvc_manager_search_helper_controller.partial_filter(rest_request, filtered_plugins, start_record, number_records)

        # retrieves the template file
        template_file = self.retrieve_template_file("plugin_partial_list_contents.html.tpl")

        # assigns the plugins to the template
        template_file.assign("plugins", partial_filtered_plugins)

        # assigns the start record to the template
        template_file.assign("start_record", start_record)

        # assigns the number records to the template
        template_file.assign("number_records", number_records)

        # assigns the total number records to the template
        template_file.assign("total_number_records", total_number_records)

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("plugins.new")
    def handle_new(self, rest_request, parameters = {}):
        # retrieves the exception handler
        exception_handler = self.web_mvc_manager.web_mvc_manager_exception_controller

        # sets the exception handler in the parameters
        parameters[EXCEPTION_HANDLER_VALUE] = exception_handler

        # retrieves the template file
        template_file = self.retrieve_template_file("../general.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "page_include", "plugin/plugin_new_contents.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "side_panel_include", "side_panel/side_panel_configuration.html.tpl")

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("plugins.new")
    def handle_new_ajx(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # retrieves the template file
        template_file = self.retrieve_template_file("plugin_new_contents.html.tpl")

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("plugins.create")
    def handle_create_serialized(self, rest_request, parameters = {}):
        # retrieves the package controller
        web_mvc_manager_package_controller = self.web_mvc_manager.web_mvc_manager_package_controller

        # deploys the package
        web_mvc_manager_package_controller._deploy_package(rest_request, COLONY_PLUGIN_FILE_EXTENSION)

    def handle_create_json(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # handles the request with the general
        # handle create serialized method
        self.handle_create_serialized(rest_request, parameters)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("plugins.show")
    def handle_show(self, rest_request, parameters = {}):
        # retrieves the exception handler
        exception_handler = self.web_mvc_manager.web_mvc_manager_exception_controller

        # sets the exception handler in the parameters
        parameters[EXCEPTION_HANDLER_VALUE] = exception_handler

        # retrieves the pattern names from the parameters
        pattern_names = parameters[PATTERN_NAMES_VALUE]

        # retrieves the plugin id pattern
        plugin_id = pattern_names["plugin_id"]

        # retrieves the specified plugin
        plugin = self._get_plugin(rest_request, plugin_id)

        # retrieves the template file
        template_file = self.retrieve_template_file("../general.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "page_include", "plugin/plugin_edit_contents.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "side_panel_include", "side_panel/side_panel_configuration.html.tpl")

        # assigns the plugin to the template
        template_file.assign("plugin", plugin)

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("plugins.show")
    def handle_show_ajx(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # retrieves the pattern names from the parameters
        pattern_names = parameters[PATTERN_NAMES_VALUE]

        # retrieves the plugin id pattern
        plugin_id = pattern_names["plugin_id"]

        # retrieves the specified plugin
        plugin = self._get_plugin(rest_request, plugin_id)

        # retrieves the template file
        template_file = self.retrieve_template_file("plugin_edit_contents.html.tpl")

        # assigns the plugin to the template
        template_file.assign("plugin", plugin)

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("plugins.change_status")
    def handle_change_status_serialized(self, rest_request, parameters = {}):
        # retrieves the serializer
        serializer = parameters[SERIALIZER_VALUE]

        # retrieves the web mvc communication helper controller
        web_mvc_manager_communication_helper_controller = self.web_mvc_manager.web_mvc_manager_communication_helper_controller

        # retrieves the form data by processing the form
        form_data_map = self.process_form_data(rest_request, DEFAULT_ENCODING)

        # retrieves the pattern names from the parameters
        pattern_names = parameters[PATTERN_NAMES_VALUE]

        # retrieves the plugin id pattern
        plugin_id = pattern_names["plugin_id"]

        # retrieves the plugin status from the form data map
        plugin_status = form_data_map["plugin_status"]

        # changes the plugin status and retrieves the result
        change_status_plugin_result = self._change_status_plugin(rest_request, plugin_id, plugin_status)

        # serializes the change status result using the json plugin
        serialized_status = serializer.dumps(change_status_plugin_result)

        # sets the serialized status as the rest request contents
        self.set_contents(rest_request, serialized_status)

        # sends the serialized broadcast message
        web_mvc_manager_communication_helper_controller.send_serialized_broadcast_message(parameters, "web_mvc_manager/communication", "web_mvc_manager/plugin/change_status", serialized_status)

    def handle_change_status_json(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # handles the request with the general
        # handle create serialized method
        self.handle_change_status_serialized(rest_request, parameters)

    def _get_plugin(self, rest_request, plugin_id):
        # retrieves the plugin manager
        plugin_manager = self.web_mvc_manager_plugin.manager

        # retrieves the plugin from the given plugin id
        plugin = plugin_manager._get_plugin_by_id(plugin_id)

        # returns the specified plugin
        return plugin

    def _get_filtered_plugins(self, rest_request, search_query):
        # retrieves the plugins
        plugins = self._get_plugins()

        # creates the filtered plugins list
        filtered_plugins = [plugin for plugin in plugins if not plugin.id.find(search_query) == -1]

        # returns the filtered plugins
        return filtered_plugins

    def _get_plugins(self):
        # retrieves the plugin manager
        plugin_manager = self.web_mvc_manager_plugin.manager

        # retrieves the plugins
        plugins = plugin_manager.get_all_plugins()

        # returns all plugins
        return plugins

    def _change_status_plugin(self, rest_request, plugin_id, plugin_status):
        # retrieves the plugin manager
        plugin_manager = self.web_mvc_manager_plugin.manager

        # retrieves the (beginning) list of loaded plugins
        loaded_plugins_beginning = copy.copy(plugin_manager.get_all_loaded_plugins())

        # loads the plugin for the given plugin id in case the plugin status is load
        (plugin_status == LOAD_VALUE) and plugin_manager.load_plugin(plugin_id)

        # unloads the plugin for the given plugin id in case the plugin status in unload
        (plugin_status == UNLOAD_VALUE) and plugin_manager.unload_plugin(plugin_id)

        # retrieves the (end) list of loaded plugins
        loaded_plugins_end = plugin_manager.get_all_loaded_plugins()

        # iterates over all the plugins loaded at the end
        # to check if they exist in the previously loaded plugins
        loaded_list = [loaded_plugin_end.id for loaded_plugin_end in loaded_plugins_end if not loaded_plugin_end in loaded_plugins_beginning]

        # iterates over all the plugins loaded at the beginning
        # to check if they exist in the current loaded plugins
        unloaded_list = [loaded_plugin_beginning.id for loaded_plugin_beginning in loaded_plugins_beginning if not loaded_plugin_beginning in loaded_plugins_end]

        # creates the delta plugin status map
        delta_plugin_status_map = {
            LOADED_VALUE : loaded_list,
            UNLOADED_VALUE : unloaded_list
        }

        # returns the delta plugin status map
        return delta_plugin_status_map

class CapabilityController:
    """
    The web mvc manager capability controller.
    """

    web_mvc_manager_plugin = None
    """ The web mvc manager plugin """

    web_mvc_manager = None
    """ The web mvc manager """

    def __init__(self, web_mvc_manager_plugin, web_mvc_manager):
        """
        Constructor of the class.

        @type web_mvc_manager_plugin: WebMvcManagerPlugin
        @param web_mvc_manager_plugin: The web mvc manager plugin.
        @type web_mvc_manager: WebMvcManager
        @param web_mvc_manager: The web mvc manager.
        """

        self.web_mvc_manager_plugin = web_mvc_manager_plugin
        self.web_mvc_manager = web_mvc_manager

    def start(self):
        """
        Method called upon structure initialization.
        """

        # sets the relative resources path
        self.set_relative_resources_path(WEB_MVC_MANAGER_RESOURCES_PATH, extra_templates_path = "capability")

    def validate(self, rest_request, parameters, validation_parameters):
        # returns the result of the require permission call
        return self.web_mvc_manager.require_permissions(self, rest_request, validation_parameters)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("capabilites.list")
    def handle_list(self, rest_request, parameters = {}):
        # retrieves the exception handler
        exception_handler = self.web_mvc_manager.web_mvc_manager_exception_controller

        # sets the exception handler in the parameters
        parameters[EXCEPTION_HANDLER_VALUE] = exception_handler

        # retrieves the template file
        template_file = self.retrieve_template_file("../general.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "page_include", "capability/capability_list_contents.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "side_panel_include", "side_panel/side_panel_configuration.html.tpl")

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("capabilites.list")
    def handle_list_ajx(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # retrieves the template file
        template_file = self.retrieve_template_file("capability_list_contents.html.tpl")

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("capabilites.list")
    def handle_partial_list_ajx(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # retrieves the web mvc manager search helper controller
        web_mvc_manager_search_helper_controller = self.web_mvc_manager.web_mvc_manager_search_helper_controller

        # retrieves the form data by processing the form
        form_data_map = self.process_form_data(rest_request, DEFAULT_ENCODING)

        # retrieves the form data attributes
        search_query = form_data_map["search_query"]

        # retrieves the start record
        start_record = form_data_map["start_record"]

        # retrieves the number records
        number_records = form_data_map["number_records"]

        # converts the start record to integer
        start_record = int(start_record)

        # converts the number records to integer
        number_records = int(number_records)

        # retrieves the filtered capabilities
        filtered_capabilities = self._get_filtered_capabilities(rest_request, search_query)

        # retrieves the partial filter from the filtered capabilities
        partial_filtered_capabilities, start_record, number_records, total_number_records = web_mvc_manager_search_helper_controller.partial_filter(rest_request, filtered_capabilities, start_record, number_records)

        # retrieves the template file
        template_file = self.retrieve_template_file("capability_partial_list_contents.html.tpl")

        # assigns the capabilities to the template
        template_file.assign("capabilities", partial_filtered_capabilities)

        # assigns the start record to the template
        template_file.assign("start_record", start_record)

        # assigns the number records to the template
        template_file.assign("number_records", number_records)

        # assigns the total number records to the template
        template_file.assign("total_number_records", total_number_records)

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.validated_method("capabilites.show")
    def handle_show(self, rest_request, parameters = {}):
        # retrieves the pattern names from the parameters
        pattern_names = parameters[PATTERN_NAMES_VALUE]

        # retrieves the capability pattern
        capability = pattern_names["capability"]

        # retrieves the plugins map for the capability
        plugins_capability = self._get_plugins_capability(rest_request, capability)

        # retrieves the sub capabilities for the capability
        sub_capabilities = self._get_sub_capabilities(rest_request, capability)

        # retrieves the template file
        template_file = self.retrieve_template_file("../general.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "page_include", "capability/capability_edit_contents.html.tpl")

        # assigns the include to the template
        self.assign_include_template_file(template_file, "side_panel_include", "side_panel/side_panel_configuration.html.tpl")

        # assigns the capability to the template
        template_file.assign("capability", capability)

        # assigns the plugins capability to the template
        template_file.assign("plugins_capability", plugins_capability)

        # assigns the sub capabilities to the template
        template_file.assign("sub_capabilities", sub_capabilities)

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    @web_mvc_utils.serialize_exceptions("all")
    @web_mvc_utils.validated_method("capabilites.show")
    def handle_show_ajx(self, rest_request, parameters = {}):
        # retrieves the json plugin
        json_plugin = self.web_mvc_manager_plugin.json_plugin

        # sets the serializer in the parameters
        parameters[SERIALIZER_VALUE] = json_plugin

        # retrieves the pattern names from the parameters
        pattern_names = parameters[PATTERN_NAMES_VALUE]

        # retrieves the capability pattern
        capability = pattern_names["capability"]

        # retrieves the plugins map for the capability
        plugins_capability = self._get_plugins_capability(rest_request, capability)

        # retrieves the sub capabilities for the capability
        sub_capabilities = self._get_sub_capabilities(rest_request, capability)

        # retrieves the template file
        template_file = self.retrieve_template_file("capability_edit_contents.html.tpl")

        # assigns the capability to the template
        template_file.assign("capability", capability)

        # assigns the plugins capability to the template
        template_file.assign("plugins_capability", plugins_capability)

        # assigns the sub capabilities to the template
        template_file.assign("sub_capabilities", sub_capabilities)

        # assigns the session variables to the template file
        self.assign_session_template_file(rest_request, template_file)

        # applies the base path to the template file
        self.apply_base_path_template_file(rest_request, template_file)

        # processes the template file and sets the request contents
        self.process_set_contents(rest_request, template_file)

    def _get_filtered_capabilities(self, rest_request, search_query):
        # retrieves the capabilities
        capabilities = self._get_capabilities()

        # creates the filtered capabilities list
        filtered_capabilities = [capability for capability in capabilities if not capability.find(search_query) == -1]

        # returns the filtered capabilities
        return filtered_capabilities

    def _get_capabilities(self):
        # retrieves the plugin manager
        plugin_manager = self.web_mvc_manager_plugin.manager

        # retrieves all the capabilities
        capabilities = plugin_manager.capabilities_plugin_instances_map.keys()

        # sorts all the capabilities
        capabilities.sort()

        # returns the capabilities
        return capabilities

    def _get_plugins_capability(self, rest_request, capability):
        # retrieves the plugin manager
        plugin_manager = self.web_mvc_manager_plugin.manager

        # retrieves the plugins providing the capability
        plugins_offering = list(set(plugin_manager.capabilities_plugin_instances_map.get(capability, [])))

        # retrieves the plugins allowing the capability
        plugins_allowing = list(set(plugin_manager.capabilities_plugins_map.get(capability, [])))

        # creates an unique set of plugins offering the capability
        plugins_offering_unique = set(plugins_offering)

        # creates an unique set of plugins allowing the capability
        plugins_allowing_unique = set(plugins_allowing)

        # defines the plugins map
        plugins_map = {
            PROVIDING_VALUE : plugins_offering_unique,
            ALLOWING_VALUE : plugins_allowing_unique
        }

        # returns the plugins map
        return plugins_map

    def _get_sub_capabilities(self, rest_request, capability):
        # retrieves the plugin manager
        plugin_manager = self.web_mvc_manager_plugin.manager

        # retrieves the sub capabilities for the capability
        sub_capabilities = plugin_manager.capabilities_sub_capabilities_map.get(capability, [])

        # returns the sub capabilities
        return sub_capabilities

class ExceptionController:
    """
    The web mvc manager exception controller.
    """

    web_mvc_manager_plugin = None
    """ The web mvc manager plugin """

    web_mvc_manager = None
    """ The web mvc manager """

    def __init__(self, web_mvc_manager_plugin, web_mvc_manager):
        """
        Constructor of the class.

        @type web_mvc_manager_plugin: WebMvcManagerPlugin
        @param web_mvc_manager_plugin: The web mvc manager plugin.
        @type web_mvc_manager: WebMvcManager
        @param web_mvc_manager: The web mvc manager.
        """

        self.web_mvc_manager_plugin = web_mvc_manager_plugin
        self.web_mvc_manager = web_mvc_manager

    def start(self):
        """
        Method called upon structure initialization.
        """

        # sets the relative resources path
        self.set_relative_resources_path(WEB_MVC_MANAGER_RESOURCES_PATH)

    def handle_exception(self, rest_request, parameters = {}):
        """
        Handles an exception.

        @type rest_request: RestRequest
        @param rest_request: The rest request for which the exception occurred.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the exception
        exception = parameters.get(EXCEPTION_VALUE)

        # retrieves the exception message
        exception_message = exception.get(MESSAGE_VALUE)

        # creates the exception complete message
        exception_complete_message = "Exception: " + exception_message

        # sets the exception message in the rest request
        self.set_contents(rest_request, exception_complete_message)
