from music21 import *
#from music21 import note,stream
#from music21 import corpus

s = converter.parse('charlie parker/Another_Hairdo.xml')
print(s.analyze('key'))

#n1= note.Note('C4')
#n1.show('midi')                # play note in soundtrack in windows media player

#littleMelody = converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#")
#littleMelody.show('midi')

#s = corpus.parse('bwv66.6')
#n=note.Note("D3")
#n.duration.type = 'half'
#n.show()
#music21.converter[:parse]("tinynotation: 3/4 c4 d8 f g16 a g f#")[:show]()
