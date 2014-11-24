#------------------------------------------------------------------------------

SOURCE    := Solution.cpp
MYPROGRAM := $(shell basename $(shell pwd))
CC        := g++

#------------------------------------------------------------------------------

all: $(MYPROGRAM)

$(MYPROGRAM): $(SOURCE)
	$(CC) $(SOURCE) -o $(MYPROGRAM)

clean:
	rm -f $(MYPROGRAM)
