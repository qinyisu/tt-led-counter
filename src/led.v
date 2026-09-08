module led(
    input  wire clk,
    input  wire rst,
    output wire [7:0] led
);
reg  [7:0] led_r;
always@(posedge clk or posedge rst) begin
    if(rst) begin
        led_r <= 8'b00000000;
    end else begin
        led_r <= led_r + 1'b1;
    end
end
assign led = led_r;
endmodule