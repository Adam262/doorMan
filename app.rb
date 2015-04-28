require 'sinatra'
require 'sinatra/activerecord'
require './config/environments'
require './models/room'

get '/' do 
  erb :index
end

after do
  # Close the connection after the request is done so that we don't
  # deplete the ActiveRecord connection pool.
  ActiveRecord::Base.connection.close
end