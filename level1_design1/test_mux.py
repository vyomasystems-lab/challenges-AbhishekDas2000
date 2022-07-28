# See LICENSE.vyoma for details

from random import randint
import cocotb
from cocotb.triggers import Timer
from matplotlib.pyplot import switch_backend

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    dut.inp0.value = 2
    dut.sel.value = 0

    await Timer(2, units="ns")
    assert dut.out.value == dut.inp0.value, f"MUX result is incorrect: {dut.out.value} != {dut.inp0.value}"

    # cocotb.log.info('##### CTB: Develop your test here ########')

@cocotb.test()
async def test_mux_random(dut):
    """random test for mux"""
    for i in range(20):
        dut.inp0.value = randint(0, 3)
        dut.inp1.value = randint(0, 3)
        dut.inp2.value = randint(0, 3)
        dut.inp3.value = randint(0, 3)
        dut.inp4.value = randint(0, 3)
        dut.inp5.value = randint(0, 3)
        dut.inp6.value = randint(0, 3)
        dut.inp7.value = randint(0, 3)
        dut.inp8.value = randint(0, 3)
        dut.inp9.value = randint(0, 3)
        
        dut.inp10.value = randint(0, 3)
        dut.inp11.value = randint(0, 3)
        dut.inp12.value = randint(0, 3)
        dut.inp13.value = randint(0, 3)
        dut.inp14.value = randint(0, 3)
        dut.inp15.value = randint(0, 3)
        dut.inp16.value = randint(0, 3)
        dut.inp17.value = randint(0, 3)
        dut.inp18.value = randint(0, 3)
        dut.inp19.value = randint(0, 3)
        
        dut.inp20.value = randint(0, 3)
        dut.inp21.value = randint(0, 3)
        dut.inp22.value = randint(0, 3)
        dut.inp23.value = randint(0, 3)
        dut.inp24.value = randint(0, 3)
        dut.inp25.value = randint(0, 3)
        dut.inp26.value = randint(0, 3)
        dut.inp27.value = randint(0, 3)
        dut.inp28.value = randint(0, 3)
        dut.inp29.value = randint(0, 3)
        
        dut.inp30.value = randint(0, 3)

        for index in range(31):
            dut.sel.value = index

            await Timer(2, units="ns")

            switcher = {
                0: dut.inp0.value,
                1: dut.inp1.value,
                2: dut.inp2.value,
                3: dut.inp3.value,
                4: dut.inp4.value,
                5: dut.inp5.value,
                6: dut.inp6.value,
                7: dut.inp7.value,
                8: dut.inp8.value,
                9: dut.inp9.value,
                10: dut.inp10.value,
                11: dut.inp11.value,
                12: dut.inp12.value,
                13: dut.inp13.value,
                14: dut.inp14.value,
                15: dut.inp15.value,
                16: dut.inp16.value,
                17: dut.inp17.value,
                18: dut.inp18.value,
                19: dut.inp19.value,
                20: dut.inp20.value,
                21: dut.inp21.value,
                22: dut.inp22.value,
                23: dut.inp23.value,
                24: dut.inp24.value,
                25: dut.inp25.value,
                26: dut.inp26.value,
                27: dut.inp27.value,
                28: dut.inp28.value,
                29: dut.inp29.value,
                30: dut.inp30.value,
            }

            assert dut.out.value == switcher[index], f"MUX result is incorrect: {dut.out.value} != {switcher[index]} , index: {index}"

            # cocotb.log.info('##### CTB: Develop your test here ########')