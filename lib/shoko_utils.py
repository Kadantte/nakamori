# -*- coding: utf-8 -*-

import xbmcaddon
import xbmcvfs
import xbmcgui
import xbmc

import json

from lib import nakamori_utils
from lib import kodi_utils

plugin_addon = xbmcaddon.Addon('plugin.video.nakamori')


def can_connect(ip: str = None, port: int = None):
    """
    check if shoko is running by quering public accessinble API Endpoint
    :param ip: IP Address or Host name of Shoko Server
    :param port: Port number of Shoko Server
    :return: Bool
    """
    if port is None:
        port = plugin_addon.getSettingInt('port')

    if ip is None:
        ip = plugin_addon.getSetting('ipaddress')

    try:
        json_file = nakamori_utils.get_json('http://%s:%i/api/version' % (ip, port), direct=True)
        if json_file is None:
            return False
        return True
    except Exception as ex:
        xbmc.log(f'We had error here: {ex}', xbmc.LOGINFO)
        return False


def get_server_status(ip: str = plugin_addon.getSetting('ipaddress'), port: int = plugin_addon.getSettingInt('port')):
    """
    Try to query server for status, display messages as needed
    don't bother with caching, this endpoint is really fast
    :return: bool
    """
    if port is None:
        port = plugin_addon.getSettingInt('port')

    if ip is None:
        ip = plugin_addon.getSetting('ipaddress')

    url = 'http://%s:%i/api/init/status' % (ip, port)
    try:
        response = nakamori_utils.get_json(url, True)

        # we should have a json response now
        # example:
        # {"startup_state":"Complete!","server_started":false,"server_uptime":"04:00:45","first_run":false,"startup_failed":false,"startup_failed_error_message":""}
        json_tree = json.loads(response)

        server_started = json_tree.get('server_started', False)
        startup_failed = json_tree.get('startup_failed', False)
        startup_state = json_tree.get('startup_state', '')

        # server started successfully
        if server_started:
            return True

        # not started successfully
        if startup_failed:
            # server finished trying to start, but failed
            kodi_utils.message_box('server was starting ', 'but it failed')
            return False

        was_canceled = False
        busy = xbmcgui.DialogProgress()
        busy.create('serwer status', startup_state)
        busy.update(1)
        # poll every second until the server gives us a response that we want
        while True:
            xbmc.sleep(1000)
            response = nakamori_utils.get_json(url, True)

            # this should not happen
            if response is None or int(response) > 200:
                busy.close()
                kodi_utils.message_box("not happening", "strange error")
                return False

            json_tree = json.loads(response)
            server_started = json_tree.get('server_started', False)
            if server_started:
                busy.close()
                return True

            startup_failed = json_tree.get('startup_failed', False)

            if json_tree.get('startup_state', '') == startup_state:
                continue
            startup_state = json_tree.get('startup_state', '')

            busy.update(1, f"current status :{startup_state}")
            if startup_failed:
                break

            if busy.iscanceled():
                was_canceled = True
                break

        busy.close()

        if was_canceled:
            return False

        if startup_failed:
            kodi_utils.message_box("startup", "failed")
            return False
        return True
    except Exception as e:
        print(e)
        return False


def can_user_connect():
    # TRY to use new method which is faster
    try:
        url = f"http://{plugin_addon.getSetting('ipaddress')}:{plugin_addon.getSetting('port')}/api/ping"
        ping = nakamori_utils.get_json(url, True)
        if ping is not None and b'pong' in ping:
            return True
        else:  # should never happen
            return False
    except Exception as ex:
        xbmc.log(' ===== auth error ===== %s ' % ex, xbmc.LOGINFO)
        plugin_addon.setSetting('apikey', '')
    return False


def auth():
    """
    Checks the apikey, if any, attempts to log in, and saves if we have auth
    :return: bool True if all completes successfully
    """
    # new flow for auth
    # we store the apikey, and its existence is what determines whether to try to connect
    # we will have a log out button, and that wipes the apikey, then we go through the log in steps
    # we have an apikey. try to connect
    if plugin_addon.getSetting('apikey') != '' and can_user_connect():
        return True
    # just in case there's a situation where the wizard isn't working, we can fill it in the settings
    if plugin_addon.getSetting('login') != '':
        login = plugin_addon.getSetting('login')
        password = plugin_addon.getSetting('password')
        apikey = get_apikey(login, password)
        if apikey is not None:
            plugin_addon.setSetting('apikey', apikey)
            plugin_addon.setSetting(id='login', value='')
            plugin_addon.setSetting(id='password', value='')
            return can_user_connect()
    # we tried the apikey, and login failed, too
    return False


def get_apikey(login, password):
    try:
        body = '{"user":"%s","pass":"%s","device":"%s"}' % (login, password, plugin_addon.getSetting("device"))
        post_body = nakamori_utils.post_data(f"http://{plugin_addon.getSetting('ipaddress')}:{plugin_addon.getSetting('port')}/api/auth", body)
        auth_body = json.loads(post_body)
        if 'apikey' in auth_body:
            apikey_found_in_auth = str(auth_body['apikey'])
            return apikey_found_in_auth
        else:
            raise Exception("eroor")
    except Exception as ex:
        xbmc.log(' === get_apikey error === %s ' % ex, xbmc.LOGINFO)
        return None