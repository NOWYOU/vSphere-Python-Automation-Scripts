#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : delete_VM.py
# @Author: NOWSHUT
# @Date  : 2023/3/10 22:44
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client
# Delete the specified VM, the VM ID is required
start_time = time.time()
try:
    del_vm = vsphere_client.vcenter.VM.delete("vm-session-ID")
    print("VM Deleted successfully")

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
