"""This module contains model that stores Robot Framework variables."""

#  Copyright (c) 2023 EPAM Systems
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License

from distutils.util import strtobool
from os import path
from warnings import warn

from reportportal_client.logs.log_manager import MAX_LOG_BATCH_PAYLOAD_SIZE
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError

# This is a storage for the result visitor
_variables = {}


def get_variable(name, default=None):
    """Get Robot Framework variable.

    :param name:    Name of the variable
    :param default: Default value
    :return:        The value of the variable, otherwise default value
    """
    try:
        return BuiltIn().get_variable_value("${" + name + "}", default=default)
    except RobotNotRunningError:
        return _variables.get(name, default)


class Variables(object):
    """This class stores Robot Framework variables related to Report Portal."""

    def __init__(self):
        """Initialize instance attributes."""
        self.endpoint = get_variable('RP_ENDPOINT')
        self.launch_name = get_variable('RP_LAUNCH')
        self.project = get_variable('RP_PROJECT')

        self._pabot_pool_id = None
        self._pabot_used = None
        self.attach_log = bool(strtobool(get_variable(
            'RP_ATTACH_LOG', default='False')))
        self.attach_report = bool(strtobool(get_variable(
            'RP_ATTACH_REPORT', default='False')))
        self.attach_xunit = bool(strtobool(get_variable(
            'RP_ATTACH_XUNIT', default='False')))
        self.launch_attributes = get_variable(
            'RP_LAUNCH_ATTRIBUTES', default='').split()
        self.launch_id = get_variable('RP_LAUNCH_UUID')
        self.launch_doc = get_variable('RP_LAUNCH_DOC')
        self.log_batch_size = int(get_variable(
            'RP_LOG_BATCH_SIZE', default='20'))
        self.mode = get_variable('RP_MODE')
        self.pool_size = int(get_variable('RP_MAX_POOL_SIZE', default='50'))
        self.rerun = bool(strtobool(get_variable(
            'RP_RERUN', default='False')))
        self.rerun_of = get_variable('RP_RERUN_OF', default=None)
        self.skipped_issue = bool(strtobool(get_variable(
            'RP_SKIPPED_ISSUE', default='True')))
        self.test_attributes = get_variable(
            'RP_TEST_ATTRIBUTES', default='').split()
        self.log_batch_payload_size = int(get_variable(
            "RP_LOG_BATCH_PAYLOAD_SIZE",
            default=str(MAX_LOG_BATCH_PAYLOAD_SIZE)))

        self.api_key = get_variable('RP_API_KEY')
        if not self.api_key:
            token = get_variable('RP_UUID')
            if token:
                warn(
                    message="Argument `token` is deprecated since 2.0.4 and "
                            "will be subject for removing in the next major "
                            "version. Use `api_key` argument instead.",
                    category=DeprecationWarning,
                    stacklevel=2
                )
                self.api_key = token
            else:
                warn(
                    message="Argument `api_key` is `None` or empty string, "
                            "that's not supposed to happen because Report "
                            "Portal is usually requires an authorization key. "
                            "Please check your code.",
                    category=RuntimeWarning,
                    stacklevel=2
                )

        cond = (self.endpoint, self.launch_name, self.project, self.api_key)
        self.enabled = all(cond)
        if not self.enabled:
            warn(
                'One or required parameter is missing, Report Portal listener '
                'will be disabled. Please check agent documentation.',
                RuntimeWarning,
                2
            )

    @property
    def pabot_pool_id(self):
        """Get pool id for the current Robot Framework executor.

        :return: Pool id for the current Robot Framework executor
        """
        if not self._pabot_pool_id:
            self._pabot_pool_id = get_variable(name='PABOTEXECUTIONPOOLID')
        return self._pabot_pool_id

    @property
    def pabot_used(self):
        """Get status of using pabot in test execution.

        :return: Cached value of the Pabotlib URI
        """
        if not self._pabot_used:
            self._pabot_used = get_variable(name='PABOTLIBURI')
        return self._pabot_used

    @property
    def verify_ssl(self):
        """Get value of the verify_ssl parameter for the client."""
        verify_ssl = get_variable('RP_VERIFY_SSL', default='True')
        if path.exists(verify_ssl):
            return verify_ssl
        return bool(strtobool(verify_ssl))
