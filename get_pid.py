#!/usr/bin/python

import os 
from collections import namedtuple

PAGESIZE = os.sysconf("SC_PAGE_SIZE")
print PAGESIZE
pextmem = namedtuple('pextmem', 'rss vms shared text lib data dirty')


def pids():
    return [int(x) for x in os.listdir(b'/proc') if x.isdigit()]

def memory_info_ex(pid):
    #  ============================================================
    # | FIELD  | DESCRIPTION                         | AKA  | TOP  |
    #  ============================================================
    # | rss    | resident set size                   |      | RES  |
    # | vms    | total program size                  | size | VIRT |
    # | shared | shared pages (from shared mappings) |      | SHR  |
    # | text   | text ('code')                       | trs  | CODE |
    # | lib    | library (unused in Linux 2.6)       | lrs  |      |
    # | data   | data + stack                        | drs  | DATA |
    # | dirty  | dirty pages (unused in Linux 2.6)   | dt   |      |
    #  ============================================================
    with open("/proc/%s/statm" % pid, "rb") as f:
        vms, rss, shared, text, lib, data, dirty = \
            [int(x) * PAGESIZE for x in f.readline().split()[:7]]
    return pextmem(rss, vms, shared, text, lib, data, dirty)

pids = pids()

for pid in pids:
    mem_info = memory_info_ex(pid)
    print pid,mem_info

