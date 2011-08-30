#!/usr/bin/python
# -*- coding: utf-8 -*-

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

__author__ = "João Magalhães <joamag@hive.pt>"
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

import web_mvc_utils_exceptions

ERROR_STATUS_CODE = 500
""" The error status code """

VALIDATE_VALUE = "validate"
""" The validate value """

VALIDATION_FAILED_VALUE = "validation_failed"
""" The validation failed value """

SERIALIZER_VALUE = "serializer"
""" The serializer value """

EXCEPTION_HANDLER_VALUE = "exception_handler"
""" The exception handler value """

PATTERN_NAMES_VALUE = "pattern_names"
""" The pattern names value """

VALIDATION_METHOD_ENABLED_VALUE = "validation_method_enabled"
""" The validation method enabled value """

def validated_method(validation_parameters = None, validation_method = None, call_validation_failed = False):
    """
    Decorator for the validated method.

    @type validation_parameters: Object
    @param validation_parameters: The parameters to be used when calling
    the validate method.
    @type validation_method: Method
    @param validation_method: The validation method to be used for extra
    validation (in case it's necessary).
    @type call_validation_failed: bool
    @param call_validation_failed: If the validation failed method should be
    called in case the validation fails.
    @rtype: Function
    @return: The created decorator.
    """

    def create_decorator_interceptor(function):
        """
        Creates a decorator interceptor, that intercepts
        the normal function call.

        @type function: Function
        @param function: The callback function.
        """

        def decorator_interceptor(*args, **kwargs):
            """
            The interceptor function for the transaction_method decorator.

            @type args: pointer
            @param args: The function arguments list.
            @type kwargs: pointer pointer
            @param kwargs: The function arguments map.
            """

            # retrieves the arguments length
            args_length = len(args)

            # retrieves the self reference
            self = args[0]

            # retrieves the rest request reference
            rest_request = args[1]

            # retrieves the parameters reference
            parameters = args_length > 2 and args[2] or {}

            # in case the controller instance
            # does not have the validate method
            if not hasattr(self, VALIDATE_VALUE):
                # raises the controller validation failed
                raise web_mvc_utils_exceptions.ControllerValidationError("validation method not found", self)

            # tests if the controller instance contains the validate method
            contains_validate = hasattr(self, "validate")

            # calls the validate method with the rest request
            # the parameters and the validation parameters and retrieves
            # the list with the validation failure reasons, in case no validate
            # method is present ignores the call
            reasons_list = contains_validate and self.validate(rest_request, parameters, validation_parameters) or []

            # tries to retrieves the validation failed method
            validation_failed_method = hasattr(self, VALIDATION_FAILED_VALUE) and self.validation_failed or None

            # retrieves validation method enabled value from the parameters
            validation_method_enabled = parameters.get(VALIDATION_METHOD_ENABLED_VALUE, True)

            # retrieves the patterns
            patterns = parameters.get(PATTERN_NAMES_VALUE, {})

            # retrieves the session attributes map
            session_attributes = rest_request.get_session_attributes_map()

            # in case the validation method is set and the validation method
            # enabled flag is set in the parameters
            if validation_method and validation_method_enabled:
                try:
                    # calls the validation method with the patterns and the session attributes
                    validation_method_result = validation_method(patterns, session_attributes)

                    # in case the validation method running failed
                    not validation_method_result and reasons_list.append(web_mvc_utils_exceptions.ValidationMethodError("validation method failed in running"))
                except BaseException, exception:
                    # adds the exception to the reasons list
                    reasons_list.append(exception)

            # in case the reasons list is not empty
            if reasons_list:
                # in case a validation failed method is defined and
                # the call validation failed flag is set
                if validation_failed_method and call_validation_failed:
                    # calls the validation failed method with the rest request the parameters the
                    # validation parameters and the reasons list and sets the return value
                    return_value = validation_failed_method(rest_request, parameters, validation_parameters, reasons_list)
                # otherwise there is no validation method defined
                else:
                    # raises the controller validation failed
                    raise web_mvc_utils_exceptions.ControllerValidationReasonFailed("validation failed for a series of reasons: " + str(reasons_list), self, reasons_list)
            # otherwise the reason list is empty (no errors)
            else:
                # calls the callback function,
                # retrieving the return value
                return_value = function(*args, **kwargs)

            # returns the return value
            return return_value

        # returns the decorator interceptor
        return decorator_interceptor

    def decorator(function, *args, **kwargs):
        """
        The decorator function for the load_allowed decorator.

        @type function: Function
        @param function: The function to be decorated.
        @type args: pointer
        @param args: The function arguments list.
        @type kwargs: pointer pointer
        @param kwargs: The function arguments map.
        @rtype: Function
        @return: The decorator interceptor function.
        """

        # creates the decorator interceptor with the given function
        decorator_interceptor_function = create_decorator_interceptor(function)

        # returns the interceptor to be used
        return decorator_interceptor_function

    # returns the created decorator
    return decorator

