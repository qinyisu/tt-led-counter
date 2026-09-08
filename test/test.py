import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_counter(dut):
    dut.ena.value = 1
    dut.clk.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 1

    await Timer(5, unit="us")

    # Assert asynchronous reset while the clock stays low.
    dut.rst_n.value = 0
    await Timer(5, unit="us")
    assert int(dut.uo_out.value) == 0, "Reset failed"

    dut.rst_n.value = 1
    await Timer(5, unit="us")

    # Run past 255 to verify wraparound.
    expected = 0
    for cycle in range(260):
        dut.clk.value = 1
        await Timer(5, unit="us")

        expected = (expected + 1) & 0xFF
        actual = int(dut.uo_out.value)
        assert actual == expected, (
            f"Cycle {cycle + 1}: expected {expected}, got {actual}"
        )

        dut.clk.value = 0
        await Timer(5, unit="us")

        assert int(dut.uo_out.value) == expected, (
            "Counter changed on a falling edge"
        )

    # Reset a nonzero count without a clock edge.
    dut.rst_n.value = 0
    await Timer(5, unit="us")
    assert int(dut.uo_out.value) == 0, "Asynchronous reset failed"

    # Clock edges must not increment the counter during reset.
    dut.clk.value = 1
    await Timer(5, unit="us")
    assert int(dut.uo_out.value) == 0, "Counter ran during reset"

    dut.clk.value = 0
    await Timer(5, unit="us")
    dut.rst_n.value = 1
    await Timer(5, unit="us")

    dut.clk.value = 1
    await Timer(5, unit="us")
    assert int(dut.uo_out.value) == 1, "Counter did not restart"

    assert int(dut.uio_out.value) == 0
    assert int(dut.uio_oe.value) == 0