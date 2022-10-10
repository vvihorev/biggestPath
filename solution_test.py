from unittest import TestCase

from main import biggestPath


class SolutionsTest(TestCase):
    def test_path_ending_in_empty_dir(self):
        self.assertEqual(
            biggestPath(
                {
                    "dir1": {},
                    "dir2": ["file1"],
                    "dir3": {"dir4": ["file2"], "dir5": {"dir6": {"dir7": {}}}},
                }
            ),
            "/dir3/dir5/dir6/dir7",
        )

    def test_path_with_duplicate_files(self):
        self.assertEqual(biggestPath({"dir1": ["file1", "file1"]}), "/")

    def test_path_ending_with_files(self):
        self.assertEqual(
            biggestPath({"dir1": ["file1", "file2", "file3"]}), "/dir1/file1"
        )

    def test_path_too_long(self):
        self.assertEqual(biggestPath({"dir1": ["2" * 255]}), "/")

    def test_improper_path_symbols(self):
        self.assertEqual(biggestPath({"diфr1": {}}), "/")
        self.assertEqual(biggestPath({"dir1": {"di_r2": {}}}), "/")
        self.assertEqual(biggestPath({"dir1": {"dir2": ["fileф"]}}), "/")
