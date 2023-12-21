#Rio de Janeiro - Federal University of Rio de Janeiro

#depedency file to build the current project code.

CC = gcc
#LDFLAGS = -pthread -lpthread -lrt

CPP = gpp
TARGET = main
SRC = $(TARGET).cpp
OBJ = $(TARGET)

all: $(OBJ)

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

clean:
	$(RM) $(TARGET)