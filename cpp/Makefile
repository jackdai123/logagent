###### compiler and linker #####
CC = gcc
AR = ar cru
LINKER = $(CC)
RM = /bin/rm -f

##### path define #####
MSGPACK_INC_PATH = /usr/local/include
MSGPACK_LIB_PATH = /usr/local/lib
MSGPACKRPC_INC_PATH = /usr/local/include
MSGPACKRPC_LIB_PATH = /usr/local/lib
MPIO_LIB_PATH = /usr/local/lib

##### cflags and ldflags #####
CFLAGS = -std=c++03 -DMSGPACK_USE_CPP03 -Wall -D_REENTRANT -D_GNU_SOURCE -fPIC -O2 -I$(MSGPACK_INC_PATH) -I$(MSGPACKRPC_INC_PATH)
STATICFLAGS = -Wl,-static
STATICLIBS = -L$(MSGPACKRPC_LIB_PATH) -ljubatus_msgpack-rpc -L$(MSGPACK_LIB_PATH) -lmsgpack -L$(MPIO_LIB_PATH) -ljubatus_mpio
DYNAMICFLAGS = -Wl,-call_shared
DYNAMICLIBS = -lstdc++ -lpthread -lm

##### make rules #####
%.o: %.c %.h
	$(CC) $(CFLAGS) -c $< -o $@
%.o: %.cc %.h
	$(CC) $(CFLAGS) -c $< -o $@
%.o: %.cpp %.h
	$(CC) $(CFLAGS) -c $< -o $@

##### objs for compiling #####
COM_OBJS = log_utils.o file_utils.o config.o opt_map.o
CLI_OBJS = $(COM_OBJS) logagent_rpc_proto.o logagent_rpc_cli.o
SVR_OBJS = $(COM_OBJS) daemon.o logagent_rpc_proto.o logagent_rpc_handler.o logagent_svr.o

##### target for compiling #####
TARGETS = liblogagent_rpc_cli.a logagent_rpc_test logagent_svr

##### make targets #####
all: $(TARGETS)

liblogagent_rpc_cli.a: $(CLI_OBJS)
	$(AR) $@ $^

logagent_rpc_test: liblogagent_rpc_cli.a logagent_rpc_test.o
	$(LINKER) $^ $(STATICFLAGS) -L. -llogagent_rpc_cli $(STATICLIBS) $(DYNAMICFLAGS) $(DYNAMICLIBS) -o $@

logagent_svr: $(SVR_OBJS)
	$(LINKER) $^ $(STATICFLAGS) $(STATICLIBS) $(DYNAMICFLAGS) $(DYNAMICLIBS) -o $@

clean:
	@($(RM) $(TARGETS))
	@($(RM) *.o)

