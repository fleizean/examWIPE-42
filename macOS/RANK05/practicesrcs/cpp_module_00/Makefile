SRCS = $(wildcard *.cpp)

CC = clang++
NAME = execute

CFLANG = -Wall -Wextra -Werror -std=c++98
OBJS = $(SRCS:.cpp=.o)

GREEN = [1;32m
RED = [1;31m
GREY = [2;37m
MAGENTA = [0;35m
RESET = [m

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

.PHONY: all clean fclean re