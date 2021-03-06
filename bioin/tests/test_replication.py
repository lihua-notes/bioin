import bioin
from .. import replication
import pytest
import sys


@pytest.mark.parametrize("pattern, genome, positions", [
    ("ATAT", "GATATATGCATATACTT", [1, 3, 9]),
    ("ACAC", "TTTTACACTTTTTTGTGTAAAAA", [4]),
    ("AAA", "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT", [0, 46, 51, 74]),
    ("TTT", "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", [88, 92, 98, 132]),
    ("ATA", "ATATATA", [0, 2, 4])
    ])
def test_pattern_matching(pattern, genome, positions):
    assert replication.pattern_matching(pattern, genome) == positions


@pytest.mark.parametrize("genome, symbol, array", [
    ("AAAAGGGG", "A", {0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}),
    ("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", "C", {0: 22, 1: 22, 2: 22, 3: 21, 4: 21, 5: 21, 6: 21, 7: 20, 8: 19, 9: 20, 10: 20, 11: 20, 12: 20, 13: 21, 14: 21, 15: 21, 16: 21, 17: 20, 18: 19, 19: 19, 20: 18, 21: 17, 22: 17, 23: 17, 24: 17, 25: 17, 26: 16, 27: 16, 28: 16, 29: 16, 30: 16, 31: 17, 32: 16, 33: 16, 34: 16, 35: 16, 36: 16, 37: 17, 38: 17, 39: 16, 40: 16, 41: 16, 42: 16, 43: 16, 44: 15, 45: 15, 46: 15, 47: 14, 48: 14, 49: 15, 50: 15, 51: 15, 52: 15, 53: 15, 54: 15, 55: 15, 56: 16, 57: 16, 58: 15, 59: 14, 60: 14, 61: 15, 62: 16, 63: 16, 64: 16, 65: 16, 66: 16, 67: 16, 68: 16, 69: 16, 70: 16, 71: 17, 72: 17, 73: 17, 74: 17, 75: 18, 76: 18, 77: 18, 78: 18, 79: 18, 80: 17, 81: 17, 82: 17, 83: 17, 84: 17, 85: 18, 86: 19, 87: 19, 88: 20, 89: 21, 90: 21, 91: 21, 92: 20, 93: 21, 94: 22, 95: 22, 96: 21, 97: 22, 98: 21, 99: 21, 100: 22, 101: 22, 102: 22, 103: 22, 104: 21, 105: 20, 106: 21, 107: 22, 108: 21, 109: 22, 110: 21, 111: 22, 112: 23, 113: 23, 114: 23, 115: 24, 116: 23, 117: 22, 118: 23, 119: 22, 120: 23, 121: 23, 122: 23, 123: 22, 124: 22, 125: 22, 126: 23, 127: 24, 128: 23, 129: 22, 130: 22, 131: 22, 132: 21, 133: 22, 134: 22})
    ])
def test_symbol_array(genome, symbol, array):
    assert replication.symbol_array(genome, symbol) == array


@pytest.mark.parametrize("genome, symbol, array", [
    ("AAAAGGGG", "A", {0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}),
    ("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", "C", {0: 22, 1: 22, 2: 22, 3: 21, 4: 21, 5: 21, 6: 21, 7: 20, 8: 19, 9: 20, 10: 20, 11: 20, 12: 20, 13: 21, 14: 21, 15: 21, 16: 21, 17: 20, 18: 19, 19: 19, 20: 18, 21: 17, 22: 17, 23: 17, 24: 17, 25: 17, 26: 16, 27: 16, 28: 16, 29: 16, 30: 16, 31: 17, 32: 16, 33: 16, 34: 16, 35: 16, 36: 16, 37: 17, 38: 17, 39: 16, 40: 16, 41: 16, 42: 16, 43: 16, 44: 15, 45: 15, 46: 15, 47: 14, 48: 14, 49: 15, 50: 15, 51: 15, 52: 15, 53: 15, 54: 15, 55: 15, 56: 16, 57: 16, 58: 15, 59: 14, 60: 14, 61: 15, 62: 16, 63: 16, 64: 16, 65: 16, 66: 16, 67: 16, 68: 16, 69: 16, 70: 16, 71: 17, 72: 17, 73: 17, 74: 17, 75: 18, 76: 18, 77: 18, 78: 18, 79: 18, 80: 17, 81: 17, 82: 17, 83: 17, 84: 17, 85: 18, 86: 19, 87: 19, 88: 20, 89: 21, 90: 21, 91: 21, 92: 20, 93: 21, 94: 22, 95: 22, 96: 21, 97: 22, 98: 21, 99: 21, 100: 22, 101: 22, 102: 22, 103: 22, 104: 21, 105: 20, 106: 21, 107: 22, 108: 21, 109: 22, 110: 21, 111: 22, 112: 23, 113: 23, 114: 23, 115: 24, 116: 23, 117: 22, 118: 23, 119: 22, 120: 23, 121: 23, 122: 23, 123: 22, 124: 22, 125: 22, 126: 23, 127: 24, 128: 23, 129: 22, 130: 22, 131: 22, 132: 21, 133: 22, 134: 22})
    ])
