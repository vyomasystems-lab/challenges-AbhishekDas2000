# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

#Testing the original design
# VERILOG_SOURCES = $(PWD)/mux.v

# Testing the modified verilog design
VERILOG_SOURCES = $(PWD)/mux_modified.v

TOPLEVEL := mux          # design
MODULE   := test_mux     # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 