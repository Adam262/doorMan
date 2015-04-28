class Room < ActiveRecord::Base

  def status
    available? 'free' : 'busy'
  end
end