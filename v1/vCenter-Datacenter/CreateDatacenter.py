#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : CreateDatacenter.py
# @Author: Nowshut
# @Date  : 2023/4/2 16:37
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client
spec ={
	"folder": "group-d1",        #Query the folder ID of type Datacenters by the list folder method
	"name": "DC3"
}
start_time = time.time()
try:
    create_dc = vsphere_client.vcenter.Datacenter.create(spec)
    print("Created successfully！")
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
