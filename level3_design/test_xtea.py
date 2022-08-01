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

freq = 25e6 #25MHz clock

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
