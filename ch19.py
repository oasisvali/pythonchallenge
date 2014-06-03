import email
import wave, struct
from pprint import pprint

if __name__ == '__main__':

  # f = open('email.dat', 'r')
  # email_txt = f.read()
  # f.close()

  # msg = email.message_from_string(email_txt)
  # attach = msg.get_payload()[0]

  # f= open(attach.get_filename(), 'wb')
  # f.write(attach.get_payload(decode=True))
  # f.close()

  inp = wave.open('indian.wav', 'r')

  out = wave.open('indian-inv.wav', 'w')


  length = inp.getnframes()
  channels = inp.getnchannels()
  print 'length:', length
  print 'channels:', channels

  out.setnchannels(channels)
  out.setnframes(length)
  out.setsampwidth(inp.getsampwidth())
  out.setframerate(inp.getframerate())

  for i in range(0,length):
    wavData = inp.readframes(channels)
    newdata = struct.pack('>h', *struct.unpack('<h', wavData))
    out.writeframes(newdata)

  inp.close()
  out.close()

