# by Bekzat
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        trial = [0, gain[0]]
        for i in range(1, len(gain)):
            trial.append(gain[i] + trial[len(trial) - 1])
        return max(trial)
            