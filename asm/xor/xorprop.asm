r
section .data
    key1 db 0xa6, 0xc8, 0xb6, 0x73, 0x3c, 0x9b, 0x22, 0xde, 0x7b, 0xc0, 0x25, 0x32, 0x66, 0xa3, 0x86, 0x7d, 0xf5, 0x5a, 0xcd, 0xe8, 0x63, 0x5e, 0x19, 0xc7, 0x33, 0x13
    op1 db 0x37, 0xdc, 0xb2, 0x92, 0x03, 0x0f, 0xaa, 0x90, 0xd0, 0x7e, 0xec, 0x17, 0xe3, 0xb1, 0xc6, 0xd8, 0xda, 0xf9, 0x4c, 0x35, 0xd4, 0xc9, 0x19, 0x1a, 0x5e, 0x1e
    op2 db 0xc1, 0x54, 0x57, 0x56, 0x68, 0x7e, 0x75, 0x73, 0xdb, 0x23, 0xaa, 0x1c, 0x34, 0x52, 0xa0, 0x98, 0xb7, 0x1a, 0x7f, 0xf0, 0xfd, 0xdd, 0xde, 0x5f, 0xc1
    op3 db 0x04, 0xee, 0x98, 0x55, 0x20, 0x8a, 0x2c, 0xd5, 0x90, 0x91, 0xd0, 0x47, 0x67, 0xae, 0x47, 0x96, 0x31, 0x70, 0xd1, 0x66, 0x0d, 0xf7, 0xf5, 0x6f, 0x5a, 0xf
    msg db "You are running Python 2, which is no longer supported. Please update to Python 3.", 0
    msg_len equ $ - msg

section .bss
    key2 resb 25
    key3 resb 25
    f1 resb 25
    f2 resb 25
    flag resb 25

section .text
    global _start

_start:
    ; Check Python version (simulated)
    ; Assuming we are not running Python 2 for this example

    ; Print KEY1
    mov rax, 1          ; syscall: write
    mov rdi, 1          ; file descriptor: stdout
    mov rsi, key1
    mov rdx, 25         ; length of key1
    syscall

    ; XOR function
    xor_func:
        ; rsi = a, rdi = b, rdx = length
        xor_loop:
            cmp rdx, 0
            je xor_done
            mov al, [rsi]      ; load byte from a
            xor al, [rdi]     ; XOR with byte from b
            mov [rsi], al     ; store result back
            inc rsi
            inc rdi
            dec rdx
            jmp xor_loop
        xor_done:
            ret

    ; Calculate key2 = xor(key1, op1)
    mov rsi, key1
    mov rdi, op1
    mov rdx, 25
    call xor_func
    mov rsi, key2

    ; Print KEY2
    mov rax, 1
    mov rdi, 1
    mov rsi, key2
    mov rdx, 25
    syscall

    ; Calculate key3 = xor(key2, op2)
    mov rsi, key2
    mov rdi, op2
    mov rdx, 25
    call xor_func
    mov rsi, key3

    ; Print KEY3
    mov rax, 1
    mov rdi, 1
    mov rsi, key3
    mov rdx, 25
    syscall

    ; Calculate f1 = xor(op3, key1)
    mov rsi, op3
    mov rdi, key1
    mov rdx, 25
    call xor_func
    mov rsi, f1

    ; Calculate f2 = xor(key2, key3)
    mov rsi, key2
    mov rdi, key3
    mov rdx, 25
    call xor_func
    mov rsi, f2

    ; Calculate flag = xor(f1, f2)
    mov rsi, f1
    mov rdi, f2
    mov rdx, 25
    call xor_func
    mov rsi, flag

    ; Print FLAG
    mov rax, 1
    mov rdi, 1
    mov rsi, flag
    mov rdx, 25
    syscall

    ; Exit
    mov rax, 60         ; syscall: exit
    xor rdi, rdi        ; status: 0
    syscall