def test_faster_symbol_array(genome, symbol, array):
    assert replication.faster_symbol_array(genome, symbol) == array

@pytest.mark.parametrize("genome, skew", [
    ("CATGGGCATCGGCCATACGCC", [0, -1, -1, -1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, -1, 0, -1, -2]),
    ("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", [0, 0, 1, 0, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 1, 0, -1, -1, 0, 0, -1, -2, -2, -1, -2, -2, -1, -2, -1, 0, 0, 1, 2, 1, 0, 0, -1, 0, -1, -2, -1, -1, -2, -2, -2, -3, -3, -4, -3, -2, -2, -2, -1, -2, -3, -3, -3, -2, -2, -1, -2, -2, -2, -2, -1, -1, 0, 1, 1, 1, 2, 1, 2, 2, 3, 2, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 6, 5, 5, 5, 5, 4, 5, 4, 4, 4, 4, 4, 4, 3, 2, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 2, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 2, 1, 0, 1, 1, 0, 0, 0, 0])
    ])
def test_skew_array(genome, skew):
    assert replication.skew_array(genome) == skew


@pytest.mark.parametrize("p, q, count", [
    ("GGGCCGTTGGT", "GGACCGTTGAC", 3),
    ("AAAA", "TTTT", 4),
    ("ACGTACGT", "TACGTACG", 8),
    ("ACGTACGT", "CCCCCCCC", 6),
    ("ACGTACGT", "TGCATGCA", 8),
    ("GATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACT", "AATAGCAGCTTCTCAACTGGTTACCTCGTATGAGTAAATTAGGTCATTATTGACTCAGGTCACTAACGTCT", 15),
    ("AGAAACAGACCGCTATGTTCAACGATTTGTTTTATCTCGTCACCGGGATATTGCGGCCACTCATCGGTCAGTTGATTACGCAGGGCGTAAATCGCCAGAATCAGGCTG", "AGAAACCCACCGCTAAAAACAACGATTTGCGTAGTCAGGTCACCGGGATATTGCGGCCACTAAGGCCTTGGATGATTACGCAGAACGTATTGACCCAGAATCAGGCTC", 28)
    ])
def test_hamming_distance(p, q, count):
    assert len(p) == len(q)
    assert replication.hamming_distance(p, q) == count


@pytest.mark.parametrize("pattern, text, d, positions", [
    ("ATTCTGGA", "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT", 3, [6, 7, 26, 27]),
    ("AAA", "TTTTTTAAATTTTAAATTTTTT", 2, [4, 5, 6, 7, 8, 11, 12, 13, 14, 15]),
    ("GAGCGCTGG", "GAGCGCTGGGTTAACTCGCTACTTCCCGACGAGCGCTGTGGCGCAAATTGGCGATGAAACTGCAGAGAGAACTGGTCATCCAACTGAATTCTCCCCGCTATCGCATTTTGATGCGCGCCGCGTCGATT", 2, [0, 30, 66]),
    ("AATCCTTTCA", "CCAAATCCCCTCATGGCATGCATTCCCGCAGTATTTAATCCTTTCATTCTGCATATAAGTAGTGAAGGTATAGAAACCCGTTCAAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGCGCCATAATCCAAACA", 3, [3, 36, 74, 137]),
    ("CCGTCATCC", "CCGTCATCCGTCATCCTCGCCACGTTGGCATGCATTCCGTCATCCCGTCAGGCATACTTCTGCATATAAGTACAAACATCCGTCATGTCAAAGGGAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGC", 3, [0, 7, 36, 44, 48, 72, 79, 112]),
    ("TTT", "AAAAAA", 3, [0, 1, 2, 3]),
    ("CCA", "CCACCT", 0, [0]),
    ("GTGCCG", "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", 3, [3, 13, 16, 22, 25, 27, 28, 30, 33, 34, 36, 39, 47, 54, 61, 71, 76, 84, 87, 91, 101, 106, 119, 124])
    ])
def test_approximate_pattern_matching(pattern, text, d, positions):
    assert replication.approximate_pattern_matching(pattern, text, d) == positions


@pytest.mark.parametrize("pattern, text, d, count", [
    ("GAGG", "TTTAGAGCCTTCAGAGG", 2, 4),
    ("AA", "AAA", 0, 2),
    ("ATA", "ATA", 1, 1),
    ("GTGCCG", "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", 3, 24)
    ])
def test_approximate_pattern_count(pattern, text, d, count):
    assert replication.approximate_pattern_count(pattern, text, d) == count

