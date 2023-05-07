#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_vcenter_signing_certificate.py
# @Author: NOWSHUT
# @Date  : 2023/3/11 22:05
# @Desc  :
# @Contact : nowshut@qq.com
 
import OpenSSL
import time
from dateutil import parser
from vSphere_Automation_SDK.Connect_to_vCenter_Server import vsphere_client
start_time = time.time()
try:
    sts = vsphere_client.vcenter.certificate_management.vcenter.SigningCertificate.get()
    sts = sts.active_cert_chain.cert_chain[0]
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, sts)
    certIssue = cert.get_issuer()
 
    get_notBefore = parser.parse(cert.get_notBefore().decode("UTF-8"))
    get_notAfter= parser.parse(cert.get_notAfter().decode("UTF-8"))
 
    print("证书信息")
    print("==============")
    for i in cert.get_subject().get_components():
        print("通用名称(CN):".ljust(20),i[1].decode("utf-8"))
    print ("序列号:".ljust(27),hex(cert.get_serial_number()))
    print ("颁发机构:".ljust(24),certIssue.commonName)
    print ("签名算法:".ljust(24),cert.get_signature_algorithm().decode("UTF-8"))
    print ("有效期自".ljust(24),get_notBefore.strftime('%Y-%m-%d %H:%M:%S'))
    print ("有效期至".ljust(24),get_notAfter.strftime('%Y-%m-%d %H:%M:%S'))
    print ("是否已经过期:".ljust(19),cert.has_expired())
    print("公钥长度".ljust(24),cert.get_pubkey().bits())
    print("公钥:\n" ,OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, cert.get_pubkey()).decode("utf-8"))
 
    print("颁发者信息")
    print("==============")
 
    for item in certIssue.get_components():
        if  item[0].decode("utf-8") == 'CN':
            print("通用名称(CN):".ljust(18), item[1].decode("utf-8"))
        if  item[0].decode("utf-8") == 'C':
            print("国家(C):".ljust(26), item[1].decode("utf-8"))
        if  item[0].decode("utf-8") == 'ST':
            print("州/省名(ST):".ljust(22), item[1].decode("utf-8"))
        if  item[0].decode("utf-8") == 'O':
            print("组织(O):".ljust(26), item[1].decode("utf-8"))
        if  item[0].decode("utf-8") == 'OU':
            print("部门(OU):".ljust(24), item[1].decode("utf-8"))
    print ("版本:".ljust(28),cert.get_version() + 1)
 
    print("证书扩展数:".ljust(19),cert.get_extension_count())
    for i in range(cert.get_extension_count()):
        # print(i+1)
        if i == 0:
            print("密钥用法:".ljust(35),cert.get_extension(i))
        if i == 1:
            print("Subject Alternative Name:".ljust(32),cert.get_extension(i))
        if i == 2:
            print("证书使用者秘钥标识符:".ljust(17),cert.get_extension(i))
        if i == 3:
            print("颁发机构秘钥标识符:".ljust(20),cert.get_extension(i))
        if i == 4:
            print("CA URL:".ljust(39),cert.get_extension(i))
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
