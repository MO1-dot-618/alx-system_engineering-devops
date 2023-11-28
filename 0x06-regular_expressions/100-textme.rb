#!/usr/bin/env ruby
puts ARGV[0].scan(/from:\K\S+\b/).join
echo ","
puts ARGV[0].scan(/to:\K\S+\b/).join
echo ","
puts ARGV[0].scan(/flags:\K\S+\b/).join
