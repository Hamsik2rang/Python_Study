# Exception Handling in Python
class TryCatch:
    @staticmethod
    def test(x):
        try:
            if x % 5 != 0:
                raise Exception("x is not multiple of 5.")
        except Exception as e:
            print(e)
        else:
            print("x is multiple of 5.")
        finally:
            print("Finish Test.")

    @staticmethod
    def recv_exception_to_out():
        try:
            if True:
                raise Exception("Error!")
        except Exception as e:
            print(e)
            # Receive Exception to upper-namespace.
            raise

    @staticmethod
    def test_assert(x):
        assert x % 3 != 0, "x is not multiple of 3."
        print("x is multiple of 3")


TryCatch.test(3)
TryCatch.test(5)

try:
    TryCatch.recv_exception_to_out()
except:
    print("raise Exception in global namespace")

# Raise AssertionError.
# TryCatch.test_assert(3)
TryCatch.test_assert(5)