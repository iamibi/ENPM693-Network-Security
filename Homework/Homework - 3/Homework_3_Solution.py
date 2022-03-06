import random
import hmac
import hashlib

# My Information
UID = 118428369
Last_Name = "Ibrahim"
First_Name = "Syed Mohammad"

# Global Constants
BLOCK_SIZE = 8
MAX_BLOCK_SIZE = 16


def F(byte_seq, k, output_len):
    # we use the hmac hash (don't worry about the meaning for now)
    h = hmac.new(k, byte_seq, hashlib.sha1)
    # return the first outputlen bytes of the hash value
    return h.digest()[:output_len]


# In a real Feistel implementation, different keys are used in different rounds. Here
# we use 64bit keys so for 16 rounds, we need 16 random 8byte keys. We can just generate
# 16 random 8 byte numbers we use the random.randint() function to be able to set the seed
# value and create the same keys for both the encoder and the decoder
def gen_keylist(keylenbytes, numkeys, seed):
    # We need to generate numkeys keys each being keylen bytes long
    random.seed(seed)

    # Use the random.randint(min,max) function to generate individual
    # random integers in range [min, max]. Generate a list of numkeys
    # random byte sequences each of them keylenbytes bytes long to be used as
    # keys for numkeys stages of the feistel encoder. To make sure we have control over
    # the generated random numbers meaning that the same sequence is
    # generated in different runs of our program,

    # keylist = [numkeys elements of 'bytes' type and keylenbytes bytes long each]
    keylist = []
    for i in range(numkeys):
        bytelist = [bytes([random.randint(0, 255)]) for x in range(keylenbytes)]
        keylist.append(bytelist)
    # example [b'\x12\xa4\x2f\xb4\x67\x80\xd4\x12', and 15 more if numkeys is 16]
    return keylist


def xor(byteseq1, byteseq2):
    # print(byteseq1)
    # print(byteseq2)
    # Python already provides the ^ operator to do xor on interger values
    # but first we need to break our input byte sequences into byte size integers
    l1 = [b for b in byteseq1]
    l2 = [b for b in byteseq2]

    l1attachl2 = zip(l1, l2)
    # zip(l1,l2) is actually a list as [(b'\xaa',b'\xcc), (b'\x33', b'\x55')]

    l1xorl2 = [bytes([elem1 ^ elem2]) for elem1, elem2 in l1attachl2]

    result = b"".join(l1xorl2)

    return result


def feistel_block(le_inp, re_inp, k):
    """Generates feistel block for left and right inputs with the key `k` provided"""

    # Set the left block output to the input right block
    le_out = re_inp

    # Generate a key hash for the right input block
    re_f = F(re_inp, k, BLOCK_SIZE)

    # Perform XOR operation between the left input block and the generated key block.
    re_out = xor(le_inp, re_f)

    return le_out, re_out


def feistel_enc(plaintext_bytes, rounds, seed):
    """
    Function that accepts one block of plaintext
    and applies all rounds of the feistel cipher and returns the
    cipher text block
    """

    # Check whether the input byte sequence is of size `MAX_BLOCK_SIZE`
    # if not, adding space (\x20) to the plain text byte sequence to make it even
    if len(plaintext_bytes) < MAX_BLOCK_SIZE:
        plaintext_bytes += b"\x20" * (MAX_BLOCK_SIZE - len(plaintext_bytes))

    # Generate the key's and store it in the list as bytes array
    key_list = gen_keylist(BLOCK_SIZE, rounds, seed)

    # Get the left input block and right input block by splitting
    # the plain text byte sequence into BLOCK_SIZE
    le_block = plaintext_bytes[0:BLOCK_SIZE]
    re_block = plaintext_bytes[BLOCK_SIZE : BLOCK_SIZE * 2]

    # Perform the operations for the `rounds` time
    for i in range(rounds):
        # Join the current index byte key into one
        key = b"".join(key_list[i])

        le_block, re_block = feistel_block(le_block, re_block, key)

    # Switch the last rotation and concatenate the byte string to get the final output
    ciphertext_bytes = re_block + le_block

    return ciphertext_bytes


def feistel_dec(ciphertext_bytes, rounds, seed):
    """
    Function that accepts one block of cipher text
    and applies all rounds of the feistel cipher and returns the
    plain text block.
    """

    # Generate the key's and store it in the list as bytes array
    key_list = gen_keylist(BLOCK_SIZE, rounds, seed)
    key_list_len = len(key_list)

    # Get the left plain text block and right plain text block by splitting
    # the cipher text byte sequence into BLOCK_SIZE
    le_block = ciphertext_bytes[0:BLOCK_SIZE]
    re_block = ciphertext_bytes[BLOCK_SIZE : BLOCK_SIZE * 2]

    # Perform the operations for the `rounds` time
    for i in range(rounds):
        # Start iterating the key_list in revers and join the bytes list to single bytes string
        key = b"".join(key_list[key_list_len - i - 1])

        le_block, re_block = feistel_block(le_block, re_block, key)

    # Switch the last rotation and concatenate the byte string to get the final output
    plaintext_bytes = re_block + le_block

    return plaintext_bytes
