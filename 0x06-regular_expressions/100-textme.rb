#!/usr/bin/env ruby
puts ARGV[0].scan(/from:\K\S+\b|to:\K\S+\b|flags:\K\S+\b/).join(",")
