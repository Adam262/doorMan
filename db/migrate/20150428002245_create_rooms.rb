class CreateRooms < ActiveRecord::Migration
  def change
    create_table :rooms do |t|
      t.string :name, :null => false
      t.boolean :available, :null => false
    end
  end
end
