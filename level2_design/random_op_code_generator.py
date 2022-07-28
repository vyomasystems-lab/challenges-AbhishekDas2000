from pprint import PrettyPrinter
import random

class instruction_1:
    def __init__(self, func7, func3, opcode):
        self.func7 = func7
        self.func3 = func3
        self.opcode = opcode
    
class instruction_2:
    def __init__(self, func7, imm_value_1, func3, opcode):
        self.func7 = func7
        self.imm_value_1 = imm_value_1
        self.func3 = func3
        self.opcode = opcode
    


# Function to create the
# random binary string
def rand_key(p):
    # Variable to store the
    # string
    key1 = ""

    # Loop to find the string
    # of desired length
    for i in range(p):

        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))

        # Concatenation the random 0, 1
        # to the final result
        key1 += temp

    return key1


def op_code_gen():
    """R Type = func7 rs2 rs1 f3 rd instruction(func7="0100000", func3="111", opcode="0110011")opcode
    R-4 Type = rs3 f2 rs2 rs1 f3 rd opcode
    I Type = imm rs1 f3 rd opcode"""
    
    instr_list = []
    instr_list_2 = []
    opcode_list = []

    rs3 = rand_key(5)
    rs2 = rand_key(5)
    rs1 = rand_key(5)
    rd = rand_key(5)
    # TYPE 1 INSTRUCTIONS

    ANDN = instruction_1(func7="0100000", func3="111", opcode="0110011")
    ORN = instruction_1(func7="0100000", func3="110", opcode="0110011")
    XNOR = instruction_1(func7="0100000", func3="100", opcode="0110011")
    SLO = instruction_1(func7="0010000", func3="001",opcode= "0110011")
    SRO = instruction_1(func7="0010000", func3="101",opcode= "0110011")
    ROL = instruction_1(func7="0110000", func3="001",opcode= "0110011")
    ROR = instruction_1(func7="0110000", func3="101",opcode= "0110011")
    SH1ADD = instruction_1(func7="0010000", func3="010",opcode= "0110011")
    SH2ADD = instruction_1(func7="0010000", func3="100",opcode= "0110011")
    SH3ADD = instruction_1(func7="0010000", func3="110",opcode= "0110011")
    SBCLR = instruction_1(func7="0100100", func3="001",opcode= "0110011")
    SBSET = instruction_1(func7="0010100", func3="001",opcode= "0110011")
    SBINV = instruction_1(func7="0110100", func3="001",opcode= "0110011")
    SBEXT = instruction_1(func7="0100100", func3="101",opcode= "0110011")
    GORC = instruction_1(func7="0010100", func3="101",opcode= "0110011")
    GREV = instruction_1(func7="0110100", func3="101",opcode= "0110011")
    CLMUL = instruction_1(func7="0000101", func3="001",opcode= "0110011")
    CLMULH = instruction_1(func7="0000101", func3="011",opcode= "0110011")
    CLMULR = instruction_1(func7="0000101", func3="010",opcode= "0110011")
    MIN = instruction_1(func7="0000101", func3="100",opcode= "0110011")
    MAX = instruction_1(func7="0000101", func3="101",opcode= "0110011")
    MINU = instruction_1(func7="0000101", func3="110",opcode= "0110011")
    MAXU = instruction_1(func7="0000101", func3="111",opcode= "0110011")
    BDEP = instruction_1(func7="0100100", func3="110",opcode= "0110011")
    BEXT = instruction_1(func7="0000100", func3="110",opcode= "0110011")
    PACK = instruction_1(func7="0000100", func3="100",opcode= "0110011")
    PACKU = instruction_1(func7="0100100", func3="100",opcode= "0110011")
    PACKH = instruction_1(func7="0000100", func3="111",opcode= "0110011")
    BFP = instruction_1(func7="0100100", func3="111",opcode= "0110011")
    SHFL = instruction_1(func7="0000100", func3="001",opcode= "0110011")
    UNSHFL = instruction_1(func7="0000100", func3="101",opcode= "0110011")

    CMIX = instruction_1(func7= rs3 + "11", func3="001",opcode= "0110011")
    CMOV = instruction_1(func7= rs3 + "11", func3="101",opcode= "0110011")
    FSL = instruction_1(func7= rs3 + "10", func3="001",opcode= "0110011")
    FSR = instruction_1(func7= rs3 + "10", func3="101",opcode= "0110011")

    SLOI = instruction_1(func7= "00100" + "00", func3="001",opcode= "0010011")
    SROI = instruction_1(func7= "01100" + "10", func3="101",opcode= "0010011")
    RORI = instruction_1(func7= "01100" + "10", func3="101",opcode= "0010011")

    SBCLRI = instruction_1(func7= "01001" + "00", func3="001",opcode= "0010011")
    SBSETI = instruction_1(func7= "00101" + "00", func3="001",opcode= "0010011")
    SBINVI = instruction_1(func7= "01101" + "00", func3="001",opcode= "0010011")
    SBEXTI = instruction_1(func7= "01001" + "00", func3="101",opcode= "0010011")

    SHFLI = instruction_1(func7= "000010" + "0", func3="001",opcode= "0010011")
    UNSHFLI = instruction_1(func7= "000010" + "0", func3="101",opcode= "0010011")
    GORCI = instruction_1(func7= "00101" + "10", func3="101",opcode= "0010011")
    GREVI = instruction_1(func7= "01101" + "10", func3="101",opcode= "0010011")
    _FSRI = instruction_1(func7= "00000" + "10", func3="101",opcode= "0010011")
    instr_list.append(ANDN)
    instr_list.append(ORN)
    instr_list.append(XNOR)
    instr_list.append(SLO)
    instr_list.append(SRO)
    instr_list.append(ROL)
    instr_list.append(ROR) 
    instr_list.append(SH1ADD)
    instr_list.append(SH2ADD)
    instr_list.append(SH3ADD) 
    instr_list.append(SBCLR)
    instr_list.append(SBSET) 
    instr_list.append(SBINV) 
    instr_list.append(SBEXT)
    instr_list.append(GORC) 
    instr_list.append(GREV) 
    instr_list.append(CLMUL) 
    instr_list.append(CLMULH) 
    instr_list.append(CLMULR) 
    instr_list.append(MIN) 
    instr_list.append(MAX) 
    instr_list.append(MINU)
    instr_list.append(MAXU)
    instr_list.append(BDEP) 
    instr_list.append(BEXT) 
    instr_list.append(PACK) 
    instr_list.append(PACKU) 
    instr_list.append(PACKH)
    instr_list.append(BFP)
    instr_list.append(SHFL)
    instr_list.append(UNSHFL)
    instr_list.append(CMIX)
    instr_list.append(CMOV)
    instr_list.append(FSL)
    instr_list.append(FSR)
    instr_list.append(SLOI)
    instr_list.append(SROI)
    instr_list.append(RORI)
    instr_list.append(SBCLRI)
    instr_list.append(SBSETI)
    instr_list.append(SBINVI)
    instr_list.append(SBEXTI)
    instr_list.append(SHFLI)
    instr_list.append(UNSHFLI)
    instr_list.append(GORCI)
    instr_list.append(GREVI)
    instr_list.append(_FSRI)

    for obj in instr_list:
        instr = obj.func7 + rs2 + rs1 + obj.func3 + rd + obj.opcode
        opcode_list.append(instr)
    
    # TYPE 2 INSTRUCTIONS
    CLZ = instruction_2(func7="0110000", imm_value_1="00000", func3="001", opcode="0010011")
    CTZ = instruction_2(func7="0110000", imm_value_1="00001", func3="001", opcode="0010011")
    PCNT = instruction_2(func7="0110000", imm_value_1="00010", func3="001", opcode="0010011")
    SEXT_B = instruction_2(func7="0110000", imm_value_1="00100", func3="001", opcode="0010011")
    SEXT_H = instruction_2(func7="0110000", imm_value_1="00101", func3="001", opcode="0010011")
    CRC32_B = instruction_2(func7="0110000", imm_value_1="10000", func3="001", opcode="0010011")
    CRC32_H = instruction_2(func7="0110000", imm_value_1="10001", func3="001", opcode="0010011")
    CRC32_W = instruction_2(func7="0110000", imm_value_1="10010", func3="001", opcode="0010011")
    CRC32C_B = instruction_2(func7="0110000", imm_value_1="11000", func3="001", opcode="0010011")
    CRC32C_H = instruction_2(func7="0110000", imm_value_1="11001", func3="001", opcode="0010011")
    CRC32C_W = instruction_2(func7="0110000", imm_value_1="11010", func3="001", opcode="0010011")

    instr_list_2.append(CLZ)
    instr_list_2.append(CTZ)
    instr_list_2.append(PCNT)
    instr_list_2.append(SEXT_B)
    instr_list_2.append(SEXT_H)
    instr_list_2.append(CRC32_B)
    instr_list_2.append(CRC32_H)
    instr_list_2.append(CRC32_W)
    instr_list_2.append(CRC32C_B)
    instr_list_2.append(CRC32C_H)
    instr_list_2.append(CRC32C_W)

    for obj in instr_list_2:
        instr = obj.func7 + obj.imm_value_1 + rs1 + obj.func3 + rd + obj.opcode
        opcode_list.append(instr)
    
    return opcode_list


# # for _ in range(0, 10):
# op_code_gen()