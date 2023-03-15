#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Connect_to_vCenter_Server.py
# @Author: Yao Zhang
# @Date  : 2023/3/9 10:40
# @Desc  :
# @Contact : nowshut@qq.com

import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client
session = requests.session()

# Disable cert verification for demo purpose.
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server='vc_fqdn_or_ip', username='administrator@vsphere.local', password='password', session=session)

