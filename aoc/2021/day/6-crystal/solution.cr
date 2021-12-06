fish = (0..8).map {|i| Int64.new(File.read("input.txt").split(',').map(&.to_i).count(i))}
(0...256).each { fish = fish.rotate; fish[6] += fish.last }
puts fish.sum