def transaction_method(entity_manager_reference, raise_exception = True):
    """
    Decorator for the transaction method.

    @type entity_manager: EntityManager
    @param entity_manager: The entity manager to be used for transaction
    management, this entity manager should be started and running.
    @type raise_exception: bool
    @param raise_exception: If an exception should be raised in case it occurs.
    @rtype: Function
    @return: The created decorator.
    """

    def create_decorator_interceptor(function):
        """
        Creates a decorator interceptor, that intercepts
        the normal function call.

        @type function: Function
        @param function: The callback function.
        """

        def decorator_interceptor(*args, **kwargs):
            """
            The interceptor function for the transaction_method decorator.

            @type args: pointer
            @param args: The function arguments list.
            @type kwargs: pointer pointer
            @param kwargs: The function arguments map.
            """

            # retrieves the self reference
            self = args[0]

            # in case the current object contains
            # the entity manager reference
            if hasattr(self, entity_manager_reference):
                # sets the entity manager as the current reference
                entity_manager = getattr(self, entity_manager_reference)
            else:
                # splits the entity manager reference
                entity_manager_reference_splitted = entity_manager_reference.split(".")

                # sets the object reference as the current value
                current = self

                # iterates over all the entity manager reference values
                # splitted in parts
                for entity_manager_reference_value in entity_manager_reference_splitted:
                    # retrieves the current value using the entity
                    # manager reference value
                    current = getattr(current, entity_manager_reference_value)

                # sets the entity manager as the current
                # value
                entity_manager = current

                # sets the entity manager in the object reference
                setattr(self, entity_manager_reference, entity_manager)

            # creates a transaction
            entity_manager.create_transaction()

            try:
                # calls the callback function,
                # retrieving the return value
                return_value = function(*args, **kwargs)
            except:
                # rolls back the transaction
                entity_manager.rollback_transaction()

                # in case the raise exception flag is set
                if raise_exception:
                    # re-raises the exception
                    raise
            else:
                # commits the transaction
                entity_manager.commit_transaction()

            # returns the return value
            return return_value

        # returns the decorator interceptor
        return decorator_interceptor

    def decorator(function, *args, **kwargs):
        """
        The decorator function for the load_allowed decorator.

        @type function: Function
        @param function: The function to be decorated.
        @type args: pointer
        @param args: The function arguments list.
        @type kwargs: pointer pointer
        @param kwargs: The function arguments map.
        @rtype: Function
        @return: The decorator interceptor function.
        """

        # creates the decorator interceptor with the given function
        decorator_interceptor_function = create_decorator_interceptor(function)

        # returns the interceptor to be used
        return decorator_interceptor_function

    # returns the created decorator
    return decorator

def serialize_exceptions(serialization_parameters = None):
    """
    Decorator for the serialize exceptions.

    @type serialization_parameters: Object
    @param serialization_parameters: The parameters to be used when serializing
    the exception.
    @rtype: Function
    @return: The created decorator.
    """

    def create_decorator_interceptor(function):
        """
        Creates a decorator interceptor, that intercepts
        the normal function call.

        @type function: Function
        @param function: The callback function.
        """

        def decorator_interceptor(*args, **kwargs):
            """
            The interceptor function for the transaction_method decorator.

            @type args: pointer
            @param args: The function arguments list.
            @type kwargs: pointer pointer
            @param kwargs: The function arguments map.
            """

            # retrieves the arguments length
            args_length = len(args)

            # retrieves the self reference
            self = args[0]

            # retrieves the rest request reference
            rest_request = args[1]

            # retrieves the parameters reference
            parameters = args_length > 2 and args[2] or {}

            try:
                # calls the callback function,
                # retrieving the return value
                return_value = function(*args, **kwargs)
            except BaseException, exception:
                # retrieves the serializer
                serializer = parameters.get(SERIALIZER_VALUE, None)

                # retrieves the exception handler
                exception_handler = parameters.get(EXCEPTION_HANDLER_VALUE, None)

                # in case the serializer and the exception
                # handler are not set
                if not serializer and not exception_handler:
                    # re-raises the exception
                    raise

                # retrieves the exception map for the exception
                exception_map = self.get_exception_map(exception)

                # sets the error status code
                self.set_status_code(rest_request, ERROR_STATUS_CODE)

                # in case the serializer is set
                if serializer:
                    # dumps the exception map to the serialized form
                    exception_map_serialized = serializer.dumps(exception_map)

                    # sets the serialized map as the rest request contents
                    self.set_contents(rest_request, exception_map_serialized)

                    # sets the return value as invalid (error)
                    return_value = False
                # in case the exception handler is set
                elif exception_handler:
                    # handles the exception map with the exception handler
                    return_value = exception_handler.handle_exception(rest_request, exception_map,)

            # returns the return value
            return return_value

        # returns the decorator interceptor
        return decorator_interceptor

    def decorator(function, *args, **kwargs):
        """
        The decorator function for the load_allowed decorator.

        @type function: Function
        @param function: The function to be decorated.
        @type args: pointer
        @param args: The function arguments list.
        @type kwargs: pointer pointer
        @param kwargs: The function arguments map.
        @rtype: Function
        @return: The decorator interceptor function.
        """

        # creates the decorator interceptor with the given function
        decorator_interceptor_function = create_decorator_interceptor(function)

        # returns the interceptor to be used
        return decorator_interceptor_function

    # returns the created decorator
    return decorator
