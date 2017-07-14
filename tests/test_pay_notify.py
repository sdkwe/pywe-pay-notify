# -*- coding: utf-8 -*-

from pywe_pay_notify import check_pay_notify

from local_pay_notify_example import WECHAT, api_key, xml


class TestPayNotifyCommands(object):

    def test_check_pay_notify_apikey(self):
        data, success = check_pay_notify(xml, api_key)
        assert isinstance(data, dict)
        assert success

    def test_check_pay_notify_configs(self):
        data, success = check_pay_notify(xml, wx_configs=WECHAT)
        assert isinstance(data, dict)
        assert success

    def test_check_pay_notify_func(self):
        def api_key(data):
            return WECHAT.get(data.get('trade_type', ''), {}).get('apiKey')
        data, success = check_pay_notify(xml, api_key_func=api_key)
        assert isinstance(data, dict)
        assert success
