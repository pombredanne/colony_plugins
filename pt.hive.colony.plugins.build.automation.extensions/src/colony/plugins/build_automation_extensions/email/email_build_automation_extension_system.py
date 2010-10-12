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

__revision__ = "$LastChangedRevision: 72 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-10-21 23:29:54 +0100 (Ter, 21 Out 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import sys
import datetime

BUILD_AUTOMATION_EXTENSIONS_EMAIL_PATH = "build_automation_extensions/email/resources"
""" The build automation extensions email resources path """

EMAIL_TEXT_REPORT_TEMPLATE_FILE_NAME = "email_text_report.txt.tpl"
""" The email text report template file name """

EMAIL_HTML_REPORT_TEMPLATE_FILE_NAME = "email_html_report.html.tpl"
""" The email html report template file name """

DEFAULT_ENCODING = "Cp1252"
""" The default encoding """

DEFAULT_SMTP_HOSTNAME = "localhost"
""" The default smtp hostname """

DEFAULT_SMTP_PORT = 25
""" The default smtp port """

DEFAULT_SENDER_NAME = "Colony Integration"
""" The default sender name """

DEFAULT_SENDER_EMAIL = "integration@getcolony.com"
""" The default sender email """

USERNAME_VALUE = "username"
""" The username value """

PASSWORD_VALUE = "password"
""" The password value """

TLS_VALUE = "tls"
""" The tls value """

FROM_VALUE = "From"
""" The from value """

TO_VALUE = "To"
""" The to value """

SUBJECT_VALUE = "Subject"
""" The subject value """

DATE_VALUE = "Date"
""" The date value """

CONTENT_TYPE_VALUE = "Content-Type"
""" The content type value """

USER_AGENT_VALUE = "User-Agent"
""" The user agent value """

USER_AGENT_NAME = "Hive-Colony-Email-Client"
""" The user agent name """

USER_AGENT_VERSION = "1.0.0"
""" The user agent version """

ENVIRONMENT_VERSION = str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]) + "-" + str(sys.version_info[3])
""" The environment version """

USER_AGENT_IDENTIFIER = USER_AGENT_NAME + "/" + USER_AGENT_VERSION + " (Python/" + sys.platform + "/" + ENVIRONMENT_VERSION + ")"
""" The user agent identifier """

DATE_TIME_FORMAT = "%a, %d %b %Y %H:%M:%S +0000 (UTC)"
""" The format for the displayed date times """

SUCCESS_CAPITALS_MAP = {True : "SUCCESS", False : "FAILED"}
""" The success capitals map """

