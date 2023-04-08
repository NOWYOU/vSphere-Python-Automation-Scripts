#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_Cluster.py
# @Author: NOWSHUT
# @Date  : 2023/3/16 18:26
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client

start_time = time.time()
try:
    get_cluster = vsphere_client.vcenter.Cluster.get(cluster="domain-c13239852")
    # print(get_cluster)
    print("Name:".ljust(31),get_cluster.name,
          "\nResource Pool:".ljust(27),get_cluster.resource_pool)

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
print("Used Time:".ljust(28), run_time)
