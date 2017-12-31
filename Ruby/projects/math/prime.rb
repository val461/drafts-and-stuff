#!/usr/bin/env ruby

def find_a_divisor(n, lower_bound = 2)
  # return nil if n is prime
  (lower_bound..(Math.sqrt n)).detect() { |i| n % i == 0 }
end

def images_of_morphism(upper_bound, get_image_of_prime)
# upper_bound: positive integer
# get_image_of_prime: prime -> real
  result = {}
  prime_index=0
  (2..upper_bound).each do |n|
    d1 = find_a_divisor(n)
    if d1
      # n is composite
      d2 = n/d1
      raise "result[d1] not found: #{result[d1]}" unless result[d1]
      raise "result[d2] not found: #{result[d2]}" unless result[d2]
      result[n]=result[d1]+result[d2]
    else
      # n is prime
      result[n]=get_image_of_prime.call(n, prime_index)
      prime_index += 1
    end
  end
  result
end

puts images_of_morphism(16, ->(p,index) {2**index})
puts "\n", images_of_morphism(16, ->(p,index) {Math.log2 p})
# these two morphisms have the property l(2^n)=n*l(2)=n*1=n
