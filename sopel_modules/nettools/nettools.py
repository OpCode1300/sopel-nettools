# coding=utf-8
"""Network tools module"""

from __future__ import unicode_literals, absolute_import, print_function, division

import socket

from sopel.module import commands, example


def configure(config):
    pass


def setup(bot=None):
    pass


def valid_ip(address):
    try:
        socket.inet_aton(address)
        return True
    except:
        return False

def lookupaddr(addr):
    try:
        return socket.gethostbyaddr(addr)
    except socket.herror:
        return None, None, None

def lookuphost(hostname):
    try:
        return socket.gethostbyname(socket.getfqdn(hostname))
    except socket.gaierror:
        return None

@commands('iplookup', 'ip')
def ip(bot, trigger):
    """IP Lookup tool"""
    if not trigger.group(2):
        return bot.reply("No search term.")
    query = trigger.group(2)

    if valid_ip(query):
        # query is IP
        hostname, aliaslist, ipaddrlist = lookupaddr(query)
        if hostname is not None:
            response = "Hostname: %s" % hostname
        else:
            response = "Unable to resolve hostname: %s" % query
    else:
        # query is hostname
        ip = lookuphost(query)
        if ip is not None:
            response = "IP: %s" % ip
        else:
            response = "Unable to lookup ip: %s" % query

    bot.say(response)
