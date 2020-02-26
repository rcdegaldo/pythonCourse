nums = [2,3,5]
words = ["fizz", "buzz", "bazz"]

def fizzbuzz_plusplus(nums, words):
  # TODO: complete
  nums_least_common_multiple = 1
  for i in range(len(nums)):
      nums_least_common_multiple = nums_least_common_multiple * nums[i]
      print(nums_least_common_multiple)
  
  return []

fizzbuzz_plusplus(nums, words)
