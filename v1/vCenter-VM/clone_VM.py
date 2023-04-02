#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : clone_VM.py
# @Author: NOWSHUT
# @Date  : 2023/3/9 16:03
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client

start_time = time.time()
# Simplest clone
sepc = {
    "name": "centos7-1-clone",           # The name of the clone VM 
    "source": "vm-13240857",             # cloned VM ID
}
start_time = time.time()
try:
  # 执行克隆动作
  clone_vm = vsphere_client.vcenter.VM.clone(sepc)
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
