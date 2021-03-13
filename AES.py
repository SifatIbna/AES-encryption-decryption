from BitVector import *
import time
from Key_Scheduling import KeyScheduling

# key_scheduling = {0: ['42', '55', '45', '54'], 1: ['20', '43', '53', '45'], 2: ['31', '36', '20', '42'], 3: ['61', '74', '63', '68'], 4: ['d1', 'ae', '00', 'bb'], 5: ['f1', 'ed', '53', 'fe'], 6: ['c0', 'db', '73', 'bc'], 7: ['a1', 'af', '10', 'd4'], 8: ['aa', '64', '48', '89'], 9: ['5b', '89', '1b', '77'], 10: ['9b', '52', '68', 'cb'], 11: ['3a', 'fd', '78', '1f'], 12: ['fa', 'd8', '88', '09'], 13: ['a1', '51', '93', '7e'], 14: ['3a', '03', 'fb', 'b5'],
# 15: ['00', 'fe', '83', 'aa'], 16: ['49', '34', '24', '6a'], 17: ['e8', '65', 'b7', '14'], 18: ['d2', '66', '4c', 'a1'], 19: ['d2', '98', 'cf', '0b'], 20: ['1f', 'be', '0f', 'df'], 21: ['f7', 'db', 'b8', 'cb'], 22: ['25', 'bd', 'f4', '6a'], 23: ['f7', '25', '3b', '61'], 24: ['00', '5c', 'e0', 'b7'], 25: ['f7', '87', '58', '7c'], 26: ['d2', '3a', 'ac', '16'], 27: ['25', '1f', '97', '77'], 28: ['80', 'd4', '15', '88'], 29: ['77', '53', '4d', 'f4'], 30: ['a5', '69', 'e1', 'e2'], 31: ['80', '76', '76', '95'], 32: ['38', 'ec', '3f', '45'], 33: ['4f', 'bf', '72', 'b1'], 34: ['ea', 'd6', '93', '53'], 35: ['6a', 'a0', 'e5', 'c6'], 36: ['c3', '35', '8b', '47'], 37: ['8c', '8a', 'f9', 'f6'], 38: ['66', '5c', '6a', 'a5'], 39: ['0c', 'fc', '8f', '63'], 40: ['45', '46', '70', 'b9'], 41: ['c9', 'cc', '89', '4f'], 42: ['af', '90', 'e3', 'ea'], 43: ['a3', '6c', '6c', '89']}

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

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"),
     BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"),
     BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"),
     BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"),
     BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"),
     BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"),
     BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"),
     BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"),
     BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

w0 = []
w1 = []
w2 = []
w3 = []


