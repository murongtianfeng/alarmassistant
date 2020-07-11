# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:09:21 2020

@author: wangt
"""
#如果无匹配，返回空，否则返回相应科室
def towhom(shebeileixing, wangyuanmingcheng):
    keshi = ''
    if shebeileixing in ['WAF', '抗DDOS']:
        keshi = '安全室'
    if shebeileixing in ['防火墙'] and '-00A-' in wangyuanmingcheng:
        keshi = '互联网室'
    if shebeileixing in ['防火墙'] and '-00A-' not in wangyuanmingcheng:
        keshi = '数据室'
    if shebeileixing in ['机架式服务器', '分布式存储', 'IS']:
        keshi = '互联网室'
    if shebeileixing in ['交换机', '路由器']:
        if '-S-TOR-' in wangyuanmingcheng or '-S-EOR-' in wangyuanmingcheng or '-E-RT-' in wangyuanmingcheng or '-S-RT-' in wangyuanmingcheng or '-NETCN' in wangyuanmingcheng:
            keshi = '话务室'
        else:
            keshi = '互联网室'
    
    if shebeileixing in ['虚拟化平台']:
        keshi = '数据室'
        
    if shebeileixing in ['主机']:
        if '-SRV-' in wangyuanmingcheng:
            keshi = '数据室'
        if '-DBS-' in wangyuanmingcheng:
            keshi = '互联网室'
    
    if shebeileixing in ['NFVO','VNFM']:
        keshi = '数据室'
    
    if shebeileixing in ['OMC']:
        keshi = '网管室'
    
    if shebeileixing in ['SBCU']:
        keshi = '话务室'
    
    if shebeileixing in ['VOLTEAS','SPG','ISBG','SBCC','IMSCG','MRFC','MRFP','ENUMDNS']:
        if 'ha' in wangyuanmingcheng or 'HA' in wangyuanmingcheng:
            keshi = '话务室'
    
    
    if shebeileixing in ['SAEGWU','MME','SAEGWC','PCRF','LCG','EPCDNS',
                         '一级通信能力开放平台','能力网元接入模块','AAC','MMSC','彩信ENUM','IP_SMGW']:
        keshi = '数据室'
        
    if shebeileixing in ['CENTREX']:
        keshi = '话务室'
    
    if shebeileixing in ['SCPAS','智能网业务服务器','智能网能力网元']:
        if 'ha' in wangyuanmingcheng or 'HA' in wangyuanmingcheng:
            keshi = '话务室'
    return keshi