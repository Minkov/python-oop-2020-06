# Test Code
class Guitar:
    def play(self):
        print("playing the guitar")


# Test Code
class Piano:
    def play(self):
        print("playing the piano")

def play_instrument(instrument):
    return instrument.play()

guitar = Guitar()
play_instrument(guitar)

piano = Piano()
play_instrument(piano)
