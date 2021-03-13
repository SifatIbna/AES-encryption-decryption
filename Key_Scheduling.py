from BitVector import *
import time

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

w0 = []
w1 = []
w2 = []
w3 = []
initial_rounding_constant = ['01', '00', '00', '00']


class KeyScheduling():
    def __init__(self):
        self.key_list = []
        self.list_dict = {}
        self.input_key()

    def input_key(self):
        print("ENTER THE KEY :")
        key = input()
        for val in key:
            word_bits = BitVector(textstring=val)
            self.key_list.append(word_bits.get_bitvector_in_hex())
        if len(self.key_list) < 16:
            for _ in range(0, 16-len(self.key_list)):
                self.key_list.append('0')
        elif len(self.key_list) > 16:
            self.key_list = self.key_list[0:16].copy()
        print("IN HEX: ", self.key_list)
        w0 = self.key_list[0:4]
        w1 = self.key_list[4:8]
        w2 = self.key_list[8:12]
        w3 = self.key_list[12:16]
        self.list_dict = {
            0: w0,
            1: w1,
            2: w2,
            3: w3,
        }

    def get_key(self):
        return self.list_dict

    def get_rounding_const(self, rounding_constant_list, step=0):

        if step > 1:

            AES_modulus = BitVector(bitstring='100011011')

            a = BitVector(bitstring=initial_rounding_constant[0])
            multiply = BitVector(intVal=2, size=8)
            c = a.gf_multiply_modular(multiply, AES_modulus, 8)
            initial_rounding_constant[0] = str(c)
            return initial_rounding_constant
        else:
            return rounding_constant_list

    def xor_hex_hex(self, hexlist1, hexlist2):
        temp_list = []

        for index in range(len(hexlist1)):
            hex_val1 = BitVector(hexstring=hexlist1[index])
            hex_val2 = BitVector(hexstring=hexlist2[index])
            temp_list.append((hex_val1 ^ hex_val2).get_bitvector_in_hex())
        return temp_list

    def xor_hex_bit(self, rounding_constant, replace_list):
        temp_list = []

        for index in range(len(rounding_constant)):
            bit_val = BitVector(bitstring=rounding_constant[index])
            hex_val = BitVector(hexstring=replace_list[index])
            temp_list.append((bit_val ^ hex_val).get_bitvector_in_hex())
        return temp_list

    def handle_replaement(self, end_word):
        replaced_list = []
        # print(end_word)
        for val in end_word:
            # print(val)
            int_val = BitVector(hexstring=val).intValue()
            int_val = Sbox[int_val]
            hex_val = BitVector(intVal=int_val, size=8).get_bitvector_in_hex()
            replaced_list.append(hex_val)
        return replaced_list

    def hangle_g_func(self, end_word, step):
        # print(end_word)
        rotate_word = end_word[1::]+end_word[:1:]  # Rotation
        # print(rotate_word)
        replaced_list = self.handle_replaement(rotate_word)
        # print(replaced_list)
        rounding_constant = self.get_rounding_const(
            rounding_constant_list=initial_rounding_constant, step=step)

        g_list = self.xor_hex_bit(rounding_constant, replaced_list)
        return g_list

    def scheduler(self):
        start_time = time.time()
        start = 0
        g_func = []

        for loop in range(4, 44, 1):

            if loop < 7:
                step = 1
            else:
                step = 2

            if loop % 4 == 0:

                # print(self.list_dict[loop-1])
                g_func = self.hangle_g_func(self.list_dict[loop-1], step=step)
                # print(g_func)
                self.list_dict[loop] = self.xor_hex_hex(
                    self.list_dict[start], g_func)
                # if loop == 4:
                #     break
                start += 1
            else:

                self.list_dict[loop] = self.xor_hex_hex(
                    self.list_dict[start+3], self.list_dict[start])
                # if loop ==7:
                #     print(start)
                #     break

                start += 1
        end_time = time.time()
        # print("Key Scheduling time: ",end_time-start_time)
        return end_time-start_time

        # print(self.list_dict)


# sch = KeyScheduling()
# sch.scheduler()
# print(sch.get_key())
