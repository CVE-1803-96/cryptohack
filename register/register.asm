section .data
    ciphertext db "QEXXIV IHMX PEOI AMRO", 0
    format db "Shift %d: %s", 10, 0

section .bss
    decrypted resb 100
    shift resb 1

section .text
    extern printf
    global _start

_start:
    mov ecx, 1          ; shift = 1
shift_loop:
    cmp ecx, 26
    jge end_shift_loop

    ; Clear decrypted string
    mov edi, decrypted
    mov eax, 0
clear_decrypted:
    mov byte [edi], 0
    inc edi
    cmp edi, decrypted + 100
    jl clear_decrypted

    ; Decrypt the ciphertext
    mov esi, ciphertext
decrypt_loop:
    mov al, [esi]
    cmp al, 0
    je print_decrypted

    ; Check if character is alphabetic
    cmp al, 'A'
    jl not_alpha
    cmp al, 'Z'
    jg not_alpha

    ; Uppercase letter
    sub al, 'A'
    sub al, [shift]
    and al, 25
    add al, 'A'
    jmp store_char

not_alpha:
    cmp al, ' '
    je store_space
    jmp store_char

store_space:
    mov byte [decrypted + edi], ' '
    inc edi
    jmp next_char

store_char:
    mov [decrypted + edi], al
    inc edi

next_char:
    inc esi
    jmp decrypt_loop

print_decrypted:
    ; Print the decrypted string
    push decrypted
    push ecx
    push format
    call printf
    add esp, 12

    inc ecx
    jmp shift_loop

end_shift_loop:
    ; Exit program
    mov eax, 1          ; syscall: exit
    xor ebx, ebx        ; status: 0
    int 0x80
