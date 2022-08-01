# Welcome to Level 3 Design!
This is  **Verilog** implementation of the `XTEA` cipher. This design takes `6` inputs and gives `3` outputs.

# IO Interface
| Pin | Description | I/O | 
|--|--|--|
| `clock` | `clock input` | `I`|
| `reset` | `single bit reset`  | `I`|
| `mode` | `single bit mode selector 0->decrypt 1->encrypt` | `I`|
| `data_in1` | `first 32-bit of the 64-bit data to be encrypted/decypted` |`I` |
| `data_in2` | `last 32-bit of the 64-bit data to be encrypted/decypted` |`I` |
| `key_in` | `128-bit key to be used for encryption/decryption` |`I` |
| `data_out1` |`first 32-bit of the 64-bit data obtained after encryption/decryption` |`O` |
| `data_out2` | `last 32-bit of the 64-bit data obtained after encryption/decryption` |`O` |
| `all_done` |`single-bit output which goes high when all the operations are complete`  |`O` |


# File Structure

|Filename           				|Description                         |
|-------------------------------|-----------------------------|
|`Makefile`            		|`Contains the Makefile Definations for building the Project`       
|`xtea.v`            |`contains the Verilog implementation of the XTEA Cipher`           |
|`xtea_modified.v`	|`contains the bug free design`|
|`test_xtea.py`		|`contains the cocotb test bench`|
|`LICENSE`	|`contains the original License of the Design` |

## Verification Strategy

The cocotb test bench has 1 test
1. run_test()
### run_test()
This test inputs the data and tries to encrypt it. However it fails.

## Bugs Found
1. There is a bug in the state machine design line 74
```verilog
s3: state = while_flag ? s4 : s14; 
```
It should be replaced with
```verilog
s3: state = while_flag ? s4 : s15; 
```
## Design Source

[Design Source Code](https://opencores.org/projects/xtea)


