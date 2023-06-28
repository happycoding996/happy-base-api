from tornado.web import url

from ext.user.handler import BindInviteCodeHandler, RealnameHandler, CertifiedHandler, UserBalanceHandler
from ext.user.handler_recharge import UserCertifiedRechargeHandler
from ext.user.handler_statistics import StatisticsUserHandler

urlpatterns = [
    # 用户扩展
    url('/user/bindInviteCode/', BindInviteCodeHandler),
    url('/user/realname/', RealnameHandler),
    url('/user/certified/', CertifiedHandler),
    url('/user/balance/', UserBalanceHandler),

    # 用户充值
    url('/user/certifiedRecharge/', UserCertifiedRechargeHandler),

    # 用户统计
    url('/user/statistics/', StatisticsUserHandler)
]
