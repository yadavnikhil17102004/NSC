s_box = [
    0x6, 0x4, 0xc, 0x5,
    0x0, 0x7, 0x2, 0xe,
    0x1, 0xf, 0x3, 0xd,
    0x8, 0xa, 0x9, 0xb
]

linear_approximation_table = [
    [1, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
]

def linear_cryptanalysis():
    count = {}

    for input_mask in range(16):
        for output_mask in range(16):
            bias = 0

            for i in range(16):
                input_bits = [(i >> k) & 1 for k in range(4)]
                output_bits = [(s_box[i] >> k) & 1 for k in range(4)]

                input_parity = sum(input_bits[k] * ((input_mask >> k) & 1) for k in range(4))
                output_parity = sum(output_bits[k] * ((output_mask >> k) & 1) for k in range(4))

                if (input_parity ^ output_parity) == 0:
                    bias += 1

            count[(input_mask, output_mask)] = abs(bias - 8) 

    max_bias = max(count.values())
    probable_masks = [masks for masks, value in count.items() if value == max_bias]

    return probable_masks

def main():
    probable_masks = linear_cryptanalysis()
    print("Most probable input-output masks found by linear cryptanalysis:", probable_masks)

if __name__ == "__main__":
    main()
