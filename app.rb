require 'sinatra'
require 'sinatra/active_record'
require ./environments

get '/' do 
  "Hello World~"
end

post '/status' do
end

class Room < ActiveRecord::Base
end