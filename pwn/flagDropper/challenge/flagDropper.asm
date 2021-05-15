          global    main


          section   .text
          extern fopen, fgets


main:
          push rbp
          mov rbp, rsp
          mov       rax, 1
          mov       rdi, 1
          mov       rsi, message
          mov       rdx, 75
          syscall                       ;write function
          mov       rax, 1
          mov       rdi, 1
          mov       rsi, catch
          mov       rdx, 17
          syscall                       ;write again
          lea       rax, [buffer]
          add       rax, 72
          mov       DWORD [rax], _exit
          mov       rax, 0
          mov       rdi, 0
          mov       rsi, buffer
          mov       rdx, 200
          syscall                       ;read into
          mov       rax, 1
          mov       rdi, 1
          mov       rsi, buffer
          mov       rdx, 64
          syscall                       ;print what was read
          lea       rax, [buffer]
          add       rax, 72
          jmp       [rax]

_exit:
          mov       rax, 60
          xor       rdi, rdi
          syscall                       ;exit


win:
          mov       rax, 0
          lea       rsi, [readonly]
          lea       rdi, [flag]
          call      fopen
          mov       rdx, rax
          mov       rax, 0
          mov       rdi, buffer2
          mov       rsi, 22
          call      fgets
          mov       rdi, 1
          mov       rax, 1
          mov       rdx, 22
          syscall
          jmp       _exit

          section   .data
message:  db        `Welcome to the Flag Dropper! \nMake sure to catch the flag when its dropped!`,10

catch:    db        `\n1,\n2,\n3,\nCATCH`,10

flag:     db        "flag.txt",0
readonly: db        "r",0

          section   .bss

buffer: resb 64
spacing: resb 64
buffer2: resb 64


