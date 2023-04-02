#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : GetDatacenter.py
# @Author: NOWSHUT
# @Date  : 2023/4/2 18:36
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client

start_time = time.time()
try:
    get_dc = vsphere_client.vcenter.Datacenter.get("datacenter-3")
    print("Name:".ljust(35),get_dc.name,
          "\nDatacenter Folder:".ljust(30),get_dc.datastore_folder,
          "\nHost Folder:".ljust(34),get_dc.host_folder,
          "\nNetwork Folder:".ljust(31),get_dc.network_folder,
          "\nVM Folder:".ljust(34),get_dc.vm_folder)

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
print("Used Time:".ljust(34), run_time)
