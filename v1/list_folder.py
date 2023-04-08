#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list_folder.py
# @Author: NOWSHUT
# @Date  : 2023/3/11 19:07
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client
start_time = time.time()
try:
    list_folder = vsphere_client.vcenter.Folder.list()
    print("Floder ID".ljust(50),"Name".ljust(60),"Type")
    for i in list_folder:
        x = 60
        y = x - len(i.folder)
        print(i.folder.ljust(40),
            i.name.ljust(50),
              i.type.ljust(y),
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
