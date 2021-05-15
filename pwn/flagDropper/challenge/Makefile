flagDropper: flagDropper.o
	gcc -no-pie -o flagDropper flagDropper.o

flagDropper.o: flagDropper.asm
	nasm  -f elf64 flagDropper.asm