class AES():
    def __init__(self, key_scheduling_list, state_mat={}):
        self.key_scheduling = key_scheduling_list
        self.state_mat = state_mat

    def take_input(self, plainText):
        ch_list = []
        # plainText = input("Give Text to encrypt: ")
        for ch in plainText:
            word_bits = BitVector(textstring=ch)
            ch_list.append(word_bits.get_bitvector_in_hex())

        if len(ch_list) < 16:
            for _ in range(0, 16-len(ch_list)):
                ch_list.append('0')

        w0 = ch_list[0:4]
        w1 = ch_list[4:8]
        w2 = ch_list[8:12]
        w3 = ch_list[12:16]

        # print("IN HEX: ", ch_list)

        self.state_mat = {
            0: w0,
            1: w1,
            2: w2,
            3: w3
        }

    def set_round_keys(self, keys):
        self.key_scheduling = keys

    def set_state_mat(self, mat):
        self.state_mat = mat

    def get_state_mat(self):
        return self.state_mat

    def xor_hex_hex(self, hexlist1, hexlist2):
        temp_list = []

        for index in range(len(hexlist1)):
            hex_val1 = BitVector(hexstring=hexlist1[index])
            hex_val2 = BitVector(hexstring=hexlist2[index])
            temp_list.append((hex_val1 ^ hex_val2).get_bitvector_in_hex())
        return temp_list

    def xor_vals(self, hexlist):
        sum_ = '0'
        for val in hexlist:
            hexval1 = BitVector(hexstring=val)
            hexval2 = BitVector(hexstring=sum_)
            sum_ = str((hexval1 ^ hexval2).get_bitvector_in_hex())
        return sum_

    def xor_hex_bit(self, rounding_constant, replace_list):
        temp_list = []

        for index in range(len(rounding_constant)):
            bit_val = BitVector(bitstring=rounding_constant[index])
            hex_val = BitVector(hexstring=replace_list[index])
            temp_list.append((bit_val ^ hex_val).get_bitvector_in_hex())
        return temp_list

    def multiply(self, mix_list, hex_list):
        AES_modulus = BitVector(bitstring='100011011')
        temp_list = []
        for count in range(4):

            bv1 = mix_list[count]
            bv2 = BitVector(hexstring=hex_list[count])
            bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
            temp_list.append(bv3.get_bitvector_in_hex())
        return temp_list

    def handle_replaement(self):
        replaced_list = []
        for count in range(4):
            for val in self.state_mat[count]:
                int_val = BitVector(hexstring=val).intValue()
                int_val = Sbox[int_val]
                hex_val = BitVector(
                    intVal=int_val, size=8).get_bitvector_in_hex()
                replaced_list.append(hex_val)
            self.state_mat[count] = replaced_list.copy()
            replaced_list.clear()

    def add_state_to_round_key(self, start):
        for count in range(4):
            # print(key_scheduling[start+count])
            self.state_mat[count] = self.xor_hex_hex(
                self.state_mat[count], self.key_scheduling[start+count])

    def make_matrix(self):
        matrix = [[] for _ in range(4)]
        # print(matrix)
        for i in range(4):
            for j in range(4):
                matrix[i].append(self.state_mat[j][i])
        # print(matrix)
        return matrix
    # return handle_rotation(matrix)

    def handle_rotation(self):
        matrix = self.make_matrix()
        for count in range(4):
            temp_list = matrix[count]
            temp_list = temp_list[count::]+temp_list[:count:]
            matrix[count] = temp_list
        return self.revert_back(matrix)

    def revert_back(self, matrix):
        temp_list = []
        for i in range(4):
            for j in range(4):
                temp_list.append(matrix[j][i])
            self.state_mat[i] = temp_list.copy()
            temp_list.clear()

    def handle_multiplication(self):
        temp_list = []
        temp_dict = self.state_mat.copy()
        for i in range(4):
            for j in range(4):
                list1 = temp_dict[j]
                list2 = Mixer[i]

                mul_list = self.multiply(mix_list=list2, hex_list=list1)

                temp_list.append(self.xor_vals(mul_list))
            self.state_mat[i] = temp_list.copy()
            temp_list.clear()

    def multiply_test(self, hexstring1, hexstring2):
        AES_modulus = BitVector(bitstring='100011011')

        bv1 = BitVector(hexstring=hexstring1)
        bv2 = BitVector(hexstring=hexstring2)
        bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
        # print()
        return bv3.get_bitvector_in_hex()

    def encryption(self):
        start_time = time.time()

        count = 0
        for loop in range(10):
            if loop == 0:
                self.add_state_to_round_key(count)
                count += 4
                self.handle_replaement()
                # make_matrix()
                self.handle_rotation()
                self.handle_multiplication()
                self.state_mat = self.make_matrix()
                self.add_state_to_round_key(count)
                count += 4
            elif loop == 9:
                self.handle_replaement()
                self.handle_rotation()
                self.add_state_to_round_key(count)
            else:
                self.handle_replaement()
                self.handle_rotation()
                self.handle_multiplication()
                self.state_mat = self.make_matrix()
                self.add_state_to_round_key(count)
                count += 4
        end_time = time.time()
        # print("Encryption time: ", end_time-start_time)
        # print(self.state_mat)

        return end_time-start_time

    def inverse_rotation(self):
        matrix = self.make_matrix()
        for count in range(4):
            amount = 4 - count

            temp_list = matrix[count]
            temp_list = temp_list[amount::]+temp_list[:amount:]
            matrix[count] = temp_list
        return self.revert_back(matrix)

    def inv_replacement(self):
        replaced_list = []
        for count in range(4):
            for val in self.state_mat[count]:
                int_val = BitVector(hexstring=val).intValue()
                int_val = InvSbox[int_val]
                hex_val = BitVector(
                    intVal=int_val, size=8).get_bitvector_in_hex()
                replaced_list.append(hex_val)
            self.state_mat[count] = replaced_list.copy()
            replaced_list.clear()

    def inv_multiplication(self):
        temp_list = []
        temp_dict = self.state_mat.copy()
        for i in range(4):
            for j in range(4):
                list1 = temp_dict[j]
                list2 = InvMixer[i]

                mul_list = self.multiply(mix_list=list2, hex_list=list1)

                temp_list.append(self.xor_vals(mul_list))
            self.state_mat[i] = temp_list.copy()
            temp_list.clear()

    def decryption(self):

        start_time = time.time()
        count = 40
        for loop in range(10):

            if loop == 0:
                self.add_state_to_round_key(count)
                count -= 4
                self.inverse_rotation()
                self.inv_replacement()
                self.add_state_to_round_key(count)
                count -= 4
                self.inv_multiplication()
                self.state_mat = self.make_matrix()
            elif loop == 9:
                self.inverse_rotation()
                self.inv_replacement()
                self.add_state_to_round_key(count)
                count -= 4
            else:
                self.inverse_rotation()
                self.inv_replacement()
                self.add_state_to_round_key(count)
                count -= 4
                self.inv_multiplication()
                self.state_mat = self.make_matrix()
        end_time = time.time()
        # print("Decrypt time: ", end_time-start_time)

        return end_time-start_time

    def print_text(self):

        final_words = ""
        for i in range(4):
            for j in range(4):
                bv = BitVector(hexstring=self.state_mat[i][j])
                final_words += str(bv.get_bitvector_in_ascii())
        # print(final_words)
        return final_words
