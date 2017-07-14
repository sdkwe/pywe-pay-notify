# -*- coding: utf-8 -*-

from pywe_pay_notify import check_pay_notify

from local_pay_notify_example import api_key, xml


class TestPayNotifyCommands(object):

    def test_check_pay_notify(self):
        data, success = check_pay_notify(xml, api_key)
        assert isinstance(data, dict)
        assert success
