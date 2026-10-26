import os
import sys

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_07.src.lessons.Lesson_01 import get_current_working_directory, decode_string, encode_string


def test_current_working_directory():
    assert os.getcwd() == get_current_working_directory()


def test_decode_string_case1():
    encoded = "UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSEgQXMgaXMgQysr"
    decoded = "Python is a cool programming language! As is C++"
    assert decode_string(encoded) == decoded, f"Failed to decode string {encoded}"


def test_decode_string_case2():
    encoded = "V2l0aCBlbm91Z2ggZXllcyBhbGwgYnVncyBhcmUgc2hhbGxvdw=="
    decoded = "With enough eyes all bugs are shallow"
    assert decode_string(encoded) == decoded, f"Failed to decode string {encoded}"


def test_decode_string_case3():
    encoded = ("UHJvZ3JhbSB0ZXN0aW5nIGNhbiBiZSB1c2VkIHRvIHNob3cgdGhlIHByZXNlbmNlIG9m"
               "IGJ1Z3MsIGJ1dCBuZXZlciB0byBzaG93IHRoZWlyIGFic2VuY2UhIFBsZWFzZSBkb24n"
               "dCBmYWxsIGludG8gdGhlIHRyYXAgb2YgYmVsaWV2aW5nIHRoYXQgSSBhbSB0ZXJyaWJs"
               "eSBkb2dtYXRpY2FsIGFib3V0IFt0aGUgZ290byBzdGF0ZW1lbnRdLg==")
    decoded = ("Program testing can be used to show the presence of bugs, but never to show their absence! "
               "Please don't fall into the trap of believing that I am terribly dogmatical about "
               "[the goto statement].")
    assert decode_string(encoded) == decoded, f"Failed to decode string {encoded}"


def test_encode_string_case1():
    decoded = "Python is a cool programming language! As is C++"
    encoded = "UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSEgQXMgaXMgQysr"
    assert encode_string(decoded) == encoded, f"Failed to encode string {decoded}"


def test_encode_string_case2():
    decoded = "With enough eyes all bugs are shallow"
    encoded = "V2l0aCBlbm91Z2ggZXllcyBhbGwgYnVncyBhcmUgc2hhbGxvdw=="
    assert encode_string(decoded) == encoded, f"Failed to encode string {decoded}"


def test_encode_string_case3():
    decoded = ("Program testing can be used to show the presence of bugs, but never to show their absence! "
               "Please don't fall into the trap of believing that I am terribly dogmatical about "
               "[the goto statement].")
    encoded = ("UHJvZ3JhbSB0ZXN0aW5nIGNhbiBiZSB1c2VkIHRvIHNob3cgdGhlIHByZXNlbmNlIG9m"
               "IGJ1Z3MsIGJ1dCBuZXZlciB0byBzaG93IHRoZWlyIGFic2VuY2UhIFBsZWFzZSBkb24n"
               "dCBmYWxsIGludG8gdGhlIHRyYXAgb2YgYmVsaWV2aW5nIHRoYXQgSSBhbSB0ZXJyaWJs"
               "eSBkb2dtYXRpY2FsIGFib3V0IFt0aGUgZ290byBzdGF0ZW1lbnRdLg==")
    assert encode_string(decoded) == encoded, f"Failed to encode string {decoded}"
