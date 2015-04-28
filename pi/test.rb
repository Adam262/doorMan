require 'pi_piper'

pin = PiPiper::Pin.new(
  :pin => 4, 
  :direction => :out
)

2.upto(100) do |i|
  i % 2 == 0? pin.on : pin.off	
  sleep 0.5 
end

pin.off


    







