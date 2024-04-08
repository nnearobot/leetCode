# 1700. Number of Students Unable to Eat Lunch
# easy
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        took_in_cycle = True
        prev_student = n - 1
        current_sandwich = 0
        q = collections.deque([i for i in range(n)])
        while len(q):
            if q[0] <= prev_student:
                if not took_in_cycle:
                    return len(q)
                took_in_cycle = False
            student = q.popleft()
            prev_student = student
            if students[student] == sandwiches[current_sandwich]:
                took_in_cycle = True
                current_sandwich += 1
            else:
                q.append(student)
        return 0

