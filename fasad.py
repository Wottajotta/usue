class Amplifier:
    def on(self):
        print("Top-O-Line Amplifier on")
    
    def off(self):
        print("Top-O-Line Amplifier off")
    
    def set_dvd(self, dvd):
        print("Top-O-Line Amplifier setting DVD player to Top-O-Line DVD Player")
    
    def set_surround_sound(self):
        print("Top-O-Line Amplifier surround sound on (5 speakers, 1 subwoofer)")
    
    def set_volume(self, level):
        print(f"Top-O-Line Amplifier setting volume to {level}")

class Tuner:
    pass

class DvdPlayer:
    def on(self):
        print("Top-O-Line DVD Player on")
    
    def off(self):
        print("Top-O-Line DVD Player off")
    
    def play(self, movie):
        print(f"Top-O-Line DVD Player playing \"{movie}\"")
    
    def stop(self):
        print("Top-O-Line DVD Player stopped \"Raiders of the Lost Ark\"")
    
    def eject(self):
        print("Top-O-Line DVD Player eject")

class CdPlayer:
    pass

class Projector:
    def on(self):
        print("Top-O-Line Projector on")
    
    def off(self):
        print("Top-O-Line Projector off")
    
    def wide_screen_mode(self):
        print("Top-O-Line Projector in widescreen mode (16x9 aspect ratio)")

class TheaterLights:
    def dim(self, level):
        print(f"Theater Ceiling Lights dimming to {level}%")
    
    def on(self):
        print("Theater Ceiling Lights on")

class Screen:
    def down(self):
        print("Theater Screen going down")
    
    def up(self):
        print("Theater Screen going up")

class PopcornPopper:
    def on(self):
        print("Popcorn Popper on")
    
    def off(self):
        print("Popcorn Popper off")
    
    def pop(self):
        print("Popcorn Popper popping popcorn!")

class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, cd, projector, screen, lights, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_dvd(self.dvd)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

if __name__ == '__main__':
    amp = Amplifier()
    tuner = Tuner()
    dvd = DvdPlayer()
    cd = CdPlayer()
    projector = Projector()
    screen = Screen()
    lights = TheaterLights()
    popper = PopcornPopper()

    home_theater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)

    home_theater.watch_movie("Raiders of the Lost Ark")
    home_theater.end_movie()