from importlib.resources import path
import os, glob

extensions = [".c", ".h", ".txt", ".out", ".gch", ".o"]

# Makefile
makefile = """SRCS = $(wildcard *.c)

CC = gcc
NAME = execute

CFLANG = -Wall -Wextra -Werror
OBJS = $(SRCS:.c=.o)

GREEN = \033[1;32m
RED = \033[1;31m
GREY = \033[2;37m
MAGENTA = \033[0;35m
RESET = \033[m

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAG) -o $(NAME) $(OBJS)
	@echo "$(NAME): $(GREEN)object files created$(RESET)"
	@echo "$(NAME): $(GREEN)$(NAME) compiled$(RESET)"

clean:
	rm -f $(OBJS)
	@echo "$(NAME): $(RED)$(OBJS) deleted$(RESET)"
	@echo "$(NAME): $(RED)object files deleted$(RESET)"

fclean: clean
	rm -f $(NAME)
	@rm -f $(NAME)
	@echo "$(NAME): $(RED)$(NAME) deleted$(RESET)"

re: fclean all

.PHONY: all clean fclean re"""

# Miniserv start message
start = """Good luck (•‿•)"""

# Subject

subject = """Assignment name  : mini_serv
Expected files   : mini_serv.c
Allowed functions: write, close, select, socket, accept, listen, send, recv, bind, strstr, malloc, realloc, free, calloc, bzero, atoi, sprintf, strlen, exit, strcpy, strcat, memset
--------------------------------------------------------------------------------

Write a program that will listen for client to connect on a certain port on 127.0.0.1 and will let clients to speak with each other

This program will take as first argument the port to bind to
If no argument is given, it should write in stderr "Wrong number of arguments" followed by a \n and exit with status 1
If a System Calls returns an error before the program start accepting connection, it should write in stderr "Fatal error" followed by a \n and exit with status 1
If you cant allocate memory it should write in stderr "Fatal error" followed by a \n and exit with status 1

Your program must be non-blocking but client can be lazy and if they don't read your message you must NOT disconnect them...

Your program must not contains #define preproc
Your program must only listen to 127.0.0.1
The fd that you will receive will already be set to make 'recv' or 'send' to block if select hasn't be called before calling them, but will not block otherwise. 

When a client connect to the server:
- the client will be given an id. the first client will receive the id 0 and each new client will received the last client id + 1
- %d will be replace by this number
- a message is sent to all the client that was connected to the server: "server: client %d just arrived\n"

clients must be able to send messages to your program.
- message will only be printable characters, no need to check
- a single message can contains multiple \n
- when the server receive a message, it must resend it to all the other client with "client %d: " before every line!

When a client disconnect from the server:
- a message is sent to all the client that was connected to the server: "server: client %d just left\n"

Memory or fd leaks are forbidden

To help you, you will find the file main.c with the beginning of a server and maybe some useful functions. (Beware this file use forbidden functions or write things that must not be there in your final program)

Warning our tester is expecting that you send the messages as fast as you can. Don't do un-necessary buffer.

Evaluation can be a bit longer than usual...

Hint: you can use nc to test your program
Hint: you should use nc to test your program
Hint: To test you can use fcntl(fd, F_SETFL, O_NONBLOCK) but use select and NEVER check EAGAIN (man 2 send)"""

mini_serv = "practicesrc/"

create_subject = r"practicesrc/subject.en.txt"
create_makefile = r"practicesrc/Makefile"
create_miniserv = r"practicesrc/mini_serv.c"

def reset():
    dosyalar = os.listdir(mini_serv)
    for dosya in dosyalar:
      dosya_adi, dosya_uzantisi = os.path.splitext(dosya)
      if dosya_uzantisi in extensions:
          dosya_yolu = os.path.join(mini_serv, dosya)
          os.remove(dosya_yolu)
    execute_path = mini_serv + "/execute"
    if os.path.isfile(execute_path):
        os.remove(execute_path)
    filemake = open(create_makefile, "w")
    filemake.write(makefile)
    filemake.close()
    file = open(create_subject, "w")
    file.write(subject)
    file.close()
    filep = open(create_miniserv, "w")
    filep.write(start)
    filep.close()
    print("mini_serv başarılı şekilde resetlendi.")

def miniserv_reset():
    filep = open(create_miniserv, "w")
    filep.write(start)
    filep.close()
    print("mini_serv.c başarılı şekilde oluşturuldu.")

def subject_reset():
    file1 = open(create_subject, "w")
    file1.write(subject)
    file1.close()
    print("Subject başarılı şekilde oluşturuldu.")

def makefile_reset():
    filemake = open(create_makefile, "w")
    filemake.write(makefile)
    filemake.close()
    print("Makefile başarılı şekilde oluşturuldu.")


while(1):
    try:
        os.system("clear")
        print("----------- examWIPE -----------")
        print("1- mini_serv'ı resetle")
        print("2- mini_serv.c dosyasını oluştur")
        print("3- Subject dosyasını oluştur")
        print("4- Makefile dosyasını oluştur")
        print("5- Exit")
        print("--------------------------------")
        secim = input("Seçim Numarınızı Giriniz: ")

        if secim == "1":
            reset()
        elif secim == "2":
            miniserv_reset()
        elif secim == "3":
            subject_reset()
        elif secim == "4":
            makefile_reset()
        elif secim == "5":
            exit()
        else:
            print("Yanlış seçim numarası girdiniz.")
            time.sleep(3)
            os.system("clear")
    except KeyboardInterrupt:
        os.system("clear")
        print("\nProgram sonlandırıldı.")
        exit(1)

