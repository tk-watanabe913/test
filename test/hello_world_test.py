import sys
sys.path.append('../')

import unittest

from src.hello_world import HelloWorld

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        expected = "hello world!"

        helloWorld = HelloWorld()
        self.assertEqual(expected, helloWorld.printHelloWorld())

if __name__ == "__main__":
    unittest.main()
