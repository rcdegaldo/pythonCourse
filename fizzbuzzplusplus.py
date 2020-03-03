from math import fmod

nums = [2,3,5,7]
words = ["fizz", "buzz", "bazz","sezz"]

def fizzbuzz_plusplus(nums, words):
  # TODO: complete
  nums_least_common_multiple = 1
  
  for i in range(len(nums)):
    nums_least_common_multiple = nums_least_common_multiple * nums[i]
  print(nums_least_common_multiple)
  
  for i in range(0,nums_least_common_multiple+1):
    
    fizzbuzzed_item = ""

    for j in range(0,len(nums)):
      if fmod(i,nums[j]) == 0:
        fizzbuzzed_item = fizzbuzzed_item + words[j]
    if fizzbuzzed_item == "":
      fizzbuzzed_item = i
    print(fizzbuzzed_item)

  return []

fizzbuzz_plusplus(nums, words)
