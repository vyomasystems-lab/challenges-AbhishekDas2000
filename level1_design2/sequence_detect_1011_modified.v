
// See LICENSE.vyoma for more details
// Verilog module for Sequence detection: 1011
module seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output reg seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3;

  reg [1:0] current_state, next_state;


  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end
  
  always @(posedge clk)
  begin
    if(reset)
      seq_seen <= 1'b0;
    else
      seq_seen <= (current_state == SEQ_101) && (inp_bit == 1'b1);
  end
  // state transition based on the input and current state
  always @(posedge clk)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
    endcase
  end
endmodule