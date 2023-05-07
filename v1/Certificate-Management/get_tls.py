#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_tls.py
# @Author: NOWSHUT
# @Date  : 2023/3/11 22:51
# @Desc  :
# @Contact : nowshut@qq.com
 
import time
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client
 
start_time = time.time()
try:
      get_cert = vsphere_client.vcenter.certificate_management.vcenter.Tls.get()
      print("========================================")
      print("Version:".ljust(40),get_cert.version,
            "\nSerial Number:".ljust(36),get_cert.serial_number,
            "\nSignature Algorithm:".ljust(34),get_cert.signature_algorithm,
            "\nIssuer Dn:".ljust(39),get_cert.issuer_dn,
            "\nValid From:".ljust(38),get_cert.valid_from,
            "\nValid To:".ljust(40),get_cert.valid_to,
            "\nSubject Dn:".ljust(38),get_cert.subject_dn,
            "\nThumbprint:".ljust(38),get_cert.thumbprint,
            "\nIs CA:".ljust(41),get_cert.is_ca,
            "\nPath Length Constraint:".ljust(32),get_cert.path_length_constraint,
            "\nKey Usage:".ljust(37),get_cert.key_usage,
            "\nExtended Key Usage:".ljust(30), get_cert.extended_key_usage,
            "\nSubject Alternative Name:".ljust(30), get_cert.subject_alternative_name,
            "\nAuthority Information Access URI:".ljust(38), get_cert.authority_information_access_uri,
            "\nCert:\n",get_cert.cert,
            )
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
print("========================================")
print("Used Time:".ljust(43), run_time)
