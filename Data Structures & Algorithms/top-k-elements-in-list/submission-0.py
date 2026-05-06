class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = {}
        for num in nums:
            if num in frequency_counter:
                frequency_counter[num] += 1
            else:
                frequency_counter[num] = 1
        sorted_frequency_counter = dict(sorted(frequency_counter.items(), key=lambda item: item[1], reverse = True))
        result = []

        print(sorted_frequency_counter)

        for i in range(k):
            result.append(list(sorted_frequency_counter.keys())[i])
        return result
        