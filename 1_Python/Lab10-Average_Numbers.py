#   Justin Hamilton
#   Lab10-Average_Numbers.py
#   2020-03-21

def main():
    nums = [5, 0, 8, 3, 4, 1, 6]
    for num in nums:
        sum_nums = sum(nums)
        avg_nums = sum_nums / len(nums)
    print(f'This is the sum = {sum_nums}')
    print(f'This is the average = {avg_nums}')
main()