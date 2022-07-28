# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

import seq_model

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    sequence = "000111011011011011"
    sequence_len = len(sequence)
    sequence_bin = [int(x) for x in sequence]
    sequence_bin_len = len(sequence_bin)
    sequence_bin_str = ''.join(str(x) for x in sequence_bin)
    sequence_bin_str_len = len(sequence_bin_str)

    # LOGGING THE SEQUENCE
    cocotb.log.info("sequence_bin_str: %s" % sequence_bin_str)
    cocotb.log.info("sequence_bin_str_len: %d" % sequence_bin_str_len)
    cocotb.log.info("sequence_bin_len: %d" % sequence_bin_len)
    cocotb.log.info("sequence_len: %d" % sequence_len)

    _, positions_model = seq_model.model(sequence)
    positions_circuit = []
    
    for pos in range(0, sequence_bin_len):

        await RisingEdge(dut.clk)
        dut.inp_bit.value = sequence_bin[pos]

        await RisingEdge(dut.clk)
        if(pos != 0 and dut.seq_seen.value == 1):
            positions_circuit.append(pos)
        
        # DEBUGGING
        print(f"position: {pos}    answer: {str(dut.seq_seen.value)}     input: {str(dut.inp_bit.value)}" )

    print(positions_model, positions_circuit)
    assert positions_model == positions_circuit, f"Sequence detection is incorrect: {positions_model} != {positions_circuit}"
