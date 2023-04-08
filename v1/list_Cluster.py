#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list_Cluster.py
# @Author: NOWSHUT
# @Date  : 2023/3/16 18:12
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client

print("Cluster ID".ljust(33),"HA Enabled".ljust(20),"DRS Enabled".ljust(17),"Cluster Name")
start_time = time.time()
try:
    list_cluster = vsphere_client.vcenter.Cluster.list()
    # print(list_cluster)
    for i in list_cluster:
        if i.ha_enabled == True:
            i.ha_enabled = "True"
        else:
            i.ha_enabled = "False"
        if i.drs_enabled == True:
            i.drs_enabled = "True"
        else:
            i.drs_enabled = "False"
        print(i.cluster.ljust(25),
              i.ha_enabled.ljust(25),
              i.drs_enabled.ljust(25),
              i.name)

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
print("Used Time:".ljust(30), run_time)
