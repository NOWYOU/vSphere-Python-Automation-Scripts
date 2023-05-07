#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : renew_vcenter_TLS.py
# @Author: NOWSHUT
# @Date  : 2023/3/30 18:56
# @Desc  :
# @Contact : nowshut@qq.com
 
import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client
start_time = time.time()
try:
    get_cert = vsphere_client.vcenter.certificate_management.vcenter.Tls.renew()
    print("MACHINE SSL Certificate Renew Successfully\n"
          "After this operation completes, the services using the certificate will be restarted for the new certificate to take effect. Service start-up may take 5-15min, please wait patiently" )
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
