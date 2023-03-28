#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list_VM.py
# @Author: NOWSHUT
# @Date  : 2023/3/9 10:41
# @Desc  :
# @Contact : nowshut@qq.com

import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client

print("VM Session ID".ljust(19),"POWER STATE".ljust(19),"CPU COUNT".ljust(19),"MEMORY SIZE MIB".ljust(19),"NAME".ljust(80))
start_time = time.time()
try:
# List all VMs inside the vCenter Server / 获取vc中所有VM，最高不超过4000台
    vm =vsphere_client.vcenter.VM.list()
    for i in vm:
        cpu = str(i.cpu_count)
        memory = str(i.memory_size_mib)
        print(i.vm.ljust(19),i.power_state.ljust(19),cpu.ljust(30),memory.ljust(37),i.name)
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
