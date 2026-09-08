<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements an 8-bit binary up-counter.

The counter increments by one on every rising edge of `clk`.
After reaching 255, it wraps around to 0.

The reset input `rst_n` is active-low and asynchronous.
When `rst_n` is low, the counter immediately resets to 0.

The counter value is connected to `uo_out[7:0]`:
- `uo_out[0]` is the least significant bit.
- `uo_out[7]` is the most significant bit.

The inputs `ui_in` and `uio_in` are unused.
The bidirectional output enables `uio_oe` are set to 0.

## How to test

1. Select and enable the project.
2. Drive `rst_n` low and verify that `uo_out` is 0.
3. Drive `rst_n` high to release reset.
4. Apply clock pulses to `clk`.
5. Verify that the output increments by one on each rising edge.
6. Verify that the output wraps from 255 to 0.
7. Assert reset between clock edges and verify that the output
   returns to 0 without waiting for another clock edge.

Use a slow clock to observe the count with LEDs, or use a logic
analyzer to capture the output at higher clock frequencies.

## External hardware

No external hardware is required for simulation.

For hardware observation, a logic analyzer or an LED display
with suitable current-limiting resistors and drivers can be
connected to the eight output signals.
