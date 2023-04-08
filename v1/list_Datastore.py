#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list_Datastore.py
# @Author: NOWSHUT
# @Date  : 2023/3/10 23:50
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client,byte_to_gb
start_time = time.time()
try:
      ds = vsphere_client.vcenter.Datastore.list()
      if ds == []:
          print("---------Empty---------")
      else:
          for i in ds:
              print("Datastore ID:".ljust(30),i.datastore,
                    "\nDatastore Name:".ljust(28),i.name,
                    "\nDatastore Type:".ljust(29),i.type,
                    "\nDatastore Free Space:".ljust(25),byte_to_gb(i.free_space),  #Byte
                    "\nDatastore Capacity".ljust(26), byte_to_gb(i.capacity),         #Byte
                    "\n=======================")
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
print("Used Time:", run_time)
