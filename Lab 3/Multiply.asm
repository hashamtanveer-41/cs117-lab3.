section .data
    msg db 'Product: ',0
    msgLen equ $ - msg

    product db 0

section .text
    global _start 

_start:
    mov al, 4  ;
    mov bl, 2  ;

    mul bl ;

    add al, '0';
    mov [product], al 

    mov eax, 4      ;   
    mov ebx, 1      ;
    mov ecx, msg
    mov edx, msgLen
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, product
    mov edx, 1
    int 0x80

    mov eax, 1
    mov ebx, 0
    int 0x80




