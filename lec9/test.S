	.intel_syntax noprefix
    .section .data
    .global XARRAY
    
    XARRAY:
        .quad 10
        .quad 20

	.section .text

xor eax, eax