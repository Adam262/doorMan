require 'sinatra'
require 'sinatra/activerecord'
require './config/environments'
require './models/room'
require 'json'

get '/' do 
  erb :index
end

post '/:id/status' do
  room = Room.find(params[:id])
  room.available = (params[:status] == 'free')
  room.save!

  { :id => room.id, :status => room.status }.to_json
end 

after do
  # Close the connection after the request is done so that we don't
  # deplete the ActiveRecord connection pool.
  ActiveRecord::Base.connection.close
end