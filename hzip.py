from bitstring import BitArray
import huffman_coding
import sys


if __name__ == '__main__':
    # unzip
    if sys.argv[1] == '-x':
        f = open(sys.argv[2], 'rb').read()
        b = BitArray(bytes=f)
        decoded = huffman_coding.TextProcessor.fileDecoder(b)

    # zip
    else:
        f = open(sys.argv[1], 'r')
        huffman_coding.text = f.read()
        textProcessor = huffman_coding.TextProcessor()
        encoded = textProcessor.process(log=False)
        fi = open(sys.argv[1] + ".hzip", "wb")
        encoded.tofile(fi)
        fi.close()
