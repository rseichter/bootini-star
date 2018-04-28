# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 0.8.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class InsuranceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_insurance_prices(self, **kwargs):  # noqa: E501
        """List insurance levels  # noqa: E501

        Return available insurance levels for all ship types  ---  This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_insurance_prices(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str language: Language to use in the response
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetInsurancePrices200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_insurance_prices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_insurance_prices_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_insurance_prices_with_http_info(self, **kwargs):  # noqa: E501
        """List insurance levels  # noqa: E501

        Return available insurance levels for all ship types  ---  This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_insurance_prices_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str language: Language to use in the response
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetInsurancePrices200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'language', 'user_agent', 'x_user_agent']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_insurance_prices" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))  # noqa: E501

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/insurance/prices/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetInsurancePrices200Ok]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
