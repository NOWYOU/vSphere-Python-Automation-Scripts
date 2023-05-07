#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : refresh_vcenter_signing_certificate.py
# @Author: NOWSHUT
# @Date  : 2023/3/11 22:19
# @Desc  :
# @Contact : nowshut@qq.com
 
'''
该脚本可以强制刷新STS证书
'''
 
import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client
start_time = time.time()
try:
      refreshsts = vsphere_client.vcenter.certificate_management.vcenter.SigningCertificate.refresh(force=True)
      print("vCenter Signing Certificate Renew Successfully\n"
          "Note: vCenter Server services do not restart")
      print("Active Cert Chain:\n", refreshsts.cert_chain[0],
            "\nSigning Cert Chains:\n", refreshsts.cert_chain[1],
            )
except Exception as err:
    for i in err.messages:
        id = i.id,
        default_message = i.default_message
        args = i.args
        params = i.params
        localized = i.localized
    print("\033[1;31m Encountered an error, Please see the following information \033[0m",
          "\n\tError Class:", id,
          "\n\tMessage:", default_message,
          "\n\tArgs:", args,
          "\n\tParams:", params,
          "\n\tLocalized:", localized,
          "\nError Data:", err.data,
          "\nError Type:", err.error_type
          )
end_time = time.time()
run_time = end_time - start_time
print("Used Time:".ljust(43), run_time)
