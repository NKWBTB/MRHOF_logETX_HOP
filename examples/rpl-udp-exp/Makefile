CONTIKI_PROJECT = udp-client udp-server
all: $(CONTIKI_PROJECT)

CONTIKI=../..

TARGET_LIBFILES += -lm

include $(CONTIKI)/Makefile.dir-variables
MODULES += $(CONTIKI_NG_SERVICES_DIR)/simple-energest

include $(CONTIKI)/Makefile.include
