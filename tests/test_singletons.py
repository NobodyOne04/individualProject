import sys
import types
import unittest

# a stand-in for pymorphy2 that counts how often the heavy analyzer is built
fake = types.ModuleType('pymorphy2')
fake.built = 0


class _Analyzer:
    def __init__(self):
        fake.built += 1


fake.MorphAnalyzer = _Analyzer
sys.modules.setdefault('pymorphy2', fake)

from operations.config.config import Config  # noqa: E402
from operations.morph.morph import MorphAnalyzer  # noqa: E402


class SingletonTests(unittest.TestCase):
    def test_morph_analyzer_is_built_once(self):
        if sys.modules['pymorphy2'] is not fake:
            self.skipTest('real pymorphy2 is loaded')
        self.assertIs(MorphAnalyzer(), MorphAnalyzer())
        self.assertEqual(fake.built, 1)

    def test_config_is_cached_and_reads_the_file(self):
        self.assertIs(Config(), Config())
        self.assertEqual(Config().get('morph', 'cases'), 'sources/morph/cases.json')


if __name__ == '__main__':
    unittest.main()
