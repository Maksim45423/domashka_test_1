import test_1

def  test_palindrome():
    if test_1.palindrome("sas") == "sas":
        print("Test palindrome(sas) is OK")
    else:
        print("Test palindrome(sas) is Fail")
def  test_palindrome():
    if test_1.palindrome("nun") == "nun":
        print("Test palindrome(nun) is OK")
    else:
        print("Test palindrome(nun) is Fail")
def  test_palindrome():
    if test_1.palindrome("deed") == "deed":
        print("Test palindrome(deed) is OK")
    else:
        print("Test palindrome(deed) is Fail")
def  test_palindrome():
    if test_1.palindrome("level") == "level":
        print("Test palindrome(level) is OK")
    else:
        print("Test palindrome(level) is Fail")
def  test_palindrome():
    if test_1.palindrome("solos") == "solos":
        print("Test palindrome(solos) is OK")
    else:
        print("Test palindrome(solos) is Fail")



def test_back_string():
    if test_1.back_string("asdfgh") == "hgfdsa":
        print("Test back_string(asdfgh) is OK")
    else:
        print("Test back_string(asdfgh) is Fail")
def test_back_string():
    if test_1.back_string("asd") == "dsa":
        print("Test back_string(asd) is OK")
    else:
        print("Test back_string(asd) is Fail")
def test_back_string():
    if test_1.back_string("kill") == "llik":
        print("Test back_string(kill) is OK")
    else:
        print("Test back_string(kill) is Fail")
def test_back_string():
    if test_1.back_string("nuul") == "luun":
        print("Test back_string(nuul) is OK")
    else:
        print("Test back_string(nuul) is Fail")
def test_back_string():
    if test_1.back_string("eqwe") == "ewqe":
        print("Test back_string(eqwe) is OK")
    else:
        print("Test back_string(eqwe) is Fail")




def test_vowels():
    if test_1.vowels("афв") == 1:
        print("Test vowels(афв) is OK")
    else:
        print("Test vowels(афв) is Fail")
def test_vowels():
    if test_1.vowels("ааффыыв") == 4:
        print("Test vowels(ааффыыв) is OK")
    else:
        print("Test vowels(ааффыыв) is Fail")
def test_vowels():
    if test_1.vowels("аюв") == 2:
        print("Test vowels(афв) is OK")
    else:
        print("Test vowels(афв) is Fail")
def test_vowels():
    if test_1.vowels("аЁфук") == 3:
        print("Test vowels(афв) is OK")
    else:
        print("Test vowels(афв) is Fail")
def test_vowels():
    if test_1.vowels("ккккукуку") == 3:
        print("Test vowels(афв) is OK")
    else:
        print("Test vowels(афв) is Fail")




def test_remove_duplicates():
    if test_1.remove_duplicates("Hello world") == "Helo wrd":
        print("Test remove_duplicates(Hello world) is OK")
    else:
        print("Test remove_duplicates(Hello world) Fail")
def test_remove_duplicates():
    if test_1.remove_duplicates("he knows English") == "he knows gli":
        print("Test remove_duplicates(he knows English) is OK")
    else:
        print("Test remove_duplicates(he knows English) Fail")
def test_remove_duplicates():
    if test_1.remove_duplicates("wooedd") == "woed":
        print("Test remove_duplicates(wooedd) is OK")
    else:
        print("Test remove_duplicates(wooedd) Fail")
def test_remove_duplicates():
    if test_1.remove_duplicates("asdasd") == "asd":
        print("Test remove_duplicates(asdasd) is OK")
    else:
        print("Test remove_duplicates(asdasd) Fail")
def test_remove_duplicates():
    if test_1.remove_duplicates("qweqweqwe") == "qwe":
        print("Test remove_duplicates(qweqweqwe) is OK")
    else:
        print("Test remove_duplicates(qweqweqwe) Fail")

test_palindrome()
test_back_string()
test_vowels()
test_remove_duplicates()