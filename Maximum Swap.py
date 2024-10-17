
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = [int(digit) for digit in str(num)]


        last = {digit: index for index, digit in enumerate(num_list)}
        for index, value in enumerate(num_list):
            for digit in range(9, value, -1):
                if last.get(digit, -1) > index:
                    num_list[index], num_list[last[digit]] = num_list[last[digit]], num_list[index]
                    return int(''.join(num_list))

        return num
