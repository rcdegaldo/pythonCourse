#traditional fizzbuzz
#fizzbuzzplusplus works, I just set nums to 2, 3 and words to fizz, bazz
from math import fmod

nums = [2,3]
words = ["fizz", "buzz"]

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
