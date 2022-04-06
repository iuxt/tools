#!/usr/bin/env python3

node_list=['baiyun.nutscloud.com','tianhe.nutscloud.com','longgang.nutscloud.com','yantian.nutscloud.com','shunde.nutscloud.com','pingshan.nutscloud.com','longhua.nutscloud.com','guangming.nutscloud.com','dapengxin.nutscloud.com','lechang.nutscloud.com','nanxiong.nutscloud.com','shixing.nutscloud.com','renhua.nutscloud.com','wengyuan.nutscloud.com','xinfeng.nutscloud.com','xiangzhou.nutscloud.com','doumen.nutscloud.com','jinwan.nutscloud.com','jinping.nutscloud.com','longhu.nutscloud.com','chaonan.nutscloud.com','chenghai.nutscloud.com','conghua.nutscloud.com','panyu.nutscloud.com','huadu.nutscloud.com','zengcheng.nutscloud.com','futian.nutscloud.com','nansha.nutscloud.com','luohu.nutscloud.com','haizhu.nutscloud.com']

for i in node_list:
    data = '''                      # %s
                     {'name' => 'check_k8s_node_mem_%s', 'desc' => 'check_k8s_node_mem_%s', 'notify' => 1, 'check_interval' => 5, 'notification_interval' => 90, 'check_timeout' => 30, 'max_check_attempts' => 1},
                     {'name' => 'check_k8s_node_load_%s', 'desc' => 'check_k8s_node_load_%s', 'notify' => 1, 'check_interval' => 5, 'notification_interval' => 90, 'check_timeout' => 30, 'max_check_attempts' => 1},
                     {'name' => 'check_k8s_node_disk_root_%s', 'desc' => 'check_k8s_node_disk_root_%s', 'notify' => 1, 'check_interval' => 5, 'notification_interval' => 90, 'check_timeout' => 30, 'max_check_attempts' => 1},
                     {'name' => 'check_k8s_node_ntp_sync_%s', 'desc' => 'check_k8s_node_ntp_sync_%s', 'notify' => 1, 'check_interval' => 5, 'notification_interval' => 90, 'check_timeout' => 30, 'max_check_attempts' => 1},
                     {'name' => 'check_k8s_node_zombie_procs_%s', 'desc' => 'check_k8s_node_zombie_procs_%s', 'notify' => 1, 'check_interval' => 5, 'notification_interval' => 90, 'check_timeout' => 30, 'max_check_attempts' => 1},
    ''' % (i,i,i,i,i,i,i,i,i,i,i)
    print(data)
