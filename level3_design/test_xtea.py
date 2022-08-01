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

freq = 25e6

@cocotb.test()
async def run_test(dut):

    # clock
    clock = Clock(dut.clock, 1, units="sec")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    #reset
    dut.reset.setimmediatevalue(0)
    await RisingEdge(dut.clock)
    await RisingEdge(dut.clock)
    dut.reset.value = 1
    await RisingEdge(dut.clock)
    await RisingEdge(dut.clock)
    await RisingEdge(dut.clock)
    dut.reset.value = 0
    

    # Input Transaction
    mode = 0x0
    data_in1 = 0x1
    data_in2 = 0x123
    key_in = 0x00000

    # Driving the input Transaction
    # dut.mode.setimmediatevalue(mode)
    dut.data_in1.value = data_in1
    dut.data_in2.value = data_in2
    dut.key_in.value = key_in
    await RisingEdge(dut.clock)
    await RisingEdge(dut.clock)

    for i in range(7):
        await RisingEdge(dut.clock)
        await RisingEdge(dut.clock)
        #Obtaining the Output
        all_done = dut.all_done.value
        data_out1 = dut.data_out1.value
        data_out2 = dut.data_out2.value

        # Logging the values to console
        # cocotb.log.info(f'mode={str(mode)}')
        # cocotb.log.info(f'data_in1={hex(data_in1)}')
        # cocotb.log.info(f'data_in2={hex(data_in2)}')
        # cocotb.log.info(f'key_in={hex(key_in)}')

    cocotb.log.info(f'All_done={str(all_done)}')
    cocotb.log.info(f'data_out1={hex(data_out1)}')
    cocotb.log.info(f'data_out2={hex(data_out2)}')



# @cocotb.test()
# def run_test(dut):

#     # clock
#     cocotb.fork(clock_gen(dut.CLK))
    
#     for operations in opcode_list:
        
#         # reset
#         dut.RST_N.value <= 0
#         yield Timer(10) 
#         dut.RST_N.value <= 1

#         ######### RANDOM INPUTS #############
#         # input transaction
#         mav_putvalue_src1 = int(hex(int(random_op_code_generator.rand_key(32), base = 2)), base=16)
#         mav_putvalue_src2 = int(hex(int(random_op_code_generator.rand_key(32), base = 2)), base=16)
#         mav_putvalue_src3 = int(hex(int(random_op_code_generator.rand_key(32), base = 2)), base=16)
#         mav_putvalue_instr = int(hex(int(operations, base = 2)), base=16)

#         # expected output from the model
#         expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

#         # driving the input transaction
#         dut.mav_putvalue_src1.value = mav_putvalue_src1
#         dut.mav_putvalue_src2.value = mav_putvalue_src2
#         dut.mav_putvalue_src3.value = mav_putvalue_src3
#         dut.EN_mav_putvalue.value = 1
#         dut.mav_putvalue_instr.value = mav_putvalue_instr
    
#         yield Timer(1) 

#         # obtaining the output
#         dut_output = dut.mav_putvalue.value

#         # DEBUGGING
    
#         cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
#         cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

#         if(dut_output != expected_mav_putvalue):
#             error_count += 1
#             cocotb.log.critical("ERROR HERE")
    
#     # # comparison
#     # error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
#     # assert dut_output == expected_mav_putvalue, error_message
#     error_message = f'There is error in {error_count} instructions'
#     assert error_count == 0, error_message

# # Clock Generation
# @cocotb.coroutine
# def clock_gen(signal):
#     while True:
#         signal.value <= 0
#         yield Timer(1/freq, units='sec') 
#         signal.value <= 1
#         yield Timer(1/freq, units='sec') 

# Test To Check All Instructions
# We Find that the ANDN Instruction is not working properly


# # dut.reset.value <= 0
#     # yield RisingEdge(dut.clock)
    
#     dut.reset.value = 1
#     yield RisingEdge(dut.clock) 
#     dut.reset.value = 0
#     yield RisingEdge(dut.clock)