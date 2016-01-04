# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class ProductVersionRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProductVersionRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'version': 'str',
            'product_id': 'int',
            'current_product_milestone_id': 'int',
            'build_configuration_set_ids': 'list[int]',
            'build_configuration_ids': 'list[int]',
            'product_milestones': 'list[int]',
            'product_releases': 'list[int]'
        }

        self.attribute_map = {
            'id': 'id',
            'version': 'version',
            'product_id': 'productId',
            'current_product_milestone_id': 'currentProductMilestoneId',
            'build_configuration_set_ids': 'buildConfigurationSetIds',
            'build_configuration_ids': 'buildConfigurationIds',
            'product_milestones': 'productMilestones',
            'product_releases': 'productReleases'
        }

        self._id = None
        self._version = None
        self._product_id = None
        self._current_product_milestone_id = None
        self._build_configuration_set_ids = None
        self._build_configuration_ids = None
        self._product_milestones = None
        self._product_releases = None

    @property
    def id(self):
        """
        Gets the id of this ProductVersionRest.


        :return: The id of this ProductVersionRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductVersionRest.


        :param id: The id of this ProductVersionRest.
        :type: int
        """
        self._id = id

    @property
    def version(self):
        """
        Gets the version of this ProductVersionRest.


        :return: The version of this ProductVersionRest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ProductVersionRest.


        :param version: The version of this ProductVersionRest.
        :type: str
        """
        self._version = version

    @property
    def product_id(self):
        """
        Gets the product_id of this ProductVersionRest.


        :return: The product_id of this ProductVersionRest.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this ProductVersionRest.


        :param product_id: The product_id of this ProductVersionRest.
        :type: int
        """
        self._product_id = product_id

    @property
    def current_product_milestone_id(self):
        """
        Gets the current_product_milestone_id of this ProductVersionRest.


        :return: The current_product_milestone_id of this ProductVersionRest.
        :rtype: int
        """
        return self._current_product_milestone_id

    @current_product_milestone_id.setter
    def current_product_milestone_id(self, current_product_milestone_id):
        """
        Sets the current_product_milestone_id of this ProductVersionRest.


        :param current_product_milestone_id: The current_product_milestone_id of this ProductVersionRest.
        :type: int
        """
        self._current_product_milestone_id = current_product_milestone_id

    @property
    def build_configuration_set_ids(self):
        """
        Gets the build_configuration_set_ids of this ProductVersionRest.


        :return: The build_configuration_set_ids of this ProductVersionRest.
        :rtype: list[int]
        """
        return self._build_configuration_set_ids

    @build_configuration_set_ids.setter
    def build_configuration_set_ids(self, build_configuration_set_ids):
        """
        Sets the build_configuration_set_ids of this ProductVersionRest.


        :param build_configuration_set_ids: The build_configuration_set_ids of this ProductVersionRest.
        :type: list[int]
        """
        self._build_configuration_set_ids = build_configuration_set_ids

    @property
    def build_configuration_ids(self):
        """
        Gets the build_configuration_ids of this ProductVersionRest.


        :return: The build_configuration_ids of this ProductVersionRest.
        :rtype: list[int]
        """
        return self._build_configuration_ids

    @build_configuration_ids.setter
    def build_configuration_ids(self, build_configuration_ids):
        """
        Sets the build_configuration_ids of this ProductVersionRest.


        :param build_configuration_ids: The build_configuration_ids of this ProductVersionRest.
        :type: list[int]
        """
        self._build_configuration_ids = build_configuration_ids

    @property
    def product_milestones(self):
        """
        Gets the product_milestones of this ProductVersionRest.


        :return: The product_milestones of this ProductVersionRest.
        :rtype: list[int]
        """
        return self._product_milestones

    @product_milestones.setter
    def product_milestones(self, product_milestones):
        """
        Sets the product_milestones of this ProductVersionRest.


        :param product_milestones: The product_milestones of this ProductVersionRest.
        :type: list[int]
        """
        self._product_milestones = product_milestones

    @property
    def product_releases(self):
        """
        Gets the product_releases of this ProductVersionRest.


        :return: The product_releases of this ProductVersionRest.
        :rtype: list[int]
        """
        return self._product_releases

    @product_releases.setter
    def product_releases(self, product_releases):
        """
        Sets the product_releases of this ProductVersionRest.


        :param product_releases: The product_releases of this ProductVersionRest.
        :type: list[int]
        """
        self._product_releases = product_releases

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
