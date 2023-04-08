#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_Datastore.py
# @Author: NOWSHUT
# @Date  : 2023/3/11 0:14
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client,byte_to_gb
start_time = time.time()
try:
      get_ds = vsphere_client.vcenter.Datastore.get('datastore-68')
      print("Datastore Name:".ljust(38),get_ds.name,
      "\nDatastore Type:".ljust(40),get_ds.type,
      "\nAccessible:".ljust(44),get_ds.accessible,
      "\nDatastore Free Space:".ljust(37),byte_to_gb(get_ds.free_space) ,
      "\nMultiple Host Access:".ljust(37),get_ds.multiple_host_access,
      "\nThin Provisioning Supported:".ljust(33),get_ds.thin_provisioning_supported
            )
except Exception as err:
    for i in err.messages:
        id = i.id,
        default_message = i.default_message
        args = i.args
        params = i.params
        localized = i.localized
    print("\033[1;31m Encountered an error, Please see the following information \033[0m" ,
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
