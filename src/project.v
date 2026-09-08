/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);
wire [7:0] led;
assign uo_out = led;
assign uio_out = 8'h00;
assign uio_oe  = 8'h00;
wire _unused;
assign _unused = &{ui_in, uio_in, ena};
led u_led(
    .clk ( clk ),
    .rst ( ~rst_n ),
    .led  ( led  )
);
endmodule
