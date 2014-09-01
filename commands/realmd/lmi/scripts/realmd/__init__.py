# Copyright (C) 2013-2014 Red Hat, Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are
# those of the authors and should not be interpreted as representing official
# policies, either expressed or implied, of the FreeBSD Project.
#
# Author: Tomas Smetana <tsmetana@redhat.com>
#
"""
LMI realmd provider client library.
"""

import pywbem
from getpass import getpass

from lmi.shell import LMIClassNotFound
from lmi.scripts.common import get_logger
from lmi.scripts.common import get_computer_system

LOG = get_logger(__name__)

def read_password():
    return getpass('Realm authentication password: ')

def join(ns, domain, user, _password = None):
    """
    Join the domain.

    :param domain: The domain to be joined.
    :type domain: string
    :param user: User name to authenticate with
    :type user: string
    :param password: The authentication password
    :type password: string
    """
    try:
        r = ns.LMI_RealmdService.first_instance()
        if (_password == None):
            _password = read_password();
        r.JoinDomain(Domain = domain, User = user, Password = _password)
    except Exception as e:
        print e

def leave(ns, domain, user, _password = None):
    """
    Leave the domain.

    :param domain: The domain to be left.
    :type domain: string
    :param user: User name to authenticate with
    :type user: string
    :param password: The authentication password
    :type password: string
    """
    try:
        r = ns.LMI_RealmdService.first_instance()
        if (_password == None):
            _password = read_password();
        r.LeaveDomain(Domain = domain, User = user, Password = _password)
    except Exception as e:
        print e

def show(ns):
    """
    Show the joined domain.

    """
    try:
        r = ns.LMI_RealmdService.first_instance()
        print r.Domain
    except Exception as e:
        print e
