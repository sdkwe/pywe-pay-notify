# -*- coding: utf-8 -*-

xml = '<xml><appid><![CDATA[appid]]></appid> <bank_type><![CDATA[CFT]]></bank_type> <cash_fee><![CDATA[1]]></cash_fee> <fee_type><![CDATA[CNY]]></fee_type> <is_subscribe><![CDATA[N]]></is_subscribe> <mch_id><![CDATA[mch_id]]></mch_id> <nonce_str><![CDATA[p9EQiW4eJbhzmFOX5ZYxNI6syRLjS0t1]]></nonce_str> <openid><![CDATA[openid]]></openid> <out_trade_no><![CDATA[Uwx4zvQ7ZVtup8X5Ry37vM]]></out_trade_no> <result_code><![CDATA[SUCCESS]]></result_code> <return_code><![CDATA[SUCCESS]]></return_code> <sign><![CDATA[AEB957317E5BE354FF42CFE08279E269]]></sign> <time_end><![CDATA[20170714135749]]></time_end> <total_fee>1</total_fee> <trade_type><![CDATA[JSAPI]]></trade_type> <transaction_id><![CDATA[4006352001201707140719143081]]></transaction_id> </xml>'
api_key = 'your_api_key'

WECHAT = {
    'JSAPI': {
        'token': '5201314',
        'appID': 'appID',
        'appsecret': 'appsecret',
        'mchID': 'mchId',
        'apiKey': 'apiKey',
        'mch_cert': '/tmp/apiclient_cert.pem',
        'mch_key': '/tmp/apiclient_key.pem',
        'redpacket': {
            'SEND_NAME': u'SEND_NAME',
            'NICK_NAME': u'NICK_NAME',
            'ACT_NAME': u'ACT_NAME',
            'WISHING': u'WISHING！',
            'REMARK': u'REMARK',
        }
    }
}
