import unittest
from day4_refactored import get_checksum, get_encrypted_name, get_sector_id, get_effective_checksum, calculate_sum_of_sector_ids, decrypt_room_name

# Test get_checksum 
class TestGetChecksumFunction(unittest.TestCase):
    def test_testcases(self):
        self.assertEqual(get_checksum("aaaaa-bbb-z-y-x-123[abxyz]"), "abxyz")
        self.assertEqual(get_checksum("a-b-c-d-e-f-g-h-987[abcde]"), "abcde")
        self.assertEqual(get_checksum("not-a-real-room-404[oarel]"), "oarel")
        self.assertEqual(get_checksum("totally-real-room-200[decoy]"), "decoy")

class TestGetEncryptedNameFunction(unittest.TestCase):
    def test_testcaseone(self):
        self.assertEqual(get_encrypted_name("aaaaa-bbb-z-y-x-123[abxyz]"), "aaaaa-bbb-z-y-x")
        self.assertEqual(get_encrypted_name("a-b-c-d-e-f-g-h-987[abcde]"), "a-b-c-d-e-f-g-h")
        self.assertEqual(get_encrypted_name("not-a-real-room-404[oarel]"), "not-a-real-room")
        self.assertEqual(get_encrypted_name("totally-real-room-200[decoy]"), "totally-real-room")

class TestGetSectorIdFunction(unittest.TestCase):
    def test_testcases(self):
        self.assertEqual(get_sector_id("aaaaa-bbb-z-y-x-123[abxyz]"), 123)
        self.assertEqual(get_sector_id("a-b-c-d-e-f-g-h-987[abcde]"), 987)
        self.assertEqual(get_sector_id("not-a-real-room-404[oarel]"), 404)
        self.assertEqual(get_sector_id("totally-real-room-200[decoy]"), 200)
        
class TestGetEffectiveChecksumFunction(unittest.TestCase):
    def test_testcases(self):
        self.assertEqual(get_effective_checksum("aaaaabbbzyx"), "abxyz")
        self.assertEqual(get_effective_checksum("abcdefgh"), "abcde")
        self.assertEqual(get_effective_checksum("xxxwwwwabccdaa"), "waxcb")

class TestDecryptRoomNameFunction(unittest.TestCase):
    def test_testcases(self):
        self.assertEqual(decrypt_room_name("qzmt-zixmtkozy-ivhz", 343), "very-encrypted-name")


testcases = [
    "aaaaa-bbb-z-y-x-123[abxyz]", 
    "a-b-c-d-e-f-g-h-987[abcde]",
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]"
]
class TestCalculateSumOfSectorIDs(unittest.TestCase):
    def test_testcase(self):
        self.assertEqual(calculate_sum_of_sector_ids(testcases), 1514)

if __name__ == "__main__":
    unittest.main()