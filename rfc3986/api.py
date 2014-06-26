# -*- coding: utf-8 -*-
# Copyright (c) 2014 Rackspace
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
rfc3986.api
~~~~~~~~~~~

This defines the simple API to rfc3986. This module defines 3 functions and
provides access to the class ``URIReference``.
"""

from .uri import URIReference


def uri_reference(uri):
    """Parse a URI string into a URIReference.

    This is a convenience function. You could achieve the same end by using
    ``URIReference.from_string(uri)``.

    :param str uri: The URI which needs to be parsed into a reference.
    :returns: A parsed URI
    :rtype: :class:`URIReference`
    """
    return URIReference.from_string(uri)


def is_valid_uri(uri):
    """Determine if the URI given is valid.

    This is a convenience function. You could use either
    ``uri_reference(uri).is_valid()`` or
    ``URIReference.from_string(uri).is_valid()`` to achieve the same result.

    :param str uri: The URI to be validated.
    :returns: ``True`` if the URI is valid, ``False`` otherwise.
    :rtype: bool
    """
    return URIReference.from_string(uri).is_valid()


def normalize_uri(uri):
    """Normalize the given URI.

    This is a convenience function. You could use either
    ``uri_reference(uri).normalize().unsplit()`` or
    ``URIReference.from_string(uri).normalize().unsplit()`` instead.

    :param str uri: The URI to be normalized.
    :returns: The normalized URI.
    :rtype: str
    """
    normalized_reference = URIReference.from_string(uri).normalize()
    return normalized_reference.unsplit()