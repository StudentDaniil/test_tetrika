def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged


def clip_intervals(intervals, start, end):
    result = []
    for i in range(0, len(intervals), 2):
        s, e = intervals[i], intervals[i + 1]
        if e <= start or s >= end:
            continue
        result.append([max(s, start), min(e, end)])
    return result


def get_total_overlap(pupil, tutor):
    i = j = total = 0
    while i < len(pupil) and j < len(tutor):
        start = max(pupil[i][0], tutor[j][0])
        end = min(pupil[i][1], tutor[j][1])
        if start < end:
            total += end - start
        if pupil[i][1] < tutor[j][1]:
            i += 1
        else:
            j += 1
    return total


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']

    pupil_intervals = clip_intervals(intervals['pupil'], lesson_start, lesson_end)
    tutor_intervals = clip_intervals(intervals['tutor'], lesson_start, lesson_end)

    pupil_merged = merge_intervals(pupil_intervals)
    tutor_merged = merge_intervals(tutor_intervals)

    return get_total_overlap(pupil_merged, tutor_merged)


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':

    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