class EmailBuildAutomationExtension:
    """
    The email build automation extension class.
    """

    email_build_automation_extension_plugin = None
    """ The email build automation extension plugin """

    def __init__(self, email_build_automation_extension_plugin):
        """
        Constructor of the class.

        @type email_build_automation_extension_plugin: EmailBuildAutomationExtensionPlugin
        @param email_build_automation_extension_plugin: The email build automation extension plugin.
        """

        self.email_build_automation_extension_plugin = email_build_automation_extension_plugin

    def run_automation(self, plugin, stage, parameters, build_automation_structure, logger):
        # prints an info message
        logger.info("Running email build automation plugin")

        # retrieves the plugin manager
        plugin_manager = self.email_build_automation_extension_plugin.manager

        # retrieves the main client smtp plugin
        main_client_smtp_plugin = self.email_build_automation_extension_plugin.main_client_smtp_plugin

        # retrieves the format mime plugin
        format_mime_plugin = self.email_build_automation_extension_plugin.format_mime_plugin

        # retrieves the format mime utils plugin
        format_mime_utils_plugin = self.email_build_automation_extension_plugin.format_mime_utils_plugin

        # retrieves the template engine manager plugin
        template_engine_manager_plugin = self.email_build_automation_extension_plugin.template_engine_manager_plugin

        # retrieves the build automation structure associated plugin
        build_automation_structure_associated_plugin = build_automation_structure.associated_plugin

        # retrieves the build automation structure runtime
        build_automation_structure_runtime = build_automation_structure.runtime

        # creates a new smtp client, using the main client smtp plugin
        smtp_client = main_client_smtp_plugin.create_client({})

        # opens the smtp client
        smtp_client.open({})

        # retrieves the sender parameters from the parameters map
        sender_name = parameters.get("sender_name", DEFAULT_SENDER_NAME)
        sender_email = parameters.get("sender_email", DEFAULT_SENDER_EMAIL)

        # retrieves the smtp parameters from the parameters map
        smtp_hostname = parameters.get("smtp_hostname", DEFAULT_SMTP_HOSTNAME)
        smtp_port = parameters.get("smtp_port", DEFAULT_SMTP_PORT)
        smtp_username = parameters.get("smtp_username", None)
        smtp_password = parameters.get("smtp_password", None)
        smtp_tls = parameters.get("smtp_tls", False)

        # creates the smtp parameters map
        smtp_parameters = {}

        # sets the authentication parameters
        smtp_parameters[USERNAME_VALUE] = smtp_username
        smtp_parameters[PASSWORD_VALUE] = smtp_password
        smtp_parameters[TLS_VALUE] = smtp_tls

        # creates the mime message
        mime_message = format_mime_plugin.create_message({})

        # creates the sender line
        sender_line = sender_name + " " + "<" + sender_email + ">"

        success_receivers = (("Jo�o Magalh�es", "joamag@hive.pt"),)
        failure_receivers = (("Jo�o Magalh�es", "joamag@hive.pt"), ("Tiago Silva", "tsilva@hive.pt"), ("Luis Martinho", "lmartinho@hive.pt"))

        # retrieves the build automation plugin name
        build_automation_plugin_name = build_automation_structure_associated_plugin.name

        # retrieves the build automation version (revision)
        build_automation_version = build_automation_structure_runtime.properties.get("version", -1)

        # creates the build automation log file name
        build_automation_log_file_name = "build_automation_" + str(build_automation_version) + ".log"

        # writes the initial subject line
        subject = "[b%i] %s " % (build_automation_version, build_automation_plugin_name)

        # in case the build automation was successful
        if build_automation_structure_runtime.success:
            # adds the successful part to the subject
            subject += "was SUCCESSFUL"

            # sets the receivers as the success receivers
            receivers = success_receivers
        # otherwise
        else:
            # adds the failed part to the subject
            subject += "as FAILED"

            # sets the receivers as the failure receivers
            receivers = failure_receivers

        # creates the receiver line with the email
        receiver_line = ""

        # creates the list to hold the receiver emails
        receiver_emails = []

        # sets the is first flag
        is_first = True

        # iterates over all the receivers
        # to creates the receiver line
        for receiver in receivers:
            # in case it's the first iteration
            if is_first:
                # unsets the is first flag
                is_first = False
            # otherwise
            else:
                # adds the separator to the receiver line
                receiver_line += ", "

            # retrieves the receiver name and email
            receiver_name, receiver_email = receiver

            # adds the receiver name and email to the receiver line
            receiver_line += receiver_name + " " + "<" + receiver_email + ">"

            # adds the receiver email to the list of receiver emails
            receiver_emails.append(receiver_email)

        # retrieves the current date time, and formats
        # it according to the "standard" format
        current_date_time = datetime.datetime.utcnow()
        current_date_time_formated = current_date_time.strftime(DATE_TIME_FORMAT)

        # sets the basic mime message headers
        mime_message.set_header(FROM_VALUE, sender_line)
        mime_message.set_header(TO_VALUE, receiver_line)
        mime_message.set_header(SUBJECT_VALUE, subject)
        mime_message.set_header(DATE_VALUE, current_date_time_formated)
        mime_message.set_header(USER_AGENT_VALUE, USER_AGENT_IDENTIFIER)

        # retrieves the logging buffer
        logging_buffer = build_automation_structure_runtime.logging_buffer

        # retrieves the logging contents from the logging buffer
        logging_contents = logging_buffer.get_value()

        # retrieves the email build automation extension plugin path
        email_build_automation_extension_plugin_path = plugin_manager.get_plugin_path_by_id(self.email_build_automation_extension_plugin.id)

        # creates the email html report template file path
        email_html_report_template_file_path = email_build_automation_extension_plugin_path + "/" + BUILD_AUTOMATION_EXTENSIONS_EMAIL_PATH + "/" + EMAIL_HTML_REPORT_TEMPLATE_FILE_NAME

        # creates the email html report images file path
        email_html_report_images_file_path = email_build_automation_extension_plugin_path + "/" + BUILD_AUTOMATION_EXTENSIONS_EMAIL_PATH + "/" + "images"

        # parses the template file path
        template_file = template_engine_manager_plugin.parse_file_path(email_html_report_template_file_path)

        # retrieves the success in normal format
        success = build_automation_structure_runtime.success

        # retrieves the success in capitals format
        success_capitals = SUCCESS_CAPITALS_MAP[build_automation_structure_runtime.success]

        # assigns the success to the parsed template file
        template_file.assign("success", success)

        # assigns the success capitals to the parsed template file
        template_file.assign("success_capitals", success_capitals)

        # assigns the plugin name to the parsed template file
        template_file.assign("plugin_name", build_automation_plugin_name)

        # assigns the log file name to the parsed template file
        template_file.assign("log_file_name", build_automation_log_file_name)

        # processes the template file
        processed_template_file = template_file.process()

        # decodes the processed template file into a unicode object
        processed_template_file_decoded = processed_template_file.decode(DEFAULT_ENCODING)

        mime_message_text_part = format_mime_plugin.create_message_part({})
        mime_message_text_part.write(logging_contents)
        mime_message_text_part.set_header(CONTENT_TYPE_VALUE, "text/plain")

        mime_message_html_part = format_mime_plugin.create_message_part({})
        mime_message_html_part.write(processed_template_file_decoded)
        mime_message_html_part.set_header(CONTENT_TYPE_VALUE, "text/html")

        mime_message_packer_part = format_mime_plugin.create_message_part({})
        mime_message_packer_part.set_multi_part("alternative")
        mime_message_packer_part.add_part(mime_message_text_part)
        mime_message_packer_part.add_part(mime_message_html_part)

        # sets the mime message as multipart mixed
        mime_message.set_multi_part("mixed")

        # adds the message packer part to the mime message
        mime_message.add_part(mime_message_packer_part)

        # adds the mime message log attachment to the mime message
        format_mime_utils_plugin.add_mime_message_attachment_contents(mime_message, logging_contents, build_automation_log_file_name)

        # adds the mime message contents (images) to the mime message
        format_mime_utils_plugin.add_mime_message_contents(mime_message, email_html_report_images_file_path, ("gif",))

        # retrieves the mime message value
        mime_message_value = mime_message.get_value()

        # send the email using the defined values
        smtp_client.send_mail(smtp_hostname, smtp_port, sender_email, receiver_emails, mime_message_value, parameters)

        # closes the smtp client
        smtp_client.close({})

        # returns true (success)
        return True
