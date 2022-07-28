# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
from typing import Literal
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

import random_op_code_generator

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Test To Check All Instructions
# We Find that the ANDN Instruction is not working properly

@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))
    opcode_list = random_op_code_generator.op_code_gen()
    error_count = 0
    
    for operations in opcode_list:
        
        # reset
        dut.RST_N.value <= 0
        yield Timer(10) 
        dut.RST_N.value <= 1

        ######### RANDOM INPUTS #############
        # input transaction
        mav_putvalue_src1 = int(hex(int(random_op_code_generator.rand_key(32), base = 2)), base=16)
        mav_putvalue_src2 = int(hex(int(random_op_code_generator.rand_key(32), base = 2)), base=16)
        mav_putvalue_src3 = int(hex(int(random_op_code_generator.rand_key(32), base = 2)), base=16)
        mav_putvalue_instr = int(hex(int(operations, base = 2)), base=16)

        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
    
        yield Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        # DEBUGGING
    
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

        if(dut_output != expected_mav_putvalue):
            error_count += 1
            cocotb.log.critical("ERROR HERE")
    
    # # comparison
    # error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    # assert dut_output == expected_mav_putvalue, error_message
    error_message = f'There is error in {error_count} instructions'
    assert error_count == 0, error_message

@cocotb.test()
def debug_ANDN(dut):
    # clock
    cocotb.fork(clock_gen(dut.CLK))

    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x1
    mav_putvalue_instr = 0b01000000000000000111000000110011
    
    for _ in range(0, 10):
        mav_putvalue_src2 = 0x0
        for __ in range(0, 10):
            # expected output from the model
            expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

            # driving the input transaction
            dut.mav_putvalue_src1.value = mav_putvalue_src1
            dut.mav_putvalue_src2.value = mav_putvalue_src2
            dut.mav_putvalue_src3.value = mav_putvalue_src3
            dut.EN_mav_putvalue.value = 1
            dut.mav_putvalue_instr.value = mav_putvalue_instr

            yield Timer(1) 
            # obtaining the output
            dut_output = dut.mav_putvalue.value
            # DEBUGGING
            cocotb.log.info(f'src1 = {hex(mav_putvalue_src1)}   src2 = {hex(mav_putvalue_src2)}')
            cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
            cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
            mav_putvalue_src2 += 1
        mav_putvalue_src1 += 1
